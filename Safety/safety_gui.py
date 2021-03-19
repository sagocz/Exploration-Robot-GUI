# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'safety_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_safetyUi(object):
    def setupUi(self, safetyUi):
        safetyUi.setObjectName("safetyUi")
        safetyUi.resize(510, 249)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("safety_resources/images/SPlogo_130x90(1naklejka).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        safetyUi.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(safetyUi)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(200, 0, 181, 161))
        self.frame.setStyleSheet("background-color: rgb(252, 175, 62);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.softStopButton = QtWidgets.QPushButton(self.frame)
        self.softStopButton.setGeometry(QtCore.QRect(40, 10, 111, 51))
        self.softStopButton.setObjectName("softStopButton")
        self.softStopLabel = QtWidgets.QLabel(self.frame)
        self.softStopLabel.setGeometry(QtCore.QRect(40, 80, 111, 71))
        self.softStopLabel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(239, 41, 41);")
        self.softStopLabel.setText("")
        self.softStopLabel.setPixmap(QtGui.QPixmap("safety_resources/images/circle_green.svg"))
        self.softStopLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.softStopLabel.setObjectName("softStopLabel")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 201, 161))
        self.frame_2.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.hardStopLabel = QtWidgets.QLabel(self.frame_2)
        self.hardStopLabel.setGeometry(QtCore.QRect(40, 80, 111, 71))
        self.hardStopLabel.setStyleSheet("background-color: rgb(239, 41, 41);\n"
"color: rgb(255, 255, 255);")
        self.hardStopLabel.setText("")
        self.hardStopLabel.setPixmap(QtGui.QPixmap("safety_resources/images/circle_green.svg"))
        self.hardStopLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.hardStopLabel.setObjectName("hardStopLabel")
        self.hardStopButton = QtWidgets.QPushButton(self.frame_2)
        self.hardStopButton.setGeometry(QtCore.QRect(30, 10, 131, 61))
        self.hardStopButton.setObjectName("hardStopButton")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(380, 0, 121, 161))
        self.frame_3.setStyleSheet("background-color: rgb(252, 175, 62);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.rpiTemperatureDisplay = QtWidgets.QLCDNumber(self.frame_3)
        self.rpiTemperatureDisplay.setGeometry(QtCore.QRect(10, 40, 61, 23))
        self.rpiTemperatureDisplay.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(52, 101, 164);")
        self.rpiTemperatureDisplay.setObjectName("rpiTemperatureDisplay")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(80, 40, 31, 21))
        self.label.setObjectName("label")
        self.rpiTemperature = QtWidgets.QLabel(self.frame_3)
        self.rpiTemperature.setGeometry(QtCore.QRect(30, 80, 61, 61))
        self.rpiTemperature.setStyleSheet("")
        self.rpiTemperature.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.rpiTemperature.setText("")
        self.rpiTemperature.setPixmap(QtGui.QPixmap("safety_resources/images/circle_green.svg"))
        self.rpiTemperature.setScaledContents(True)
        self.rpiTemperature.setAlignment(QtCore.Qt.AlignCenter)
        self.rpiTemperature.setObjectName("rpiTemperature")
        self.motorsLockCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.motorsLockCheck.setGeometry(QtCore.QRect(0, 170, 501, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.motorsLockCheck.setFont(font)
        self.motorsLockCheck.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.motorsLockCheck.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(239, 41, 41);")
        self.motorsLockCheck.setIconSize(QtCore.QSize(20, 20))
        self.motorsLockCheck.setObjectName("motorsLockCheck")
        safetyUi.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(safetyUi)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 510, 22))
        self.menubar.setObjectName("menubar")
        safetyUi.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(safetyUi)
        self.statusbar.setObjectName("statusbar")
        safetyUi.setStatusBar(self.statusbar)

        self.retranslateUi(safetyUi)
        QtCore.QMetaObject.connectSlotsByName(safetyUi)

    def retranslateUi(self, safetyUi):
        _translate = QtCore.QCoreApplication.translate
        safetyUi.setWindowTitle(_translate("safetyUi", "Safety"))
        self.softStopButton.setText(_translate("safetyUi", "SOFT STOP"))
        self.hardStopButton.setText(_translate("safetyUi", "HARD STOP"))
        self.label_2.setText(_translate("safetyUi", "RPi Temp"))
        self.label.setText(_translate("safetyUi", "[°C]"))
        self.motorsLockCheck.setWhatsThis(_translate("safetyUi", "<html><head/><body><p>XD </p></body></html>"))
        self.motorsLockCheck.setText(_translate("safetyUi", "MOTORS LOCK"))
        self.motorsLockCheck.setShortcut(_translate("safetyUi", "Return"))
