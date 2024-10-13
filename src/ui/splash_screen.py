# This Python file uses the following encoding: utf-8
from PySide6.QtCore import Qt, QTimer, QUuid
from PySide6.QtGui import QPixmap, QMovie, QColor
from PySide6.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsPixmapItem, QGraphicsView, QLabel
from src.ui.ui_splash_screen import Ui_SplashScreen
from src.utils.path_utils import get_resource_path
from src.utils.version import appVersion

version = appVersion

class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.counter = 0

        # Remove title bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowTitle("ImageNexus")
        self.ui.versionLabel.setText(f"v{version}")


        # QTimer Start
        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)
        # Timer in milliseconds
        self.timer.start(340) # default time

        # Change Description
        # Initial Text
        self.ui.label_description.setText("Welcome to ImageNexus")

        # Change Texts
        QTimer.singleShot(1500, lambda: self.ui.label_description.setText("Loading models..."))
        QTimer.singleShot(3000, lambda: self.ui.label_description.setText("Loading UI"))

        # Show Main Window
        self.show()


    def progress(self):
        # Set Value to progress bar
        self.ui.progressBar.setValue(self.counter)

        # Close splash screen and open app
        if self.counter > 100:
            # Stop Timer
            self.timer.stop()

            # Close Splash Screen
            self.close()

        # Increase counter
        self.counter += 1
