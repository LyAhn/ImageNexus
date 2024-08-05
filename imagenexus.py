# This Python file uses the following encoding: utf-8
import sys
from src.core.frame_extractor import FrameExtractor
from src.core.img_converter import ImgConverter
from src.core.batch_converter import BatchConvert
from src.core.qr_generator import QRGenerator
from src.core.pixelate import Pixelate
from src.ui.ui_form import Ui_ImageNexus
from src.utils.aboutDialog import aboutDialog
from src.utils.ascii_handler import AsciiHandler
from src.utils.version import appVersion
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt
from art import text2art


version = appVersion

class ImageNexus(QMainWindow):
    def __init__(self, parent=None):
        ascii_version = text2art(f"ImageNexus v{version}", font="doom", chr_ignore=True)
        print(ascii_version)
        print("Copyright (c) 2024, LyAhn")
        print("This code is licensed under the GPL-3.0 license (see LICENSE.txt for details)")
        print("----------------------------------------------------------")
        print("Welcome to ImageNexus!")
        super().__init__(parent)
        self.ui = Ui_ImageNexus()
        self.ui.setupUi(self)
        self.setWindowTitle("ImageNexus")
        self.frame_extractor = FrameExtractor(self.ui)
        self.img_converter = ImgConverter(self.ui)
        self.batch_converter = BatchConvert(self.ui)
        self.qr_generator = QRGenerator(self.ui)
        self.pixelizer = Pixelate(self.ui)
        self.ascii_handler = AsciiHandler(self.ui)

        self.setup_connections()
        self.qr_generator.load_qr_templates()


    def setup_connections(self):

        # Top Menu Bar
        self.ui.actionAbout.triggered.connect(self.show_about)
        self.ui.actionReloadTemplates.triggered.connect(self.qr_generator.load_qr_templates)

    def show_about(self):
        self.about_dialog = aboutDialog(self)
        self.about_dialog.setAttribute(Qt.WA_DeleteOnClose)
        self.about_dialog.show()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if self.ui.qrOutputView.scene():

            self.ui.qrOutputView.fitInView(self.ui.qrOutputView.scene().sceneRect(), Qt.KeepAspectRatio)

        if hasattr(self, 'pixelizer'):
            self.pixelizer.resize_image()

        if hasattr(self.ascii_handler.ascii_art, 'resize_event'):
            self.ascii_handler.resize_event()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = ImageNexus()
    widget.show()
    sys.exit(app.exec())
