#!/usr/bin/env python

from safety_publisher import safetySending
from safety_subscriber import safetyReceiver
from safety_gui import Ui_safetyUi

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QObject, QRect
from PyQt5.QtWidgets import QApplication, QMessageBox
import rospy

### Path of graphics resources ###
greenControl = "../src/safety_gui/src/safety_resources/images/circle_green.svg"
yellowControl = "../src/safety_gui/src/safety_resources/images/circle_yellow.svg"
orangeControl = "../src/safety_gui/src/safety_resources/images/circle_orange.svg"
redControl = "../src/safety_gui/src/safety_resources/images/circle_red.svg"

### Style Sheet colors templates ###
green = "background-color: rgb(50, 205, 50);"
red = "background-color: rgb(255, 51, 51);"
grey = "background-color: rgb(77, 77, 77);"
yellow = "background-color: rgb(255, 255, 51);"
orange = "background-color: rgb(255, 165, 0);"

greenFont = "color: rgb(50, 205, 50);"
redFont = "color: rgb(255, 51, 51);"
greyFont = "color: rgb(77, 77, 77);"
yellowFont = "color: rgb(255, 255, 51);"
orangeFont = "color: rgb(255, 165, 0);"

class safetyController(Ui_safetyUi, QObject):
    #setup elements on gui 
    def setupUi(self, safetyUi):
        Ui_safetyUi.setupUi(self, safetyUi)

        #initializating Sending 
        self.safetyPublisher = safetySending()
        self.safetySubscriber = safetyReceiver()

        # connecting elements
        self.softStopButton.clicked.connect(self.softStopButtonClicked)
        self.hardStopButton.clicked.connect(self.hardStopButtonClicked)
        self.safetySubscriber.safetySignal.connect(self.updateButtonInfo)
        self.safetySubscriber.safetySignal.connect(self.updateRpiTemperature)
        
        self.motorsOffBox = QMessageBox()
        self.hardStopBox = QMessageBox()
        self.softStopBox = QMessageBox()
        self.redButtonBox = QMessageBox()

        self.rpiTemperature.setPixmap(QtGui.QPixmap(greenControl))
        self.softStopLabel.setPixmap(QtGui.QPixmap(greenControl))
        self.hardStopLabel.setPixmap(QtGui.QPixmap(greenControl))
        self.motorsLockCheck.clicked.connect(self.checkBoxChecked)
        self.safetySubscriber.safetySignal.connect(self.updateState)

    ### Rpi temperature display and label color change
    @QtCore.pyqtSlot()
    def updateRpiTemperature(self):
        self.rpiTemperatureDisplay.display(self.safetySubscriber.temperatureActual)
        self.rpiTemp = self.safetySubscriber.temperatureActual

        if self.rpiTemp < 60:
            self.rpiTemperature.setPixmap(QtGui.QPixmap(greenControl))
            self.rpiTemperatureDisplay.setStyleSheet(green)

        elif self.rpiTemp >= 60 and self.rpiTemp < 70:
            self.rpiTemperature.setPixmap(QtGui.QPixmap(yellowControl))
            self.rpiTemperatureDisplay.setStyleSheet(yellow)

        elif self.rpiTemp >= 70 and self.rpiTemp < 80:
            self.rpiTemperature.setPixmap(QtGui.QPixmap(orangeControl))
            self.rpiTemperatureDisplay.setStyleSheet(orange)

        elif self.rpiTemp >=80:
            self.rpiTemperature.setPixmap(QtGui.QPixmap(redControl))
            self.rpiTemperatureDisplay.setStyleSheet(red)

    ### message box updates ###
    @QtCore.pyqtSlot()
    def updateState(self):
        if self.safetySubscriber.motorsOffActual == True:
            self.motorsOffBoxMsg()

        if self.safetySubscriber.redButtonActual == True:
            self.redButtonBoxMsg()
            
    ### Message BOX CONFIG ###
    @QtCore.pyqtSlot()
    def motorsOffBoxMsg(self):
        self.motorsOffBox.setWindowTitle("WARNING!!!!")
        self.motorsOffBox.setText("MOTORS ARE DISABLED!!!!!")
        self.motorsOffBox.exec_()
    
    @QtCore.pyqtSlot()
    def redButtonBoxMsg(self):
        self.redButtonBox.setWindowTitle("WARNING!!!!")
        self.redButtonBox.setText("RED BUTTON WAS\nPRESSED!!!!!")
        self.redButtonBox.exec_()

    ### Config of soft stop dialog box
    @QtCore.pyqtSlot()
    def softStopBoxMsg(self):
        self.softStopBox.setWindowTitle("WARNING!!!!")
        self.softStopBox.setText("SOFT STOP WAS\nPRESSED!!!!!")
        self.softStopBox.exec_()

    ### Config of hard stop dialog box ###
    @QtCore.pyqtSlot()
    def hardStopBoxMsg(self):
        self.hardStopBox.setWindowTitle("WARNING!!!!")
        self.hardStopBox.setText("HARD STOP WAS\nPRESSED!!!!!")
        self.hardStopBox.exec_()

    
    ### Update Button Info Callback
    @QtCore.pyqtSlot()
    def updateButtonInfo(self):
        if self.safetySubscriber.softStopActual == True:

            self.softStopLabel.setPixmap(QtGui.QPixmap(redControl))
            self.softStopBoxMsg()

        elif self.safetySubscriber.hardStopActual == True:

            self.hardStopLabel.setPixmap(QtGui.QPixmap(redControl))
            self.hardStopBoxMsg()

        elif self.safetySubscriber.softStopActual == False:
            self.softStopLabel.setPixmap(QtGui.QPixmap(greenControl))

        elif self.safetySubscriber.hardStopActual == False:    
            self.hardStopLabel.setPixmap(QtGui.QPixmap(greenControl))

        else:
            pass

    ### BUTTON EVENTS ###
    @QtCore.pyqtSlot()
    def hardStopButtonClicked(self):
        self.safetyPublisher.hardStopPublisher(True)

    @QtCore.pyqtSlot()
    def softStopButtonClicked(self):
        self.safetyPublisher.softStopPublisher(True)
        
    ### CHECK BOX EVENT ###

    @QtCore.pyqtSlot()
    def checkBoxChecked(self):
        if self.motorsLockCheck.isChecked():
            self.safetyPublisher.motorsLockPublisher(True)
        else:
            self.safetyPublisher.motorsLockPublisher(False)