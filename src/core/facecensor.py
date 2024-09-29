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

    def setup_connections(self):
        self.ui.fcBrowseBtn.clicked.connect(self.load_and_detect_faces)
        self.ui.fcCensorBtn.clicked.connect(self.censor_faces)
        self.ui.fcSaveBtn.clicked.connect(self.save_image)
        self.ui.fcResetBtn.clicked.connect(self.reset_image)
        self.ui.fcBlur.toggled.connect(self.censor_faces)
        self.ui.fcBox.toggled.connect(self.censor_faces)
        self.ui.fcPixelate.toggled.connect(self.censor_faces)
        self.ui.fcBlackBar.toggled.connect(self.censor_faces)

    def detect_faces(self, image):
        (h, w) = image.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0,
                                     (300, 300), (104.0, 177.0, 123.0))
        
        self.face_net.setInput(blob)
        detections = self.face_net.forward()
        
        faces = []
        for i in range(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > 0.5:  # Adjust this threshold as needed
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
                faces.append((startX, startY, endX - startX, endY - startY))
                cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
        
        return image, faces

    def load_and_detect_faces(self):
        file_path, _ = QFileDialog.getOpenFileName(
            parent=None, 
            caption="Open Image",
            dir="",
            filter="Image Files (*.png *.jpg *.bmp *.tiff *.webp)"
        )

        if file_path:
            try:
                self.original_image = cv2.imread(file_path)
                if self.original_image is None:
                    raise ValueError("Failed to load image")
                
                image_with_faces, self.faces = self.detect_faces(self.original_image.copy())
                self.display_image(image_with_faces)
                self.update_face_list(self.faces)
                self.ui.fcInputImage.setText(file_path)
            except Exception as e:
                print(f"Error loading image: {e}")

    def display_image(self, image):
        height, width, channel = image.shape
        bytes_per_line = 3 * width
        q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format.Format_RGB888).rgbSwapped()
        pixmap = QPixmap.fromImage(q_image)
        
        scene = QGraphicsScene()
        pixmap_item = QGraphicsPixmapItem(pixmap)
        scene.addItem(pixmap_item)
        
        self.ui.fcImageView.setScene(scene)
        self.ui.fcImageView.fitInView(scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)

    def update_face_list(self, faces):
        self.ui.fcFaceList.clear()
        for i, (x, y, w, h) in enumerate(faces):
            self.ui.fcFaceList.addItem(f"Face {i+1}: ({x}, {y}, {w}, {h})")

    def censor_faces(self):
        if not hasattr(self, 'original_image'):
            return

        # Determine which radio button is checked
        if self.ui.fcBlur.isChecked():
            censoring_method = "Blur"
        elif self.ui.fcBox.isChecked():
            censoring_method = "Black Box"
        elif self.ui.fcPixelate.isChecked():
            censoring_method = "Pixelate"
        elif self.ui.fcBlackBar.isChecked():
            censoring_method = "Eye Bars"
        else:
            print("No censoring method selected")
            return

        image = self.original_image.copy()

        self.censored_image = image # Initialize censored_image
        self.display_image(image)

        for (x, y, w, h) in self.faces:
            face_roi = image[y:y+h, x:x+w]
            if censoring_method == "Blur":
                face_roi = cv2.GaussianBlur(face_roi, (99, 99), 30)
            elif censoring_method == "Pixelate":
                face_roi = self.pixelate(face_roi)
            elif censoring_method == "Black Box":
                face_roi[:] = (0, 0, 0)
            elif censoring_method == "Eye Bars":
                self.draw_eye_bars(image, x, y, w, h)
            image[y:y+h, x:x+w] = face_roi

        self.display_image(image)

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
                image[y:y+y_steps, x:x+x_steps] = color
    
        return image
    
    def reset_image(self):
        if hasattr(self, 'original_image'):
            self.display_image(self.original_image.copy())

    def save_image(self):
        if not hasattr(self, 'censored_image'):
            print("No censored image to save.")
            return
        
        file_path, _ = QFileDialog.getSaveFileName(
            None, 
            "Save Censored Image",
            "",
            "Image Files (*.png *.jpg *.bmp *.tiff *.webp)"
        )
        
        if file_path:
            try:
                cv2.imwrite(file_path, self.censored_image)
                print(f"Censored image saved successfully to {file_path}")
            except Exception as e:
                print(f"Error saving censored image: {e}")

# Todo: Implement selecting specific faces 
# Todo: fix transparency issue


