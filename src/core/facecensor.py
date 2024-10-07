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
from PySide6.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QFileDialog
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import Qt

class FaceCensor:
    def __init__(self, ui):
        self.ui = ui
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Points application to app root directory
        root_dir = os.path.abspath(os.path.join(current_dir, '..', '..', '.'))
        
        prototxt_path = os.path.join(root_dir, 'resources', 'models', 'facedetection', 'deploy.prototxt')
        model_path = os.path.join(root_dir, 'resources', 'models', 'facedetection', 'res10_300x300_ssd_iter_140000.caffemodel')
        
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

    def setup_connections(self):
        self.ui.fcBrowseBtn.clicked.connect(self.load_and_detect_faces)
        self.ui.fcCensorBtn.clicked.connect(self.censor_faces)
        self.ui.fcSaveBtn.clicked.connect(self.save_image)
        self.ui.fcResetBtn.clicked.connect(self.reset_image)
        self.ui.fcBlur.toggled.connect(self.update_image_view)
        self.ui.fcBox.toggled.connect(self.update_image_view)
        self.ui.fcPixelate.toggled.connect(self.update_image_view)
        self.ui.fcBlackBar.toggled.connect(self.update_image_view)

        self.ui.fcFaceList.itemSelectionChanged.connect(self.update_selected_faces)

    def update_selected_faces(self):
        selected_indices = [self.ui.fcFaceList.row(item) for item in self.ui.fcFaceList.selectedItems()]
        self.selected_faces = [self.faces[i] for i in selected_indices]
        self.update_image_view()

    def update_image_view(self):
        if hasattr(self, 'original_image'):
            image_with_faces = self.draw_faces_with_colors(self.original_image.copy())
            self.display_image(image_with_faces)

    def detect_faces(self, image):
        (h, w) = image.shape[:2]
        # Convert BGRA to BGR for face detection
        bgr_image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
        blob = cv2.dnn.blobFromImage(cv2.resize(bgr_image, (300, 300)), 1.0,
                                    (300, 300), (104.0, 177.0, 123.0))
        self.face_net.setInput(blob)
        detections = self.face_net.forward()

        faces = []
        for i in range(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > 0.5:
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
                faces.append((startX, startY, endX - startX, endY - startY))

        # Draw bounding boxes and add face IDs on the BGRA image
        for i, (x, y, w, h) in enumerate(faces):
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255, 255), 2)
            cv2.putText(image, f"Face {i+1}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255, 255), 2)

        return image, faces

    def load_and_detect_faces(self):
        file_path = QFileDialog.getOpenFileName(
            parent=None,
            caption="Open Image",
            dir="",
            filter="Image Files (*.png *.jpg *.bmp *.tiff *.webp)"
        )

        if file_path:
            try:
                self.original_image = cv2.imread(file_path[0], cv2.IMREAD_UNCHANGED)
                if self.original_image is None:
                    raise ValueError("Failed to load image")
                
                # Ensure the image has an alpha channel
                if self.original_image.shape[2] == 3:
                    self.original_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2BGRA)
                
                image_with_faces, self.faces = self.detect_faces(self.original_image.copy())
                self.display_image(image_with_faces)
                self.update_face_list(self.faces)
                self.ui.fcInputImage.setText(file_path[0])
            except Exception as e:
                print(f"Error loading image: {e}")

    def get_censoring_method(self):
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
        censoring_method = self.get_censoring_method()
        if draw_boxes:
            image = self.draw_faces_with_colors(image)
        
        if censoring_method:
            for x, y, w, h in self.selected_faces:
                face_roi = image[y:y+h, x:x+w]
                
                if censoring_method == "Blur":
                    blurred = cv2.GaussianBlur(face_roi, (99, 99), 30)
                    alpha = face_roi[:,:,3]
                    face_roi[:,:,:3] = blurred[:,:,:3]
                    face_roi[:,:,3] = alpha
                elif censoring_method == "Black Box":
                    face_roi[:,:,:3] = (0, 0, 0)
                elif censoring_method == "Pixelate":
                    face_roi = self.pixelate(face_roi)
                elif censoring_method == "Eye Bars":
                    self.draw_eye_bars(image, x, y, w, h)
                
                image[y:y+h, x:x+w] = face_roi

        return image

    def apply_censoring_without_boxes(self):
        if not hasattr(self, 'original_image') or not hasattr(self, 'selected_faces'):
            return None

        image = self.original_image.copy()
        return self.apply_censoring(image, draw_boxes=False)

    def resizeEvent(self, event):
        self.fit_image_in_view()

    def display_image(self, image):
        height, width = image.shape[:2]
        bytes_per_line = 4 * width
        q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format_ARGB32)
        pixmap = QPixmap.fromImage(q_image)
        scene = QGraphicsScene()
        self.pixmap_item = QGraphicsPixmapItem(pixmap)
        scene.addItem(self.pixmap_item)
        self.ui.fcImageView.setScene(scene)
        self.fit_image_in_view()

    def fit_image_in_view(self):
        if self.pixmap_item:
            self.ui.fcImageView.fitInView(self.pixmap_item, Qt.KeepAspectRatio)

    def update_face_list(self, faces):
        self.ui.fcFaceList.clear()
        for i, (x, y, w, h) in enumerate(faces):
            self.ui.fcFaceList.addItem(f"Face {i+1}: ({x}, {y}, {w}, {h})")

    def censor_faces(self):
        if not hasattr(self, 'original_image') or not hasattr(self, 'selected_faces'):
            return

        image = self.original_image.copy()
        censored_image = self.apply_censoring(image, draw_boxes=True)
        self.display_image(censored_image)

    def draw_eye_bars(self, image, x, y, w, h):
        # Estimate eye positions (this is a rough estimation)
        eye_y = y + int(h * 0.3)  # Eyes are typically in the upper third of the face
        eye_h = int(h * 0.16)  # Eye height is roughly 15% of face height
        
        # Calculate the width of the bar to cover both eyes
        bar_w = int(w * 1.0)  # Extend the bar to cover approximately 100% of face width
        
        # Calculate the x-position of the bar (centered on the face)
        bar_x = x + int(w * 0.00)  # Start at 15% of face width
        
        # Draw a single black bar across both eyes
        cv2.rectangle(image, (bar_x, eye_y), (bar_x + bar_w, eye_y + eye_h), (0, 0, 0), -1)

    def pixelate(self, image, blocks=10):
        (h, w) = image.shape[:2]
        x_steps = w // blocks
        y_steps = h // blocks
        
        for y in range(0, h, y_steps):
            for x in range(0, w, x_steps):
                roi = image[y:y+y_steps, x:x+x_steps]
                color = roi.mean(axis=(0,1)).astype(int)
                image[y:y+y_steps, x:x+x_steps, :3] = color[:3]
                # Preserve original alpha values
                image[y:y+y_steps, x:x+x_steps, 3] = roi[:,:,3]
        
        return image
    
    def reset_image(self):
        if hasattr(self, 'original_image'):
            image_with_faces, self.faces = self.detect_faces(self.original_image.copy())
            self.display_image(image_with_faces)
            self.update_face_list(self.faces)

    def save_image(self):
        censored_image = self.apply_censoring_without_boxes()
        if censored_image is None:
            print("No censored image to save.")
            return

        file_path, _ = QFileDialog.getSaveFileName(
            None,
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
                print(f"Censored image saved successfully to {file_path}")
            except Exception as e:
                print(f"Error saving censored image: {e}")

    def draw_faces_with_colors(self, image):
        for i, (x, y, w, h) in enumerate(self.faces):
            color = (0, 255, 0, 255) if (x, y, w, h) in self.selected_faces else (0, 0, 255, 255)
            cv2.rectangle(image, (x, y), (x+w, y+h), color, 2)
            cv2.putText(image, f"Face {i+1}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, color, 2)
        return image

# Todo: Implement selecting specific faces via preview
# Fixme: fix transparency issue w/ png


