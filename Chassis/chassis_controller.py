#!/usr/bin/env python
from chassis_publisher import chassisSending
from chassis_subscriber import chassisReceiver
from chassis_gui import Ui_chassisGui
import chassis_enums as ce

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QRect
from PyQt5.QtWidgets import QMessageBox
from joypad import Joystick


green = "background-color: rgb(50, 205, 50);"
red = "background-color: rgb(255, 51, 51);"
grey = "background-color: rgb(77, 77, 77);"
yellow = "background-color: rgb(255, 255, 51);"
orange = "background-color: rgb(255, 165, 0);"
chassis = "../chassis_gui_v2/src/Resources/images/podwozie6kol.png"

class chassisController(Ui_chassisGui, QObject):
    
    #Setup elements on GUI
    def setupUi(self, chassisGui):
        # Calling generated class setupUi
        Ui_chassisGui.setupUi(self, chassisGui)
        joystick = Joystick()
        self.chassisPublisher = chassisSending()
        self.chassisSubscriber = chassisReceiver()
        self.chassisLabel.setPixmap(QtGui.QPixmap(chassis))
        self.gridLayout.addWidget(joystick,0,0)
        ### Visibility Setup ###
        self.frameJoypad.setDisabled(True)
        self.frameJoypad.setVisible(False)
        self.xboxArmedFrame.setVisible(False)
        self.joypadArmedFrame.setVisible(False)
        self.joypadArmedFrame.setDisabled(True)

        #### Radio Buttons Connecting ####
        self.xboxControlRadio.clicked.connect(self.xboxControlRadioClicked)
        self.guiControlRadio.clicked.connect(self.guiControlRadioClicked)
        self.rcControlRadio.clicked.connect(self.rcControlRadioClicked)

        self.rotaryModeRadio.clicked.connect(self.rotaryModeRadioClicked)
        self.twistModeRadio.clicked.connect(self.twistModeRadioClicked)
        self.tankModeRadio.clicked.connect(self.tankModeRadioClicked)

        self.slowSpeedRadio.clicked.connect(self.slowSpeedRadioClicked)
        self.fastSpeedRadio.clicked.connect(self.fastSpeedRadioClicked)
        self.turboSpeedRadio.clicked.connect(self.turboSpeedRadioClicked)

        self.guiArmingCheck.clicked.connect(self.guiArmingCheckClicked)
        
        ### Data Actualisation ###
        self.chassisSubscriber.chassisSignal.connect(self.updateDriveMode)
        self.chassisSubscriber.chassisSignal.connect(self.updateSpeedMode)
        self.chassisSubscriber.chassisSignal.connect(self.updateDrivingStrategy)
        self.chassisSubscriber.chassisSignal.connect(self.updateSafetyX)
        self.chassisSubscriber.chassisSignal.connect(self.updateSafetyY)
        self.chassisSubscriber.chassisSignal.connect(self.updateDriveModeArduino)
        self.chassisSubscriber.chassisSignal.connect(self.updateSpeedModeArduino)
        self.chassisSubscriber.chassisSignal.connect(self.updateDrivingStrategyArduino)
        self.chassisSubscriber.chassisSignal.connect(self.updateArmingState)
        self.chassisSubscriber.chassisSignal.connect(self.updatePadVelocity)
        self.chassisSubscriber.chassisSignal.connect(self.updatePadTurnRatio)
        self.chassisSubscriber.chassisSignal.connect(self.updatePadSoftStop)
        self.chassisSubscriber.chassisSignal.connect(self.updatePadHardStop)
        self.chassisSubscriber.chassisSignal.connect(self.updateWheelsVelocity)
        self.chassisSubscriber.chassisSignal.connect(self.updateJoypadFrame)
        self.chassisSubscriber.chassisSignal.connect(self.updateWheelsAngle)

        self.padSoftStopMsg = QMessageBox()
        self.padHardStopMsg = QMessageBox()

    ### update of joypad values ###
    @QtCore.pyqtSlot()
    def updateJoypadFrame(self):
        self.joypadTurnRatio.display(self.chassisSubscriber.guiTurnRatioActual)
        self.joypadVelocity.display(self.chassisSubscriber.guiVelocityActual)
    
    ### Angle callback from chassis state ###
    @QtCore.pyqtSlot()
    def updateWheelsAngle(self):
        self.angleLeftForwardLabel.display(self.chassisSubscriber.steerAngle[0])
        self.angleRightForwardLabel.display(self.chassisSubscriber.steerAngle[1])
        self.angleLeftRewardLabel.display(self.chassisSubscriber.steerAngle[2])
        self.angleRightRewardLabel.display(self.chassisSubscriber.steerAngle[3])
        
    ### Velocity callback from chassis state ###
    @QtCore.pyqtSlot()
    def updateWheelsVelocity(self):
        self.velLeftForwardLabel.display(self.chassisSubscriber.driveSpeed[0])
        self.velRightForwardLabel.display(self.chassisSubscriber.driveSpeed[1])
        self.velLeftRewardLabel.display(self.chassisSubscriber.driveSpeed[2])
        self.velRightRewardLabel.display(self.chassisSubscriber.driveSpeed[3])
        self.velLeftCenterLabel.display(self.chassisSubscriber.driveSpeed[4])
        self.velRightCenterLabel.display(self.chassisSubscriber.driveSpeed[5])

    ### Pad message boxes ###
    @QtCore.pyqtSlot()
    def padSoftStopMsgBox(self):
        self.padSoftStopMsg.setText("PAD SOFT STOP PRESSED!!!")
        self.padSoftStopMsg.setWindowTitle("WARNING!")
        self.padSoftStopMsg.exec_()
        self.chassisSubscriber.softStopActual = False

    @QtCore.pyqtSlot()
    def padHardStopMsgBox(self):
        self.padSoftStopMsg.setText("PAD HARD STOP PRESSED!!!")
        self.padSoftStopMsg.setWindowTitle("WARNING!")
        self.padSoftStopMsg.exec_()
        self.chassisSubscriber.hardStopActual = False

    ### Pad message box activate methods ###
    @QtCore.pyqtSlot()
    def updatePadSoftStop(self):
        if self.chassisSubscriber.softStopActual == True:
            self.padSoftStopMsgBox()
        else:
            pass

    @QtCore.pyqtSlot()
    def updatePadHardStop(self):
        if self.chassisSubscriber.hardStopActual == True:
            self.padHardStopMsgBox()
        else:
            pass
    
    ### Pad velocity and turn ratio values ###
    @QtCore.pyqtSlot()
    def updatePadVelocity(self):
        self.padVelocity.display(self.chassisSubscriber.velocityActual)

    @QtCore.pyqtSlot()
    def updatePadTurnRatio(self):
        self.padTurnRatio.display(self.chassisSubscriber.turnRatioActual)

    ### Arming state status updates ###
    @QtCore.pyqtSlot()
    def updateArmingState(self):

        self.armingStateActual = self.chassisSubscriber.armingState

        if self.armingStateActual == ce.ArmingState.Armed:
            self.armedStatusLabel.setStyleSheet(green)
            self.armedStatusLabel.setText("Armed")
            self.joypadArmedStatusLabel.setStyleSheet(green)
            self.joypadArmedStatusLabel.setText("Armed")

        elif self.armingStateActual == ce.ArmingState.InProgress:
            self.armedStatusLabel.setStyleSheet(yellow)
            self.armedStatusLabel.setText("In Progress")
            self.joypadArmedStatusLabel.setStyleSheet(yellow)
            self.joypadArmedStatusLabel.setText("In Progress")

        elif self.armingStateActual == ce.ArmingState.Started:
            self.armedStatusLabel.setStyleSheet(orange)
            self.armedStatusLabel.setText("Started")
            self.joypadArmedStatusLabel.setStyleSheet(orange)
            self.joypadArmedStatusLabel.setText("Started")

        elif self.armingStateActual == ce.ArmingState.Failed:
            self.armedStatusLabel.setStyleSheet(red)
            self.armedStatusLabel.setText("Failed")
            self.joypadArmedStatusLabel.setStyleSheet(red)
            self.joypadArmedStatusLabel.setText("Failed")

        elif self.armingStateActual == ce.ArmingState.Disarmed:
            self.armedStatusLabel.setStyleSheet(grey)
            self.armedStatusLabel.setText("Disarmed")
            self.joypadArmedStatusLabel.setStyleSheet(grey)
            self.joypadArmedStatusLabel.setText("Disarmed")

    ### Update of driving strategy callback ###
    @QtCore.pyqtSlot()
    def updateDrivingStrategyArduino(self):

        self.drivingStrategyArduinoActual = self.chassisSubscriber.priorityDevice

        if self.drivingStrategyArduinoActual == ce.DrivingStrategy.RC:
            self.rcPriorityLabelArduino.setStyleSheet(green)
            self.padPriorityLabelArduino.setStyleSheet(red)
            self.guiPriorityLabelArduino.setStyleSheet(red)

        elif self.drivingStrategyArduinoActual == ce.DrivingStrategy.Xbox:
            self.padPriorityLabelArduino.setStyleSheet(green)
            self.rcPriorityLabelArduino.setStyleSheet(red)
            self.guiPriorityLabelArduino.setStyleSheet(red)

        elif self.drivingStrategyArduinoActual == ce.DrivingStrategy.Gui:
            self.guiPriorityLabelArduino.setStyleSheet(green)
            self.padPriorityLabelArduino.setStyleSheet(red)
            self.rcPriorityLabelArduino.setStyleSheet(red)

        else:
            self.rcPriorityLabelArduino.setStyleSheet(grey)
            self.padPriorityLabelArduino.setStyleSheet(grey)
            self.guiPriorityLabelArduino.setStyleSheet(grey)

    ### update of drive mode callback ###         
    @QtCore.pyqtSlot()
    def updateDriveModeArduino(self):
        
        self.driveModeArduinoActual = self.chassisSubscriber.drivingStrategy
        if self.driveModeArduinoActual == ce.DrivingType.Tank:
            self.arduinoModeLabel.setStyleSheet(green)
            self.arduinoModeLabel.setText("Tank")
        elif self.driveModeArduinoActual == ce.DrivingType.Rotary:
            self.arduinoModeLabel.setStyleSheet(green)
            self.arduinoModeLabel.setText("Rotary")
        elif self.driveModeArduinoActual == ce.DrivingType.Twist:
            self.arduinoModeLabel.setStyleSheet(green)
            self.arduinoModeLabel.setText("Twist")
        elif self.driveModeArduinoActual == ce.DrivingType.Stop:
            self.arduinoModeLabel.setStyleSheet(red)
            self.arduinoModeLabel.setText("Stop")
    
    ### update of speed mode callback ###
    @QtCore.pyqtSlot()
    def updateSpeedModeArduino(self):

        self.speedModeArduinoActual = self.chassisSubscriber.speedLevel

        if self.speedModeArduinoActual == ce.SpeedLevel.Slow:
            self.arduinoSpeedLabel.setStyleSheet(green)
            self.arduinoSpeedLabel.setText("Slow")

        elif self.speedModeArduinoActual == ce.SpeedLevel.Fast:
            self.arduinoSpeedLabel.setStyleSheet(green)
            self.arduinoSpeedLabel.setText("Fast")

        elif self.speedModeArduinoActual == ce.SpeedLevel.Turbo:
            self.arduinoSpeedLabel.setStyleSheet(green)
            self.arduinoSpeedLabel.setText("Turbo")
        
    ### Drive mode updates ###
    @QtCore.pyqtSlot()
    def updateDriveMode(self):
        self.drivingStrategyMemoryGui = self.chassisSubscriber.guiDrivingStrategyActual
        self.drivingStrategyMemoryPad = self.chassisSubscriber.drivingStrategyActual
        
        if self.xboxControlRadio.isChecked():

            if self.drivingStrategyMemoryPad == ce.DrivingType.Tank:
                self.pcModeLabel.setStyleSheet(green)
                self.pcModeLabel.setText("Tank")

            elif self.drivingStrategyMemoryPad == ce.DrivingType.Rotary:
                self.pcModeLabel.setStyleSheet(green)
                self.pcModeLabel.setText("Rotary")

            elif self.drivingStrategyMemoryPad == ce.DrivingType.Twist:
                self.pcModeLabel.setStyleSheet(green)
                self.pcModeLabel.setText("Twist")

        elif self.guiControlRadio.isChecked():

            if self.drivingStrategyMemoryGui == ce.DrivingType.Tank:
                self.pcModeLabel.setStyleSheet(green)
                self.pcModeLabel.setText("Tank")

            elif self.drivingStrategyMemoryGui == ce.DrivingType.Rotary:
                self.pcModeLabel.setStyleSheet(green)
                self.pcModeLabel.setText("Rotary")

            elif self.drivingStrategyMemoryGui == ce.DrivingType.Twist:
                self.pcModeLabel.setStyleSheet(green)
                self.pcModeLabel.setText("Twist")

    ### operator speed mode update ###
    @QtCore.pyqtSlot()
    def updateSpeedMode(self):
        self.speedModeMemoryGui = self.chassisSubscriber.guiSpeedLevelActual
        self.speedModeMemoryPad = self.chassisSubscriber.speedLevelActual

        if self.xboxControlRadio.isChecked():

            if self.speedModeMemoryPad == ce.SpeedLevel.Slow:
                self.pcSpeedLabel.setStyleSheet(green)
                self.pcSpeedLabel.setText("Slow")

            elif self.speedModeMemoryPad == ce.SpeedLevel.Fast:
                self.pcSpeedLabel.setStyleSheet(green)
                self.pcSpeedLabel.setText("Fast")

            elif self.speedModeMemoryPad == ce.SpeedLevel.Turbo:
                self.pcSpeedLabel.setStyleSheet(green)
                self.pcSpeedLabel.setText("Turbo")

        elif self.guiControlRadio.isChecked():

            if self.speedModeMemoryGui == ce.SpeedLevel.Slow:
                self.pcSpeedLabel.setStyleSheet(green)
                self.pcSpeedLabel.setText("Slow")

            elif self.speedModeMemoryGui == ce.SpeedLevel.Fast:
                self.pcSpeedLabel.setStyleSheet(green)
                self.pcSpeedLabel.setText("Fast")

            elif self.speedModeMemoryGui == ce.SpeedLevel.Turbo:
                self.pcSpeedLabel.setStyleSheet(green)
                self.pcSpeedLabel.setText("Turbo")

    ### operator control choice update ###
    @QtCore.pyqtSlot()
    def updateDrivingStrategy(self):
        self.drivingStrategyMemoryGui = self.chassisSubscriber.controlPriorityActual

        if self.drivingStrategyMemoryGui == ce.DrivingStrategy.Gui:
            self.guiPriorityLabelPc.setStyleSheet(green)
            self.rcPriorityLabelPc.setStyleSheet(red)
            self.padPriorityLabelPc.setStyleSheet(red)

        elif self.drivingStrategyMemoryGui == ce.DrivingStrategy.RC:
            self.rcPriorityLabelPc.setStyleSheet(green)
            self.guiPriorityLabelPc.setStyleSheet(red)
            self.padPriorityLabelPc.setStyleSheet(red)

        elif self.drivingStrategyMemoryGui == ce.DrivingStrategy.Xbox:
            self.padPriorityLabelPc.setStyleSheet(green)
            self.rcPriorityLabelPc.setStyleSheet(red)
            self.guiPriorityLabelPc.setStyleSheet(red)
    
    ### Mapping of values from pad arming process ###
    @QtCore.pyqtSlot()
    def updateSafetyX(self):
        if self.xboxControlRadio.isChecked():
        # Figure out how 'wide' each range is
            leftMax = int(255)
            leftMin = 0
            rightMax = float(100)
            rightMin = 0

            leftSpan = leftMax - leftMin
            rightSpan = rightMax - rightMin

            valueScaled = float(self.chassisSubscriber.safetyYActual - leftMin) / float(leftSpan) 
            value = float(rightMin + (valueScaled * rightSpan))
            self.progressBarX.setValue(int(value))
    
    
    @QtCore.pyqtSlot()
    def updateSafetyY(self):
        if self.xboxControlRadio.isChecked():
            # Figure out how 'wide' each range is
            leftMax = int(255)
            leftMin = 0
            rightMax = float(100)
            rightMin = 0

            leftSpan = leftMax - leftMin
            rightSpan = rightMax - rightMin

            valueScaled = float(self.chassisSubscriber.safetyYActual - leftMin) / float(leftSpan) 
            value = float(rightMin + (valueScaled * rightSpan))
            self.progressBarY.setValue(int(value))

    ### Control choice methods ###
    @QtCore.pyqtSlot()
    def xboxControlRadioClicked(self):

        self.xboxArmedFrame.setEnabled(True)
        self.xboxArmedFrame.setVisible(True)
        self.frameJoypad.setDisabled(True)
        self.frameJoypad.setVisible(False)
        self.joypadArmedFrame.setVisible(False)
        self.joypadArmedFrame.setDisabled(True)
        self.guiArmingCheck.setChecked(False)
        
        if self.xboxControlRadio.isChecked():
            self.chassisPublisher.controlPriority(ce.DrivingStrategy.Xbox)
        

    @QtCore.pyqtSlot()
    def guiControlRadioClicked(self):

        self.xboxArmedFrame.setDisabled(True)
        self.xboxArmedFrame.setVisible(False)
        self.frameJoypad.setEnabled(True)
        self.frameJoypad.setVisible(True)
        self.joypadArmedFrame.setVisible(True)
        self.joypadArmedFrame.setEnabled(True)
        self.chassisPublisher.controlPriority(ce.DrivingStrategy.Gui)
    
    @QtCore.pyqtSlot()
    def rcControlRadioClicked(self):

        self.xboxArmedFrame.setDisabled(True)
        self.xboxArmedFrame.setVisible(False)
        self.frameJoypad.setDisabled(True)
        self.frameJoypad.setVisible(False)
        self.joypadArmedFrame.setVisible(False)
        self.joypadArmedFrame.setDisabled(True)
        self.chassisPublisher.controlPriority(ce.DrivingStrategy.RC)

    ### drriving type choice methods ###
    @QtCore.pyqtSlot()
    def rotaryModeRadioClicked(self):
        self.chassisPublisher.driveModeControl(ce.DrivingType.Rotary)
        
    @QtCore.pyqtSlot()
    def twistModeRadioClicked(self):
        self.chassisPublisher.driveModeControl(ce.DrivingType.Twist)
    
    @QtCore.pyqtSlot()
    def tankModeRadioClicked(self):
        self.chassisPublisher.driveModeControl(ce.DrivingType.Tank)

    ### speed mode methods choice ###
    @QtCore.pyqtSlot()
    def slowSpeedRadioClicked(self):

        self.chassisPublisher.speedLevelControl(ce.SpeedLevel.Slow)

    @QtCore.pyqtSlot()
    def fastSpeedRadioClicked(self):

        self.chassisPublisher.speedLevelControl(ce.SpeedLevel.Fast)  

    @QtCore.pyqtSlot()
    def turboSpeedRadioClicked(self): 

        self.chassisPublisher.speedLevelControl(ce.SpeedLevel.Turbo)

    ### arming check box logic ###
    @QtCore.pyqtSlot()
    def guiArmingCheckClicked(self):
        if self.guiArmingCheck.isChecked():

            self.chassisPublisher.safetyArmGui(True)
            if self.slowSpeedRadio.isChecked():
                self.slowSpeedRadioClicked()
                self.chassisPublisher.speedLevelControl(ce.SpeedLevel.Slow)
            elif self.fastSpeedRadio.isChecked():
                self.chassisPublisher.speedLevelControl(ce.SpeedLevel.Fast)
            elif self.turboSpeedRadio.isChecked():
                self.chassisPublisher.speedLevelControl(ce.SpeedLevel.Turbo)

            if self.tankModeRadio.isChecked():
                self.chassisPublisher.driveModeControl(ce.DrivingType.Tank)
            elif self.twistModeRadio.isChecked():
                self.chassisPublisher.driveModeControl(ce.DrivingType.Twist)
            elif self.rotaryModeRadio.isChecked():
                self.chassisPublisher.driveModeControl(ce.DrivingType.Rotary)       
            
        else: self.chassisPublisher.safetyArmGui(False)