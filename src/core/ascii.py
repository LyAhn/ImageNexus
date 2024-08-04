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

    def apply_ascii_art_effect(self, image_path, char_size, font_size):
        img = cv2.imread(image_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = self.ascii_art_effect(img, char_size, font_size)

        height, width, channel = result.shape
        bytes_per_line = 3 * width
        qimage = QImage(result.data, width, height, bytes_per_line, QImage.Format_RGB888)
        self.original_pixmap = QPixmap.fromImage(qimage)
        self.update_display()


    def ascii_art_effect(self, image, char_size, font_size):
        chars = " .'`^\",:;I1!i><-+_-?][}{1)(|\/tfjrxnuvczXYUCLQ0OZmwqpbdkhao*#MW&8%B@$"
        height, width = image.shape[:2]
        small_image = cv2.resize(image, (width // char_size, height // char_size), interpolation=cv2.INTER_NEAREST)

        def get_char(value):
            return chars[int(value * len(chars) / 256)]

        ascii_image = np.zeros((height, width, 3), dtype=np.uint8)

        for i in range(small_image.shape[0]):
            for j in range(small_image.shape[1]):
                r, g, b = small_image[i, j]
                k = (int(r) + int(g) + int(b)) // 3
                cv2.putText(ascii_image, get_char(k),
                            (j * char_size, i * char_size + font_size),
                            cv2.FONT_HERSHEY_SIMPLEX, font_size / 30,
                            (int(r), int(g), int(b)), 1, cv2.LINE_AA)

        return ascii_image

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