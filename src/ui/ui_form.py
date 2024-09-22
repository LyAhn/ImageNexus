# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QGraphicsView, QGridLayout, QGroupBox,
    QLabel, QLayout, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QProgressBar, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QStatusBar,
    QTabWidget, QTextEdit, QToolBox, QToolButton,
    QWidget)
import rc_resources

class Ui_ImageNexus(object):
    def setupUi(self, ImageNexus):
        if not ImageNexus.objectName():
            ImageNexus.setObjectName(u"ImageNexus")
        ImageNexus.resize(938, 681)
        ImageNexus.setMinimumSize(QSize(938, 681))
        icon = QIcon()
        icon.addFile(u":/images/resources/icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        ImageNexus.setWindowIcon(icon)
        self.actionHelp = QAction(ImageNexus)
        self.actionHelp.setObjectName(u"actionHelp")
        self.actionHelp.setEnabled(False)
        self.actionAbout = QAction(ImageNexus)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionAbout.setEnabled(True)
        self.actionExit = QAction(ImageNexus)
        self.actionExit.setObjectName(u"actionExit")
        self.actionReloadTemplates = QAction(ImageNexus)
        self.actionReloadTemplates.setObjectName(u"actionReloadTemplates")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ViewRefresh))
        self.actionReloadTemplates.setIcon(icon1)
        self.actionQRTemplateEditor = QAction(ImageNexus)
        self.actionQRTemplateEditor.setObjectName(u"actionQRTemplateEditor")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.InputKeyboard))
        self.actionQRTemplateEditor.setIcon(icon2)
        self.centralwidget = QWidget(ImageNexus)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_12 = QGridLayout(self.centralwidget)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.frameExtractor = QWidget()
        self.frameExtractor.setObjectName(u"frameExtractor")
        self.gridLayout_2 = QGridLayout(self.frameExtractor)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget = QWidget(self.frameExtractor)
        self.widget.setObjectName(u"widget")
        self.widget.setAcceptDrops(False)
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.feBrowseInput = QToolButton(self.widget)
        self.feBrowseInput.setObjectName(u"feBrowseInput")

        self.gridLayout_3.addWidget(self.feBrowseInput, 0, 5, 1, 1)

        self.feFormatOptions = QComboBox(self.widget)
        self.feFormatOptions.addItem("")
        self.feFormatOptions.addItem("")
        self.feFormatOptions.setObjectName(u"feFormatOptions")

        self.gridLayout_3.addWidget(self.feFormatOptions, 3, 2, 1, 1)

        self.feSelectGifLbl = QLabel(self.widget)
        self.feSelectGifLbl.setObjectName(u"feSelectGifLbl")

        self.gridLayout_3.addWidget(self.feSelectGifLbl, 0, 0, 1, 2)

        self.feOutputFolder = QLineEdit(self.widget)
        self.feOutputFolder.setObjectName(u"feOutputFolder")

        self.gridLayout_3.addWidget(self.feOutputFolder, 2, 4, 1, 1)

        self.feBrowseOutput = QToolButton(self.widget)
        self.feBrowseOutput.setObjectName(u"feBrowseOutput")

        self.gridLayout_3.addWidget(self.feBrowseOutput, 2, 5, 1, 1)

        self.feFormatOptionsLbl = QLabel(self.widget)
        self.feFormatOptionsLbl.setObjectName(u"feFormatOptionsLbl")

        self.gridLayout_3.addWidget(self.feFormatOptionsLbl, 3, 1, 1, 1)

        self.feProgressBar = QProgressBar(self.widget)
        self.feProgressBar.setObjectName(u"feProgressBar")
        self.feProgressBar.setValue(0)
        self.feProgressBar.setTextVisible(False)

        self.gridLayout_3.addWidget(self.feProgressBar, 9, 0, 1, 6)

        self.feFileInput = QLineEdit(self.widget)
        self.feFileInput.setObjectName(u"feFileInput")

        self.gridLayout_3.addWidget(self.feFileInput, 0, 4, 1, 1)

        self.feOutputFolderLbl = QLabel(self.widget)
        self.feOutputFolderLbl.setObjectName(u"feOutputFolderLbl")

        self.gridLayout_3.addWidget(self.feOutputFolderLbl, 2, 0, 1, 3)

        self.feInfoCheckbox = QCheckBox(self.widget)
        self.feInfoCheckbox.setObjectName(u"feInfoCheckbox")
        self.feInfoCheckbox.setChecked(True)

        self.gridLayout_3.addWidget(self.feInfoCheckbox, 3, 4, 1, 1)

        self.feExtractBtn = QPushButton(self.widget)
        self.feExtractBtn.setObjectName(u"feExtractBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feExtractBtn.sizePolicy().hasHeightForWidth())
        self.feExtractBtn.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.feExtractBtn, 3, 5, 1, 1)


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
        self.icBrowseInput = QToolButton(self.widget_2)
        self.icBrowseInput.setObjectName(u"icBrowseInput")

        self.gridLayout_4.addWidget(self.icBrowseInput, 0, 5, 1, 1)

        self.icInputFileLbl = QLabel(self.widget_2)
        self.icInputFileLbl.setObjectName(u"icInputFileLbl")

        self.gridLayout_4.addWidget(self.icInputFileLbl, 0, 0, 1, 2)

        self.icBrowseOutput = QToolButton(self.widget_2)
        self.icBrowseOutput.setObjectName(u"icBrowseOutput")

        self.gridLayout_4.addWidget(self.icBrowseOutput, 2, 5, 1, 1)

        self.icFormatOptionsLbl = QLabel(self.widget_2)
        self.icFormatOptionsLbl.setObjectName(u"icFormatOptionsLbl")

        self.gridLayout_4.addWidget(self.icFormatOptionsLbl, 4, 0, 1, 1)

        self.icProgressBar = QProgressBar(self.widget_2)
        self.icProgressBar.setObjectName(u"icProgressBar")
        self.icProgressBar.setValue(0)
        self.icProgressBar.setTextVisible(False)

        self.gridLayout_4.addWidget(self.icProgressBar, 5, 0, 1, 6)

        self.icFileInput = QLineEdit(self.widget_2)
        self.icFileInput.setObjectName(u"icFileInput")

        self.gridLayout_4.addWidget(self.icFileInput, 0, 4, 1, 1)

        self.icOutputFolderLbl = QLabel(self.widget_2)
        self.icOutputFolderLbl.setObjectName(u"icOutputFolderLbl")

        self.gridLayout_4.addWidget(self.icOutputFolderLbl, 2, 0, 1, 3)

        self.icOutputFolder = QLineEdit(self.widget_2)
        self.icOutputFolder.setObjectName(u"icOutputFolder")

        self.gridLayout_4.addWidget(self.icOutputFolder, 2, 4, 1, 1)

        self.icFormatOptions = QComboBox(self.widget_2)
        self.icFormatOptions.addItem("")
        self.icFormatOptions.addItem("")
        self.icFormatOptions.addItem("")
        self.icFormatOptions.addItem("")
        self.icFormatOptions.addItem("")
        self.icFormatOptions.setObjectName(u"icFormatOptions")

        self.gridLayout_4.addWidget(self.icFormatOptions, 4, 2, 1, 1)

        self.icConvertBtn = QPushButton(self.widget_2)
        self.icConvertBtn.setObjectName(u"icConvertBtn")

        self.gridLayout_4.addWidget(self.icConvertBtn, 4, 5, 1, 1)


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
        self.bcInputBrowse = QToolButton(self.widget_3)
        self.bcInputBrowse.setObjectName(u"bcInputBrowse")

        self.gridLayout_5.addWidget(self.bcInputBrowse, 1, 3, 1, 1)

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

        self.bcOutputFolderLbl = QLabel(self.widget_3)
        self.bcOutputFolderLbl.setObjectName(u"bcOutputFolderLbl")

        self.gridLayout_5.addWidget(self.bcOutputFolderLbl, 2, 0, 1, 1)

        self.bcOutputFormatLbl = QLabel(self.widget_3)
        self.bcOutputFormatLbl.setObjectName(u"bcOutputFormatLbl")

        self.gridLayout_5.addWidget(self.bcOutputFormatLbl, 3, 0, 1, 1)

        self.bcConvertBtn = QPushButton(self.widget_3)
        self.bcConvertBtn.setObjectName(u"bcConvertBtn")

        self.gridLayout_5.addWidget(self.bcConvertBtn, 3, 3, 1, 1)

        self.bcOutputFolder = QLineEdit(self.widget_3)
        self.bcOutputFolder.setObjectName(u"bcOutputFolder")

        self.gridLayout_5.addWidget(self.bcOutputFolder, 2, 2, 1, 1)

        self.bcConversionTypeLbl = QLabel(self.widget_3)
        self.bcConversionTypeLbl.setObjectName(u"bcConversionTypeLbl")

        self.gridLayout_5.addWidget(self.bcConversionTypeLbl, 0, 0, 1, 1)

        self.bcInputFileLbl = QLabel(self.widget_3)
        self.bcInputFileLbl.setObjectName(u"bcInputFileLbl")

        self.gridLayout_5.addWidget(self.bcInputFileLbl, 1, 0, 1, 1)

        self.bcFileInput = QLineEdit(self.widget_3)
        self.bcFileInput.setObjectName(u"bcFileInput")

        self.gridLayout_5.addWidget(self.bcFileInput, 1, 2, 1, 1)

        self.bcOutputBrowse = QToolButton(self.widget_3)
        self.bcOutputBrowse.setObjectName(u"bcOutputBrowse")

        self.gridLayout_5.addWidget(self.bcOutputBrowse, 2, 3, 1, 1)


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
        self.qrGenButton = QPushButton(self.widget_4)
        self.qrGenButton.setObjectName(u"qrGenButton")
        sizePolicy.setHeightForWidth(self.qrGenButton.sizePolicy().hasHeightForWidth())
        self.qrGenButton.setSizePolicy(sizePolicy)
        self.qrGenButton.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.qrGenButton.setFlat(False)

        self.gridLayout_7.addWidget(self.qrGenButton, 14, 9, 1, 1)

        self.qrCodeSize = QSpinBox(self.widget_4)
        self.qrCodeSize.setObjectName(u"qrCodeSize")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.qrCodeSize.sizePolicy().hasHeightForWidth())
        self.qrCodeSize.setSizePolicy(sizePolicy1)
        self.qrCodeSize.setMaximumSize(QSize(80, 16777215))
        self.qrCodeSize.setMinimum(1)
        self.qrCodeSize.setMaximum(40)

        self.gridLayout_7.addWidget(self.qrCodeSize, 14, 5, 1, 3)

        self.qrAddBGCheck = QCheckBox(self.widget_4)
        self.qrAddBGCheck.setObjectName(u"qrAddBGCheck")

        self.gridLayout_7.addWidget(self.qrAddBGCheck, 9, 2, 1, 1)

        self.qrBorderSize = QSpinBox(self.widget_4)
        self.qrBorderSize.setObjectName(u"qrBorderSize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.qrBorderSize.sizePolicy().hasHeightForWidth())
        self.qrBorderSize.setSizePolicy(sizePolicy2)
        self.qrBorderSize.setMaximumSize(QSize(80, 16777215))
        self.qrBorderSize.setMaximum(10)
        self.qrBorderSize.setValue(1)

        self.gridLayout_7.addWidget(self.qrBorderSize, 12, 5, 1, 5)

        self.qrAspectRatioCheck = QCheckBox(self.widget_4)
        self.qrAspectRatioCheck.setObjectName(u"qrAspectRatioCheck")

        self.gridLayout_7.addWidget(self.qrAspectRatioCheck, 9, 3, 1, 1)

        self.qrTemplates = QComboBox(self.widget_4)
        self.qrTemplates.addItem("")
        self.qrTemplates.setObjectName(u"qrTemplates")

        self.gridLayout_7.addWidget(self.qrTemplates, 0, 7, 1, 1)

        self.codeColourGroup = QGroupBox(self.widget_4)
        self.codeColourGroup.setObjectName(u"codeColourGroup")
        self.codeColourGroup.setEnabled(True)
        self.gridLayout_9 = QGridLayout(self.codeColourGroup)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.qrCodeColourInput = QLineEdit(self.codeColourGroup)
        self.qrCodeColourInput.setObjectName(u"qrCodeColourInput")

        self.gridLayout_9.addWidget(self.qrCodeColourInput, 0, 0, 1, 1)

        self.qrCodeColourBtn = QToolButton(self.codeColourGroup)
        self.qrCodeColourBtn.setObjectName(u"qrCodeColourBtn")

        self.gridLayout_9.addWidget(self.qrCodeColourBtn, 0, 1, 1, 1)


        self.gridLayout_7.addWidget(self.codeColourGroup, 11, 3, 1, 5)

        self.qrTextInput = QTextEdit(self.widget_4)
        self.qrTextInput.setObjectName(u"qrTextInput")
        self.qrTextInput.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.qrTextInput.setFrameShape(QFrame.Shape.Panel)
        self.qrTextInput.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_7.addWidget(self.qrTextInput, 0, 1, 1, 5)

        self.qrBrowseLogo = QPushButton(self.widget_4)
        self.qrBrowseLogo.setObjectName(u"qrBrowseLogo")
        sizePolicy.setHeightForWidth(self.qrBrowseLogo.sizePolicy().hasHeightForWidth())
        self.qrBrowseLogo.setSizePolicy(sizePolicy)

        self.gridLayout_7.addWidget(self.qrBrowseLogo, 6, 7, 1, 1)

        self.qrLogoInputLbl = QLabel(self.widget_4)
        self.qrLogoInputLbl.setObjectName(u"qrLogoInputLbl")

        self.gridLayout_7.addWidget(self.qrLogoInputLbl, 6, 0, 1, 1)

        self.qrBrowseOutput = QPushButton(self.widget_4)
        self.qrBrowseOutput.setObjectName(u"qrBrowseOutput")

        self.gridLayout_7.addWidget(self.qrBrowseOutput, 15, 3, 1, 1)

        self.qrFormatOptionsLbl = QLabel(self.widget_4)
        self.qrFormatOptionsLbl.setObjectName(u"qrFormatOptionsLbl")

        self.gridLayout_7.addWidget(self.qrFormatOptionsLbl, 14, 0, 1, 2)

        self.qrOutputFolderLbl = QLabel(self.widget_4)
        self.qrOutputFolderLbl.setObjectName(u"qrOutputFolderLbl")

        self.gridLayout_7.addWidget(self.qrOutputFolderLbl, 15, 0, 1, 1)

        self.qrUseArtisticCheck = QCheckBox(self.widget_4)
        self.qrUseArtisticCheck.setObjectName(u"qrUseArtisticCheck")

        self.gridLayout_7.addWidget(self.qrUseArtisticCheck, 10, 2, 1, 1)

        self.qrOutputGroup = QGroupBox(self.widget_4)
        self.qrOutputGroup.setObjectName(u"qrOutputGroup")
        self.gridLayout_11 = QGridLayout(self.qrOutputGroup)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.qrOutputView = QGraphicsView(self.qrOutputGroup)
        self.qrOutputView.setObjectName(u"qrOutputView")
        self.qrOutputView.setBaseSize(QSize(0, 0))

        self.gridLayout_11.addWidget(self.qrOutputView, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.qrOutputGroup, 0, 9, 12, 1)

        self.qrErrorCorrectLbl = QLabel(self.widget_4)
        self.qrErrorCorrectLbl.setObjectName(u"qrErrorCorrectLbl")

        self.gridLayout_7.addWidget(self.qrErrorCorrectLbl, 12, 0, 1, 1)

        self.qrFormatOptions = QComboBox(self.widget_4)
        self.qrFormatOptions.addItem("")
        self.qrFormatOptions.addItem("")
        self.qrFormatOptions.addItem("")
        self.qrFormatOptions.addItem("")
        self.qrFormatOptions.addItem("")
        self.qrFormatOptions.addItem("")
        self.qrFormatOptions.setObjectName(u"qrFormatOptions")

        self.gridLayout_7.addWidget(self.qrFormatOptions, 14, 2, 1, 1)

        self.qrBorderSizeLbl = QLabel(self.widget_4)
        self.qrBorderSizeLbl.setObjectName(u"qrBorderSizeLbl")

        self.gridLayout_7.addWidget(self.qrBorderSizeLbl, 12, 3, 1, 2)

        self.qrSaveQRBtn = QPushButton(self.widget_4)
        self.qrSaveQRBtn.setObjectName(u"qrSaveQRBtn")

        self.gridLayout_7.addWidget(self.qrSaveQRBtn, 15, 9, 1, 1)

        self.bgColourGroup = QGroupBox(self.widget_4)
        self.bgColourGroup.setObjectName(u"bgColourGroup")
        self.bgColourGroup.setEnabled(True)
        self.gridLayout_8 = QGridLayout(self.bgColourGroup)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.qrBgColourInput = QLineEdit(self.bgColourGroup)
        self.qrBgColourInput.setObjectName(u"qrBgColourInput")

        self.gridLayout_8.addWidget(self.qrBgColourInput, 0, 0, 1, 1)

        self.qrBgColourBtn = QToolButton(self.bgColourGroup)
        self.qrBgColourBtn.setObjectName(u"qrBgColourBtn")

        self.gridLayout_8.addWidget(self.qrBgColourBtn, 0, 1, 1, 1)


        self.gridLayout_7.addWidget(self.bgColourGroup, 11, 0, 1, 3)

        self.qrPlaceholderEditor = QPushButton(self.widget_4)
        self.qrPlaceholderEditor.setObjectName(u"qrPlaceholderEditor")
        sizePolicy2.setHeightForWidth(self.qrPlaceholderEditor.sizePolicy().hasHeightForWidth())
        self.qrPlaceholderEditor.setSizePolicy(sizePolicy2)
        icon3 = QIcon()
        if QIcon.hasThemeIcon(QIcon.ThemeIcon.DocumentProperties):
            icon3 = QIcon.fromTheme(QIcon.ThemeIcon.DocumentProperties)
        else:
            icon3.addFile(u":/images/resources/wrench32px.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.qrPlaceholderEditor.setIcon(icon3)

        self.gridLayout_7.addWidget(self.qrPlaceholderEditor, 0, 8, 1, 1)

        self.qrSizeLabel = QLabel(self.widget_4)
        self.qrSizeLabel.setObjectName(u"qrSizeLabel")

        self.gridLayout_7.addWidget(self.qrSizeLabel, 14, 3, 1, 2)

        self.qrLogoInput = QLineEdit(self.widget_4)
        self.qrLogoInput.setObjectName(u"qrLogoInput")

        self.gridLayout_7.addWidget(self.qrLogoInput, 6, 1, 1, 5)

        self.qrOutputFolder = QLineEdit(self.widget_4)
        self.qrOutputFolder.setObjectName(u"qrOutputFolder")

        self.gridLayout_7.addWidget(self.qrOutputFolder, 15, 2, 1, 1)

        self.qrColorizedCheck = QCheckBox(self.widget_4)
        self.qrColorizedCheck.setObjectName(u"qrColorizedCheck")

        self.gridLayout_7.addWidget(self.qrColorizedCheck, 10, 3, 1, 1)

        self.qrTextInputLabel = QLabel(self.widget_4)
        self.qrTextInputLabel.setObjectName(u"qrTextInputLabel")

        self.gridLayout_7.addWidget(self.qrTextInputLabel, 0, 0, 1, 1)

        self.qrErrorCorrectList = QComboBox(self.widget_4)
        self.qrErrorCorrectList.addItem("")
        self.qrErrorCorrectList.addItem("")
        self.qrErrorCorrectList.addItem("")
        self.qrErrorCorrectList.addItem("")
        self.qrErrorCorrectList.setObjectName(u"qrErrorCorrectList")

        self.gridLayout_7.addWidget(self.qrErrorCorrectList, 12, 2, 1, 1)


        self.gridLayout_10.addWidget(self.widget_4, 0, 0, 1, 1)

        self.tabWidget.addTab(self.qrGenerator, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.qrGenerator), u"QR Generator")
        self.pixelTab = QWidget()
        self.pixelTab.setObjectName(u"pixelTab")
        self.pixelTab.setAcceptDrops(True)
        self.gridLayout_17 = QGridLayout(self.pixelTab)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.pxOptions = QWidget(self.pixelTab)
        self.pxOptions.setObjectName(u"pxOptions")
        self.gridLayout_16 = QGridLayout(self.pxOptions)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_16.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.optionsGroup = QGroupBox(self.pxOptions)
        self.optionsGroup.setObjectName(u"optionsGroup")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.optionsGroup.sizePolicy().hasHeightForWidth())
        self.optionsGroup.setSizePolicy(sizePolicy3)
        self.gridLayout_14 = QGridLayout(self.optionsGroup)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.pxSizeLabel = QLabel(self.optionsGroup)
        self.pxSizeLabel.setObjectName(u"pxSizeLabel")

        self.gridLayout_14.addWidget(self.pxSizeLabel, 0, 0, 1, 1)

        self.pxSizeSlider = QSlider(self.optionsGroup)
        self.pxSizeSlider.setObjectName(u"pxSizeSlider")
        self.pxSizeSlider.setMinimum(2)
        self.pxSizeSlider.setMaximum(128)
        self.pxSizeSlider.setSliderPosition(8)
        self.pxSizeSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_14.addWidget(self.pxSizeSlider, 1, 0, 1, 1)

        self.pxSpinBox = QSpinBox(self.optionsGroup)
        self.pxSpinBox.setObjectName(u"pxSpinBox")
        self.pxSpinBox.setMinimumSize(QSize(75, 0))
        self.pxSpinBox.setMaximumSize(QSize(75, 16777215))
        self.pxSpinBox.setMinimum(2)
        self.pxSpinBox.setMaximum(128)
        self.pxSpinBox.setValue(8)

        self.gridLayout_14.addWidget(self.pxSpinBox, 1, 1, 1, 1)

        self.pxLoadImageBtn = QPushButton(self.optionsGroup)
        self.pxLoadImageBtn.setObjectName(u"pxLoadImageBtn")
        sizePolicy.setHeightForWidth(self.pxLoadImageBtn.sizePolicy().hasHeightForWidth())
        self.pxLoadImageBtn.setSizePolicy(sizePolicy)

        self.gridLayout_14.addWidget(self.pxLoadImageBtn, 2, 0, 1, 1)


        self.gridLayout_16.addWidget(self.optionsGroup, 0, 0, 1, 1)


        self.gridLayout_17.addWidget(self.pxOptions, 0, 0, 1, 1)

        self.pxSepLine1 = QFrame(self.pixelTab)
        self.pxSepLine1.setObjectName(u"pxSepLine1")
        self.pxSepLine1.setFrameShape(QFrame.Shape.VLine)
        self.pxSepLine1.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_17.addWidget(self.pxSepLine1, 0, 1, 1, 1)

        self.pxOutput = QWidget(self.pixelTab)
        self.pxOutput.setObjectName(u"pxOutput")
        self.gridLayout_13 = QGridLayout(self.pxOutput)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.pxGraphicsView = QGraphicsView(self.pxOutput)
        self.pxGraphicsView.setObjectName(u"pxGraphicsView")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pxGraphicsView.sizePolicy().hasHeightForWidth())
        self.pxGraphicsView.setSizePolicy(sizePolicy4)

        self.gridLayout_13.addWidget(self.pxGraphicsView, 0, 0, 1, 1)

        self.pxSepLine2 = QFrame(self.pxOutput)
        self.pxSepLine2.setObjectName(u"pxSepLine2")
        self.pxSepLine2.setFrameShape(QFrame.Shape.HLine)
        self.pxSepLine2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_13.addWidget(self.pxSepLine2, 1, 0, 1, 1)

        self.pxFunctionBox = QGroupBox(self.pxOutput)
        self.pxFunctionBox.setObjectName(u"pxFunctionBox")
        sizePolicy.setHeightForWidth(self.pxFunctionBox.sizePolicy().hasHeightForWidth())
        self.pxFunctionBox.setSizePolicy(sizePolicy)
        self.pxFunctionBox.setMaximumSize(QSize(300, 16777215))
        self.pxFunctionBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pxFunctionBox.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.pxFunctionBox.setFlat(False)
        self.gridLayout_15 = QGridLayout(self.pxFunctionBox)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.pxSaveBtn = QPushButton(self.pxFunctionBox)
        self.pxSaveBtn.setObjectName(u"pxSaveBtn")

        self.gridLayout_15.addWidget(self.pxSaveBtn, 1, 2, 1, 1)

        self.pxFileFormats = QComboBox(self.pxFunctionBox)
        self.pxFileFormats.addItem("")
        self.pxFileFormats.addItem("")
        self.pxFileFormats.addItem("")
        self.pxFileFormats.addItem("")
        self.pxFileFormats.addItem("")
        self.pxFileFormats.setObjectName(u"pxFileFormats")
        sizePolicy.setHeightForWidth(self.pxFileFormats.sizePolicy().hasHeightForWidth())
        self.pxFileFormats.setSizePolicy(sizePolicy)
        self.pxFileFormats.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout_15.addWidget(self.pxFileFormats, 1, 1, 1, 1)

        self.pxPixelateBtn = QPushButton(self.pxFunctionBox)
        self.pxPixelateBtn.setObjectName(u"pxPixelateBtn")
        sizePolicy.setHeightForWidth(self.pxPixelateBtn.sizePolicy().hasHeightForWidth())
        self.pxPixelateBtn.setSizePolicy(sizePolicy)

        self.gridLayout_15.addWidget(self.pxPixelateBtn, 0, 2, 1, 1)

        self.pxFileTypeLbl = QLabel(self.pxFunctionBox)
        self.pxFileTypeLbl.setObjectName(u"pxFileTypeLbl")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pxFileTypeLbl.sizePolicy().hasHeightForWidth())
        self.pxFileTypeLbl.setSizePolicy(sizePolicy5)
        self.pxFileTypeLbl.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_15.addWidget(self.pxFileTypeLbl, 1, 0, 1, 1)


        self.gridLayout_13.addWidget(self.pxFunctionBox, 2, 0, 1, 1)


        self.gridLayout_17.addWidget(self.pxOutput, 0, 2, 1, 1)

        self.tabWidget.addTab(self.pixelTab, "")
        self.ascii = QWidget()
        self.ascii.setObjectName(u"ascii")
        self.gridLayout_19 = QGridLayout(self.ascii)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.toolBox = QToolBox(self.ascii)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"QToolBox {\n"
