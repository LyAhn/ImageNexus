"""
This file is part of ImageNexus

ImageNexus is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation

Copyright (c) 2024, LyAhn

This code is licensed under the GPL-3.0 license (see LICENSE.txt for details)
"""
import os
from PIL import Image
from PySide6.QtWidgets import QFileDialog, QMessageBox


class ImgConverter:
    def __init__(self, ui):
        self.ui = ui
        self.setup_connections()

    def setup_connections(self):
        # Image Converter tab
        self.ui.inputBrowse2.clicked.connect(self.select_input_file)
        self.ui.outputBrowse2.clicked.connect(self.select_output_folder_converter)
        self.ui.converter_button.clicked.connect(self.convert_file)

    def select_input_file(self):
        file_path, _ = QFileDialog.getOpenFileName(None, "Select Input File", "", "Image files (*.gif *.png *.jpg *.jpeg *.bmp *.tiff)")
        if file_path:
            self.ui.fileInput2.setText(file_path)
            self.input_format = os.path.splitext(file_path)[1][1:].lower()

    def select_output_folder_converter(self):
        folder_path = QFileDialog.getExistingDirectory(None, "Select Output Folder")
        if folder_path:
            self.ui.outputFolder2.setText(folder_path)

    def convert_file(self):
        input_path = self.ui.fileInput2.text()
        output_folder = self.ui.outputFolder2.text()
        output_format = self.ui.saveAsFormat_2.currentText().lower()

        if not input_path or not output_folder:
            QMessageBox.critical(None, "Error", "Please select both input file and output folder.")
            return

        input_filename = os.path.basename(input_path)
        output_filename = os.path.splitext(input_filename)[0] + f".{output_format}"
        output_path = os.path.join(output_folder, output_filename)

        if not os.path.exists(output_folder):
            try:
                os.makedirs(output_folder)
            except OSError as e:
                QMessageBox.critical(None, "Error", f"Failed to create output folder: {e}")
                return

        if os.path.isfile(output_path):
            overwrite = QMessageBox.question(None, "Overwrite Existing File",
                "An existing file with the same name already exists.\n\nDo you want to overwrite it?",
                QMessageBox.Yes | QMessageBox.No)
            if overwrite == QMessageBox.No:
                return

        try:
            with Image.open(input_path) as img:
                if self.input_format == 'gif' and output_format != 'gif':
                    img.seek(0)
                    if output_format == 'jpeg':
                        if img.mode == 'RGBA':
                            img = img.convert('RGB')
                    elif output_format == 'bmp':
                        if img.mode != 'RGB':
                            img = img.convert('RGB')
                img.save(output_path, format=output_format.upper())

            self.ui.statusbar.showMessage("Image converted successfully!")
            QMessageBox.information(None, "Success", "Image converted successfully!")
        except Exception as e:
            self.ui.statusbar.showMessage(f"Error: {str(e)}")
            QMessageBox.critical(None, "Error", f"An error occurred: {str(e)}")