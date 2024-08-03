"""
This file is part of ImageNexus

ImageNexus is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation

Copyright (c) 2024, LyAhn

This code is licensed under the GPL-3.0 license (see LICENSE.txt for details)
"""
import os
import io
import json
import cv2
import numpy as np
from PIL import Image
import qrcode
from PySide6.QtWidgets import QMessageBox, QFileDialog, QColorDialog, QDialog, QLabel, QLineEdit, QDialogButtonBox, QVBoxLayout
from PySide6.QtWidgets import QGridLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap, QKeySequence, QShortcut, QIcon
from PySide6.QtWidgets import QGraphicsScene, QPushButton, QSizePolicy, QScrollArea, QWidget
from src.utils.templateEditor import JSONEditorDialog


class QRGenerator:
    def __init__(self, ui):
        self.ui = ui
        self.setup_connections()
        self.qr_templates = []
        self.load_qr_templates()
        self.current_qr_image = None
        self.create_shortcut()
        self.editor = JSONEditorDialog

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
        self.ui.qrCodeSize.valueChanged.connect(self.preview_qr_code)
        self.ui.qrBorderSize.valueChanged.connect(self.preview_qr_code)
        self.ui.qrErrorCorrectList.currentIndexChanged.connect(self.preview_qr_code)
        self.ui.qrLogoInput.textChanged.connect(self.preview_qr_code)
        self.ui.qrBgColourInput.textChanged.connect(self.preview_qr_code)
        self.ui.qrCodeColourInput.textChanged.connect(self.preview_qr_code)
        self.ui.actionQRTemplateEditor.triggered.connect(self.open_json_editor)

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
        qr_data = self.ui.qrTextInput.toPlainText().strip()
        if qr_data:
            qr_image = self.generate_qr_code()
            if qr_image:
                self.display_qr_code(qr_image)
        else:
            # Clear the QR code display if the input is empty
            self.clear_qr_display()
            self.current_qr_image = None # Clears the buffer

    def clear_qr_display(self):
        scene = self.ui.qrOutputView.scene()
        if scene:
            scene.clear()
        self.ui.qrOutputView.setScene(QGraphicsScene())
        self.current_qr_image = None # Clear the buffer

    # def generate_qr_code(self):
    #     qr_data = self.ui.qrTextInput.toPlainText().strip()
    #     if not qr_data:
    #         return None

    #     qr = qrcode.QRCode(
    #         version=self.ui.qrCodeSize.value(),
    #         error_correction=self.get_error_correction(),
    #         box_size=15,
    #         border=self.ui.qrBorderSize.value(),
    #     )
    #     qr.add_data(qr_data)
    #     qr.make(fit=True)

    def generate_qr_code(self):
        qr_data = self.ui.qrTextInput.toPlainText().strip()
        if not qr_data:
            return None

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
        qr_code_resized = cv2.resize(qr_cv, target_size, interpolation=cv2.INTER_AREA)

        logo_path = self.ui.qrLogoInput.text()
        if logo_path and os.path.isfile(logo_path):
            logo = Image.open(logo_path).convert('RGBA')
            if logo is not None:
                logo_size = min(qr_code_resized.shape[0], qr_code_resized.shape[1]) // 3

                if self.ui.qrAspectRatioCheck.isChecked():
                    # Preserve aspect ratio
                    logo.thumbnail((logo_size, logo_size), Image.LANCZOS)
                else:
                    # Resize without preserving aspect ratio
                    logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

                if self.ui.qrAddBGCheck.isChecked():
                    bg_size = (logo_size, logo_size)
                    logo_bg = Image.new('RGBA', bg_size, (255, 255, 255, 255))
                    logo_pos = ((bg_size[0] - logo.size[0]) // 2,
                                (bg_size[1] - logo.size[1]) // 2)
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

                    roi = qr_code_resized[top_left_y:top_left_y+logo_cv.shape[0], 
                                        top_left_x:top_left_x+logo_cv.shape[1]]
                    qr_code_resized[top_left_y:top_left_y+logo_cv.shape[0], 
                                    top_left_x:top_left_x+logo_cv.shape[1]] = \
                        (1 - alpha) * roi + alpha * rgb

        return Image.fromarray(cv2.cvtColor(qr_code_resized, cv2.COLOR_BGR2RGB))

    def generate_and_display_qr(self):
        qr_data = self.ui.qrTextInput.toPlainText().strip()
        if qr_data:
            qr_image = self.generate_qr_code()
            if qr_image:
                self.display_qr_code(qr_image)
        else:
            self.clear_qr_display()
            self.current_qr_image = None

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

    def save_qr_code(self):
        qr_data = self.ui.qrTextInput.toPlainText().strip()
        if not qr_data:
            QMessageBox.warning(None, "Warning", "Please enter some data for the QR code.")
            return

        output_folder = self.ui.qrOutputFolder.text()
        if not output_folder:
            QMessageBox.warning(None, "Warning", "Please select an output folder.")
            if self.browse_output_folder():
                self.save_qr_code()
            pass

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

            self.ui.qrTemplates.clear()
            self.ui.qrTemplates.addItem("Select a template")
            for template in self.qr_templates:
                self.ui.qrTemplates.addItem(template['name'])
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
                label.width(), label.height(),
                Qt.KeepAspectRatio, Qt.SmoothTransformation
            ))

            layout.addWidget(label)

            close_button = QPushButton("Close")
            close_button.clicked.connect(preview_dialog.close)
            layout.addWidget(close_button)

            preview_dialog.setLayout(layout)
            preview_dialog.exec()
        else:
            # Only show a warning if there's no QR code and the user explicitly tries to preview
            QMessageBox.warning(None, "Warning", "No QR code has been generated yet.")