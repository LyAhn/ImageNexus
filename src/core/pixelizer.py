from PIL import Image, UnidentifiedImageError, ExifTags, ImageSequence
from PySide6.QtWidgets import QFileDialog, QMessageBox, QGraphicsScene
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt
import traceback
import os

class Pixelize:
    def __init__(self, ui):
        self.ui = ui
        self.image = None
        self.pixelated_image = None
        self.original_file_path = None
        self.last_save_directory = None
        self.setup_connections()

    def setup_connections(self):
        self.ui.pxLoadImageBtn.clicked.connect(self.load_image_for_pixelation)
        self.ui.pxPixelateBtn.clicked.connect(self.process_image)
        self.ui.pxSizeSlider.valueChanged.connect(self.ui.pxSpinBox.setValue)
        self.ui.pxSpinBox.valueChanged.connect(self.ui.pxSizeSlider.setValue)
        self.ui.pxSaveBtn.clicked.connect(self.save_pixelated_image)

    def save_dialog(self):
        if self.pixelated_image is None:
            QMessageBox.warning(None, "Warning", "Please pixelate an image first.")
            return

        selected_format = self.ui.pxFileFormats.currentText().lower()
        file_filter = f"{selected_format.upper()} Files (*.{selected_format})"
        file_path, _ = QFileDialog.getSaveFileName(
            None,
            "Save Image",
            "",
            file_filter
        )

        if file_path:
            self.save_pixelated_image(file_path)

    def load_image_for_pixelation(self):
        file_path, _ = QFileDialog.getOpenFileName(
            None,
            "Select Image",
            "",
            "Image files (*.png *.jpg *.jpeg *.bmp *.gif *.tiff *.webp)"
        )
        if file_path:
            if self.load_image(file_path):
                self.ui.statusbar.showMessage("Image loaded successfully!")
                self.display_image()
            else:
                QMessageBox.critical(None, "Error", "Failed to load image.")

    def load_image(self, file_path):
        try:
            self.original_file_path = file_path
            with Image.open(file_path) as img:
                # Handle transparency
                if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
                    # Convert to RGBA if it's not already
                    img = img.convert('RGBA')

                    # Create a new image with dark but not black background
                    background = Image.new('RGBA', img.size, (31, 31, 31, 31))

                    # Paste the image on the background, using its alpha channel as mask
                    background.paste(img, (0, 0), img)

                    # Convert to RGB
                    self.image = background.convert('RGB')
                else:
                    self.image = img.convert('RGB')

                # Check if the image is a GIF
                if img.format == 'GIF' and getattr(img, 'is_animated', False):
                    # Extract the first frame of the GIF
                    frames = list(ImageSequence.Iterator(img))
                    self.image = frames[0].convert('RGB')

                # Handle EXIF orientation
                for orientation in ExifTags.TAGS.keys():
                    if ExifTags.TAGS[orientation] == 'Orientation':
                        break

                try:
                    exif = self.image._getexif()
                    if exif is not None:
                        exif = dict(exif.items())
                        if orientation in exif:
                            if exif[orientation] == 3:
                                self.image = self.image.rotate(180, expand=True)
                            elif exif[orientation] == 6:
                                self.image = self.image.rotate(270, expand=True)
                            elif exif[orientation] == 8:
                                self.image = self.image.rotate(90, expand=True)
                except AttributeError:
                    # Image doesn't have _getexif method, skip EXIF processing
                    pass

                # Debug information
                print(f"Image mode: {self.image.mode}")
                print(f"Image size: {self.image.size}")
                print(f"Image format: {self.image.format}")

                return True

        except UnidentifiedImageError:
            print(f"Cannot identify image file: {file_path}")
            error_message = (
                "The selected file could not be loaded as an image.\n\n"
                "Possible reasons:\n"
                "- The file may be corrupted. \n"
                "- The file may not actually be an image file. \n"
                "- The file may be an unsupported image format.\n\n"
                "Please check the file and try again with a valid image."
            )
            QMessageBox.critical(None, "Error Loading Image", error_message)
            return False

        except Exception as e:
            print(f"Error loading image: {e}")
            traceback.print_exc()
            error_message = f"An unexpected error occurred while loading the image:\n\n{str(e)}"
            QMessageBox.critical(None, "Error", error_message)
            return False


    def process_image(self):
        if self.image is None:
            QMessageBox.warning(None, "Warning", "Please load an image first.")
            return

        try:
            pixel_size = self.ui.pxSpinBox.value()
            pixelated_image = self.pixelize_image(pixel_size)
            if pixelated_image:
                self.display_image(pixelated=True)
                self.ui.statusbar.showMessage("Image pixelated successfully!")
            else:
                QMessageBox.critical(None, "Error", "Failed to pixelate image.")
        except Exception as e:
            QMessageBox.critical(None, "Error", f"An error occurred while pixelating: {str(e)}")
            traceback.print_exc()

    def pixelize_image(self, pixel_size):
        width, height = self.image.size
        new_width = max(1, width // pixel_size)
        new_height = max(1, height // pixel_size)

        # Resize the image to create pixelation effect
        small = self.image.resize((new_width, new_height), Image.BILINEAR)
        self.pixelated_image = small.resize((width, height), Image.NEAREST)
        return self.pixelated_image

    def get_pixmap(self, pixelated=False):
        image = self.pixelated_image if pixelated else self.image
        if image is None:
            return None

        # Convert PIL Image to QPixmap
        data = image.tobytes("raw", "RGB")
        qimage = QImage(data, image.width, image.height, image.width * 3, QImage.Format_RGB888)
        return QPixmap.fromImage(qimage)

    def resize_image(self):
        if self.image:
            self.display_image(pixelated=self.pixelated_image is not None)

    def display_image(self, pixelated=False):
        pixmap = self.get_pixmap(pixelated)
        if pixmap:
            scene = QGraphicsScene()
            scene.addPixmap(pixmap)
            self.ui.pxGraphicsView.setScene(scene)
            self.ui.pxGraphicsView.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)

    def save_pixelated_image(self):
        if self.pixelated_image is None:
            QMessageBox.warning(None, "Warning", "Please pixelate an image first.")
            return False

        # Get the selected file format from the QComboBox
        selected_format = self.ui.pxFileFormats.currentText().lower()
        # Get the pixel size used for pixelation
        pixel_size = self.ui.pxSpinBox.value()
        # Create a file filter based on the selected format
        file_filter = f"{selected_format.upper()} Files (*.{selected_format})"
        # Get the original file name without extension
        original_filename = os.path.splitext(os.path.basename(self.original_file_path))[0]
        # Create the suggested file name
        suggested_filename = f"{original_filename}_Pixelated_{pixel_size}px.{selected_format}"

        # Open a file dialog to choose the save location
        file_path, _ = QFileDialog.getSaveFileName(
            None,
            "Save Pixelated Image",
            suggested_filename,
            file_filter
        )

        if not file_path:  # User cancelled the dialog
            return False

        try:
            # Ensure the file has the correct extension
            if not file_path.lower().endswith(f".{selected_format}"):
                file_path += f".{selected_format}"

            # Save the image in the selected format
            self.pixelated_image.save(file_path, format=selected_format.upper())
            self.ui.statusbar.showMessage(f"Image saved successfully as {file_path}")

            # Update the last save directory
            self.last_save_directory = os.path.dirname(file_path)
            return True
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Failed to save image: {str(e)}")
            print(f"Error saving image: {e}")
            traceback.print_exc()
            return False

#TODO: Add drag and drop support