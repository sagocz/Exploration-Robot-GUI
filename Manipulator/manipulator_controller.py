#!/usr/bin/env python


from manipulator_publisher import manipulatorSending
from manipulator_subscriber import manipulatorReceiver
from manipulator_gui import Ui_manipulatorGui

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QRect

manipulatorPicture = "../src/manipulator_gui/src/resources/images/Manipulator.png"
class manipulatorController(Ui_manipulatorGui, QObject):

    #setup elements on gui
    def setupUi(self, Form):
        Ui_manipulatorGui.setupUi(self, Form)       
        
        self.label_9.setPixmap(QtGui.QPixmap(manipulatorPicture))
        #initializating Sending
        self.manipPublisher = manipulatorSending()
        self.manipSubscriber = manipulatorReceiver()
        self.positionFrame.setDisabled(True)

        # connecting elements
        self.openGripperButton.clicked.connect(self.gripperCloseJawsClicked)
        self.closeGripperButton.clicked.connect(self.gripperOpenJawsClicked)
        self.commandSendButton.clicked.connect(self.gripperCommandSendClicked)
        self.positionSendingRadio.clicked.connect(self.positionSendingRadioClicked)
        self.mouseControlRadio.clicked.connect(self.mouseControlRadioClicked)
        self.firstAxisManipButton.clicked.connect(self.firstAxisManipButtonClicked)
        self.secondAxisManipButton.clicked.connect(self.secondAxisManipButtonClicked)
        self.thirdAxisManipButton.clicked.connect(self.thirdAxisManipButtonClicked)
        self.fourthAxisManipButton.clicked.connect(self.fourthAxisManipButtonClicked)
        self.fifthAxisManipButton.clicked.connect(self.fifthAxisManipButtonClicked)

        self.manipSubscriber.manipulatorSignal.connect(self.updateOne)        
        self.manipSubscriber.manipulatorSignal.connect(self.updateTwo)  
        self.manipSubscriber.manipulatorSignal.connect(self.updateThree)  
        self.manipSubscriber.manipulatorSignal.connect(self.updateFour)  
        self.manipSubscriber.manipulatorSignal.connect(self.updateFive)
        self.manipSubscriber.manipulatorSignal.connect(self.updateDistanceInformation)
        self.manipSubscriber.manipulatorSignal.connect(self.updateForceInformation)
        self.manipSubscriber.manipulatorSignal.connect(self.updateEncoderInformation)
        self.manipSubscriber.manipulatorSignal.connect(self.updateActiveAxis)
    
    @QtCore.pyqtSlot()
    def updateActiveAxis(self):
        self.activeAxisDisplay.display(self.manipSubscriber.manipulatorCurrentActiveAxis)

    ### POSITION SENDING CONTROLS ###
    @QtCore.pyqtSlot()
    def firstAxisManipButtonClicked(self):
        actualValue = self.firstAxisLine.text()
        if actualValue == '':
            self.manipPublisher.positionOneControl(0)
        else:
            intActualValue = (int(actualValue))
            if intActualValue >= -180 and intActualValue <= 180:
                self.manipPublisher.positionThreeControl(int(actualValue))
            else:
                pass

    @QtCore.pyqtSlot()
    def secondAxisManipButtonClicked(self):
        actualValue = self.secondAxisLine.text()

        if actualValue == '':
            self.manipPublisher.positionTwoControl(0)

        else:
            intActualValue = (int(actualValue))
            if intActualValue >= 0 and intActualValue <= 75:
                self.manipPublisher.positionThreeControl(int(actualValue))
            else:
                pass
    
    @QtCore.pyqtSlot()
    def thirdAxisManipButtonClicked(self):
        actualValue = self.thirdAxisLine.text()

        if actualValue == '':
            self.manipPublisher.positionThreeControl(0)

        else:
            intActualValue = (int(actualValue))
            if intActualValue >= 0 and intActualValue <= 135:
                self.manipPublisher.positionThreeControl(int(actualValue))
            else:
                pass
    
    @QtCore.pyqtSlot()
    def fourthAxisManipButtonClicked(self):
        actualValue = self.fourthAxisLine.text()

        if actualValue == '':
            self.manipPublisher.positionFourControl(0)

        else:
            intActualValue = (int(actualValue))
            if intActualValue >= -90 and intActualValue <= 90:
                self.manipPublisher.positionThreeControl(int(actualValue))
            else:
                pass
    
    @QtCore.pyqtSlot()
    def fifthAxisManipButtonClicked(self):
        actualValue = self.fifthAxisLine.text()

        if actualValue == '':
            self.manipPublisher.positionFiveControl(0)

        else:
            intActualValue = (int(actualValue))
            if intActualValue >= -180 and intActualValue <= 180:
                self.manipPublisher.positionThreeControl(int(actualValue))
            else:
                pass
    
    ### CONTROL CHOICE ###
    @QtCore.pyqtSlot()
    def mouseControlRadioClicked(self):
        self.positionFrame.setDisabled(True)
        if self.mouseControlRadio.isChecked():
            self.manipPublisher.controlChoiceSending(1)

    @QtCore.pyqtSlot()
    def positionSendingRadioClicked(self):
        self.positionFrame.setEnabled(True)
        if self.positionSendingRadio.isChecked():
            self.manipPublisher.controlChoiceSending(2)
    
    ### GRIPPER FRAME METHODS ###
    @QtCore.pyqtSlot()
    def gripperCloseJawsClicked(self):
        self.manipPublisher.gripperCommandSending("-")

    @QtCore.pyqtSlot()
    def gripperOpenJawsClicked(self):
        self.manipPublisher.gripperCommandSending("+")

    @QtCore.pyqtSlot()
    def gripperCommandSendClicked(self):
        self.commandToSend = self.comboBox.currentText()
        self.manipPublisher.gripperCommandSending(self.commandToSend)

    ### POSITION VIEW ###
    @QtCore.pyqtSlot()
    def updateOne(self):
        self.firstAxisDisplay.display(self.manipSubscriber.manipulatorAxisOneActual)
    
    @QtCore.pyqtSlot()
    def updateTwo(self):
        self.secondAxisDisplay.display(self.manipSubscriber.manipulatorAxisTwoActual)

    @QtCore.pyqtSlot()
    def updateThree(self):
        self.thirdAxisDisplay.display(self.manipSubscriber.manipulatorAxisThreeActual)

    @QtCore.pyqtSlot()
    def updateFour(self):
        self.fourthAxisDisplay.display(self.manipSubscriber.manipulatorAxisFourActual)

    @QtCore.pyqtSlot()
    def updateFive(self):
        self.fifthAxisDisplay.display(self.manipSubscriber.manipulatorAxisFiveActual)

    ### GRIPPER SENSORS CALLBACK ###
    @QtCore.pyqtSlot()
    def updateDistanceInformation(self):
        self.distanceLcd.display(self.manipSubscriber.gripperDistanceActual)
    
    @QtCore.pyqtSlot()
    def updateForceInformation(self):
        self.forceLcd.display(self.manipSubscriber.gripperForceActual)
    
    @QtCore.pyqtSlot()
    def updateEncoderInformation(self):
        self.encoderLcd.display(self.manipSubscriber.gripperEncoderActual)