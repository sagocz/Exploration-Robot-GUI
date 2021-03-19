#!/usr/bin/env python

from containers_publisher import containersSending
from containers_subscriber import containersReceiver
from containers_ui import Ui_containersUi

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QRect
import rospy

greenControl = "../src/containers_gui/src/resources/images/circle_green.svg"
redControl = "../src/containers_gui/src/resources/images/circle_red.svg"

class labProbeController(Ui_containersUi, QObject):

    #setup elements on gui
    def setupUi(self, Form):
        Ui_containersUi.setupUi(self, Form)       
        self.textToSend = ""
        #initializating Sending
        self.containersPublisher = containersSending()
        self.containersSubscriber = containersReceiver()

        # connecting elements
        self.firstContainerOpen.clicked.connect(self.firstContainerOpenClicked)
        self.firstContainerClose.clicked.connect(self.firstContainerCloseClicked)
        self.secondContainerOpen.clicked.connect(self.secondContainerOpenClicked)
        self.secondContainerClose.clicked.connect(self.secondContainerCloseClicked)
        self.thirdContainerOpen.clicked.connect(self.thirdContainerOpenClicked)
        self.thirdContainerClose.clicked.connect(self.thirdContainerCloseClicked)

        self.containersSubscriber.containersSignal.connect(self.updateOne)
        self.containersSubscriber.containersSignal.connect(self.updateTwo)
        self.containersSubscriber.containersSignal.connect(self.updateThree)

        self.containersSubscriber.containersSignal.connect(self.updateState)
        
        self.firstCalibrationSend.clicked.connect(self.firstCalibrationSendClicked)
        self.secondCalibrationSend.clicked.connect(self.secondCalibrationSendClicked)
        self.thirdCalibrationSend.clicked.connect(self.thirdCalibrationSendClicked)

    ### CHANGE OF INDICATORS COLOR
    @QtCore.pyqtSlot()
    def updateState(self):

        first = self.containersSubscriber.firstServoActual
        second = self.containersSubscriber.secondServoActual
        third = self.containersSubscriber.thirdServoActual

        if first == True:
            self.indicatorOne.setPixmap(QtGui.QPixmap(redControl))
        elif first == False:
            self.indicatorOne.setPixmap(QtGui.QPixmap(greenControl))
        
        if second == True:
            self.indicatorTwo.setPixmap(QtGui.QPixmap(redControl))
        elif second == False:
            self.indicatorTwo.setPixmap(QtGui.QPixmap(greenControl))
        
        if third == True:
            self.indicatorThree.setPixmap(QtGui.QPixmap(redControl))
        elif third == False:
            self.indicatorThree.setPixmap(QtGui.QPixmap(greenControl))

    ### CONTAINERS OPEN / CLOSE CONTROL ###
    @QtCore.pyqtSlot()
    def firstContainerOpenClicked(self):
       
        self.containersPublisher.containerOne(True)

    @QtCore.pyqtSlot()
    def firstContainerCloseClicked(self):
       
        self.containersPublisher.containerOne(False)

    @QtCore.pyqtSlot()
    def secondContainerOpenClicked(self):
       
        self.containersPublisher.containerTwo(True)

    @QtCore.pyqtSlot()
    def secondContainerCloseClicked(self):
       
        self.containersPublisher.containerTwo(False)

    @QtCore.pyqtSlot()
    def thirdContainerOpenClicked(self):
       
        self.containersPublisher.containerThree(True)

    @QtCore.pyqtSlot()
    def thirdContainerCloseClicked(self):
       
        self.containersPublisher.containerThree(False)

    ### UPDATE OF TENSOMETRIC BEAM MEASUREMENT ###
    @QtCore.pyqtSlot()
    def updateOne(self):
        self.firstContainerMeasurement.display(self.containersSubscriber.containersMeasurementOne)

    @QtCore.pyqtSlot()
    def updateTwo(self):
        self.secondContainerMeasurement.display(self.containersSubscriber.containersMeasurementTwo)

    @QtCore.pyqtSlot()
    def updateThree(self):
        self.thirdContainerMeasurement.display(self.containersSubscriber.containersMeasurementThree)

    ### SENDING CALIBRATION PARAMETER ###
    @QtCore.pyqtSlot()
    def firstCalibrationSendClicked(self):

        textToSend = self.firstCalibrationValue.text()
        if textToSend == "":
            pass
        elif textToSend != "":
            self.containersPublisher.calibrationOne(int(textToSend))
    
    @QtCore.pyqtSlot()
    def secondCalibrationSendClicked(self):

        textToSend = self.secondCalibrationValue.text()
        if textToSend == "":
            pass
        elif textToSend != "":
            self.containersPublisher.calibrationTwo(int(textToSend))

    @QtCore.pyqtSlot()
    def thirdCalibrationSendClicked(self):

        textToSend = self.thirdCalibrationValue.text()
        if textToSend == "":
            pass
        elif textToSend != "":
            self.containersPublisher.calibrationThree(int(textToSend))
    