"    border: none;\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"    background: palette(base);\n"
"    color: palette(text);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    margin: 2px;\n"
"}\n"
"\n"
"QToolBox::tab:selected {\n"
"    background: palette(highlight);\n"
"    color: palette(highlighted-text);\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QToolBox::tab:hover {\n"
"    background: palette(alternate-base);\n"
"}\n"
"\n"
"QToolBox::pane {\n"
"    border: 1px solid palette(mid);\n"
"    background: palette(window);\n"
"    border-radius: 5px;\n"
"}")
        self.toolBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.toolBox.setFrameShadow(QFrame.Shadow.Plain)
        self.img2ascii = QWidget()
        self.img2ascii.setObjectName(u"img2ascii")
        self.img2ascii.setGeometry(QRect(0, 0, 898, 512))
        self.gridLayout_24 = QGridLayout(self.img2ascii)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.i2aInputFrame = QFrame(self.img2ascii)
        self.i2aInputFrame.setObjectName(u"i2aInputFrame")
        self.i2aInputFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.i2aInputFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_23 = QGridLayout(self.i2aInputFrame)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.i2aInputGridLayout = QGridLayout()
        self.i2aInputGridLayout.setObjectName(u"i2aInputGridLayout")
        self.i2aInputGridLayout.setHorizontalSpacing(6)
        self.i2aLoadImageBtn = QPushButton(self.i2aInputFrame)
        self.i2aLoadImageBtn.setObjectName(u"i2aLoadImageBtn")
        sizePolicy.setHeightForWidth(self.i2aLoadImageBtn.sizePolicy().hasHeightForWidth())
        self.i2aLoadImageBtn.setSizePolicy(sizePolicy)

        self.i2aInputGridLayout.addWidget(self.i2aLoadImageBtn, 0, 0, 1, 2)

        self.i2aFontSizeLbl = QLabel(self.i2aInputFrame)
        self.i2aFontSizeLbl.setObjectName(u"i2aFontSizeLbl")

        self.i2aInputGridLayout.addWidget(self.i2aFontSizeLbl, 1, 0, 1, 1)

        self.i2aFontSize = QSpinBox(self.i2aInputFrame)
        self.i2aFontSize.setObjectName(u"i2aFontSize")
        self.i2aFontSize.setMinimumSize(QSize(71, 0))
        self.i2aFontSize.setMaximum(64)
        self.i2aFontSize.setSingleStep(2)
        self.i2aFontSize.setValue(12)

        self.i2aInputGridLayout.addWidget(self.i2aFontSize, 1, 1, 1, 1)

        self.i2aCharSizeLbl = QLabel(self.i2aInputFrame)
        self.i2aCharSizeLbl.setObjectName(u"i2aCharSizeLbl")

        self.i2aInputGridLayout.addWidget(self.i2aCharSizeLbl, 2, 0, 1, 1)

        self.i2aCharSize = QSpinBox(self.i2aInputFrame)
        self.i2aCharSize.setObjectName(u"i2aCharSize")
        self.i2aCharSize.setMinimumSize(QSize(71, 0))
        self.i2aCharSize.setMaximum(64)
        self.i2aCharSize.setSingleStep(2)
        self.i2aCharSize.setValue(12)

        self.i2aInputGridLayout.addWidget(self.i2aCharSize, 2, 1, 1, 1)


        self.gridLayout_23.addLayout(self.i2aInputGridLayout, 2, 0, 1, 1)

        self.i2aInputSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_23.addItem(self.i2aInputSpacer, 5, 0, 1, 1)

        self.i2aConvertBtn = QPushButton(self.i2aInputFrame)
        self.i2aConvertBtn.setObjectName(u"i2aConvertBtn")

        self.gridLayout_23.addWidget(self.i2aConvertBtn, 2, 1, 1, 1)

        self.i2aSaveBtn = QPushButton(self.i2aInputFrame)
        self.i2aSaveBtn.setObjectName(u"i2aSaveBtn")

        self.gridLayout_23.addWidget(self.i2aSaveBtn, 3, 1, 1, 1)

        self.i2aAddBgCheck = QCheckBox(self.i2aInputFrame)
        self.i2aAddBgCheck.setObjectName(u"i2aAddBgCheck")
        self.i2aAddBgCheck.setChecked(False)

        self.gridLayout_23.addWidget(self.i2aAddBgCheck, 3, 0, 1, 1)


        self.gridLayout_24.addWidget(self.i2aInputFrame, 0, 0, 1, 1)

        self.line = QFrame(self.img2ascii)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_24.addWidget(self.line, 0, 1, 1, 1)

        self.i2aOutputFrame = QFrame(self.img2ascii)
        self.i2aOutputFrame.setObjectName(u"i2aOutputFrame")
        sizePolicy4.setHeightForWidth(self.i2aOutputFrame.sizePolicy().hasHeightForWidth())
        self.i2aOutputFrame.setSizePolicy(sizePolicy4)
        self.i2aOutputFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.i2aOutputFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_22 = QGridLayout(self.i2aOutputFrame)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.i2aOutputGroup = QGroupBox(self.i2aOutputFrame)
        self.i2aOutputGroup.setObjectName(u"i2aOutputGroup")
        self.gridLayout_18 = QGridLayout(self.i2aOutputGroup)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.i2aGraphicsView = QGraphicsView(self.i2aOutputGroup)
        self.i2aGraphicsView.setObjectName(u"i2aGraphicsView")

        self.gridLayout_18.addWidget(self.i2aGraphicsView, 0, 0, 1, 1)


        self.gridLayout_22.addWidget(self.i2aOutputGroup, 0, 0, 1, 1)


        self.gridLayout_24.addWidget(self.i2aOutputFrame, 0, 2, 1, 1)

        self.toolBox.addItem(self.img2ascii, u"IMG2ASCII")
        self.txt2ascii = QWidget()
        self.txt2ascii.setObjectName(u"txt2ascii")
        self.txt2ascii.setGeometry(QRect(0, 0, 830, 380))
        self.gridLayout_27 = QGridLayout(self.txt2ascii)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.t2aInputFrame = QFrame(self.txt2ascii)
        self.t2aInputFrame.setObjectName(u"t2aInputFrame")
        sizePolicy.setHeightForWidth(self.t2aInputFrame.sizePolicy().hasHeightForWidth())
        self.t2aInputFrame.setSizePolicy(sizePolicy)
        self.t2aInputFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.t2aInputFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_28 = QGridLayout(self.t2aInputFrame)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.t2aFontGridLayout = QGridLayout()
        self.t2aFontGridLayout.setObjectName(u"t2aFontGridLayout")
        self.t2aFontList = QListWidget(self.t2aInputFrame)
        self.t2aFontList.setObjectName(u"t2aFontList")
        self.t2aFontList.setMinimumSize(QSize(284, 171))
        self.t2aFontList.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.t2aFontGridLayout.addWidget(self.t2aFontList, 2, 0, 1, 1)

        self.t2aFontsLbl = QLabel(self.t2aInputFrame)
        self.t2aFontsLbl.setObjectName(u"t2aFontsLbl")

        self.t2aFontGridLayout.addWidget(self.t2aFontsLbl, 1, 0, 1, 1)

        self.t2aFontSearch = QLineEdit(self.t2aInputFrame)
        self.t2aFontSearch.setObjectName(u"t2aFontSearch")

        self.t2aFontGridLayout.addWidget(self.t2aFontSearch, 0, 0, 1, 1)


        self.gridLayout_28.addLayout(self.t2aFontGridLayout, 0, 0, 1, 1)

        self.t2aInputGridLayout = QGridLayout()
        self.t2aInputGridLayout.setObjectName(u"t2aInputGridLayout")
        self.t2aInputGridLayout.setVerticalSpacing(31)
        self.t2aInputGridLayout.setContentsMargins(5, 10, 8, 30)
        self.t2aDiscordCheck = QCheckBox(self.t2aInputFrame)
        self.t2aDiscordCheck.setObjectName(u"t2aDiscordCheck")

        self.t2aInputGridLayout.addWidget(self.t2aDiscordCheck, 0, 1, 1, 1)

        self.t2aTextInput = QLineEdit(self.t2aInputFrame)
        self.t2aTextInput.setObjectName(u"t2aTextInput")
        self.t2aTextInput.setMinimumSize(QSize(401, 41))

        self.t2aInputGridLayout.addWidget(self.t2aTextInput, 0, 0, 1, 1)

        self.t2aFontSize = QComboBox(self.t2aInputFrame)
        self.t2aFontSize.setObjectName(u"t2aFontSize")
        self.t2aFontSize.setEnabled(False)
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.t2aFontSize.sizePolicy().hasHeightForWidth())
        self.t2aFontSize.setSizePolicy(sizePolicy6)
        self.t2aFontSize.setToolTipDuration(-4)
        self.t2aFontSize.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.t2aInputGridLayout.addWidget(self.t2aFontSize, 1, 0, 1, 1)

        self.t2aConvertBtn = QPushButton(self.t2aInputFrame)
        self.t2aConvertBtn.setObjectName(u"t2aConvertBtn")
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSend))
        self.t2aConvertBtn.setIcon(icon4)

        self.t2aInputGridLayout.addWidget(self.t2aConvertBtn, 1, 1, 1, 1)

        self.t2aCopyBtn = QPushButton(self.t2aInputFrame)
        self.t2aCopyBtn.setObjectName(u"t2aCopyBtn")
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditCopy))
        self.t2aCopyBtn.setIcon(icon5)

        self.t2aInputGridLayout.addWidget(self.t2aCopyBtn, 2, 1, 1, 1)


        self.gridLayout_28.addLayout(self.t2aInputGridLayout, 0, 1, 1, 1)


        self.gridLayout_27.addWidget(self.t2aInputFrame, 0, 0, 1, 1)

        self.t2aOutputFrame = QFrame(self.txt2ascii)
        self.t2aOutputFrame.setObjectName(u"t2aOutputFrame")
        self.t2aOutputFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.t2aOutputFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_29 = QGridLayout(self.t2aOutputFrame)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.t2aTextOutput = QPlainTextEdit(self.t2aOutputFrame)
        self.t2aTextOutput.setObjectName(u"t2aTextOutput")
        font = QFont()
        font.setPointSize(12)
        self.t2aTextOutput.setFont(font)
        self.t2aTextOutput.setReadOnly(True)
        self.t2aTextOutput.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)

        self.gridLayout_29.addWidget(self.t2aTextOutput, 0, 0, 1, 1)


        self.gridLayout_27.addWidget(self.t2aOutputFrame, 1, 0, 1, 1)

        self.toolBox.addItem(self.txt2ascii, u"TXT2ASCII")

        self.gridLayout_19.addWidget(self.toolBox, 1, 0, 1, 1)

        self.tabWidget.addTab(self.ascii, "")

        self.gridLayout_12.addWidget(self.tabWidget, 0, 0, 1, 1)

        ImageNexus.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ImageNexus)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 938, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuTools = QMenu(self.menuFile)
        self.menuTools.setObjectName(u"menuTools")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        ImageNexus.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ImageNexus)
        self.statusbar.setObjectName(u"statusbar")
        ImageNexus.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.menuTools.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuTools.addAction(self.actionQRTemplateEditor)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionReloadTemplates)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(ImageNexus)
        self.actionExit.triggered.connect(ImageNexus.close)
        self.pxSizeSlider.sliderMoved.connect(self.pxSpinBox.setValue)
        self.pxSpinBox.valueChanged.connect(self.pxSizeSlider.setValue)

        self.tabWidget.setCurrentIndex(0)
        self.qrGenButton.setDefault(False)
        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ImageNexus)
    # setupUi

    def retranslateUi(self, ImageNexus):
        ImageNexus.setWindowTitle(QCoreApplication.translate("ImageNexus", u"ImageNexus {version}", None))
        self.actionHelp.setText(QCoreApplication.translate("ImageNexus", u"Help...", None))
        self.actionAbout.setText(QCoreApplication.translate("ImageNexus", u"About", None))
        self.actionExit.setText(QCoreApplication.translate("ImageNexus", u"Exit", None))
        self.actionReloadTemplates.setText(QCoreApplication.translate("ImageNexus", u"Reload Templates", None))
        self.actionQRTemplateEditor.setText(QCoreApplication.translate("ImageNexus", u"QR Template Editor", None))
        self.feBrowseInput.setText(QCoreApplication.translate("ImageNexus", u"Browse", None))
        self.feFormatOptions.setItemText(0, QCoreApplication.translate("ImageNexus", u"PNG", None))
        self.feFormatOptions.setItemText(1, QCoreApplication.translate("ImageNexus", u"GIF", None))

        self.feSelectGifLbl.setText(QCoreApplication.translate("ImageNexus", u"Select GIF:", None))
        self.feOutputFolder.setPlaceholderText(QCoreApplication.translate("ImageNexus", u"Select an output folder...", None))
        self.feBrowseOutput.setText(QCoreApplication.translate("ImageNexus", u"Browse", None))
        self.feFormatOptionsLbl.setText(QCoreApplication.translate("ImageNexus", u"Save as:", None))
        self.feFileInput.setPlaceholderText(QCoreApplication.translate("ImageNexus", u"Select a GIF...", None))
        self.feOutputFolderLbl.setText(QCoreApplication.translate("ImageNexus", u"Output Folder:", None))
        self.feInfoCheckbox.setText(QCoreApplication.translate("ImageNexus", u"Generate frame info file", None))
        self.feExtractBtn.setText(QCoreApplication.translate("ImageNexus", u"Extract Frames", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.frameExtractor), QCoreApplication.translate("ImageNexus", u"Frame Extractor", None))
        self.icBrowseInput.setText(QCoreApplication.translate("ImageNexus", u"Browse", None))
        self.icInputFileLbl.setText(QCoreApplication.translate("ImageNexus", u"Select Input File:", None))
        self.icBrowseOutput.setText(QCoreApplication.translate("ImageNexus", u"Browse", None))
        self.icFormatOptionsLbl.setText(QCoreApplication.translate("ImageNexus", u"Output Format:", None))
        self.icFileInput.setPlaceholderText(QCoreApplication.translate("ImageNexus", u"Select an image...", None))
        self.icOutputFolderLbl.setText(QCoreApplication.translate("ImageNexus", u"Output Folder:", None))
        self.icOutputFolder.setPlaceholderText(QCoreApplication.translate("ImageNexus", u"Select an output folder...", None))
        self.icFormatOptions.setItemText(0, QCoreApplication.translate("ImageNexus", u"GIF", None))
        self.icFormatOptions.setItemText(1, QCoreApplication.translate("ImageNexus", u"PNG", None))
        self.icFormatOptions.setItemText(2, QCoreApplication.translate("ImageNexus", u"JPEG", None))
        self.icFormatOptions.setItemText(3, QCoreApplication.translate("ImageNexus", u"BMP", None))
        self.icFormatOptions.setItemText(4, QCoreApplication.translate("ImageNexus", u"TIFF", None))

        self.icConvertBtn.setText(QCoreApplication.translate("ImageNexus", u"Convert", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.imageConverter), QCoreApplication.translate("ImageNexus", u"Image Converter", None))
        self.bcInputBrowse.setText(QCoreApplication.translate("ImageNexus", u"Browse", None))
        self.formatOptions.setItemText(0, QCoreApplication.translate("ImageNexus", u"GIF", None))
        self.formatOptions.setItemText(1, QCoreApplication.translate("ImageNexus", u"PNG", None))
        self.formatOptions.setItemText(2, QCoreApplication.translate("ImageNexus", u"JPEG", None))
        self.formatOptions.setItemText(3, QCoreApplication.translate("ImageNexus", u"BMP", None))
        self.formatOptions.setItemText(4, QCoreApplication.translate("ImageNexus", u"TIFF", None))

        self.conversionType.setItemText(0, QCoreApplication.translate("ImageNexus", u"Files", None))
        self.conversionType.setItemText(1, QCoreApplication.translate("ImageNexus", u"Folder", None))

        self.bcOutputFolderLbl.setText(QCoreApplication.translate("ImageNexus", u"Output Folder:", None))
        self.bcOutputFormatLbl.setText(QCoreApplication.translate("ImageNexus", u"Output Format:", None))
        self.bcConvertBtn.setText(QCoreApplication.translate("ImageNexus", u"Convert Files", None))
        self.bcOutputFolder.setPlaceholderText(QCoreApplication.translate("ImageNexus", u"Select an output folder...", None))
        self.bcConversionTypeLbl.setText(QCoreApplication.translate("ImageNexus", u"Conversion Type:", None))
        self.bcInputFileLbl.setText(QCoreApplication.translate("ImageNexus", u"Select Input File:", None))
        self.bcFileInput.setPlaceholderText(QCoreApplication.translate("ImageNexus", u"Select an image or folder...", None))
        self.bcOutputBrowse.setText(QCoreApplication.translate("ImageNexus", u"Browse", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.batchConverter), QCoreApplication.translate("ImageNexus", u"Batch Converter", None))
        self.qrGenButton.setText(QCoreApplication.translate("ImageNexus", u"Generate QR", None))
