"""
This file is part of ImageNexus

ImageNexus is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation

Copyright (c) 2024, LyAhn

This code is licensed under the GPL-3.0 license (see LICENSE.txt for details)
"""

from PySide6.QtWidgets import QFileDialog, QMessageBox, QPlainTextEdit
from PySide6.QtGui import QFont
from src.core.ascii import AsciiArt
from art import text2art, FONT_NAMES

class AsciiHandler:
    def __init__(self, ui):
        self.ui = ui
        self.ascii_art = AsciiArt(ui)
        self.setup_connections()
        self.populate_fonts()
        self.setup_text_output()

    def setup_connections(self):
        self.ui.i2aLoadImageBtn.clicked.connect(self.load_image)
        self.ui.i2aConvertBtn.clicked.connect(self.convert_image)
        self.ui.i2aSaveBtn.clicked.connect(self.save_image)
        self.ui.i2aAddBgCheck.stateChanged.connect(self.convert_image)
        self.ui.t2aConvertBtn.clicked.connect(self.convert_text)
        self.ui.t2aFontList.itemSelectionChanged.connect(self.update_font_size)
        self.ui.t2aDiscordCheck.stateChanged.connect(self.convert_text)

    def populate_fonts(self):
        self.ui.t2aFontList.clear()
        self.ui.t2aFontList.addItems(FONT_NAMES)

    def update_font_size(self):
        selected_font = self.ui.t2aFontList.currentItem().text()
        self.ui.t2aFontSize.clear()
        if selected_font in ["block", "banner", "banner3", "banner3-D", "banner4", "colossal", "doh", "isometric1", "isometric2", "isometric3", "isometric4", "letters", "alligator", "alligator2", "dotmatrix"]:
            self.ui.t2aFontSize.addItems(["", "small", "medium", "big"])
        else:
            self.ui.t2aFontSize.addItems([""])

    def convert_text(self):
        text = self.ui.t2aTextInput.text()
        if not text:
            QMessageBox.warning(self.ui.centralwidget, "Error", "Please enter some text to convert.")
            return

        selected_font = self.ui.t2aFontList.currentItem().text() if self.ui.t2aFontList.currentItem() else None
        if not selected_font:
            QMessageBox.warning(self.ui.centralwidget, "Error", "Please select a font.")
            return

        #font_size = self.ui.t2aFontSize.currentText()

        try:
            ascii_art = text2art(text, font=selected_font, chr_ignore=True)

            # Check if Discord formatting is enabled
            if self.ui.t2aDiscordCheck.isChecked():
                ascii_art = self.format_for_discord(ascii_art)

            self.ui.t2aTextOutput.setPlainText(ascii_art)
            # Adjust the text edit size to fit the content
            document_height = self.ui.t2aTextOutput.document().size().height()
            self.ui.t2aTextOutput.setMinimumHeight(int(document_height + 10))  # Add some padding
        except Exception as e:
            QMessageBox.warning(self.ui.centralwidget, "Error", f"Failed to generate ASCII art: {str(e)}")


    def format_for_discord(self, ascii_art):
        # Split the ASCII art into lines
        lines = ascii_art.split('\n')

        # Add a single space at the beginning of each line
        indented_lines = [' ' + line for line in lines]

        # Join the lines back together
        formatted_art = '\n'.join(indented_lines)

        # Wrap the entire art in a single pair of backticks
        formatted_art = f"```\n{formatted_art}\n```"

        return formatted_art


    def setup_text_output(self):
        font = QFont("Courier")
        font.setStyleHint(QFont.Monospace)
        font.setFixedPitch(True)
        font.setPointSize(12)
        self.ui.t2aTextOutput.setFont(font)
        self.ui.t2aTextOutput.setLineWrapMode(QPlainTextEdit.NoWrap)

    def load_image(self):
        file_dialog = QFileDialog()
        image_path, _ = file_dialog.getOpenFileName(self.ui.centralwidget, "Select Image", "", "Image Files (*.png *.jpg *.bmp *.tiff *.gif)")
        if image_path:
            self.image_path = image_path
            self.ascii_art.apply_ascii_art_effect(image_path, self.ui.i2aCharSize.value(), self.ui.i2aFontSize.value())

    def convert_image(self):
        if hasattr(self, 'image_path'):
            char_size = self.ui.i2aCharSize.value()
            font_size = self.ui.i2aFontSize.value()
            add_background = self.ui.i2aAddBgCheck.isChecked()
            self.ascii_art.apply_ascii_art_effect(self.image_path, char_size, font_size, add_background)

    def save_image(self):
        if self.ascii_art.original_pixmap:
            file_dialog = QFileDialog()
            file_path, _ = file_dialog.getSaveFileName(self.ui.centralwidget, "Save ASCII Art", "", "PNG Files (*.png)")
            if file_path:
                if self.ascii_art.original_pixmap.save(file_path, "PNG"):  # Specify PNG format
                    QMessageBox.information(self.ui.centralwidget, "Success", "ASCII art saved successfully!")
                else:
                    QMessageBox.warning(self.ui.centralwidget, "Error", "Failed to save ASCII art.")
        else:
            QMessageBox.warning(self.ui.centralwidget, "Error", "No ASCII art to save. Please convert an image first.")

    def resize_event(self):
        self.ascii_art.resize_event()