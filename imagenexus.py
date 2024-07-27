# This Python file uses the following encoding: utf-8
import sys
import os
import io
from PIL import Image, UnidentifiedImageError
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QColorDialog, QGraphicsScene
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QImage
from ui_form import Ui_ImageNexus
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
from aboutDialog import aboutDialog
from version import appVersion
from pixelizer import Pixelize


version = appVersion

class ImageNexus(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ImageNexus()
        self.ui.setupUi(self)
        self.setup_connections()
        self.setWindowTitle(f"ImageNexus v{version}")
        self.pixelizer = Pixelize(self.ui)


    def setup_connections(self):
        # Frame Extractor tab
        self.ui.browseInput1.clicked.connect(self.select_gif)
        self.ui.browseOutput1.clicked.connect(self.select_output_folder)
        self.ui.extractor_button.clicked.connect(self.extract_frames)

        # Image Converter tab
        self.ui.inputBrowse2.clicked.connect(self.select_input_file)
        self.ui.outputBrowse2.clicked.connect(self.select_output_folder_converter)
        self.ui.converter_button.clicked.connect(self.convert_file)

        # Batch Converter tab
        self.ui.inputBrowse3.clicked.connect(self.select_batch_input)
        self.ui.outputBrowse3.clicked.connect(self.select_output_folder_batch)
        self.ui.converter_button2.clicked.connect(self.convert_batch)

        # QR Code Generator tab
        self.ui.qrGenButton.clicked.connect(self.preview_qr_code)
        self.ui.saveQRButton.clicked.connect(self.save_qr_code)
        self.ui.browseFolderButton.clicked.connect(self.browse_output_folder)
        self.ui.logoBrowseButton.clicked.connect(self.browse_logo)
        self.ui.bgColourButton.clicked.connect(lambda: self.choose_color('bg'))
        self.ui.codeColourButton.clicked.connect(lambda: self.choose_color('code'))
        self.ui.addBgCheckbox.stateChanged.connect(self.preview_qr_code)
        self.ui.aspectRatioCheck.stateChanged.connect(self.preview_qr_code)

        # Help Menu
        self.ui.actionAbout.triggered.connect(self.show_about)

    def show_about(self):
        self.about_dialog = aboutDialog(self)
        self.about_dialog.setAttribute(Qt.WA_DeleteOnClose)
        self.about_dialog.show()



    def select_gif(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select GIF", "", "Image files (*.gif *.webp)")
        if file_path:
            self.ui.fileInput1.setText(file_path)

    def select_output_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Output Folder")
        if folder_path:
            self.ui.output_folder_entry.setText(folder_path)

    def select_input_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Input File", "", "Image files (*.gif *.png *.jpg *.jpeg *.bmp *.tiff)")
        if file_path:
            self.ui.fileInput2.setText(file_path)
            self.input_format = os.path.splitext(file_path)[1][1:].lower()

    def select_output_folder_converter(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Output Folder")
        if folder_path:
            self.ui.outputFolder2.setText(folder_path)

    def select_batch_input(self):
        conversion_type = self.ui.conversionType.currentText()
        if conversion_type == "Files":
            file_paths, _ = QFileDialog.getOpenFileNames(self, "Select Input Files", "", "Image files (*.gif *.png *.jpg *.jpeg *.bmp *.tiff)")
            self.ui.fileInput3.setText(", ".join(file_paths))
        elif conversion_type == "Folder":
            folder_path = QFileDialog.getExistingDirectory(self, "Select Input Folder")
            self.ui.fileInput3.setText(folder_path)

    def select_output_folder_batch(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Output Folder")
        if folder_path:
            self.ui.outputFolder3.setText(folder_path)

    def extract_frames(self):
        gif_path = self.ui.fileInput1.text()
        output_folder = self.ui.output_folder_entry.text()
        file_type = self.ui.saveAsFormat.currentText().lower()
        generate_frame_info = self.ui.generate_infocheckBox.isChecked()

        if not gif_path or not output_folder:
            QMessageBox.critical(self, "Error", "Please select both GIF file and output folder.")
            return

        if not os.path.exists(output_folder):
            try:
                os.makedirs(output_folder)
            except OSError as e:
                QMessageBox.critical(self, "Error", f"Failed to create output folder: {e}")
                return

        existing_files = [f for f in os.listdir(output_folder) if f.startswith('frame_') and f.endswith(f'.{file_type}')]
        filecount = len(existing_files)
        if filecount > 0:
            overwrite = QMessageBox.question(self, "Overwrite Existing Files", 
                f"The output folder already contains {filecount} existing files with the same name.\n\nDo you want to overwrite these files?",
                QMessageBox.Yes | QMessageBox.No)
            if overwrite == QMessageBox.No:
                return

        try:
            with Image.open(gif_path) as img:
                self.ui.progressBar.setMaximum(img.n_frames)
                frame_info = []
                total_duration = 0

                for i in range(img.n_frames):
                    img.seek(i)
                    duration = img.info.get('duration', 0) / 1000
                    total_duration += duration
                    frame_info.append((i, duration, total_duration))

                    frame_filename = f"frame_{i:03d}_{duration:.3f}s.{file_type}"
                    frame_path = os.path.join(output_folder, frame_filename)

                    if file_type == 'gif':
                        single_frame = Image.new('RGBA', img.size)
                        single_frame.paste(img)
                        single_frame.info = img.info
                        single_frame.save(frame_path, format='GIF', save_all=True, append_images=[], duration=duration, loop=1)
                    else:
                        img.save(frame_path)

                    self.ui.progressBar.setValue(i + 1)
                    self.ui.statusbar.showMessage(f"Extracting frame {i+1} of {img.n_frames}")
                    QApplication.processEvents()

                if generate_frame_info:
                    self.generate_frame_info_file(output_folder, frame_info)

            self.ui.statusbar.showMessage("Frames extracted successfully!")
            QMessageBox.information(self, "Success", "Frames extracted successfully!")
        except Exception as e:
            self.ui.statusbar.showMessage(f"Error: {str(e)}")
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
        finally:
            self.ui.progressBar.setValue(0)

    def generate_frame_info_file(self, output_folder, frame_info):
        info_file_path = os.path.join(output_folder, "frame_info.txt")
        with open(info_file_path, 'w') as f:
            f.write("Frame Information:\n")
            f.write("------------------\n")
            total_time = frame_info[-1][2]
            fps = len(frame_info) / total_time
            f.write(f"FPS: {fps:.2f}\n\n")
            for frame, duration, total_time in frame_info:
                f.write(f"Frame {frame:03d}: Duration = {duration:.3f}s, Total Time = {total_time:.3f}s\n")

    def convert_file(self):
        input_path = self.ui.fileInput2.text()
        output_folder = self.ui.outputFolder2.text()
        output_format = self.ui.saveAsFormat_2.currentText().lower()

        if not input_path or not output_folder:
            QMessageBox.critical(self, "Error", "Please select both input file and output folder.")
            return

        input_filename = os.path.basename(input_path)
        output_filename = os.path.splitext(input_filename)[0] + f".{output_format}"
        output_path = os.path.join(output_folder, output_filename)

        if not os.path.exists(output_folder):
            try:
                os.makedirs(output_folder)
            except OSError as e:
                QMessageBox.critical(self, "Error", f"Failed to create output folder: {e}")
                return

        if os.path.isfile(output_path):
            overwrite = QMessageBox.question(self, "Overwrite Existing File",
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
            QMessageBox.information(self, "Success", "Image converted successfully!")
        except Exception as e:
            self.ui.statusbar.showMessage(f"Error: {str(e)}")
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

    def convert_batch(self):
        input_paths = self.ui.fileInput3.text()
        output_folder = self.ui.outputFolder3.text()
        output_format = self.ui.formatOptions.currentText().lower()

        if not input_paths or not output_folder:
            QMessageBox.critical(self, "Error", "Please select input files/folder and output folder.")
            return

        conversion_type = self.ui.conversionType.currentText()

        if conversion_type == "Files":
            input_paths = input_paths.split(", ")
            self.convert_batch_files(input_paths, output_folder, output_format)
        elif conversion_type == "Folder":
            self.convert_batch_folder(input_paths, output_folder, output_format)

    def convert_jpeg_mode(self, img):
        if img.mode == 'RGB':
            img = img.convert('RGB')
        elif img.mode == 'RGBA':
            img = img.convert('RGB')
        elif img.mode == 'LA':
            img = img.convert('L')
        return img

    def convert_batch_folder(self, folder_path, output_folder, output_format):
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

                                img.save(output_path, format=output_format)

                            self.ui.statusbar.showMessage(f"File {input_path} converted successfully!")
                        except UnidentifiedImageError:
                            self.ui.statusbar.showMessage(f"Skipping invalid image file: {input_path}")
                        except Exception as e:
                            self.ui.statusbar.showMessage(f"Error converting {input_path}: {str(e)}")
                    else:
                        self.ui.statusbar.showMessage(f"Skipping unsupported file: {input_path}")
                elif extension.lower() not in ['.exe', '.dll', '.sys', '.bat', '.cmd']:
                    self.ui.statusbar.showMessage(f"Skipping unsupported file: {input_path}")

        QMessageBox.information(self, "Success", "Batch conversion completed!")

    def convert_batch_files(self, input_paths, output_folder, output_format):
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
                            QMessageBox.critical(self, "Error", f"Failed to create output folder: {e}")
                        return

                    if output_format == 'jpeg':
                        img = self.convert_jpeg_mode(img)
                    elif output_format == 'bmp':
                        if img.mode != 'RGB':
                            img = img.convert('RGB')

                    output_filename = os.path.splitext(os.path.basename(input_path))[0] + f".{output_format}"
                    output_path = os.path.join(output_folder, output_filename)

                    img.save(output_path, format=output_format.upper())

                self.ui.statusbar.showMessage(f"File {input_path} converted successfully!")
            except Exception as e:
                self.ui.statusbar.showMessage(f"Error converting {input_path}: {str(e)}")

        QMessageBox.information(self, "Success", "Batch conversion completed!")
### QR Code Generator Start ###
    def preview_qr_code(self):
        qr_image = self.generate_qr_code()
        if qr_image:
            self.display_qr_code(qr_image)

    def generate_qr_code(self):
        qr_data = self.ui.qrTextInput.toPlainText()
        if not qr_data:
            QMessageBox.warning(self, "Warning", "Please enter some data for the QR code.")
            return None

        qr = qrcode.QRCode(
            version=self.ui.qrSizeSpinBox.value(),
            error_correction=self.get_error_correction(),
            box_size=40,
            border=self.ui.borderSpinBox.value(),
        )
        qr.add_data(qr_data)
        qr.make(fit=True)

        # Convert color strings to tuples
        def color_string_to_tuple(color_string):
            return tuple(map(int, color_string.split(',')))
        
        def get_color(color_input, default):
            color_text = color_input.text().strip()
            return color_string_to_tuple(color_text) if color_text else default

        #bg_color = color_string_to_tuple(self.ui.bgColourInput.text())
        #fill_color = color_string_to_tuple(self.ui.codeColourInput.text())
        bg_color = get_color(self.ui.bgColourInput, (255, 255, 255))
        fill_color = get_color(self.ui.codeColourInput, (0, 0, 0))

        # Create the QR code image
        qr_image = qr.make_image(
            fill_color=fill_color,
            back_color=bg_color,

        )

        logo_path = self.ui.logoImageInput.text()
        if logo_path and os.path.isfile(logo_path):
            logo = Image.open(logo_path).convert('RGBA')
            
            qr_size = qr_image.size[0]
            max_size = qr_size // 3

            # Preserve aspect ratio
            if self.ui.aspectRatioCheck.isChecked():
                ratio = min(max_size / logo.width, max_size / logo.height)
                new_size = (int(logo.width * ratio), int(logo.height * ratio))
            else:
                new_size = (max_size, max_size)

            logo = logo.resize(new_size, Image.LANCZOS)

            # Create a new image with the background if checkbox is checked
            if self.ui.addBgCheckbox.isChecked():
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
        error_correction = self.ui.errorCorrectionCombo.currentText()
        if error_correction == "Low":
            return qrcode.constants.ERROR_CORRECT_L
        elif error_correction == "Medium":
            return qrcode.constants.ERROR_CORRECT_M
        elif error_correction == "Quartile":
            return qrcode.constants.ERROR_CORRECT_Q
        else:
            return qrcode.constants.ERROR_CORRECT_H

    def display_qr_code(self, qr_image):
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
        output_folder = self.ui.outputFolderText.text()
        if not output_folder:
            QMessageBox.warning(self, "Warning", "Please select an output folder.")
            return
        # Check if output folder exists, if not create it
        if not os.path.exists(output_folder):
            try:
                os.makedirs(output_folder)
            except OSError as e:
                QMessageBox.critical(self, "Error", f"Failed to create output folder: {e}")
                return

        qr_image = self.generate_qr_code()
        if qr_image:
            # ensure the image is 1024x1024
            qr_image= qr_image.resize((1024, 1024), Image.LANCZOS)
            
            save_format = self.ui.saveAsComboBox.currentText().lower()
            file_name = f"qr_code.{save_format}"
            file_path = os.path.join(output_folder, file_name)

            qr_image.save(file_path)
            QMessageBox.information(self, "Success", f"QR code saved as {file_path}")



    def browse_output_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Output Folder")
        if folder_path:
            self.ui.outputFolderText.setText(folder_path)

    def browse_logo(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Logo Image", "", "Image Files (*.png *.jpg *.bmp)")
        if file_path:
            self.ui.logoImageInput.setText(file_path)

    def choose_color(self, color_type):
        color = QColorDialog.getColor()
        if color.isValid():
            rgb_values = f"{color.red()}, {color.green()}, {color.blue()}"
            if color_type == 'bg':
                self.ui.bgColourInput.setText(rgb_values)
            else:
                self.ui.codeColourInput.setText(rgb_values)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if self.ui.qrOutputView.scene():

            self.ui.qrOutputView.fitInView(self.ui.qrOutputView.scene().sceneRect(), Qt.KeepAspectRatio)

        if hasattr(self, 'pixelizer'):
            self.pixelizer.resize_image()

### QR Code Generator End ###

#TODO: Add built-in templates for these QR formats, making it easier to create specialized QR codes.
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = ImageNexus()
    widget.show()
    sys.exit(app.exec())