#if QT_CONFIG(shortcut)
        self.qrGenButton.setShortcut(QCoreApplication.translate("ImageNexus", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(statustip)
        self.qrCodeSize.setStatusTip(QCoreApplication.translate("ImageNexus", u"Value between 1-40", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.qrAddBGCheck.setStatusTip(QCoreApplication.translate("ImageNexus", u"Add a background to a transparent logo", None))
#endif // QT_CONFIG(statustip)
        self.qrAddBGCheck.setText(QCoreApplication.translate("ImageNexus", u"Add background?", None))
#if QT_CONFIG(statustip)
        self.qrBorderSize.setStatusTip(QCoreApplication.translate("ImageNexus", u"Value between 0-10", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.qrAspectRatioCheck.setStatusTip(QCoreApplication.translate("ImageNexus", u"Keeps the aspect ratio of the embeded image", None))
#endif // QT_CONFIG(statustip)
        self.qrAspectRatioCheck.setText(QCoreApplication.translate("ImageNexus", u"Keep Aspect Ratio?", None))
        self.qrTemplates.setItemText(0, QCoreApplication.translate("ImageNexus", u"Select a template", None))

        self.codeColourGroup.setTitle(QCoreApplication.translate("ImageNexus", u"QR Code Colour", None))
        self.qrCodeColourInput.setText("")
        self.qrCodeColourInput.setPlaceholderText(QCoreApplication.translate("ImageNexus", u"0, 0, 0", None))
        self.qrCodeColourBtn.setText(QCoreApplication.translate("ImageNexus", u"...", None))
        self.qrTextInput.setPlaceholderText(QCoreApplication.translate("ImageNexus", u"Please enter some text to generate a QR code... See the QR Guidelines in the resources folder on QR Formats.", None))
        self.qrBrowseLogo.setText(QCoreApplication.translate("ImageNexus", u"Browse", None))
        self.qrLogoInputLbl.setText(QCoreApplication.translate("ImageNexus", u"Logo Image:", None))
        self.qrBrowseOutput.setText(QCoreApplication.translate("ImageNexus", u"Browse", None))
        self.qrFormatOptionsLbl.setText(QCoreApplication.translate("ImageNexus", u"Save As:", None))
        self.qrOutputFolderLbl.setText(QCoreApplication.translate("ImageNexus", u"Output Folder:", None))
        self.qrUseArtisticCheck.setText(QCoreApplication.translate("ImageNexus", u"Artistic QR", None))
        self.qrOutputGroup.setTitle(QCoreApplication.translate("ImageNexus", u"Generated QR", None))
        self.qrErrorCorrectLbl.setText(QCoreApplication.translate("ImageNexus", u"Error Correction:", None))
        self.qrFormatOptions.setItemText(0, QCoreApplication.translate("ImageNexus", u"BMP", None))
        self.qrFormatOptions.setItemText(1, QCoreApplication.translate("ImageNexus", u"JPG", None))
        self.qrFormatOptions.setItemText(2, QCoreApplication.translate("ImageNexus", u"GIF", None))
        self.qrFormatOptions.setItemText(3, QCoreApplication.translate("ImageNexus", u"PNG", None))
        self.qrFormatOptions.setItemText(4, QCoreApplication.translate("ImageNexus", u"TIFF", None))
        self.qrFormatOptions.setItemText(5, QCoreApplication.translate("ImageNexus", u"WEBP", None))

        self.qrBorderSizeLbl.setText(QCoreApplication.translate("ImageNexus", u"Border Size:", None))
        self.qrSaveQRBtn.setText(QCoreApplication.translate("ImageNexus", u"Save QR Code", None))
        self.bgColourGroup.setTitle(QCoreApplication.translate("ImageNexus", u"Background Colour", None))
        self.qrBgColourInput.setText("")
        self.qrBgColourInput.setPlaceholderText(QCoreApplication.translate("ImageNexus", u"255, 255, 255", None))
        self.qrBgColourBtn.setText(QCoreApplication.translate("ImageNexus", u"...", None))
#if QT_CONFIG(statustip)
        self.qrPlaceholderEditor.setStatusTip(QCoreApplication.translate("ImageNexus", u"Placeholder Editor", None))
#endif // QT_CONFIG(statustip)
        self.qrPlaceholderEditor.setText("")
        self.qrSizeLabel.setText(QCoreApplication.translate("ImageNexus", u"QR Size:", None))
        self.qrLogoInput.setText("")
        self.qrLogoInput.setPlaceholderText(QCoreApplication.translate("ImageNexus", u"Insert a logo... (Optional)", None))
        self.qrColorizedCheck.setText(QCoreApplication.translate("ImageNexus", u"Colourised?", None))
        self.qrTextInputLabel.setText(QCoreApplication.translate("ImageNexus", u"QR Data:", None))
        self.qrErrorCorrectList.setItemText(0, QCoreApplication.translate("ImageNexus", u"Low", None))
        self.qrErrorCorrectList.setItemText(1, QCoreApplication.translate("ImageNexus", u"Medium", None))
        self.qrErrorCorrectList.setItemText(2, QCoreApplication.translate("ImageNexus", u"Quartile", None))
        self.qrErrorCorrectList.setItemText(3, QCoreApplication.translate("ImageNexus", u"High", None))

        self.optionsGroup.setTitle(QCoreApplication.translate("ImageNexus", u"Options", None))
        self.pxSizeLabel.setText(QCoreApplication.translate("ImageNexus", u"Pixel Size", None))
        self.pxLoadImageBtn.setText(QCoreApplication.translate("ImageNexus", u"Load Image", None))
        self.pxFunctionBox.setTitle("")
        self.pxSaveBtn.setText(QCoreApplication.translate("ImageNexus", u"Save", None))
        self.pxFileFormats.setItemText(0, QCoreApplication.translate("ImageNexus", u"BMP", None))
        self.pxFileFormats.setItemText(1, QCoreApplication.translate("ImageNexus", u"JPG", None))
        self.pxFileFormats.setItemText(2, QCoreApplication.translate("ImageNexus", u"PNG", None))
        self.pxFileFormats.setItemText(3, QCoreApplication.translate("ImageNexus", u"TIFF", None))
        self.pxFileFormats.setItemText(4, QCoreApplication.translate("ImageNexus", u"WEBP", None))

        self.pxPixelateBtn.setText(QCoreApplication.translate("ImageNexus", u"Pixelate", None))
        self.pxFileTypeLbl.setText(QCoreApplication.translate("ImageNexus", u"FIle Type", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pixelTab), QCoreApplication.translate("ImageNexus", u"Quick Pixelator", None))
        self.i2aLoadImageBtn.setText(QCoreApplication.translate("ImageNexus", u"Load Image", None))
        self.i2aFontSizeLbl.setText(QCoreApplication.translate("ImageNexus", u"Font Size", None))
        self.i2aCharSizeLbl.setText(QCoreApplication.translate("ImageNexus", u"Char Size", None))
        self.i2aConvertBtn.setText(QCoreApplication.translate("ImageNexus", u"Convert", None))
        self.i2aSaveBtn.setText(QCoreApplication.translate("ImageNexus", u"Save Image", None))
        self.i2aAddBgCheck.setText(QCoreApplication.translate("ImageNexus", u"Add Background", None))
        self.i2aOutputGroup.setTitle(QCoreApplication.translate("ImageNexus", u"Output", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.img2ascii), QCoreApplication.translate("ImageNexus", u"IMG2ASCII", None))
        self.t2aFontsLbl.setText(QCoreApplication.translate("ImageNexus", u"Fonts:", None))
        self.t2aFontSearch.setPlaceholderText(QCoreApplication.translate("ImageNexus", u"Search...", None))
#if QT_CONFIG(statustip)
        self.t2aDiscordCheck.setStatusTip(QCoreApplication.translate("ImageNexus", u"Format for Discord", None))
#endif // QT_CONFIG(statustip)
        self.t2aDiscordCheck.setText(QCoreApplication.translate("ImageNexus", u"Discord?", None))
        self.t2aTextInput.setPlaceholderText(QCoreApplication.translate("ImageNexus", u"Enter some text...", None))
        self.t2aFontSize.setPlaceholderText(QCoreApplication.translate("ImageNexus", u"Choose Size", None))
        self.t2aConvertBtn.setText(QCoreApplication.translate("ImageNexus", u"Convert", None))
#if QT_CONFIG(shortcut)
        self.t2aConvertBtn.setShortcut(QCoreApplication.translate("ImageNexus", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.t2aCopyBtn.setText(QCoreApplication.translate("ImageNexus", u"Copy", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.txt2ascii), QCoreApplication.translate("ImageNexus", u"TXT2ASCII", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ascii), QCoreApplication.translate("ImageNexus", u"ASCII", None))
        self.menuFile.setTitle(QCoreApplication.translate("ImageNexus", u"File", None))
        self.menuTools.setTitle(QCoreApplication.translate("ImageNexus", u"Tools", None))
        self.menuHelp.setTitle(QCoreApplication.translate("ImageNexus", u"Help", None))
    # retranslateUi

