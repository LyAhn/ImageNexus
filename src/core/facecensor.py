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
import os
from PySide6.QtWidgets import (
    QGraphicsScene,
    QGraphicsPixmapItem,
    QFileDialog,
    QListWidgetItem,
    QMessageBox,
    QGraphicsRectItem
)
from PySide6.QtGui import QImage, QPixmap, QPen, QColor
from PySide6.QtCore import Qt, QRectF, Signal, QObject


class ClickableRectItem(QObject, QGraphicsRectItem):
    """
    A QGraphicsRectItem that emits a signal when clicked.
    """
    faceSelected = Signal(int, bool)  # Signal: face_index, is_selected

    def __init__(self, rect, face_index, parent=None):
        QObject.__init__(self)
        QGraphicsRectItem.__init__(self, rect, parent)
        self.face_index = face_index
        self.selected = False
        self.setPen(QPen(QColor(255, 0, 0), 4)) # Red border, width of 4
        self.setBrush(Qt.NoBrush)
        self.setFlag(QGraphicsRectItem.ItemIsSelectable, True)
        self.setAcceptHoverEvents(True)

    def mousePressEvent(self, event):
        self.toggle_selection()
        event.accept()

    def toggle_selection(self):
        self.selected = not self.selected
        self.update_appearance()
        self.faceSelected.emit(self.face_index, self.selected)

    def update_appearance(self):
        color = QColor(0, 255, 0) if self.selected else QColor(255, 0, 0) # Green if selected, red if not
        self.setPen(QPen(color, 4)) # keep the border width at 4

    def hoverEnterEvent(self, event):
        self.setPen(QPen(QColor(0, 0, 255), 4)) # Blue border width of 4
        super().hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):
        self.update_appearance()
        super().hoverLeaveEvent(event)


