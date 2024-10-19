# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screen.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QProgressBar,
    QSizePolicy, QWidget)
import rc_resources

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(688, 500)
        SplashScreen.setMinimumSize(QSize(688, 500))
        SplashScreen.setMaximumSize(QSize(688, 500))
        SplashScreen.setContextMenuPolicy(Qt.ContextMenuPolicy.PreventContextMenu)
        self.mainUI = QWidget(SplashScreen)
        self.mainUI.setObjectName(u"mainUI")
        self.versionLabel = QLabel(self.mainUI)
        self.versionLabel.setObjectName(u"versionLabel")
        self.versionLabel.setGeometry(QRect(110, 200, 49, 16))
        self.appLabel = QLabel(self.mainUI)
        self.appLabel.setObjectName(u"appLabel")
        self.appLabel.setGeometry(QRect(80, 170, 111, 31))
        font = QFont()
        font.setFamilies([u"Gill Sans MT"])
        font.setPointSize(15)
        self.appLabel.setFont(font)
        self.label_description = QLabel(self.mainUI)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(30, 450, 201, 31))
        self.progressBar = QProgressBar(self.mainUI)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(1, 497, 258, 3))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    border: none;\n"
"    background-color: rgba(255, 255, 255, 0.1);\n"
"    border-radius: 2px;\n"
"    text-align: center;\n"
"    color: transparent;\n"
"    height: 4px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: white;\n"
"    border-radius: 2px;\n"
"}")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)
        self.loadingLabel = QLabel(self.mainUI)
        self.loadingLabel.setObjectName(u"loadingLabel")
        self.loadingLabel.setGeometry(QRect(50, 300, 150, 150))
        self.loadingLabel.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.loadingLabel.setAutoFillBackground(False)
        self.loadingLabel.setTextFormat(Qt.TextFormat.RichText)
        self.loadingLabel.setScaledContents(False)
        self.logoView = QLabel(self.mainUI)
        self.logoView.setObjectName(u"logoView")
        self.logoView.setGeometry(QRect(60, 20, 150, 150))
        self.logoView.setPixmap(QPixmap(u":/images/resources/logo.svg"))
        self.logoView.setScaledContents(True)
        self.bgLabel = QLabel(self.mainUI)
        self.bgLabel.setObjectName(u"bgLabel")
        self.bgLabel.setGeometry(QRect(0, 0, 688, 500))
        self.bgLabel.setAutoFillBackground(True)
        self.bgLabel.setPixmap(QPixmap(u":/images/splash/resources/splash/sp01.png"))
        self.bgLabel.setScaledContents(True)
        SplashScreen.setCentralWidget(self.mainUI)
        self.bgLabel.raise_()
        self.versionLabel.raise_()
        self.appLabel.raise_()
        self.label_description.raise_()
        self.progressBar.raise_()
        self.loadingLabel.raise_()
        self.logoView.raise_()

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.versionLabel.setText(QCoreApplication.translate("SplashScreen", u"Version", None))
        self.appLabel.setText(QCoreApplication.translate("SplashScreen", u"ImageNexus", None))
        self.label_description.setText(QCoreApplication.translate("SplashScreen", u"{loading_messages}", None))
        self.loadingLabel.setText("")
        self.logoView.setText("")
        self.bgLabel.setText("")
    # retranslateUi

