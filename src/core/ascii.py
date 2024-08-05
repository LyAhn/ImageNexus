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
from PySide6.QtGui import QPixmap, QImage, Qt
from PySide6.QtWidgets import QGraphicsScene, QGraphicsPixmapItem
from PySide6.QtCore import QRectF
from art import text2art

class AsciiArt:
    def __init__(self, ui):
        self.ui = ui
        self.scene = QGraphicsScene()
        self.ui.i2aGraphicsView.setScene(self.scene)
        self.pixmap_item = None
        self.original_pixmap = None

    def apply_ascii_art_effect(self, image_path, char_size, font_size, add_background=False):
        img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
        if img.shape[2] == 3:  # If the image is RGB, add an alpha channel
            img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
        else:
            img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)

        result = self.ascii_art_effect(img, char_size, font_size, add_background)

        height, width, channel = result.shape
        bytes_per_line = 4 * width
        qimage = QImage(result.data, width, height, bytes_per_line, QImage.Format_RGBA8888)
        self.original_pixmap = QPixmap.fromImage(qimage)
        self.update_display()

    def ascii_art_effect(self, image, char_size, font_size, add_background=False):
        chars = " .'`^\",:;I1!i><-+_-?][}{1)(|\/tfjrxnuvczXYUCLQ0OZmwqpbdkhao*#MW&8%B@$"
        height, width = image.shape[:2]
        small_image = cv2.resize(image, (width // char_size, height // char_size), interpolation=cv2.INTER_NEAREST)

        def get_char(value):
            return chars[int(value * (len(chars) - 1) / 255)]

        ascii_image = np.zeros((height, width, 4), dtype=np.uint8)

        for i in range(small_image.shape[0]):
            for j in range(small_image.shape[1]):
                r, g, b, a = small_image[i, j]

                # Only skip if the pixel is fully transparent
                if a == 0:
                    continue

                k = (int(r) + int(g) + int(b)) // 3

                # Draw characters for all non-transparent pixels, including black
                cv2.putText(ascii_image, get_char(k),
                            (j * char_size, i * char_size + font_size),
                            cv2.FONT_HERSHEY_SIMPLEX, font_size / 30,
                            (int(r), int(g), int(b), int(a)), 1, cv2.LINE_AA)

        if add_background:
            # Create a black background
            background = np.zeros((height, width, 4), dtype=np.uint8)
            background[:, :, 3] = 255  # Set alpha to fully opaque

            # Blend the ASCII art with the background
            alpha = ascii_image[:, :, 3:4] / 255.0
            ascii_image = alpha * ascii_image[:, :, :3] + (1 - alpha) * background[:, :, :3]
            ascii_image = np.concatenate([ascii_image, np.full((height, width, 1), 255, dtype=np.uint8)], axis=2)

        return ascii_image.astype(np.uint8)

    def text_to_ascii(self, text, font, size=""):
        return text2art(text, font=font, chr_ignore=True) if size == "" else text2art(text, font=font, chr_ignore=True, size=size)

    def update_display(self):
        if self.original_pixmap:
            self.scene.clear()
            view_rect = self.ui.i2aGraphicsView.viewport().rect()
            scaled_pixmap = self.original_pixmap.scaled(view_rect.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)

            self.pixmap_item = QGraphicsPixmapItem(scaled_pixmap)
            self.scene.addItem(self.pixmap_item)

            scene_rect = QRectF(self.pixmap_item.boundingRect())
            self.scene.setSceneRect(scene_rect)
            self.ui.i2aGraphicsView.fitInView(scene_rect, Qt.KeepAspectRatio)

    def resize_event(self):
        self.update_display()