class FaceCensor:
    """
    The main FaceCensor class that handles loading images, detecting faces,
    displaying bounding boxes, and applying censoring methods.
    """

    def __init__(self, ui):
        self.ui = ui
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Point application to app root directory
        root_dir = os.path.abspath(os.path.join(current_dir, '..', '..', '.'))
        prototxt_path = os.path.join(
            root_dir, 'resources', 'models', 'facedetection', 'deploy.prototxt'
        )
        model_path = os.path.join(
            root_dir, 'resources', 'models', 'facedetection', 'res10_300x300_ssd_iter_140000.caffemodel'
        )

        print(f"Attempting to load prototxt from: {prototxt_path}")
        print(f"Attempting to load model from: {model_path}")

        if not os.path.exists(prototxt_path):
            raise FileNotFoundError(f"Prototxt file not found at {prototxt_path}")
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found at {model_path}")

        self.face_net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)
        print("Face detection model loaded successfully.")

        self.setup_connections()
        self.pixmap_item = None
        self.ui.fcImageView.resizeEvent = self.resizeEvent
        self.selected_faces = []
        self.rect_items = []

        # Initialize the Graphics Scene once
        self.scene = QGraphicsScene()
        self.ui.fcImageView.setScene(self.scene)

    def setup_connections(self):
        self.ui.fcBrowseBtn.clicked.connect(self.load_and_detect_faces)
        self.ui.fcCensorBtn.clicked.connect(self.censor_faces)
        self.ui.fcSaveBtn.clicked.connect(self.save_image)
        self.ui.fcResetBtn.clicked.connect(self.reset_image)
        self.ui.fcBlur.toggled.connect(self.censor_faces)
        self.ui.fcBox.toggled.connect(self.censor_faces)
        self.ui.fcPixelate.toggled.connect(self.censor_faces)
        self.ui.fcBlackBar.toggled.connect(self.censor_faces)
        self.ui.fcFaceList.itemSelectionChanged.connect(self.update_selected_faces)

    def handle_face_selection(self, face_index, is_selected):
        """
        Handle selection toggling from ClickableRectItem.
        """
        if is_selected:
            if self.faces[face_index] not in self.selected_faces:
                self.selected_faces.append(self.faces[face_index])
        else:
            if self.faces[face_index] in self.selected_faces:
                self.selected_faces.remove(self.faces[face_index])
        
        # Update GUI list selection
        self.ui.fcFaceList.item(face_index).setSelected(is_selected)
        
        # Update rectangle appearance
        self.rect_items[face_index].update_appearance()
        
        self.censor_faces()

    def update_selected_faces(self):
        """
        Update the list of selected faces based on the GUI list selections.
        """
        selected_items = self.ui.fcFaceList.selectedItems()
        selected_indices = [self.ui.fcFaceList.row(item) for item in selected_items]
        self.selected_faces = [self.faces[i] for i in selected_indices]
        
        # Update rectangles' selection state
        for idx, rect_item in enumerate(self.rect_items):
            is_selected = self.faces[idx] in self.selected_faces
            rect_item.selected = is_selected
            rect_item.update_appearance()
        
        self.censor_faces()

    def detect_faces(self, image):
        """
        Detect faces in the given image using the pre-loaded face detection model.
        Returns the image with drawn bounding boxes and a list of face coordinates.
        """
        (h, w) = image.shape[:2]
        # Convert BGRA to BGR for face detection
        bgr_image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
        blob = cv2.dnn.blobFromImage(
            cv2.resize(bgr_image, (300, 300)),
            1.0,
            (300, 300),
            (104.0, 177.0, 123.0),
        )
        self.face_net.setInput(blob)
        detections = self.face_net.forward()
        faces = []
        for i in range(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > 0.5:
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
                # Ensure bounding boxes are within image dimensions
                startX = max(0, startX)
                startY = max(0, startY)
                endX = min(w - 1, endX)
                endY = min(h - 1, endY)
                faces.append((startX, startY, endX - startX, endY - startY))
        return image, faces

    def load_and_detect_faces(self):
        """
        Load an image file, detect faces, display the image with bounding boxes,
        and populate the face list.
        """
        file_path = QFileDialog.getOpenFileName(
            parent=None,
            caption="Open Image",
            dir="",
            filter="Image Files (*.png *.jpg *.bmp *.tiff *.webp)"
        )
        if file_path[0]:
            try:
                self.original_image = cv2.imread(file_path[0], cv2.IMREAD_UNCHANGED)
                if self.original_image is None:
                    raise ValueError("Failed to load image")
                # Ensure the image has an alpha channel
                if self.original_image.shape[2] == 3:
                    self.original_image = cv2.cvtColor(
                        self.original_image, cv2.COLOR_BGR2BGRA
                    )
                image_with_faces, self.faces = self.detect_faces(self.original_image.copy())
                self.display_image(image_with_faces)
                self.update_face_list(self.faces)
                self.ui.fcInputImage.setText(file_path[0])
            except Exception as e:
                QMessageBox.critical(self.ui, "Error", f"Error loading image: {e}")

    def get_censoring_method(self):
        """
        Retrieve the selected censoring method from the UI.
        """
        methods = {
            self.ui.fcBlur: "Blur",
            self.ui.fcBox: "Black Box",
            self.ui.fcPixelate: "Pixelate",
            self.ui.fcBlackBar: "Eye Bars"
        }
        for radio_button, method in methods.items():
            if radio_button.isChecked():
                return method
        return None

    def apply_censoring(self, image, draw_boxes=False):
        """
        Apply the selected censoring method to the selected faces in the image.
        """
        censoring_method = self.get_censoring_method()
        if draw_boxes:
            # Drawing is handled by ClickableRectItem
            pass
        if censoring_method:
            for x, y, w, h in self.selected_faces:
                face_roi = image[y:y + h, x:x + w]
                if censoring_method == "Blur":
                    blurred = cv2.GaussianBlur(face_roi, (119, 119), 60) # Apply strong blur: 119x119 kernel, sigma=60
                    alpha = face_roi[:, :, 3]
                    face_roi[:, :, :3] = blurred[:, :, :3]
                    face_roi[:, :, 3] = alpha
                elif censoring_method == "Black Box":
                    face_roi[:, :, :3] = (0, 0, 0)
                elif censoring_method == "Pixelate":
                    face_roi = self.pixelate(face_roi)
                elif censoring_method == "Eye Bars":
                    self.draw_eye_bars(image, x, y, w, h)
                image[y:y + h, x:x + w] = face_roi
        return image

    def apply_censoring_without_boxes(self):
        """
        Apply censoring without redrawing bounding boxes.
        """
        if not hasattr(self, 'original_image') or not hasattr(self, 'selected_faces'):
            return None
        image = self.original_image.copy()
        return self.apply_censoring(image, draw_boxes=False)

    def resizeEvent(self, event):
        """
        Handle the resize event to adjust the image view.
        """
        self.fit_image_in_view()

    def display_image(self, image):
        """
        Display the given image in the QGraphicsView, adding interactive bounding boxes.
        """
        # Clear the existing scene
        self.scene.clear()

        # Convert the image to QPixmap
        height, width = image.shape[:2]
        bytes_per_line = 4 * width
        q_image = QImage(
            image.data, width, height, bytes_per_line, QImage.Format_ARGB32
        )
        pixmap = QPixmap.fromImage(q_image)
        self.pixmap_item = QGraphicsPixmapItem(pixmap)
        self.scene.addItem(self.pixmap_item)

        # Add ClickableRectItems for each face
        self.rect_items = []
        for idx, (x, y, w, h) in enumerate(self.faces):
            rect = QRectF(x, y, w, h)
            rect_item = ClickableRectItem(rect, idx)
            rect_item.faceSelected.connect(self.handle_face_selection)
            self.scene.addItem(rect_item)
            self.rect_items.append(rect_item)
            
            # Set initial selection state
            is_selected = self.faces[idx] in self.selected_faces
            rect_item.selected = is_selected
            rect_item.update_appearance()

        self.fit_image_in_view()

    def fit_image_in_view(self):
        """
        Adjust the QGraphicsView to fit the image while maintaining aspect ratio,
        and ensure proper scaling for transparent images.
        """
        if self.pixmap_item:
            # Reset the view transformation
            self.ui.fcImageView.resetTransform()
            
            # Get the size of the view and the pixmap
            view_size = self.ui.fcImageView.viewport().size()
            pixmap_size = self.pixmap_item.pixmap().size()
            
            # Calculate the scaling factors
            scale_x = view_size.width() / pixmap_size.width()
            scale_y = view_size.height() / pixmap_size.height()
            scale = min(scale_x, scale_y)
            
            # Scale the view
            self.ui.fcImageView.scale(scale, scale)
            
            # Center the image in the view
            self.ui.fcImageView.centerOn(self.pixmap_item)
            
            # Disable scrollbars
            self.ui.fcImageView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.ui.fcImageView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def update_face_list(self, faces):
        """
        Populate the face list (fcFaceList) with detected faces.
        """
        self.ui.fcFaceList.clear()
        for i, (x, y, w, h) in enumerate(faces):
            self.ui.fcFaceList.addItem(f"Face {i+1}: ({x}, {y}, {w}, {h})")

    def censor_faces(self):
        """
        Apply the selected censoring method to the selected faces and update the display.
        If no faces are selected, display the original image without censoring.
        """
        if not hasattr(self, 'original_image'):
            return

        if not self.selected_faces:
            # No faces selected, display the original image
            self.display_image(self.original_image.copy())
        else:
            # Apply censoring to selected faces
            image = self.original_image.copy()
            censored_image = self.apply_censoring(image, draw_boxes=True)
            self.display_image(censored_image)

    def draw_eye_bars(self, image, x, y, w, h):
        """
        Draw horizontal black bars over the eyes region of the face.
        """
        # Estimate eye positions (rough estimation)
        eye_y = y + int(h * 0.3)  # Eyes typically in the upper third
        eye_h = int(h * 0.16)     # Eye height roughly 16% of face height
        bar_w = int(w * 1.0)      # Bar width to cover 100% of face width
        bar_x = x                  # Start at face's x position
        cv2.rectangle(
            image,
            (bar_x, eye_y),
            (bar_x + bar_w, eye_y + eye_h),
            (0, 0, 0),
            -1
        )

    def pixelate(self, image, blocks=8): # blocks refers to pixels per block
        """
        Pixelate the given image region.
        """
        # Get the height and width of the image
        (h, w) = image.shape[:2]
        
        # Calculate the step size for x and y directions
        # Ensure at least 1 pixel per step to avoid division by zero
        x_steps = max(1, w // blocks)
        y_steps = max(1, h // blocks)

        # Iterate over the image in blocks
        for y in range(0, h, y_steps):
            for x in range(0, w, x_steps):
                # Extract the region of interest (ROI)
                roi = image[y:y + y_steps, x:x + x_steps]
                
                # Skip empty ROIs
                if roi.size == 0:
                    continue
                
                # Calculate the average color of the ROI
                color = roi.mean(axis=(0, 1)).astype(int)
                
                # Apply the average color to the entire ROI
                # Note: Only modifying the first 3 channels (RGB), preserving alpha if present
                image[y:y + y_steps, x:x + x_steps, :3] = color[:3]
        
        return image

    def reset_image(self):
        """
        Reset the image to its original state, removing all censoring.
        """
        if hasattr(self, 'original_image'):
            image_with_faces, self.faces = self.detect_faces(self.original_image.copy())
            self.display_image(image_with_faces)
            self.update_face_list(self.faces)
            self.selected_faces = []
            # Deselect all items in the face list
            self.ui.fcFaceList.clearSelection()

    def save_image(self):
        """
        Save the censored image to a file.
        """
        censored_image = self.apply_censoring_without_boxes()
        if censored_image is None:
            QMessageBox.warning(self.ui.centralwidget, "Warning", "No censored image to save.")
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self.ui.centralwidget,
            "Save Censored Image",
            "",
            "PNG Images (*.png);;JPEG Images (*.jpg *.jpeg);;BMP Images (*.bmp);;WebP Images (*.webp);;TIFF Images (*.tif *.tiff);;All Files (*.*)"
        )

        if file_path:
            try:
                # Ensure the image is in BGRA format
                if censored_image.shape[2] == 3:
                    censored_image = cv2.cvtColor(censored_image, cv2.COLOR_BGR2BGRA)
                # Save as PNG to preserve transparency
                cv2.imwrite(file_path, censored_image)
                QMessageBox.information(self.ui.centralwidget, "Success", f"Censored image saved successfully to {file_path}")
            except Exception as e:
                QMessageBox.critical(self.ui.centralwidget, "Error", f"Error saving censored image: {str(e)}")