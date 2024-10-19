# This Python file uses the following encoding: utf-8
from PySide6.QtCore import Qt, QTimer, QUuid
from PySide6.QtGui import QPixmap, QMovie, QColor
from PySide6.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsPixmapItem, QGraphicsView, QLabel
from src.ui.ui_splash_screen import Ui_SplashScreen
from src.utils.path_utils import get_project_root
from src.utils.version import appVersion

version = appVersion

class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.ui.progressBar.setRange(0, 100)
        self.ui.progressBar.setValue(0)
        self.counter = 0

        # Remove title bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowTitle("ImageNexus")
        self.ui.versionLabel.setText(f"v{version}")

        # Load and set the animated GIF
        gif_path = get_project_root("resources/ui/loading.gif")
        self.movie = QMovie(gif_path)

        # Get the size of the loadingLabel
        label_size = self.ui.loadingLabel.size()

        # Set the movie to the label and start it
        self.ui.loadingLabel.setMovie(self.movie)
        self.movie.start()

        # QTimer Start
        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)
        # Timer in milliseconds
        self.timer.start(50) # default time

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
        self.ui.progressBar.repaint()

        # Close splash screen and open app
        if self.counter > 100:
            # Stop Timer
            self.timer.stop()

            # Close Splash Screen
            #self.closeEvent()

        # Increase counter
        self.counter += 2

    def closeEvent(self, event):
        self.movie.stop()
        event.accept()