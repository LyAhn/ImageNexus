"""
This file is part of ImageNexus

ImageNexus is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation

Copyright (c) 2024, LyAhn

This code is licensed under the GPL-3.0 license (see LICENSE.txt for details)
"""

import os
from PIL import Image, UnidentifiedImageError
from PySide6.QtWidgets import QFileDialog, QMessageBox

class BatchConvert:

    def __init__(self, ui):
        self.ui = ui
        self.setup_connections()

    def setup_connections(self):
        self.ui.bcInputBrowse.clicked.connect(self.select_batch_input)
        self.ui.bcOutputBrowse.clicked.connect(self.select_output_folder_batch)
        self.ui.bcConvertBtn.clicked.connect(self.convert_batch)

    def select_batch_input(self):
        conversion_type = self.ui.conversionType.currentText()
        if conversion_type == "Files":
            file_paths, _ = QFileDialog.getOpenFileNames(None, "Select Input Files", "", "Image files (*.gif *.png *.jpg *.jpeg *.bmp *.tiff)")
            self.ui.bcFileInput.setText(", ".join(file_paths))
        elif conversion_type == "Folder":
            folder_path = QFileDialog.getExistingDirectory(None, "Select Input Folder")
            self.ui.bcFileInput.setText(folder_path)

    def select_output_folder_batch(self):
        folder_path = QFileDialog.getExistingDirectory(None, "Select Output Folder")
        if folder_path:
            self.ui.bcOutputFolder.setText(folder_path)


    def convert_batch(self):
        input_paths = self.ui.bcFileInput.text()
        output_folder = self.ui.bcOutputFolder.text()
        output_format = self.ui.formatOptions.currentText().lower()

        if not os.path.exists(output_folder):
            try:
                os.makedirs(output_folder)
            except OSError as e:
                QMessageBox.critical(None, "Error", f"Failed to create output folder: {e}")
                return

        if not input_paths or not output_folder:
            QMessageBox.critical(None, "Error", "Please select input files/folder and output folder.")
            return

        conversion_type = self.ui.conversionType.currentText()

        # Check for existing files before conversion
        existing_files_count = self.count_existing_files(input_paths, output_folder, output_format, conversion_type)

        # Single overwrite confirmation dialog
        overwrite = True

        if existing_files_count > 0:
            message = f"{existing_files_count} file(s) with the same name and format already exist in the output folder.\n\nDo you want to overwrite these files?"
            reply = QMessageBox.question(None, "Overwrite Existing Files", message,
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            overwrite = (reply == QMessageBox.Yes)

        skipped_files_count = 0
        if conversion_type == "Files":
            input_paths = input_paths.split(", ")
            skipped_files_count = self.convert_batch_files(input_paths, output_folder, output_format, overwrite)
        elif conversion_type == "Folder":
            skipped_files_count = self.convert_batch_folder(input_paths, output_folder, output_format, overwrite)

        if skipped_files_count > 0:
            QMessageBox.information(None, "Batch Conversion Complete", 
                                    f"Batch conversion completed.\n{skipped_files_count} file(s) were skipped due to existing files.")
        else:
            QMessageBox.information(None, "Success", "Batch conversion completed!")

    def count_existing_files(self, input_paths, output_folder, output_format, conversion_type):
        existing_files_count = 0
        if conversion_type == "Files":
            for input_path in input_paths.split(", "):
                output_filename = os.path.splitext(os.path.basename(input_path))[0] + f".{output_format}"
                output_path = os.path.join(output_folder, output_filename)
                if os.path.exists(output_path):
                    existing_files_count += 1
        elif conversion_type == "Folder":
            for root, _, files in os.walk(input_paths):
                for file in files:
                    if file.lower().endswith(('.gif', '.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
                        output_filename = os.path.splitext(file)[0] + f".{output_format}"
                        output_path = os.path.join(output_folder, output_filename)
                        if os.path.exists(output_path):
                            existing_files_count += 1
        return existing_files_count

    def convert_jpeg_mode(self, img):
        if img.mode == 'RGB':
            img = img.convert('RGB')
        elif img.mode == 'RGBA':
            img = img.convert('RGB')
        elif img.mode == 'LA':
            img = img.convert('L')
        return img

    def convert_batch_folder(self, folder_path, output_folder, output_format, overwrite):
        skipped_files_count = 0
        image_extensions = ['.gif', '.png', '.jpg', '.jpeg', '.bmp', '.tiff']
        supported_formats = ['GIF', 'PNG', 'JPEG', 'JPG', 'BMP', 'TIFF']

        if not os.path.exists(output_folder):
            try:
                os.makedirs(output_folder)
            except OSError as e:
                QMessageBox.critical(None, "Error", f"Failed to create output folder: {e}")
                return

        for root, dirs, files in os.walk(folder_path):
            for file in files:
                input_path = os.path.join(root, file)
                extension = os.path.splitext(input_path)[1].lower()
                input_format = extension[1:].upper()

                if extension in image_extensions and input_format in supported_formats:
                    try:
                        with Image.open(input_path) as img:
                            if input_format == 'GIF' and output_format != 'GIF':
                                img.seek(0)
                            if output_format == 'jpeg':
                                img = self.convert_jpeg_mode(img)
                            elif output_format == 'BMP':
                                if img.mode != 'RGB':
                                    img = img.convert('RGB')

                            output_filename = os.path.splitext(file)[0] + f".{output_format}"
                            output_path = os.path.join(output_folder, output_filename)

                            if not os.path.exists(output_path) or overwrite:
                                img.save(output_path, format=output_format)
                                self.ui.statusbar.showMessage(f"File {input_path} converted successfully!")
                            else:
                                self.ui.statusbar.showMessage(f"Skipped existing file: {output_path}")
                                skipped_files_count += 1

                    except UnidentifiedImageError:
                        self.ui.statusbar.showMessage(f"Skipping invalid image file: {input_path}")
                    except Exception as e:
                        self.ui.statusbar.showMessage(f"Error converting {input_path}: {str(e)}")
                else:
                    self.ui.statusbar.showMessage(f"Skipping unsupported file: {input_path}")

        return skipped_files_count

    def convert_batch_files(self, input_paths, output_folder, output_format, overwrite):
        skipped_files_count = 0

        if not os.path.exists(output_folder):
            try:
                os.makedirs(output_folder)
            except OSError as e:
                QMessageBox.critical(None, "Error", f"Failed to create output folder: {e}")
                return

        for input_path in input_paths:
            try:
                with Image.open(input_path) as img:
                    input_format = img.format.lower()
                    if input_format == 'gif' and output_format != 'gif':
                        img.seek(0)

                    if output_format == 'jpeg':
                        img = self.convert_jpeg_mode(img)
                    elif output_format == 'bmp':
                        if img.mode != 'RGB':
                            img = img.convert('RGB')

                    output_filename = os.path.splitext(os.path.basename(input_path))[0] + f".{output_format}"
                    output_path = os.path.join(output_folder, output_filename)

                    if not os.path.exists(output_path) or overwrite:
                        img.save(output_path, format=output_format.upper())
                        self.ui.statusbar.showMessage(f"File {input_path} converted successfully!")
                    else:
                        self.ui.statusbar.showMessage(f"Skipped existing file: {output_path}")
                        skipped_files_count += 1

            except Exception as e:
                self.ui.statusbar.showMessage(f"Error converting {input_path}: {str(e)}")

        return skipped_files_count