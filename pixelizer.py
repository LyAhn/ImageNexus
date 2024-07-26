import numpy as np
from PIL import Image, UnidentifiedImageError, ExifTags
from PySide6.QtWidgets import QFileDialog, QMessageBox, QGraphicsScene
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt
import traceback

class Pixelize:
    def __init__(self, ui):
        self.ui = ui
        self.image = None
        self.pixelated_image = None
        self.setup_connections()

    def setup_connections(self):
        self.ui.pxLoadImageBtn.clicked.connect(self.load_image_for_pixelation)
        self.ui.pxPixelateBtn.clicked.connect(self.pixelate_image)
        self.ui.pxSizeSlider.valueChanged.connect(self.ui.pxSpinBox.setValue)
        self.ui.pxSpinBox.valueChanged.connect(self.ui.pxSizeSlider.setValue)

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
            self.image = Image.open(file_path)
            
            # Check for EXIF orientation data
            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation] == 'Orientation':
                    break
            
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
            
            # Convert to RGB mode
            self.image = self.image.convert('RGB')
            
            # Debug information
            print(f"Image mode: {self.image.mode}")
            print(f"Image size: {self.image.size}")
            print(f"Image format: {self.image.format}")
            
            return True
        except Exception as e:
            print(f"Error loading image: {e}")
            traceback.print_exc()
            return False

    def pixelate_image(self):
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

    def save_pixelated_image(self, file_path):
        if self.pixelated_image is None:
            return False
        try:
            self.pixelated_image.save(file_path)
            return True
        except Exception as e:
            print(f"Error saving image: {e}")
            traceback.print_exc()
            return False