# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGraphicsView, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QSpinBox,
    QStatusBar, QTabWidget, QTextEdit, QToolButton,
    QWidget)
import resources_rc

class Ui_ImageNexus(object):
    def setupUi(self, ImageNexus):
        if not ImageNexus.objectName():
            ImageNexus.setObjectName(u"ImageNexus")
        ImageNexus.resize(872, 602)
        ImageNexus.setMinimumSize(QSize(650, 475))
        icon = QIcon()
        icon.addFile(u":/images/resources/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        ImageNexus.setWindowIcon(icon)
        self.actionHelp = QAction(ImageNexus)
        self.actionHelp.setObjectName(u"actionHelp")
        self.actionHelp.setEnabled(False)
        self.actionAboutg = QAction(ImageNexus)
        self.actionAboutg.setObjectName(u"actionAboutg")
        self.actionAboutg.setEnabled(False)
        self.actionExit = QAction(ImageNexus)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(ImageNexus)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_12 = QGridLayout(self.centralwidget)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.frameExtractor = QWidget()
        self.frameExtractor.setObjectName(u"frameExtractor")
        self.gridLayout_2 = QGridLayout(self.frameExtractor)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget = QWidget(self.frameExtractor)
        self.widget.setObjectName(u"widget")
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.browseInput1 = QToolButton(self.widget)
        self.browseInput1.setObjectName(u"browseInput1")

        self.gridLayout_3.addWidget(self.browseInput1, 0, 5, 1, 1)

        self.saveAsFormat = QComboBox(self.widget)
        self.saveAsFormat.addItem("")
        self.saveAsFormat.addItem("")
        self.saveAsFormat.setObjectName(u"saveAsFormat")

        self.gridLayout_3.addWidget(self.saveAsFormat, 3, 2, 1, 1)

        self.selectGifLabel = QLabel(self.widget)
        self.selectGifLabel.setObjectName(u"selectGifLabel")

        self.gridLayout_3.addWidget(self.selectGifLabel, 0, 0, 1, 2)

        self.output_folder_entry = QLineEdit(self.widget)
        self.output_folder_entry.setObjectName(u"output_folder_entry")

        self.gridLayout_3.addWidget(self.output_folder_entry, 2, 4, 1, 1)

        self.browseOutput1 = QToolButton(self.widget)
        self.browseOutput1.setObjectName(u"browseOutput1")

        self.gridLayout_3.addWidget(self.browseOutput1, 2, 5, 1, 1)

        self.saveAsLabel = QLabel(self.widget)
        self.saveAsLabel.setObjectName(u"saveAsLabel")

        self.gridLayout_3.addWidget(self.saveAsLabel, 3, 1, 1, 1)

        self.progressBar = QProgressBar(self.widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)

        self.gridLayout_3.addWidget(self.progressBar, 9, 0, 1, 6)

        self.fileInput1 = QLineEdit(self.widget)
        self.fileInput1.setObjectName(u"fileInput1")

        self.gridLayout_3.addWidget(self.fileInput1, 0, 4, 1, 1)

        self.outputFolderLabel = QLabel(self.widget)
        self.outputFolderLabel.setObjectName(u"outputFolderLabel")

        self.gridLayout_3.addWidget(self.outputFolderLabel, 2, 0, 1, 3)

        self.generate_infocheckBox = QCheckBox(self.widget)
        self.generate_infocheckBox.setObjectName(u"generate_infocheckBox")
        self.generate_infocheckBox.setChecked(True)

        self.gridLayout_3.addWidget(self.generate_infocheckBox, 3, 4, 1, 1)

        self.extractor_button = QPushButton(self.widget)
        self.extractor_button.setObjectName(u"extractor_button")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.extractor_button.sizePolicy().hasHeightForWidth())
        self.extractor_button.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.extractor_button, 3, 5, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        self.tabWidget.addTab(self.frameExtractor, "")
        self.imageConverter = QWidget()
        self.imageConverter.setObjectName(u"imageConverter")
        self.gridLayout = QGridLayout(self.imageConverter)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_2 = QWidget(self.imageConverter)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_4 = QGridLayout(self.widget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.inputBrowse2 = QToolButton(self.widget_2)
        self.inputBrowse2.setObjectName(u"inputBrowse2")

        self.gridLayout_4.addWidget(self.inputBrowse2, 0, 5, 1, 1)

        self.selectGifLabel_2 = QLabel(self.widget_2)
        self.selectGifLabel_2.setObjectName(u"selectGifLabel_2")

        self.gridLayout_4.addWidget(self.selectGifLabel_2, 0, 0, 1, 2)

        self.outputBrowse2 = QToolButton(self.widget_2)
        self.outputBrowse2.setObjectName(u"outputBrowse2")

        self.gridLayout_4.addWidget(self.outputBrowse2, 2, 5, 1, 1)

        self.saveAsLabel_2 = QLabel(self.widget_2)
        self.saveAsLabel_2.setObjectName(u"saveAsLabel_2")

        self.gridLayout_4.addWidget(self.saveAsLabel_2, 4, 0, 1, 1)

        self.progressBar_2 = QProgressBar(self.widget_2)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setValue(0)
        self.progressBar_2.setTextVisible(False)

        self.gridLayout_4.addWidget(self.progressBar_2, 5, 0, 1, 6)

        self.fileInput2 = QLineEdit(self.widget_2)
        self.fileInput2.setObjectName(u"fileInput2")

        self.gridLayout_4.addWidget(self.fileInput2, 0, 4, 1, 1)

        self.outputFolderLabel_2 = QLabel(self.widget_2)
        self.outputFolderLabel_2.setObjectName(u"outputFolderLabel_2")

        self.gridLayout_4.addWidget(self.outputFolderLabel_2, 2, 0, 1, 3)

        self.outputFolder2 = QLineEdit(self.widget_2)
        self.outputFolder2.setObjectName(u"outputFolder2")

        self.gridLayout_4.addWidget(self.outputFolder2, 2, 4, 1, 1)

        self.saveAsFormat_2 = QComboBox(self.widget_2)
        self.saveAsFormat_2.addItem("")
        self.saveAsFormat_2.addItem("")
        self.saveAsFormat_2.addItem("")
        self.saveAsFormat_2.addItem("")
        self.saveAsFormat_2.addItem("")
        self.saveAsFormat_2.setObjectName(u"saveAsFormat_2")

        self.gridLayout_4.addWidget(self.saveAsFormat_2, 4, 2, 1, 1)

        self.converter_button = QPushButton(self.widget_2)
        self.converter_button.setObjectName(u"converter_button")

        self.gridLayout_4.addWidget(self.converter_button, 4, 5, 1, 1)


        self.gridLayout.addWidget(self.widget_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.imageConverter, "")
        self.batchConverter = QWidget()
        self.batchConverter.setObjectName(u"batchConverter")
        self.gridLayout_6 = QGridLayout(self.batchConverter)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.widget_3 = QWidget(self.batchConverter)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_5 = QGridLayout(self.widget_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.inputBrowse3 = QToolButton(self.widget_3)
        self.inputBrowse3.setObjectName(u"inputBrowse3")

        self.gridLayout_5.addWidget(self.inputBrowse3, 1, 3, 1, 1)

        self.formatOptions = QComboBox(self.widget_3)
        self.formatOptions.addItem("")
        self.formatOptions.addItem("")
        self.formatOptions.addItem("")
        self.formatOptions.addItem("")
        self.formatOptions.addItem("")
        self.formatOptions.setObjectName(u"formatOptions")

        self.gridLayout_5.addWidget(self.formatOptions, 3, 1, 1, 1)

        self.conversionType = QComboBox(self.widget_3)
        self.conversionType.addItem("")
        self.conversionType.addItem("")
        self.conversionType.setObjectName(u"conversionType")

        self.gridLayout_5.addWidget(self.conversionType, 0, 1, 1, 1)

        self.outputFolderLabel_3 = QLabel(self.widget_3)
        self.outputFolderLabel_3.setObjectName(u"outputFolderLabel_3")

        self.gridLayout_5.addWidget(self.outputFolderLabel_3, 2, 0, 1, 1)

        self.outputFormatLabel = QLabel(self.widget_3)
        self.outputFormatLabel.setObjectName(u"outputFormatLabel")

        self.gridLayout_5.addWidget(self.outputFormatLabel, 3, 0, 1, 1)

        self.converter_button2 = QPushButton(self.widget_3)
        self.converter_button2.setObjectName(u"converter_button2")

        self.gridLayout_5.addWidget(self.converter_button2, 3, 3, 1, 1)

        self.outputFolder3 = QLineEdit(self.widget_3)
        self.outputFolder3.setObjectName(u"outputFolder3")

        self.gridLayout_5.addWidget(self.outputFolder3, 2, 2, 1, 1)

        self.selectGifLabel_4 = QLabel(self.widget_3)
        self.selectGifLabel_4.setObjectName(u"selectGifLabel_4")

        self.gridLayout_5.addWidget(self.selectGifLabel_4, 0, 0, 1, 1)

        self.selectGifLabel_3 = QLabel(self.widget_3)
        self.selectGifLabel_3.setObjectName(u"selectGifLabel_3")

        self.gridLayout_5.addWidget(self.selectGifLabel_3, 1, 0, 1, 1)

        self.fileInput3 = QLineEdit(self.widget_3)
        self.fileInput3.setObjectName(u"fileInput3")

        self.gridLayout_5.addWidget(self.fileInput3, 1, 2, 1, 1)

        self.outputBrowse3 = QToolButton(self.widget_3)
        self.outputBrowse3.setObjectName(u"outputBrowse3")

        self.gridLayout_5.addWidget(self.outputBrowse3, 2, 3, 1, 1)


        self.gridLayout_6.addWidget(self.widget_3, 0, 0, 1, 1)

        self.tabWidget.addTab(self.batchConverter, "")
        self.qrGenerator = QWidget()
        self.qrGenerator.setObjectName(u"qrGenerator")
        self.gridLayout_10 = QGridLayout(self.qrGenerator)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.widget_4 = QWidget(self.qrGenerator)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_7 = QGridLayout(self.widget_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.logoBrowseButton = QPushButton(self.widget_4)
        self.logoBrowseButton.setObjectName(u"logoBrowseButton")
        sizePolicy.setHeightForWidth(self.logoBrowseButton.sizePolicy().hasHeightForWidth())
        self.logoBrowseButton.setSizePolicy(sizePolicy)

        self.gridLayout_7.addWidget(self.logoBrowseButton, 1, 6, 1, 1)

        self.qrOutputGroup = QGroupBox(self.widget_4)
        self.qrOutputGroup.setObjectName(u"qrOutputGroup")
        self.gridLayout_11 = QGridLayout(self.qrOutputGroup)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.qrOutputView = QGraphicsView(self.qrOutputGroup)
        self.qrOutputView.setObjectName(u"qrOutputView")
        self.qrOutputView.setBaseSize(QSize(0, 0))

        self.gridLayout_11.addWidget(self.qrOutputView, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.qrOutputGroup, 0, 8, 3, 1)

        self.qrSizeSpinBox = QSpinBox(self.widget_4)
        self.qrSizeSpinBox.setObjectName(u"qrSizeSpinBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.qrSizeSpinBox.sizePolicy().hasHeightForWidth())
        self.qrSizeSpinBox.setSizePolicy(sizePolicy1)
        self.qrSizeSpinBox.setMaximumSize(QSize(80, 16777215))
        self.qrSizeSpinBox.setMinimum(1)
        self.qrSizeSpinBox.setMaximum(40)

        self.gridLayout_7.addWidget(self.qrSizeSpinBox, 5, 5, 1, 2)

        self.logoImageLabel = QLabel(self.widget_4)
        self.logoImageLabel.setObjectName(u"logoImageLabel")

        self.gridLayout_7.addWidget(self.logoImageLabel, 1, 0, 1, 1)

        self.errorCorrectionCombo = QComboBox(self.widget_4)
        self.errorCorrectionCombo.addItem("")
        self.errorCorrectionCombo.addItem("")
        self.errorCorrectionCombo.addItem("")
        self.errorCorrectionCombo.addItem("")
        self.errorCorrectionCombo.setObjectName(u"errorCorrectionCombo")

        self.gridLayout_7.addWidget(self.errorCorrectionCombo, 3, 2, 1, 1)

        self.qrTextInput = QTextEdit(self.widget_4)
        self.qrTextInput.setObjectName(u"qrTextInput")
        self.qrTextInput.setFrameShape(QFrame.Panel)
        self.qrTextInput.setFrameShadow(QFrame.Sunken)

        self.gridLayout_7.addWidget(self.qrTextInput, 0, 1, 1, 5)

        self.logoImageInput = QLineEdit(self.widget_4)
        self.logoImageInput.setObjectName(u"logoImageInput")

        self.gridLayout_7.addWidget(self.logoImageInput, 1, 1, 1, 5)

        self.qrTextInputLabel = QLabel(self.widget_4)
        self.qrTextInputLabel.setObjectName(u"qrTextInputLabel")

        self.gridLayout_7.addWidget(self.qrTextInputLabel, 0, 0, 1, 1)

        self.errorCorrectLabel = QLabel(self.widget_4)
        self.errorCorrectLabel.setObjectName(u"errorCorrectLabel")

        self.gridLayout_7.addWidget(self.errorCorrectLabel, 3, 0, 1, 1)

        self.saveAsLabel_3 = QLabel(self.widget_4)
        self.saveAsLabel_3.setObjectName(u"saveAsLabel_3")

        self.gridLayout_7.addWidget(self.saveAsLabel_3, 5, 0, 1, 2)

        self.borderSpinLabel = QLabel(self.widget_4)
        self.borderSpinLabel.setObjectName(u"borderSpinLabel")

        self.gridLayout_7.addWidget(self.borderSpinLabel, 3, 3, 1, 2)

        self.saveAsComboBox = QComboBox(self.widget_4)
        self.saveAsComboBox.addItem("")
        self.saveAsComboBox.addItem("")
        self.saveAsComboBox.setObjectName(u"saveAsComboBox")

        self.gridLayout_7.addWidget(self.saveAsComboBox, 5, 2, 1, 1)

        self.qrSizeLabel = QLabel(self.widget_4)
        self.qrSizeLabel.setObjectName(u"qrSizeLabel")

        self.gridLayout_7.addWidget(self.qrSizeLabel, 5, 3, 1, 2)

        self.borderSpinBox = QSpinBox(self.widget_4)
        self.borderSpinBox.setObjectName(u"borderSpinBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.borderSpinBox.sizePolicy().hasHeightForWidth())
        self.borderSpinBox.setSizePolicy(sizePolicy2)
        self.borderSpinBox.setMaximumSize(QSize(80, 16777215))
        self.borderSpinBox.setMaximum(10)

        self.gridLayout_7.addWidget(self.borderSpinBox, 3, 5, 1, 4)

        self.outputFolderText = QLineEdit(self.widget_4)
        self.outputFolderText.setObjectName(u"outputFolderText")

        self.gridLayout_7.addWidget(self.outputFolderText, 6, 2, 1, 1)

        self.outputFolderLabel_4 = QLabel(self.widget_4)
        self.outputFolderLabel_4.setObjectName(u"outputFolderLabel_4")

        self.gridLayout_7.addWidget(self.outputFolderLabel_4, 6, 0, 1, 1)

        self.browseFolderButton = QPushButton(self.widget_4)
        self.browseFolderButton.setObjectName(u"browseFolderButton")

        self.gridLayout_7.addWidget(self.browseFolderButton, 6, 3, 1, 1)

        self.saveQRButton = QPushButton(self.widget_4)
        self.saveQRButton.setObjectName(u"saveQRButton")

        self.gridLayout_7.addWidget(self.saveQRButton, 6, 8, 1, 1)

        self.codeColourGroup = QGroupBox(self.widget_4)
        self.codeColourGroup.setObjectName(u"codeColourGroup")
        self.codeColourGroup.setEnabled(False)
        self.gridLayout_9 = QGridLayout(self.codeColourGroup)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.codeColourInput = QLineEdit(self.codeColourGroup)
        self.codeColourInput.setObjectName(u"codeColourInput")

        self.gridLayout_9.addWidget(self.codeColourInput, 0, 0, 1, 1)

        self.codeColourButton = QToolButton(self.codeColourGroup)
        self.codeColourButton.setObjectName(u"codeColourButton")

        self.gridLayout_9.addWidget(self.codeColourButton, 0, 1, 1, 1)


        self.gridLayout_7.addWidget(self.codeColourGroup, 2, 3, 1, 4)

        self.bgColourGroup = QGroupBox(self.widget_4)
        self.bgColourGroup.setObjectName(u"bgColourGroup")
        self.bgColourGroup.setEnabled(False)
        self.gridLayout_8 = QGridLayout(self.bgColourGroup)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.bgColourInput = QLineEdit(self.bgColourGroup)
        self.bgColourInput.setObjectName(u"bgColourInput")

        self.gridLayout_8.addWidget(self.bgColourInput, 0, 0, 1, 1)

        self.bgColourButton = QToolButton(self.bgColourGroup)
        self.bgColourButton.setObjectName(u"bgColourButton")

        self.gridLayout_8.addWidget(self.bgColourButton, 0, 1, 1, 1)


        self.gridLayout_7.addWidget(self.bgColourGroup, 2, 0, 1, 3)

        self.qrGenButton = QPushButton(self.widget_4)
        self.qrGenButton.setObjectName(u"qrGenButton")
        sizePolicy.setHeightForWidth(self.qrGenButton.sizePolicy().hasHeightForWidth())
        self.qrGenButton.setSizePolicy(sizePolicy)
        self.qrGenButton.setLayoutDirection(Qt.RightToLeft)
        self.qrGenButton.setFlat(False)

        self.gridLayout_7.addWidget(self.qrGenButton, 5, 8, 1, 1)


        self.gridLayout_10.addWidget(self.widget_4, 0, 0, 1, 1)

        self.tabWidget.addTab(self.qrGenerator, "")

        self.gridLayout_12.addWidget(self.tabWidget, 0, 0, 1, 1)

        ImageNexus.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ImageNexus)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 872, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        ImageNexus.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ImageNexus)
        self.statusbar.setObjectName(u"statusbar")
        ImageNexus.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAboutg)

        self.retranslateUi(ImageNexus)
        self.actionExit.triggered.connect(ImageNexus.close)

        self.tabWidget.setCurrentIndex(0)
        self.qrGenButton.setDefault(False)


        QMetaObject.connectSlotsByName(ImageNexus)
    # setupUi

    def retranslateUi(self, ImageNexus):
        ImageNexus.setWindowTitle(QCoreApplication.translate("ImageNexus", u"ImageNexus {version}", None))
        self.actionHelp.setText(QCoreApplication.translate("ImageNexus", u"Help...", None))
        self.actionAboutg.setText(QCoreApplication.translate("ImageNexus", u"About", None))
        self.actionExit.setText(QCoreApplication.translate("ImageNexus", u"Exit", None))
        self.browseInput1.setText(QCoreApplication.translate("ImageNexus", u"Browse", None))
        self.saveAsFormat.setItemText(0, QCoreApplication.translate("ImageNexus", u"PNG", None))
        self.saveAsFormat.setItemText(1, QCoreApplication.translate("ImageNexus", u"GIF", None))

        self.selectGifLabel.setText(QCoreApplication.translate("ImageNexus", u"Select GIF:", None))
        self.output_folder_entry.setPlaceholderText(QCoreApplication.translate("ImageNexus", u"Select an output folder...", None))
        self.browseOutput1.setText(QCoreApplication.translate("ImageNexus", u"Browse", None))
        self.saveAsLabel.setText(QCoreApplication.translate("ImageNexus", u"Save as:", None))
        self.fileInput1.setPlaceholderText(QCoreApplication.translate("ImageNexus", u"Select a GIF...", None))
        self.outputFolderLabel.setText(QCoreApplication.translate("ImageNexus", u"Output Folder:", None))
        self.generate_infocheckBox.setText(QCoreApplication.translate("ImageNexus", u"Generate frame info file", None))
        self.extractor_button.setText(QCoreApplication.translate("ImageNexus", u"Extract Frames", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.frameExtractor), QCoreApplication.translate("ImageNexus", u"Frame Extractor", None))
        self.inputBrowse2.setText(QCoreApplication.translate("ImageNexus", u"Browse", None))
        self.selectGifLabel_2.setText(QCoreApplication.translate("ImageNexus", u"Select Input File:", None))
        self.outputBrowse2.setText(QCoreApplication.translate("ImageNexus", u"Browse", None))
        self.saveAsLabel_2.setText(QCoreApplication.translate("ImageNexus", u"Output Format:", None))
        self.fileInput2.setPlaceholderText(QCoreApplication.translate("ImageNexus", u"Select an image...", None))
        self.outputFolderLabel_2.setText(QCoreApplication.translate("ImageNexus", u"Output Folder:", None))
        self.outputFolder2.setPlaceholderText(QCoreApplication.translate("ImageNexus", u"Select an output folder...", None))
        self.saveAsFormat_2.setItemText(0, QCoreApplication.translate("ImageNexus", u"GIF", None))
        self.saveAsFormat_2.setItemText(1, QCoreApplication.translate("ImageNexus", u"PNG", None))
        self.saveAsFormat_2.setItemText(2, QCoreApplication.translate("ImageNexus", u"JPEG", None))
        self.saveAsFormat_2.setItemText(3, QCoreApplication.translate("ImageNexus", u"BMP", None))
        self.saveAsFormat_2.setItemText(4, QCoreApplication.translate("ImageNexus", u"TIFF", None))

        self.converter_button.setText(QCoreApplication.translate("ImageNexus", u"Convert", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.imageConverter), QCoreApplication.translate("ImageNexus", u"Image Converter", None))
        self.inputBrowse3.setText(QCoreApplication.translate("ImageNexus", u"Browse", None))
        self.formatOptions.setItemText(0, QCoreApplication.translate("ImageNexus", u"GIF", None))
        self.formatOptions.setItemText(1, QCoreApplication.translate("ImageNexus", u"PNG", None))
        self.formatOptions.setItemText(2, QCoreApplication.translate("ImageNexus", u"JPEG", None))
        self.formatOptions.setItemText(3, QCoreApplication.translate("ImageNexus", u"BMP", None))
        self.formatOptions.setItemText(4, QCoreApplication.translate("ImageNexus", u"TIFF", None))

        self.conversionType.setItemText(0, QCoreApplication.translate("ImageNexus", u"Files", None))
        self.conversionType.setItemText(1, QCoreApplication.translate("ImageNexus", u"Folder", None))

        self.outputFolderLabel_3.setText(QCoreApplication.translate("ImageNexus", u"Output Folder:", None))
        self.outputFormatLabel.setText(QCoreApplication.translate("ImageNexus", u"Output Format:", None))
        self.converter_button2.setText(QCoreApplication.translate("ImageNexus", u"Convert Files", None))
        self.outputFolder3.setPlaceholderText(QCoreApplication.translate("ImageNexus", u"Select an output folder...", None))
        self.selectGifLabel_4.setText(QCoreApplication.translate("ImageNexus", u"Conversion Type:", None))
        self.selectGifLabel_3.setText(QCoreApplication.translate("ImageNexus", u"Select Input File:", None))
        self.fileInput3.setPlaceholderText(QCoreApplication.translate("ImageNexus", u"Select an image or folder...", None))
        self.outputBrowse3.setText(QCoreApplication.translate("ImageNexus", u"Browse", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.batchConverter), QCoreApplication.translate("ImageNexus", u"Batch Converter", None))
        self.logoBrowseButton.setText(QCoreApplication.translate("ImageNexus", u"Browse", None))
        self.qrOutputGroup.setTitle(QCoreApplication.translate("ImageNexus", u"Generated QR", None))
#if QT_CONFIG(statustip)
        self.qrSizeSpinBox.setStatusTip(QCoreApplication.translate("ImageNexus", u"Value between 1-40", None))
#endif // QT_CONFIG(statustip)
        self.logoImageLabel.setText(QCoreApplication.translate("ImageNexus", u"Logo Image:", None))
        self.errorCorrectionCombo.setItemText(0, QCoreApplication.translate("ImageNexus", u"Low", None))
        self.errorCorrectionCombo.setItemText(1, QCoreApplication.translate("ImageNexus", u"Medium", None))
        self.errorCorrectionCombo.setItemText(2, QCoreApplication.translate("ImageNexus", u"Quartile", None))
        self.errorCorrectionCombo.setItemText(3, QCoreApplication.translate("ImageNexus", u"High", None))

        self.qrTextInput.setPlaceholderText(QCoreApplication.translate("ImageNexus", u"Please enter some text to generate a QR code...", None))
        self.logoImageInput.setText("")
        self.logoImageInput.setPlaceholderText(QCoreApplication.translate("ImageNexus", u"Insert a logo... (Optional)", None))
        self.qrTextInputLabel.setText(QCoreApplication.translate("ImageNexus", u"QR Data:", None))
        self.errorCorrectLabel.setText(QCoreApplication.translate("ImageNexus", u"Error Correction:", None))
        self.saveAsLabel_3.setText(QCoreApplication.translate("ImageNexus", u"Save As:", None))
        self.borderSpinLabel.setText(QCoreApplication.translate("ImageNexus", u"Border Size:", None))
        self.saveAsComboBox.setItemText(0, QCoreApplication.translate("ImageNexus", u"PNG", None))
        self.saveAsComboBox.setItemText(1, QCoreApplication.translate("ImageNexus", u"SVG", None))

        self.qrSizeLabel.setText(QCoreApplication.translate("ImageNexus", u"QR Size:", None))
#if QT_CONFIG(statustip)
        self.borderSpinBox.setStatusTip(QCoreApplication.translate("ImageNexus", u"Value between 0-10", None))
#endif // QT_CONFIG(statustip)
        self.outputFolderLabel_4.setText(QCoreApplication.translate("ImageNexus", u"Output Folder:", None))
        self.browseFolderButton.setText(QCoreApplication.translate("ImageNexus", u"Browse", None))
        self.saveQRButton.setText(QCoreApplication.translate("ImageNexus", u"Save QR Code", None))
#if QT_CONFIG(statustip)
        self.codeColourGroup.setStatusTip(QCoreApplication.translate("ImageNexus", u"Disabled", None))
#endif // QT_CONFIG(statustip)
        self.codeColourGroup.setTitle(QCoreApplication.translate("ImageNexus", u"QR Code Colour", None))
        self.codeColourInput.setText(QCoreApplication.translate("ImageNexus", u"0,0,0", None))
        self.codeColourButton.setText(QCoreApplication.translate("ImageNexus", u"...", None))
#if QT_CONFIG(statustip)
        self.bgColourGroup.setStatusTip(QCoreApplication.translate("ImageNexus", u"Disabled", None))
#endif // QT_CONFIG(statustip)
        self.bgColourGroup.setTitle(QCoreApplication.translate("ImageNexus", u"Background Colour", None))
        self.bgColourInput.setText(QCoreApplication.translate("ImageNexus", u"255, 0, 0", None))
        self.bgColourButton.setText(QCoreApplication.translate("ImageNexus", u"...", None))
        self.qrGenButton.setText(QCoreApplication.translate("ImageNexus", u"Generate QR", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.qrGenerator), QCoreApplication.translate("ImageNexus", u"QR Generator", None))
        self.menuFile.setTitle(QCoreApplication.translate("ImageNexus", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("ImageNexus", u"Help", None))
    # retranslateUi

