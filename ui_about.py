# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QLabel,
    QSizePolicy, QTextEdit, QWidget)
import rc_resources

class Ui_aboutWindow(object):
    def setupUi(self, aboutWindow):
        if not aboutWindow.objectName():
            aboutWindow.setObjectName(u"aboutWindow")
        aboutWindow.setWindowModality(Qt.ApplicationModal)
        aboutWindow.resize(472, 516)
        aboutWindow.setMinimumSize(QSize(472, 516))
        aboutWindow.setMaximumSize(QSize(472, 516))
        icon = QIcon()
        icon.addFile(u":/images/resources/icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        aboutWindow.setWindowIcon(icon)
        self.appTextLabel = QLabel(aboutWindow)
        self.appTextLabel.setObjectName(u"appTextLabel")
        self.appTextLabel.setGeometry(QRect(100, 30, 181, 41))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(20)
        self.appTextLabel.setFont(font)
        self.line = QFrame(aboutWindow)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(20, 80, 431, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.versionLabel = QLabel(aboutWindow)
        self.versionLabel.setObjectName(u"versionLabel")
        self.versionLabel.setGeometry(QRect(230, 60, 49, 16))
        self.logoView = QGraphicsView(aboutWindow)
        self.logoView.setObjectName(u"logoView")
        self.logoView.setGeometry(QRect(20, 10, 75, 75))
        self.copyrightLbl = QLabel(aboutWindow)
        self.copyrightLbl.setObjectName(u"copyrightLbl")
        self.copyrightLbl.setGeometry(QRect(40, 460, 201, 16))
        self.devLabel = QLabel(aboutWindow)
        self.devLabel.setObjectName(u"devLabel")
        self.devLabel.setGeometry(QRect(40, 440, 191, 16))
        self.aboutText = QTextEdit(aboutWindow)
        self.aboutText.setObjectName(u"aboutText")
        self.aboutText.setGeometry(QRect(30, 110, 411, 321))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        self.aboutText.setFont(font1)
        self.aboutText.setMouseTracking(False)
        self.aboutText.setFocusPolicy(Qt.NoFocus)
        self.aboutText.setAutoFormatting(QTextEdit.AutoAll)
        self.aboutText.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.retranslateUi(aboutWindow)

        QMetaObject.connectSlotsByName(aboutWindow)
    # setupUi

    def retranslateUi(self, aboutWindow):
        aboutWindow.setWindowTitle(QCoreApplication.translate("aboutWindow", u"About", None))
        self.appTextLabel.setText(QCoreApplication.translate("aboutWindow", u"ImageNexus", None))
        self.versionLabel.setText(QCoreApplication.translate("aboutWindow", u"v", None))
        self.copyrightLbl.setText(QCoreApplication.translate("aboutWindow", u"Copyright \u00a9 2024 LyAhn", None))
        self.devLabel.setText(QCoreApplication.translate("aboutWindow", u"Developed by: LyAhn", None))
        self.aboutText.setHtml(QCoreApplication.translate("aboutWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">This application is built using Python and PySide6. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-b"
                        "lock-indent:0; text-indent:0px; font-family:'Segoe UI';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Have an issue or found a bug? Submit an issue at the repo</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">(https://github.com/lyahn/ImageNexus/issues)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Special thanks to the open-source community and the developers of the libraries used in this project for their valuable work, including Pillow, qrco"
                        "de, and PySide6.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This software is licenced under the GNU General Public Licence v3.0 (GPL-3.0)</p></body></html>", None))
    # retranslateUi

