# This Python file uses the following encoding: utf-8
import sys
from src.core.qr_generator import QRGenerator
from src.core.pixelizer import Pixelize
from src.core.frame_extractor import FrameExtractor
from src.core.img_converter import ImgConverter
from src.core.batch_converter import BatchConvert
from src.ui.ui_form import Ui_ImageNexus
from src.utils.aboutDialog import aboutDialog
from src.utils.version import appVersion
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt



version = appVersion

class ImageNexus(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ImageNexus()
        self.ui.setupUi(self)
        self.setWindowTitle(f"ImageNexus v{version}")
        self.frame_extractor = FrameExtractor(self.ui)
        self.img_converter = ImgConverter(self.ui)
        self.batch_converter = BatchConvert(self.ui)
        self.qr_generator = QRGenerator(self.ui)
        self.pixelizer = Pixelize(self.ui)

        self.setup_connections()
        self.qr_generator.load_qr_templates()


    def setup_connections(self):


        # QR Code Generator tab
        self.ui.qrGenButton.clicked.connect(self.qr_generator.preview_qr_code)
        self.ui.saveQRButton.clicked.connect(self.qr_generator.save_qr_code)
        self.ui.browseFolderButton.clicked.connect(self.qr_generator.browse_output_folder)
        self.ui.logoBrowseButton.clicked.connect(self.qr_generator.browse_logo)
        self.ui.bgColourButton.clicked.connect(lambda: self.qr_generator.choose_color('bg'))
        self.ui.codeColourButton.clicked.connect(lambda: self.qr_generator.choose_color('code'))
        self.ui.addBgCheckbox.stateChanged.connect(self.qr_generator.preview_qr_code)
        self.ui.aspectRatioCheck.stateChanged.connect(self.qr_generator.preview_qr_code)
        self.ui.qrTemplates.currentIndexChanged.connect(self.qr_generator.on_qr_template_changed)
        self.ui.fillPlaceHoldersButton.clicked.connect(self.qr_generator.fill_placeholders)

        # Help Menu
        self.ui.actionAbout.triggered.connect(self.show_about)

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



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = ImageNexus()
    widget.show()
    sys.exit(app.exec())
