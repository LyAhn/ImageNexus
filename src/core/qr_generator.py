"""
This file is part of ImageNexus

ImageNexus is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation

Copyright (c) 2024, LyAhn

This code is licensed under the GPL-3.0 license (see LICENSE.txt for details)
"""
import os
import tempfile
import io
import json
import cv2
from MyQR import myqr
import numpy as np
from PIL import Image
import qrcode
import asyncio
from PySide6.QtWidgets import QMessageBox, QFileDialog, QColorDialog, QDialog, QLabel, QLineEdit, QDialogButtonBox, QVBoxLayout
from PySide6.QtWidgets import QGridLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap, QKeySequence, QShortcut, QIcon
from PySide6.QtWidgets import QGraphicsScene, QPushButton, QSizePolicy, QScrollArea, QWidget
from src.utils.templateEditor import JSONEditorDialog
from PySide6.QtCore import QThreadPool, QRunnable, Slot, Signal, QObject, QTimer


class WorkerSignals(QObject):
    finished = Signal(object)
    error = Signal(tuple)

class QRGeneratorWorker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super().__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @Slot()
    def run(self):
        try:
            result = self.fn(*self.args, **self.kwargs)
        except Exception as e:
            self.signals.error.emit((str(e),))
        else:
            self.signals.finished.emit(result)


