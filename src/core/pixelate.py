"""
This file is part of ImageNexus

ImageNexus is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation

Copyright (c) 2024, LyAhn

This code is licensed under the GPL-3.0 license (see LICENSE.txt for details)
"""

import cv2
import numpy as np
from PIL import UnidentifiedImageError
from PySide6.QtWidgets import QFileDialog, QMessageBox, QGraphicsScene
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt
import traceback
import os

class Pixelate:
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
            self.image = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)

            if self.image is None:
                raise ValueError("Image could not be loaded")

            # Convert BGR to RGB
            if len(self.image.shape) == 3 and self.image.shape[2] == 3:
                self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            elif len(self.image.shape) == 3 and self.image.shape[2] == 4:
                self.image = cv2.cvtColor(self.image, cv2.COLOR_BGRA2RGBA)

            # Debug information
            print(f"Image shape: {self.image.shape}")
            print(f"Image dtype: {self.image.dtype}")

            return True
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
            self.pixelated_image = self.pixelize_image(pixel_size)
            if self.pixelated_image is not None:
                self.display_image(pixelated=True)
                self.ui.statusbar.showMessage("Image pixelated successfully!")
            else:
                QMessageBox.critical(None, "Error", "Failed to pixelate image.")
        except Exception as e:
            QMessageBox.critical(None, "Error", f"An error occurred while pixelating: {str(e)}")
            traceback.print_exc()

    def pixelize_image(self, pixel_size):
        if self.image is None:
            return None

        # Convert image to NumPy array if it's not already
        img_array = np.array(self.image)
        height, width = img_array.shape[:2]

        # Calculate new dimensions
        h = height // pixel_size
        w = width // pixel_size

        # Reshape and compute mean of pixel blocks
        pixelated = img_array[:h*pixel_size, :w*pixel_size].reshape(h, pixel_size, w, pixel_size, -1).mean(axis=(1, 3))

        # Repeat each pixel to create the pixelated effect
        pixelated = np.repeat(np.repeat(pixelated, pixel_size, axis=0), pixel_size, axis=1)

        # Handle potential size mismatch due to integer division
        if pixelated.shape[0] < height or pixelated.shape[1] < width:
            pad_h = height - pixelated.shape[0]
            pad_w = width - pixelated.shape[1]
            pixelated = np.pad(pixelated, ((0, pad_h), (0, pad_w), (0, 0)), mode='edge')
        elif pixelated.shape[0] > height or pixelated.shape[1] > width:
            pixelated = pixelated[:height, :width]

        # Ensure the output is in the correct data type
        self.pixelated_image = pixelated.astype(np.uint8)

        return self.pixelated_image

    def get_pixmap(self, pixelated=False):
        image = self.pixelated_image if pixelated else self.image
        if image is None:
            return None

        height, width = image.shape[:2]
        bytes_per_line = 3 * width
        if len(image.shape) == 3 and image.shape[2] == 4:  # RGBA
            qimage = QImage(image.data, width, height, 4 * width, QImage.Format_RGBA8888)
        else:  # RGB
            qimage = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888)
        return QPixmap.fromImage(qimage)

    def resize_image(self):
        if self.image is not None:
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

        selected_format = self.ui.pxFileFormats.currentText().lower()
        pixel_size = self.ui.pxSpinBox.value()
        file_filter = f"{selected_format.upper()} Files (*.{selected_format})"
        original_filename = os.path.splitext(os.path.basename(self.original_file_path))[0]
        suggested_filename = f"{original_filename}_Pixelated_{pixel_size}px.{selected_format}"

        file_path, _ = QFileDialog.getSaveFileName(
            None,
            "Save Pixelated Image",
            suggested_filename,
            file_filter
        )

        if not file_path:
            return False

        try:
            if not file_path.lower().endswith(f".{selected_format}"):
                file_path += f".{selected_format}"

            # Convert RGBA to BGR or BGRA for saving
            if len(self.pixelated_image.shape) == 3 and self.pixelated_image.shape[2] == 4:
                save_image = cv2.cvtColor(self.pixelated_image, cv2.COLOR_RGBA2BGRA)
            else:
                save_image = cv2.cvtColor(self.pixelated_image, cv2.COLOR_RGB2BGR)

            cv2.imwrite(file_path, save_image)
            return True
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Failed to save image: {str(e)}")
            print(f"Error saving image: {e}")
            traceback.print_exc()
            return False

    # TODO: Add drag and drop support