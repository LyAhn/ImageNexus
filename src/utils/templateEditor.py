"""
This file is part of ImageNexus

ImageNexus is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation

Copyright (c) 2024, LyAhn

This code is licensed under the GPL-3.0 license (see LICENSE.txt for details)
"""

from PySide6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout,
                                QPushButton, QMessageBox, QInputDialog,
                               QListWidget, QLabel, QLineEdit, QDialogButtonBox, QTableWidget,
                               QTableWidgetItem, QSplitter, QWidget, QHeaderView, QUndoView)
from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import Qt
from src.utils.path_utils import get_project_root
import json
import os

class JSONEditorDialog(QDialog):
    def __init__(self, json_file_path, parent=None):
        super().__init__(None)
        self.json_file_path = json_file_path
        self.setWindowTitle("QR Template Editor")
        self.setWindowIcon(QIcon.fromTheme("input-keyboard"))
        self.setMinimumSize(800, 600)

        main_layout = QHBoxLayout(self)
        splitter = QSplitter(Qt.Horizontal)
        main_layout.addWidget(splitter)

        # Left panel
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        self.template_list = QListWidget()
        self.template_list.setFont(QFont("Arial", 10))
        left_layout.addWidget(QLabel("Templates"))
        left_layout.addWidget(self.template_list)

        # Button layout for left panel
        left_button_layout = QHBoxLayout()
        self.add_button = QPushButton("Add")
        self.add_button.setIcon(QIcon.fromTheme("list-add"))
        self.delete_button = QPushButton("Delete")
        self.delete_button.setIcon(QIcon.fromTheme("list-remove"))
        left_button_layout.addWidget(self.add_button)
        left_button_layout.addWidget(self.delete_button)
        left_layout.addLayout(left_button_layout)

        splitter.addWidget(left_widget)

        # Right panel
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)

        # Template details
        self.template_view = QTableWidget()
        self.template_view.setColumnCount(2)
        self.template_view.setHorizontalHeaderLabels(["Property", "Value"])
        self.template_view.horizontalHeader().setStretchLastSection(True)
        self.template_view.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        right_layout.addWidget(QLabel("Template Details"))
        right_layout.addWidget(self.template_view)

        # Placeholders
        right_layout.addWidget(QLabel("Placeholders"))
        self.placeholder_list = QListWidget()
        right_layout.addWidget(self.placeholder_list)

        # Placeholder buttons
        placeholder_button_layout = QHBoxLayout()
        self.add_placeholder_button = QPushButton("Add Placeholder")
        self.add_placeholder_button.setIcon(QIcon.fromTheme("list-add"))
        self.edit_placeholder_button = QPushButton("Edit Placeholder")
        self.edit_placeholder_button.setIcon(QIcon.fromTheme("mail-message-new"))
        self.remove_placeholder_button = QPushButton("Remove Placeholder")
        self.remove_placeholder_button.setIcon(QIcon.fromTheme("list-remove"))
        placeholder_button_layout.addWidget(self.add_placeholder_button)
        placeholder_button_layout.addWidget(self.edit_placeholder_button)
        placeholder_button_layout.addWidget(self.remove_placeholder_button)
        right_layout.addLayout(placeholder_button_layout)

        # Save button
        self.save_button = QPushButton("Save Changes")
        self.save_button.setIcon(QIcon.fromTheme("document-save"))
        right_layout.addWidget(self.save_button)

        splitter.addWidget(right_widget)

        # Connect signals
        self.template_list.currentItemChanged.connect(self.on_template_selected)
        self.template_view.itemChanged.connect(self.on_template_item_changed)
        self.add_button.clicked.connect(self.add_template)
        self.delete_button.clicked.connect(self.delete_template)
        self.save_button.clicked.connect(self.save_changes)
        self.add_placeholder_button.clicked.connect(self.add_placeholder)
        self.remove_placeholder_button.clicked.connect(self.remove_placeholder)
        self.edit_placeholder_button.clicked.connect(self.edit_placeholder)

        self.load_json()

    def load_json(self):
        try:
            if not os.path.exists(self.json_file_path):
                raise FileNotFoundError(f"'{self.json_file_path}' does not exist.")

            with open(self.json_file_path, 'r') as file:
                data = json.load(file)
                self.populate_template_list(data)
            print(f"QR Templates loaded in editor from: {self.json_file_path}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load JSON file: {str(e)}")

    def populate_template_list(self, data):
        self.template_list.clear()
        for template in data['qr_code_types']:
            self.template_list.addItem(template['name'])

    def on_template_selected(self, current, previous):
        if current:
            self.load_template_details(current.text())

    def load_template_details(self, template_name):
        self.template_view.clearContents()
        self.template_view.setRowCount(0)
        self.placeholder_list.clear()

        with open(self.json_file_path, 'r') as file:
            data = json.load(file)

        template = next((t for t in data['qr_code_types'] if t['name'] == template_name), None)
        if template:
            for key, value in template.items():
                if key != 'placeholders':
                    row = self.template_view.rowCount()
                    self.template_view.insertRow(row)
                    self.template_view.setItem(row, 0, QTableWidgetItem(key))
                    self.template_view.setItem(row, 1, QTableWidgetItem(str(value)))
                else:
                    for placeholder, ph_value in value.items():
                        self.placeholder_list.addItem(f"{placeholder}: {ph_value}")

    def on_template_item_changed(self, item):
        if item.column() == 1:  # Only handle changes in the value column
            property_name = self.template_view.item(item.row(), 0).text()
            new_value = item.text()
            self.update_template_property(property_name, new_value)

    def update_template_property(self, property_name, new_value):
        current_template = self.template_list.currentItem().text()
        with open(self.json_file_path, 'r+') as file:
            data = json.load(file)
            for template in data['qr_code_types']:
                if template['name'] == current_template:
                    template[property_name] = new_value
                    break
            file.seek(0)
            json.dump(data, file, indent=2)
            file.truncate()

    def add_template(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Add New Template")
        layout = QVBoxLayout(dialog)

        name_input = QLineEdit()
        format_input = QLineEdit()
        layout.addWidget(QLabel("Template Name:"))
        layout.addWidget(name_input)
        layout.addWidget(QLabel("Format:"))
        layout.addWidget(format_input)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        layout.addWidget(buttons)

        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)

        if dialog.exec_() == QDialog.Accepted:
            name = name_input.text()
            format_value = format_input.text()
            if name and format_value:
                self.create_new_template(name, format_value)
            else:
                QMessageBox.warning(self, "Invalid Input", "Both name and format are required.")

    def create_new_template(self, name, format_value):
        with open(self.json_file_path, 'r+') as file:
            data = json.load(file)
            new_template = {
                "name": name,
                "format": format_value,
                "placeholders": {}
            }
            data['qr_code_types'].append(new_template)
            file.seek(0)
            json.dump(data, file, indent=2)
            file.truncate()

        self.template_list.addItem(name)
        self.template_list.setCurrentRow(self.template_list.count() - 1)

    def delete_template(self):
        current_item = self.template_list.currentItem()
        if current_item:
            reply = QMessageBox.question(self, "Delete Template",
                                         f"Are you sure you want to delete the template '{current_item.text()}'?",
                                         QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.remove_template(current_item.text())
                self.template_list.takeItem(self.template_list.row(current_item))

    def remove_template(self, template_name):
        with open(self.json_file_path, 'r+') as file:
            data = json.load(file)
            data['qr_code_types'] = [t for t in data['qr_code_types'] if t['name'] != template_name]
            file.seek(0)
            json.dump(data, file, indent=2)
            file.truncate()

    def add_placeholder(self):
        current_template = self.template_list.currentItem()
        if current_template:
            name, ok = QInputDialog.getText(self, "Add Placeholder", "Enter placeholder name:")
            if ok and name:
                value, ok = QInputDialog.getText(self, "Add Placeholder", "Enter placeholder value:")
                if ok:
                    self.update_placeholder(current_template.text(), name, value)
                    self.placeholder_list.addItem(f"{name}: {value}")

    def remove_placeholder(self):
        current_item = self.placeholder_list.currentItem()
        if current_item:
            placeholder_name = current_item.text().split(':')[0]
            current_template = self.template_list.currentItem().text()
            self.update_placeholder(current_template, placeholder_name, None, remove=True)
            self.placeholder_list.takeItem(self.placeholder_list.row(current_item))

    def edit_placeholder(self):
        current_item = self.placeholder_list.currentItem()
        if current_item:
            placeholder_name, old_value = current_item.text().split(': ')
            new_value, ok = QInputDialog.getText(self, "Edit Placeholder", "Enter new default value:", text=old_value)
            if ok:
                current_template = self.template_list.currentItem().text()
                self.update_placeholder(current_template, placeholder_name, new_value)
                current_item.setText(f"{placeholder_name}: {new_value}")


    def update_placeholder(self, template_name, placeholder_name, value, remove=False):
        with open(self.json_file_path, 'r+') as file:
            data = json.load(file)
            for template in data['qr_code_types']:
                if template['name'] == template_name:
                    if remove:
                        template['placeholders'].pop(placeholder_name, None)
                    else:
                        template['placeholders'][placeholder_name] = value
                    break
            file.seek(0)
            json.dump(data, file, indent=2)
            file.truncate()

    def save_changes(self):
        try:
            with open(self.json_file_path, 'r+') as file:
                data = json.load(file)
                file.seek(0)
                json.dump(data, file, indent=2)
                file.truncate()
            QMessageBox.information(self, "Success", "Templates saved successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save templates: {str(e)}")

    def show_preview(self):
        current_template = self.template_list.currentItem()
        if current_template:
            # Here you would generate a preview of the QR code
            # For this example, we'll just show a message
            QMessageBox.information(self, "Preview", f"Previewing template: {current_template.text()}")

    # def setup_shortcuts(self):
    #     QShortcut(QKeySequence("Ctrl+S"), self, self.save_changes)
    #     QShortcut(QKeySequence("Ctrl+N"), self, self.add_template)
    #     QShortcut(QKeySequence("Ctrl+De"), self, self.delete_template)

    # def setup_undo_redo(self):
    #     self.undo_stack = QUndoStack(self)
    #     self.undo_view = QUndoView(self.undo_stack)
    #     self.undo_action = self.undo_stack.createUndoAction(self, "Undo")
    #     self.redo_action = self.undo_stack.createRedoAction(self, "Redo")
        #TODO need to implement custom QUndoCommand classes for each action and push them onto the undo_stack when actions are performed

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     dialog = JSONEditorDialog('resources/qr_templates.json')
#     dialog.show()
#     sys.exit(app.exec())