#!/usr/bin/env python

from probe_subscriber import probeReceiver
from probe_publisher import probeSending
from probe_gui import Ui_probeGui
import probe_enums as ce

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSlot
from enum import Enum
import rospy        

green = "background-color: rgb(50, 205, 50);"
red = "background-color: rgb(255, 51, 51);"
grey = "background-color: rgb(77, 77, 77);"

class probeController(Ui_probeGui, QObject):

    #setup elements on gui
    def setupUi(self, probeGui):
        Ui_probeGui.setupUi(self, probeGui)

        #initializating Sending and Receiving
        self.labProbePublisher = probeSending()
        self.labProbeSubscriber = probeReceiver()

        # Initializating
        self.autoFrame.setDisabled(True)
        self.manualFrame.setDisabled(True)
        
        ### Process State Connection
        self.labProbeSubscriber.labProbeSignal.connect(self.updateProcessState)

        ### Probe State Connection
        self.labProbeSubscriber.labProbeSignal.connect(self.updateProbeState)

        ### Sensor displays ###

        self.labProbeSubscriber.labProbeSignal.connect(self.updateSensorsValue)
        self.labProbeSubscriber.labProbeSignal.connect(self.updateRpmValue)
        
        ### RADIO BUTTONS ###

        self.manualControlRadio.clicked.connect(self.manualControlRadioClicked)
        self.autoControlRadio.clicked.connect(self.autoControlRadioClicked)

        ### PUSH BUTTONS ###
        # Clicked
        self.sendVelocityButton.clicked.connect(self.sendVelocityButtonClicked)
        self.startCycleButton.clicked.connect(self.startCycleButtonClicked)
        self.stopCycleButton.clicked.connect(self.stopCycleButtonClicked)
        # Pressed
        self.upArrowButtonDrill.pressed.connect(self.upArrowButtonDrillPressed)
        self.downArrowButtonDrill.pressed.connect(self.downArrowButtonDrillPressed)
        self.upArrowButtonProbe.pressed.connect(self.upArrowButtonProbePressed)
        self.downArrowButtonProbe.pressed.connect(self.downArrowButtonProbePressed)
        # Released
        self.upArrowButtonDrill.released.connect(self.upArrowButtonDrillReleased)
        self.downArrowButtonDrill.released.connect(self.downArrowButtonDrillReleased)
        self.upArrowButtonProbe.released.connect(self.upArrowButtonProbeReleased)
        self.downArrowButtonProbe.released.connect(self.downArrowButtonProbeReleased)

        ### MESSAGE BOX ###
        self.drillingProcessBox = QMessageBox()

    ### MSG BOX CONFIG ###
    @QtCore.pyqtSlot()
    def drillingProcessDialog(self):
        self.drillingProcessBox.setText("PROCESS FINISHED!!! :)")
        self.drillingProcessBox.setWindowTitle("INFORM")
        self.drillingProcessBox.exec_()

    ### Process State Update ###
    @QtCore.pyqtSlot()
    def updateProcessState(self):
        self.processStateValue = self.labProbeSubscriber.processStateActual
        if self.autoFrame.isEnabled():
            if self.processStateValue == ce.processState.StepOne:

                self.stateOneLabel.setStyleSheet(green)
                self.stateTwoLabel.setStyleSheet(red)
                self.stateThreeLabel.setStyleSheet(red)
                self.stateFourLabel.setStyleSheet(red)
                self.stateFiveLabel.setStyleSheet(red)
                self.stateSixLabel.setStyleSheet(red)
                self.processLabel.setText("LAB PROBE IS LOWERING")
        
            elif self.processStateValue == ce.processState.StepTwo:

                self.stateOneLabel.setStyleSheet(green)
                self.stateTwoLabel.setStyleSheet(green)
                self.stateThreeLabel.setStyleSheet(red)
                self.stateFourLabel.setStyleSheet(red)
                self.stateFiveLabel.setStyleSheet(red)
                self.stateSixLabel.setStyleSheet(red)
                self.processLabel.setText("TURN ON DRILL ROTATION")

            elif self.processStateValue == ce.processState.StepThree:

                self.stateOneLabel.setStyleSheet(green)
                self.stateTwoLabel.setStyleSheet(green)
                self.stateThreeLabel.setStyleSheet(green)
                self.stateFourLabel.setStyleSheet(red)
                self.stateFiveLabel.setStyleSheet(red)
                self.stateSixLabel.setStyleSheet(red)
                self.processLabel.setText("START OF THE DRILLING PROCESS")
        
            elif self.processStateValue == ce.processState.StepFour:

                self.stateOneLabel.setStyleSheet(green)
                self.stateTwoLabel.setStyleSheet(green)
                self.stateThreeLabel.setStyleSheet(green)
                self.stateFourLabel.setStyleSheet(green)
                self.stateFiveLabel.setStyleSheet(red)
                self.stateSixLabel.setStyleSheet(red)
                self.processLabel.setText("DRILL RETURNING")
        
            elif self.processStateValue == ce.processState.StepFive:

                self.stateOneLabel.setStyleSheet(green)
                self.stateTwoLabel.setStyleSheet(green)
                self.stateThreeLabel.setStyleSheet(green)
                self.stateFourLabel.setStyleSheet(green)
                self.stateFiveLabel.setStyleSheet(green)
                self.stateSixLabel.setStyleSheet(red)
                self.processLabel.setText("TURN OFF DRILL ROTATION")

            elif self.processStateValue == ce.processState.StepSix:

                self.stateOneLabel.setStyleSheet(green)
                self.stateTwoLabel.setStyleSheet(green)
                self.stateThreeLabel.setStyleSheet(green)
                self.stateFourLabel.setStyleSheet(green)
                self.stateFiveLabel.setStyleSheet(green)
                self.stateSixLabel.setStyleSheet(green)
                self.processLabel.setText("LAB PROBE IS LIFTING")

            elif self.processStateValue == ce.processState.StepSeven:

                self.processLabel.setText("PROCESS FINISHED")
                self.stateOneLabel.setStyleSheet(red)
                self.stateTwoLabel.setStyleSheet(red)
                self.stateThreeLabel.setStyleSheet(red)
                self.stateFourLabel.setStyleSheet(red)
                self.stateFiveLabel.setStyleSheet(red)
                self.stateSixLabel.setStyleSheet(red)
                self.drillingProcessDialog()

        else:
            self.stateOneLabel.setStyleSheet(grey)
            self.stateTwoLabel.setStyleSheet(grey)
            self.stateThreeLabel.setStyleSheet(grey)
            self.stateFourLabel.setStyleSheet(grey)
            self.stateFiveLabel.setStyleSheet(grey)
            self.stateSixLabel.setStyleSheet(grey)

    ### Probe State Update ###
    @QtCore.pyqtSlot()
    def updateProbeState(self):
        self.stateValue = self.labProbeSubscriber.probeStateActual

        if self.stateValue == ce.probeState.up:

            self.upStateLabel.setStyleSheet(green)
            self.downStateLabel.setStyleSheet(red)
            self.stopStateLabel.setStyleSheet(red)

        elif self.stateValue == ce.probeState.down:

            self.upStateLabel.setStyleSheet(red)
            self.downStateLabel.setStyleSheet(green)
            self.stopStateLabel.setStyleSheet(red)

        elif self.stateValue == ce.probeState.stop:
            
            self.upStateLabel.setStyleSheet(red)
            self.downStateLabel.setStyleSheet(red)
            self.stopStateLabel.setStyleSheet(green)

        else:

            self.upStateLabel.setStyleSheet(grey)
            self.downStateLabel.setStyleSheet(grey)
            self.stopStateLabel.setStyleSheet(grey)

    #### SENSORS VALUE UPDATE ####
    @QtCore.pyqtSlot()
    def updateRpmValue(self):
        self.rpmLcd.display(self.labProbeSubscriber.rpmActual)

    @QtCore.pyqtSlot()
    def updateSensorsValue(self):
        self.temperatureLcd.display(self.labProbeSubscriber.temperatureActual)
        self.soilTemperatureLcd.display(self.labProbeSubscriber.soilTemperatureActual)
        self.humidityLcd.display(self.labProbeSubscriber.humidityActual)

    #### Manual CONTROL METHODS ####
    # Velocity Send
    @QtCore.pyqtSlot()
    def sendVelocityButtonClicked(self):
        self.labProbePublisher.probeVelocitySend(self.velocityInputLabel.text)


    # Probe Control
    @QtCore.pyqtSlot()
    def downArrowButtonProbePressed(self):
        self.labProbePublisher.probeLiftLowControl(2)

    @QtCore.pyqtSlot()
    def downArrowButtonProbeReleased(self):
        self.labProbePublisher.probeLiftLowControl(0)

    @QtCore.pyqtSlot()
    def upArrowButtonProbePressed(self):
        self.labProbePublisher.probeLiftLowControl(1)

    @QtCore.pyqtSlot()
    def upArrowButtonProbeReleased(self):
        self.labProbePublisher.probeLiftLowControl(0)   


    # Drill Control
    @QtCore.pyqtSlot()
    def downArrowButtonDrillPressed(self):
        self.labProbePublisher.drillLiftLowControl(2)

    @QtCore.pyqtSlot()
    def downArrowButtonDrillReleased(self):
        self.labProbePublisher.drillLiftLowControl(0)

    @QtCore.pyqtSlot()
    def upArrowButtonDrillPressed(self):
        self.labProbePublisher.drillLiftLowControl(1)

    @QtCore.pyqtSlot()
    def upArrowButtonDrillReleased(self): 
        self.labProbePublisher.drillLiftLowControl(0)
    
    #### Manual Control END ####

    @QtCore.pyqtSlot()
    def manualControlRadioClicked(self):
        self.labProbePublisher.probeControlChoiceSend(ce.controlChoice.manual)
        self.manualFrame.setEnabled(True)
        self.autoFrame.setDisabled(True)

    @QtCore.pyqtSlot()
    def autoControlRadioClicked(self):
        self.labProbePublisher.probeControlChoiceSend(ce.controlChoice.auto)
        self.manualFrame.setDisabled(True)
        self.autoFrame.setEnabled(True)

    ### LAB PROBE AUTO METHODS ###

    @QtCore.pyqtSlot()
    def startCycleButtonClicked(self):
        self.labProbePublisher.probeProcessStart(True)
        
    @QtCore.pyqtSlot()
    def stopCycleButtonClicked(self):
        self.labProbePublisher.probeProcessStart(False)