class QRGenerator:
    def __init__(self, ui):
        self.ui = ui
        self.setup_connections()
        self.qr_templates = []
        self.load_qr_templates()
        self.current_qr_image = None
        self.create_shortcut()
        self.editor = JSONEditorDialog
        self.threadpool = QThreadPool()
        self.debounce_timer = QTimer()
        self.debounce_timer.setSingleShot(True)
        self.debounce_timer.timeout.connect(self.generate_qr_code_debounced)

    def setup_connections(self):
        self.ui.qrGenButton.clicked.connect(self.preview_qr_code)
        self.ui.qrSaveQRBtn.clicked.connect(self.save_qr_code)
        self.ui.qrBrowseOutput.clicked.connect(self.browse_output_folder)
        self.ui.qrBrowseLogo.clicked.connect(self.browse_logo)
        self.ui.qrBgColourBtn.clicked.connect(lambda: self.choose_color('bg'))
        self.ui.qrCodeColourBtn.clicked.connect(lambda: self.choose_color('code'))
        self.ui.qrAddBGCheck.stateChanged.connect(self.preview_qr_code)
        self.ui.qrAspectRatioCheck.stateChanged.connect(self.preview_qr_code)
        self.ui.qrTemplates.currentIndexChanged.connect(self.on_qr_template_changed)
        self.ui.qrPlaceholderEditor.clicked.connect(self.fill_placeholders)
        self.ui.qrOutputView.mousePressEvent = self.on_preview_clicked

        #self.ui.qrTextInput.textChanged.connect(self.preview_qr_code) # remove this comment if you want live QR code preview while typing - Not advised
        self.ui.qrTextInput.textChanged.connect(self.debounce_preview_qr_code) # Newer version of live preview - Less taxing on system
        self.ui.qrCodeSize.valueChanged.connect(self.preview_qr_code)
        self.ui.qrBorderSize.valueChanged.connect(self.preview_qr_code)
        self.ui.qrErrorCorrectList.currentIndexChanged.connect(self.preview_qr_code)
        self.ui.qrLogoInput.textChanged.connect(self.preview_qr_code)
        self.ui.qrBgColourInput.textChanged.connect(self.preview_qr_code)
        self.ui.qrCodeColourInput.textChanged.connect(self.preview_qr_code)
        self.ui.actionQRTemplateEditor.triggered.connect(self.open_json_editor)
        #self.ui.qrUseArtisticCheck.stateChanged.connect(self.preview_qr_code)
        self.ui.qrUseArtisticCheck.stateChanged.connect(self.on_artistic_check_changed)
        self.ui.qrColorizedCheck.stateChanged.connect(self.preview_qr_code)
        #self.ui.qrBgImageInput.textChanged.connect(self.preview_qr_code)

    # Debounce code

    def debounce_preview_qr_code(self):
        self.debounce_timer.start(150)  # 300 ms debounce time default

    def generate_qr_code_debounced(self):
        worker = QRGeneratorWorker(self.generate_qr_code)
        worker.signals.finished.connect(self.display_qr_code)
        worker.signals.error.connect(self.handle_error)
        self.threadpool.start(worker)

    def on_artistic_check_changed(self, state):
        self.debounce_preview_qr_code()

    # End of Debounce code


    async def generate_qr_async(self):
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self.generate_qr_code)
        
    def open_json_editor(self):
        editor = JSONEditorDialog('resources/qr_templates.json', self.ui)
        if editor.exec() == QDialog.Accepted:
            self.load_qr_templates()  # Reload templates after editing

    def create_shortcut(self):
        shortcut = QShortcut(QKeySequence("Ctrl+Return"), self.ui.qrTextInput)
        shortcut.activated.connect(self.preview_qr_code)

    def on_preview_clicked(self, event):
        if event.button() == Qt.LeftButton:
            self.show_preview_window()

    def preview_qr_code(self):
        self.generate_qr_code_debounced()

    def handle_error(self, error):
        QMessageBox.critical(None, "Error", f"An error occured: {error[0]}")


    def clear_qr_display(self):
        scene = self.ui.qrOutputView.scene()
        if scene:
            scene.clear()
        self.ui.qrOutputView.setScene(QGraphicsScene())
        self.current_qr_image = None # Clear the buffer

    def generate_qr_code(self):
        qr_data = self.ui.qrTextInput.toPlainText().strip()
        if not qr_data or len(qr_data) < 2:
            return None

        use_artistic = self.ui.qrUseArtisticCheck.isChecked()

        if use_artistic:
            return self.generate_artistic_qr(qr_data)
        else:
            # Check if the data is purely numeric
            if qr_data.isdigit():
                mode = 'numeric'
            else:
                mode = 'binary'  # Use byte mode for non-numeric data

            qr = qrcode.QRCode(
                version=self.ui.qrCodeSize.value(),
                error_correction=self.get_error_correction(),
                box_size=10,
                border=self.ui.qrBorderSize.value(),
            )
            qr.add_data(qr_data, optimize=0)  # Disable automatic mode optimization
            qr.make(fit=True)

            bg_color = self.get_color_tuple(self.ui.qrBgColourInput.text(), (255, 255, 255))
            fg_color = self.get_color_tuple(self.ui.qrCodeColourInput.text(), (0, 0, 0))
            qr_image = qr.make_image(fill_color=fg_color, back_color=bg_color)
            qr_image = qr_image.convert('RGB')

            qr_array = np.array(qr_image)
            qr_cv = cv2.cvtColor(qr_array, cv2.COLOR_RGB2BGR)
            target_size = (1024, 1024)
            qr_code_resized = cv2.resize(qr_cv, target_size, interpolation=cv2.INTER_LANCZOS4)

            logo_path = self.ui.qrLogoInput.text()
            if logo_path and os.path.isfile(logo_path):
                qr_code_resized = self.add_logo_to_qr(qr_code_resized, logo_path)

            return Image.fromarray(cv2.cvtColor(qr_code_resized, cv2.COLOR_BGR2RGB))

    # def generate_artistic_qr(self, qr_data):
    #     version = self.ui.qrCodeSize.value()
    #     error_correction = self.get_error_correction_level()
    #     picture = self.ui.qrLogoInput.text()
    #     #picture = self.ui.qrBgImageInput.text()
    #     colorized = self.ui.qrColorizedCheck.isChecked()
    #     border_size = self.ui.qrBorderSize.value()
        
    #     save_name = "temp_artistic_qr.png"
    #     version, level, qr_name = myqr.run(
    #         qr_data,
    #         version=version,
    #         level=error_correction,
    #         picture=picture,
    #         colorized=colorized,
    #         save_name=save_name
    #     )
        
    #     # Open the generated QR code
    #     qr_image = Image.open(save_name)
        
    #     # Crop the white border
    #     bbox = qr_image.getbbox()
    #     cropped_qr = qr_image.crop(bbox)
        
    #     # Create a new image with desired border
    #     qr_size = cropped_qr.size[0]
    #     new_size = qr_size + 2 * border_size
    #     bg_color = self.get_color_tuple(self.ui.qrBgColourInput.text(), (255, 255, 255))
    #     new_image = Image.new('RGB', (new_size, new_size), bg_color)
        
    #     # Paste the cropped QR code onto the new image
    #     new_image.paste(cropped_qr, (border_size, border_size))
        
    #     # Remove the temporary file
    #     os.remove(save_name)
        
    #     return new_image
    def generate_artistic_qr(self, qr_data):
        try:
            version = self.ui.qrCodeSize.value()
            error_correction = self.get_error_correction_level()
            picture = self.ui.qrLogoInput.text()
            colorized = self.ui.qrColorizedCheck.isChecked()
            border_size = self.ui.qrBorderSize.value()

            # Use a temporary directory to save the file
            with tempfile.TemporaryDirectory() as temp_dir:
                save_name = os.path.join(temp_dir, "temp_artistic_qr.png")
                
                version, level, qr_name = myqr.run(
                    qr_data,
                    version=version,
                    level=error_correction,
                    picture=picture,
                    colorized=True,
                    save_name=save_name
                )
                
                # Open the generated QR code
                qr_image = Image.open(save_name)
                
                # Crop the white border
                bbox = qr_image.getbbox()
                cropped_qr = qr_image.crop(bbox)
                
                # Create a new image with desired border
                qr_size = cropped_qr.size[0]
                new_size = qr_size + 2 * border_size
                bg_color = self.get_color_tuple(self.ui.qrBgColourInput.text(), (255, 255, 255))
                new_image = Image.new('RGB', (new_size, new_size), bg_color)
                
                # Paste the cropped QR code onto the new image
                new_image.paste(cropped_qr, (border_size, border_size))
                
                return new_image

        except Exception as e:
            print(f"Error in generate_artistic_qr: {str(e)}")
            # Return a default QR code or None
            return self.generate_standard_qr(qr_data)

    def generate_standard_qr(self, qr_data):
        qr = qrcode.QRCode(
            version=self.ui.qrCodeSize.value(),
            error_correction=self.get_error_correction(),
            box_size=10,
            border=self.ui.qrBorderSize.value(),
        )
        qr.add_data(qr_data)
        qr.make(fit=True)

        bg_color = self.get_color_tuple(self.ui.qrBgColourInput.text(), (255, 255, 255))
        fg_color = self.get_color_tuple(self.ui.qrCodeColourInput.text(), (0, 0, 0))

        qr_image = qr.make_image(fill_color=fg_color, back_color=bg_color)
        qr_image = qr_image.convert('RGB')

        qr_array = np.array(qr_image)
        qr_cv = cv2.cvtColor(qr_array, cv2.COLOR_RGB2BGR)
        target_size = (1024, 1024)
        qr_code_resized = cv2.resize(qr_cv, target_size, interpolation=cv2.INTER_LANCZOS4)

        logo_path = self.ui.qrLogoInput.text()
        if logo_path and os.path.isfile(logo_path):
            qr_code_resized = self.add_logo_to_qr(qr_code_resized, logo_path)

        return Image.fromarray(cv2.cvtColor(qr_code_resized, cv2.COLOR_BGR2RGB))

    def add_logo_to_qr(self, qr_code_resized, logo_path):
        logo = Image.open(logo_path).convert('RGBA')
        if logo is not None:
            logo_size = min(qr_code_resized.shape[0], qr_code_resized.shape[1]) // 3
            if self.ui.qrAspectRatioCheck.isChecked():
                logo.thumbnail((logo_size, logo_size), Image.LANCZOS)
            else:
                logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

            if self.ui.qrAddBGCheck.isChecked():
                bg_size = (logo_size, logo_size)
                logo_bg = Image.new('RGBA', bg_size, (255, 255, 255, 255))
                logo_pos = ((bg_size[0] - logo.size[0]) // 2, (bg_size[1] - logo.size[1]) // 2)
                logo_bg.paste(logo, logo_pos, logo)
                logo = logo_bg

            logo_np = np.array(logo)
            logo_cv = cv2.cvtColor(logo_np, cv2.COLOR_RGBA2BGRA)
            top_left_x = (qr_code_resized.shape[1] - logo_cv.shape[1]) // 2
            top_left_y = (qr_code_resized.shape[0] - logo_cv.shape[0]) // 2

            if logo_cv.shape[2] == 4:
                alpha = logo_cv[:, :, 3] / 255.0
                alpha = np.expand_dims(alpha, axis=2)
                rgb = cv2.cvtColor(logo_cv, cv2.COLOR_BGRA2BGR)
                roi = qr_code_resized[top_left_y:top_left_y+logo_cv.shape[0], top_left_x:top_left_x+logo_cv.shape[1]]
                qr_code_resized[top_left_y:top_left_y+logo_cv.shape[0], top_left_x:top_left_x+logo_cv.shape[1]] = \
                    (1 - alpha) * roi + alpha * rgb

        return qr_code_resized

    def get_color_tuple(self, color_string, default):
        try:
            return tuple(map(int, color_string.split(',')))
        except ValueError:
            return default

    def get_error_correction(self):
        error_correction = self.ui.qrErrorCorrectList.currentText()
        if error_correction == "Low":
            return qrcode.constants.ERROR_CORRECT_L
        elif error_correction == "Medium":
            return qrcode.constants.ERROR_CORRECT_M
        elif error_correction == "Quartile":
            return qrcode.constants.ERROR_CORRECT_Q
        else:
            return qrcode.constants.ERROR_CORRECT_H

    def display_qr_code(self, qr_image):
        if qr_image:
            self.current_qr_image = qr_image  # Store the current QR image
            buffer = io.BytesIO()
            qr_image.save(buffer, format="PNG")
            qimage = QImage()
            qimage.loadFromData(buffer.getvalue())
            pixmap = QPixmap.fromImage(qimage)
            scene = self.ui.qrOutputView.scene()
            if scene is None:
                scene = QGraphicsScene()
                self.ui.qrOutputView.setScene(scene)
            scene.clear()
            scene_item = scene.addPixmap(pixmap)
            scene.setSceneRect(scene_item.boundingRect())
            self.ui.qrOutputView.setSceneRect(scene.sceneRect())
            self.ui.qrOutputView.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)
        else:
            self.clear_qr_display()

    def save_qr_code(self):
        qr_data = self.ui.qrTextInput.toPlainText().strip()
        if not qr_data:
            QMessageBox.warning(None, "Warning", "Please enter some data for the QR code.")
            return

        output_folder = self.ui.qrOutputFolder.text()
        if not output_folder:
            output_folder = QFileDialog.getExistingDirectory(None, "Select Output Folder")
            if not output_folder:
                return  # User cancelled folder selection
            self.ui.qrOutputFolder.setText(output_folder)

        # Continue with the rest of the save_qr_code() method
        qr_image = self.generate_qr_code()
        if qr_image:
            qr_image = qr_image.resize((1024, 1024), Image.BICUBIC)

            save_format = self.ui.qrFormatOptions.currentText().lower()
            file_name = f"qr_code.{save_format}"
            file_path = os.path.join(output_folder, file_name)

            # Convert to RGB if saving as JPEG
            if save_format.lower() in ['jpg', 'jpeg']:
                qr_image = qr_image.convert('RGB')

            qr_image.save(file_path)
            QMessageBox.information(None, "Success", f"QR code saved as {file_path}")


    def browse_output_folder(self):
        folder_path = QFileDialog.getExistingDirectory(None, "Select Output Folder")
        if folder_path:
            self.ui.qrOutputFolder.setText(folder_path)

    def browse_logo(self):
        file_path, _ = QFileDialog.getOpenFileName(None, "Select Logo Image", "", "Image Files (*.png *.jpg *.bmp)")
        if file_path:
            self.ui.qrLogoInput.setText(file_path)

    def choose_color(self, color_type):
        color = QColorDialog.getColor()
        if color.isValid():
            rgb_values = f"{color.red()}, {color.green()}, {color.blue()}"
            if color_type == 'bg':
                self.ui.qrBgColourInput.setText(rgb_values)
            else:
                self.ui.qrCodeColourInput.setText(rgb_values)

    def populate_qr_templates(self):
        self.ui.qrTemplates.clear()
        self.ui.qrTemplates.addItem("Select a template")
        for template in self.qr_templates:
            self.ui.qrTemplates.addItem(template['name'])

    def load_qr_templates(self):
        try:
            with open('resources/qr_templates.json', 'r') as file:
                data = json.load(file)
            self.qr_templates = data['qr_code_types']
            self.populate_qr_templates()
        except FileNotFoundError:
            print("Error: 'resources/qr_templates.json' file not found.")
            QMessageBox.warning(None, "Warning", "Error: 'resources/qr_templates.json' file not found.\nRedownload the template file and try again.")
            self.qr_templates = []
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in 'resources/qr_templates.json'.")
            QMessageBox.warning(None, "Warning", "Error: Invalid JSON format in 'resources/qr_templates.json'.\nCheck any new additions match the format.")
            self.qr_templates = []

    def on_qr_template_changed(self, index):
        if index > 0:  # index 0 is the "Select a template" item
            template = self.qr_templates[index - 1]
            format_with_placeholders = template['format']
            for key, value in template.get('placeholders', {}).items():
                format_with_placeholders = format_with_placeholders.replace(f"{{{key}}}", f"[{key.upper()}]")
            self.ui.qrTextInput.setPlainText(format_with_placeholders)

    def fill_placeholders(self):
        template_index = self.ui.qrTemplates.currentIndex()
        if template_index > 0 and template_index <= len(self.qr_templates):
            template = self.qr_templates[template_index - 1]
            placeholders = template.get('placeholders', {})
            if not placeholders:
                return

            dialog = QDialog()
            dialog.setWindowTitle("Placeholder Editor")
            dialog.setWindowIcon(QIcon.fromTheme("document-properties"))
            layout = QVBoxLayout()

            # Create a scroll area
            scroll_area = QScrollArea()
            scroll_area.setWidgetResizable(True)
            scroll_content = QWidget()
            grid_layout = QGridLayout(scroll_content)

            inputs = {}
            row = 0
            col = 0
            max_cols = 2  # Adjust this value to change the number of columns

            for key, default_value in placeholders.items():
                label = QLabel(f"{key}:")
                input_field = QLineEdit(default_value)
                inputs[key] = input_field

                grid_layout.addWidget(label, row, col * 2)
                grid_layout.addWidget(input_field, row, col * 2 + 1)

                col += 1
                if col >= max_cols:
                    col = 0
                    row += 1

            scroll_area.setWidget(scroll_content)
            layout.addWidget(scroll_area)

            # Add buttons
            buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
            buttons.accepted.connect(dialog.accept)
            buttons.rejected.connect(dialog.reject)
            layout.addWidget(buttons)

            dialog.setLayout(layout)

            if dialog.exec() == QDialog.Accepted:
                # Process the inputs and update the QR code text
                format_with_placeholders = template['format']
                for key, input_field in inputs.items():
                    placeholder = f"{{{key}}}"
                    format_with_placeholders = format_with_placeholders.replace(placeholder, input_field.text())
                self.ui.qrTextInput.setPlainText(format_with_placeholders)
                self.preview_qr_code()

    def show_preview_window(self):
        if hasattr(self, 'current_qr_image') and self.current_qr_image:
            preview_dialog = QDialog(self.ui.qrOutputView)
            preview_dialog.setWindowTitle("QR Code Preview")
            # set minimum size
            #preview_dialog.setMinimumSize(300, 300)
            layout = QVBoxLayout()
            label = QLabel()

            # Convert PIL Image to QPixmap
            buffer = io.BytesIO()
            self.current_qr_image.save(buffer, format="PNG")
            qimage = QImage()
            qimage.loadFromData(buffer.getvalue())
            pixmap = QPixmap.fromImage(qimage)

            label.setPixmap(pixmap)
            #label.setScaledContents(True)  # This will scale the image to fit the label
            label.setAlignment(Qt.AlignCenter)
            label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            label.setMinimumSize(200, 200)

            # Resize the pixmap to fit the label while preserving aspect ratio
            label.resizeEvent = lambda event: label.setPixmap(pixmap.scaled(
                label.width(), label.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation
            ))

            layout.addWidget(label)
            close_button = QPushButton("Close")
            close_button.clicked.connect(preview_dialog.close)
            layout.addWidget(close_button)
            preview_dialog.setLayout(layout)
            preview_dialog.exec()
        else:
            QMessageBox.warning(None, "Warning", "No QR code has been generated yet.")

    # def generate_artistic_qr(self, qr_data):
        
    #     version = self.ui.qrCodeSize.value()
    #     error_correction = self.get_error_correction_level()
    #     picture = self.ui.qrLogoInput.text()
    #     #picture = self.ui.qrBgImageInput.text()
    #     colorized = self.ui.qrColorizedCheck.isChecked()
        
    #     save_name = "temp_artistic_qr.png"
    #     version, level, qr_name = myqr.run(
    #         qr_data,
    #         version=version,
    #         level=error_correction,
    #         picture=picture,
    #         colorized=colorized,
    #         save_name=save_name
    #     )
        
    #     return Image.open(save_name)

    # def generate_artistic_qr(self, qr_data):
    #     version = self.ui.qrCodeSize.value()
    #     error_correction = self.get_error_correction_level()
    #     picture = self.ui.qrLogoInput.text()
    #     colorized = self.ui.qrColorizedCheck.isChecked()
    #     border_size = self.ui.qrBorderSize.value()

    #     with tempfile.TemporaryDirectory() as temp_dir:
    #         save_name = os.path.join(temp_dir, "temp_artistic_qr.png")
    #         try:
    #             version, level, qr_name = myqr.run(
    #                 qr_data,
    #                 version=version,
    #                 level=error_correction,
    #                 picture=picture,
    #                 colorized=colorized,
    #                 save_name=save_name
    #             )

    #             # Open the generated QR code
    #             qr_image = Image.open(save_name)

    #             # Crop the white border
    #             bbox = qr_image.getbbox()
    #             cropped_qr = qr_image.crop(bbox)

    #             # Create a new image with desired border
    #             qr_size = cropped_qr.size[0]
    #             new_size = qr_size + 2 * border_size
    #             bg_color = self.get_color_tuple(self.ui.qrBgColourInput.text(), (255, 255, 255))
    #             new_image = Image.new('RGB', (new_size, new_size), bg_color)

    #             # Paste the cropped QR code onto the new image
    #             new_image.paste(cropped_qr, (border_size, border_size))

    #             return new_image

    #         except Exception as e:
    #             print(f"Error in generate_artistic_qr: {str(e)}")
    #             # Return a default QR code or None
    #             return self.generate_standard_qr(qr_data)

    def generate_artistic_qr(self, qr_data):
        version = self.ui.qrCodeSize.value()
        error_correction = self.get_error_correction_level()
        picture = self.ui.qrLogoInput.text()
        colorized = self.ui.qrColorizedCheck.isChecked()
        border_size = self.ui.qrBorderSize.value()

        # Create a unique temporary directory
        temp_dir = tempfile.mkdtemp(prefix="myqr_")
        try:
            # Use a unique filename
            save_name = os.path.join(temp_dir, f"temp_artistic_qr_{os.urandom(8).hex()}.png")
            
            version, level, qr_name = myqr.run(
                qr_data,
                version=version,
                level=error_correction,
                picture=picture,
                colorized=colorized,
                save_name=save_name
            )

            # Open the generated QR code
            qr_image = Image.open(save_name)

            # Crop the white border
            bbox = qr_image.getbbox()
            cropped_qr = qr_image.crop(bbox)

            # Create a new image with desired border
            qr_size = cropped_qr.size[0]
            new_size = qr_size + 2 * border_size
            bg_color = self.get_color_tuple(self.ui.qrBgColourInput.text(), (255, 255, 255))
            new_image = Image.new('RGB', (new_size, new_size), bg_color)

            # Paste the cropped QR code onto the new image
            new_image.paste(cropped_qr, (border_size, border_size))

            return new_image

        except Exception as e:
            print(f"Error in generate_artistic_qr: {str(e)}")
            # Return a default QR code or None
            return self.generate_standard_qr(qr_data)
        finally:
            # Clean up temporary files
            if os.path.exists(save_name):
                os.remove(save_name)
            os.rmdir(temp_dir)

    def get_error_correction_level(self):
        error_correction = self.ui.qrErrorCorrectList.currentText()
        if error_correction == "Low":
            return 'L'
        elif error_correction == "Medium":
            return 'M'
        elif error_correction == "Quartile":
            return 'Q'
        else:
            return 'H'
        
# TODO: crop into generated Artistic QR by 140px to attempt to match same output as standard QR
# TODO: #22 Fix regression of sharpness in saved&previewed QR codes
# TODO: Add filename save box w/ additional variables e.g (date, time, sequence count etc)
