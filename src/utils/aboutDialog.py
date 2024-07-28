from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QGraphicsView, QMainWindow
from PySide6.QtGui import QPixmap, QCursor
from src.ui.ui_about import Ui_aboutWindow
from src.utils.version import appVersion

class aboutDialog(QMainWindow):

    version = appVersion

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_aboutWindow()
        self.ui.setupUi(self)
        self.setup_connections()
        self.setWindowTitle("About")
        self.ui.versionLabel.setText(f"v{aboutDialog.version}")
        self.ui.ghLink.setOpenExternalLinks(True)
        # Logo section
        self.scene = QGraphicsScene()
        self.scene.setBackgroundBrush(Qt.transparent)
        logo = QPixmap("resources/logo_256.png")
        logo_item = QGraphicsPixmapItem(logo)
        self.scene.addItem(logo_item)
        self.scene.setSceneRect(self.scene.itemsBoundingRect())

        self.ui.logoView.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        self.ui.logoView.setStyleSheet("border: none; background: transparent;")
        self.ui.logoView.setScene(self.scene)
        self.ui.logoView.fitInView(logo_item.boundingRect(), Qt.KeepAspectRatio)

        # Sets the cursor to standard whilst hovering over aboutText
        self.ui.aboutText.viewport().setCursor(QCursor(Qt.CursorShape.ArrowCursor))

    def setup_connections(self):
        # Add connections here

        pass

    def closeEvent(self, event):
        self.close()
        event.accept()

    def show_about(self):
       self.show()
