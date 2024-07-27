import os
from PIL import Image, UnidentifiedImageError
from PySide6.QtWidgets import QFileDialog, QMessageBox

class BatchConvert:

    def __init__(self, ui):
        self.ui = ui
        self.setup_connections()


    def setup_connections(self):
        self.ui.inputBrowse3.clicked.connect(self.select_batch_input)
        self.ui.outputBrowse3.clicked.connect(self.select_output_folder_batch)
        self.ui.converter_button2.clicked.connect(self.convert_batch)

    def select_batch_input(self):
        conversion_type = self.ui.conversionType.currentText()
        if conversion_type == "Files":
            file_paths, _ = QFileDialog.getOpenFileNames(None, "Select Input Files", "", "Image files (*.gif *.png *.jpg *.jpeg *.bmp *.tiff)")
            self.ui.fileInput3.setText(", ".join(file_paths))
        elif conversion_type == "Folder":
            folder_path = QFileDialog.getExistingDirectory(None, "Select Input Folder")
            self.ui.fileInput3.setText(folder_path)

    def select_output_folder_batch(self):
        folder_path = QFileDialog.getExistingDirectory(None, "Select Output Folder")
        if folder_path:
            self.ui.outputFolder3.setText(folder_path)


    def convert_batch(self):
        input_paths = self.ui.fileInput3.text()
        output_folder = self.ui.outputFolder3.text()
        output_format = self.ui.formatOptions.currentText().lower()

        if not input_paths or not output_folder:
            QMessageBox.critical(None, "Error", "Please select input files/folder and output folder.")
            return

        # Add overwrite check here
        existing_files = [f for f in os.listdir(output_folder) if f.endswith(f'.{output_format}')]
        filecount = len(existing_files)
        
        if filecount > 0:
            overwrite = QMessageBox.question(None, "Overwrite Existing Files",
                                            f"The output folder already contains {filecount} existing files with the same format.\n\nDo you want to overwrite these files?",
                                            QMessageBox.Yes | QMessageBox.No)
            if overwrite == QMessageBox.No:
                return

        conversion_type = self.ui.conversionType.currentText()
        
        if conversion_type == "Files":
            input_paths = input_paths.split(", ")
            self.convert_batch_files(input_paths, output_folder, output_format, overwrite == QMessageBox.Yes)
        elif conversion_type == "Folder":
            self.convert_batch_folder(input_paths, output_folder, output_format, overwrite == QMessageBox.Yes)


    def convert_jpeg_mode(self, img):
        if img.mode == 'RGB':
            img = img.convert('RGB')
        elif img.mode == 'RGBA':
            img = img.convert('RGB')
        elif img.mode == 'LA':
            img = img.convert('L')
        return img

    def convert_batch_folder(self, folder_path, output_folder, output_format, overwrite):
        image_extensions = ['.gif', '.png', '.jpg', '.jpeg', '.bmp', '.tiff']
        supported_formats = ['GIF', 'PNG', 'JPEG', 'JPG', 'BMP', 'TIFF']

        for root, dirs, files in os.walk(folder_path):
            for file in files:
                input_path = os.path.join(root, file)
                extension = os.path.splitext(input_path)[1].lower()
                input_format = extension[1:].upper()

                if extension in image_extensions:
                    if input_format in supported_formats:
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

                        except UnidentifiedImageError:
                            self.ui.statusbar.showMessage(f"Skipping invalid image file: {input_path}")
                        except Exception as e:
                            self.ui.statusbar.showMessage(f"Error converting {input_path}: {str(e)}")
                    else:
                        self.ui.statusbar.showMessage(f"Skipping unsupported file: {input_path}")
                elif extension.lower() not in ['.exe', '.dll', '.sys', '.bat', '.cmd']:
                    self.ui.statusbar.showMessage(f"Skipping unsupported file: {input_path}")

        QMessageBox.information(None, "Success", "Batch conversion completed!")

    def convert_batch_files(self, input_paths, output_folder, output_format, overwrite):
        for input_path in input_paths:
            try:
                with Image.open(input_path) as img:
                    input_format = img.format.lower()
                    if input_format == 'gif' and output_format != 'gif':
                        img.seek(0)

                    if not os.path.exists(output_folder):
                        try:
                            os.makedirs(output_folder)
                        except OSError as e:
                            QMessageBox.critical(None, "Error", f"Failed to create output folder: {e}")
                            return

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

            except Exception as e:
                self.ui.statusbar.showMessage(f"Error converting {input_path}: {str(e)}")

        QMessageBox.information(None, "Success", "Batch conversion completed!")