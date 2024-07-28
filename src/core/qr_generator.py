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
from PIL import Image
import qrcode
from PySide6.QtWidgets import QMessageBox, QFileDialog, QColorDialog, QDialog, QLabel, QLineEdit, QDialogButtonBox, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QGraphicsScene, QPushButton, QSizePolicy

class QRGenerator:
    def __init__(self, ui):
        self.ui = ui
        self.setup_connections()
        self.qr_templates = []
        self.load_qr_templates()
        self.current_qr_image = None

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

    def generate_qr_code(self):
        qr_data = self.ui.qrTextInput.toPlainText().strip()
        if not qr_data:
            return None

        qr = qrcode.QRCode(
            version=self.ui.qrCodeSize.value(),
            error_correction=self.get_error_correction(),
            box_size=40,
            border=self.ui.qrBorderSize.value(),
        )
        qr.add_data(qr_data)
        qr.make(fit=True)

        # Convert color strings to tuples
        def color_string_to_tuple(color_string):
            return tuple(map(int, color_string.split(',')))

        def get_color(color_input, default):
            color_text = color_input.text().strip()
            return color_string_to_tuple(color_text) if color_text else default

        #bg_color = color_string_to_tuple(self.ui.qrBgColourInput.text())
        #fill_color = color_string_to_tuple(self.ui.qrCodeColourInput.text())
        bg_color = get_color(self.ui.qrBgColourInput, (255, 255, 255))
        fill_color = get_color(self.ui.qrCodeColourInput, (0, 0, 0))

        # Create the QR code image
        qr_image = qr.make_image(
            fill_color=fill_color,
            back_color=bg_color,

        )

        logo_path = self.ui.qrLogoInput.text()
        if logo_path and os.path.isfile(logo_path):
            logo = Image.open(logo_path).convert('RGBA')

            qr_size = qr_image.size[0]
            max_size = qr_size // 3

            # Preserve aspect ratio
            if self.ui.qrAspectRatioCheck.isChecked():
                ratio = min(max_size / logo.width, max_size / logo.height)
                new_size = (int(logo.width * ratio), int(logo.height * ratio))
            else:
                new_size = (max_size, max_size)

            logo = logo.resize(new_size, Image.LANCZOS)

            # Create a new image with the background if checkbox is checked
            if self.ui.qrAddBGCheck.isChecked():
                bg = Image.new('RGBA', (max_size, max_size), (255, 255, 255, 255))
                offset = ((max_size - logo.width) // 2, (max_size - logo.height) // 2)
                bg.paste(logo, offset, logo)
                logo = bg
            else:
                # If no background, create a transparent image of max_size
                bg = Image.new('RGBA', (max_size, max_size), (0, 0, 0, 0))
                offset = ((max_size - logo.width) // 2, (max_size - logo.height) // 2)
                bg.paste(logo, offset, logo)
                logo = bg

            # Calculate the position to paste the logo
            box = ((qr_image.size[0] - logo.size[0]) // 2,
                (qr_image.size[1] - logo.size[1]) // 2)

            # Convert QR image to RGBA if it's not already
            if qr_image.mode != 'RGBA':
                qr_image = qr_image.convert('RGBA')

            # Paste the logo onto the QR code
            qr_image.paste(logo, box, logo)

            # After generating QR, resize to 1024
            qr_image = qr_image.resize((1024, 1024), Image.LANCZOS)

        return qr_image

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
            return

        qr_image = self.generate_qr_code()
        if qr_image:
            qr_image = qr_image.resize((1024, 1024), Image.LANCZOS)

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
            layout = QVBoxLayout()
            inputs = {}

            for key, default_value in placeholders.items():
                label = QLabel(f"{key}:")
                input_field = QLineEdit(default_value)
                inputs[key] = input_field
                layout.addWidget(label)
                layout.addWidget(input_field)

            buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
            buttons.accepted.connect(dialog.accept)
            buttons.rejected.connect(dialog.reject)
            layout.addWidget(buttons)
            dialog.setLayout(layout)

            if dialog.exec() == QDialog.Accepted:
                # Get the original template format
                format_with_placeholders = template['format']

                # Replace placeholders with user input
                for key, input_field in inputs.items():
                    placeholder = f"{{{key}}}"
                    format_with_placeholders = format_with_placeholders.replace(placeholder, input_field.text())

                # Update the QR text input with the new text
                self.ui.qrTextInput.setPlainText(format_with_placeholders)

    # def show_preview_window(self):
    #     if hasattr(self, 'current_qr_image'):
    #         preview_dialog = QDialog(self.ui.qrOutputView)
    #         preview_dialog.setWindowTitle("QR Code Preview")
    #         preview_dialog.setGeometry(100, 100, 300, 300)
    #         layout = QVBoxLayout()
    #         label = QLabel()

    #         # Convert PIL Image to QPixmap
    #         buffer = io.BytesIO()
    #         self.current_qr_image.save(buffer, format="PNG")
    #         qimage = QImage()
    #         qimage.loadFromData(buffer.getvalue())
    #         pixmap = QPixmap.fromImage(qimage)

    #         label.setPixmap(pixmap)
    #         layout.addWidget(label)

    #         close_button = QPushButton("Close")
    #         close_button.clicked.connect(preview_dialog.close)
    #         layout.addWidget(close_button)

    #         preview_dialog.setLayout(layout)
    #         preview_dialog.exec()
    #     else:
    #         QMessageBox.warning(None, "Warning", "No QR code has been generated yet.")
    
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