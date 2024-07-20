# This Python file uses the following encoding: utf-8
import sys
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QGraphicsScene, QGraphicsPixmapItem
from PySide6.QtGui import QPixmap, QCursor
from ui_about import Ui_aboutWindow


class aboutDialog(QtWidgets.QMainWindow):
    
    version = "0.4.2"
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_aboutWindow()
        self.ui.setupUi(self)
        self.setup_connections()
        self.setWindowTitle("About")
        self.ui.versionLabel.setText(f"v{aboutDialog.version}")

        self.scene = QGraphicsScene()
        self.scene.setBackgroundBrush(QtCore.Qt.transparent)
        logo = QPixmap("resources/logo_256.png")
        logo_item = QGraphicsPixmapItem(logo)
        self.scene.addItem(logo_item)
        self.scene.setSceneRect(self.scene.itemsBoundingRect())
        self.ui.logoView.setViewportUpdateMode(QtWidgets.QGraphicsView.FullViewportUpdate)
        self.ui.logoView.setStyleSheet("border: none; background: transparent;")
        self.ui.logoView.setScene(self.scene)
        self.ui.logoView.fitInView(logo_item.boundingRect(), QtCore.Qt.KeepAspectRatio)
        # Sets the cursor to standard whilst hovering over textEdit
        self.ui.textEdit.viewport().setCursor(QCursor(QtCore.Qt.CursorShape.ArrowCursor))
  

    def setup_connections(self):
        # Add connections here

        pass


    def closeEvent(self, event):
        self.close()
        event.accept()

    def show_about(self):
        self.show() 

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = aboutDialog()
    dialog.show()
    sys.exit(app.exec())