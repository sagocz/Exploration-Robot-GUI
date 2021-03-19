#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16, String, Float64, UInt8, Bool, UInt8
from custom_msgs.msg import ChassisState
from PyQt5.QtCore import QObject, pyqtSignal


class chassisReceiver(QObject):
    
    chassisSignal = pyqtSignal()
    def __init__(self):
        super(chassisReceiver, self).__init__()

        self.PubNameOne = "pad/drivingStrategy"
        self.PubNameTwo = "pad/softStop"
        self.PubNameThree = "pad/hardStop"
        self.PubNameFour = "pad/speedLevel"
        self.PubNameFive = "pad/velocity"
        self.PubNameSix = "pad/turnRatio"
        self.PubNameSeven = "pad/safetyX"
        self.PubNameEight = "pad/safetyY"
        self.PubNameNine = "pad/safetyButton"
        self.PubNameTen = "gui/priorityDevice"
        self.PubNameEleven = "chassis/state"
        self.PubNameTwelve = "gui/drivingStrategy"
        self.PubNameTheerteen = "gui/speedLevel"
        self.PubNameFourteen = "gui/velocity"
        self.PubNameFiveteen = "gui/turnRatio"
        
        self.drivingStrategyActual = 0
        self.softStopActual = False
        self.hardStopActual = False
        self.speedLevelActual = 0
        self.velocityActual = 0
        self.turnRatioActual = 0
        self.safetyXActual = 0
        self.safetyYActual = 0
        self.safetyButtonActual = False
        self.controlPriorityActual = 0
        self.guiDrivingStrategyActual = 0
        self.guiSpeedLevelActual = 0
        self.guiVelocityActual = 0
        self.guiTurnRatioActual = 0

        self.speedLevel = 0
        self.priorityDevice = 0
        self.armingState = 0
        self.drivingStrategy = 0
        self.driveSpeed = [0,0,0,0,0,0]
        self.steerAngle = [0,0,0,0]

        rospy.Subscriber(self.PubNameOne, UInt8, self.drivingStrategyCallback)
        rospy.Subscriber(self.PubNameTwo, Bool, self.softStopCallback)
        rospy.Subscriber(self.PubNameThree, Bool, self.hardStopCallback)
        rospy.Subscriber(self.PubNameFour, UInt8, self.speedLevelCallback)
        rospy.Subscriber(self.PubNameFive, Int16, self.velocityCallback)
        rospy.Subscriber(self.PubNameSix, Int16, self.turnRatioCallback)
        rospy.Subscriber(self.PubNameSeven, UInt8, self.safetyXCallback)
        rospy.Subscriber(self.PubNameEight, UInt8, self.safetyYCallback)
        rospy.Subscriber(self.PubNameNine, Bool, self.safetyButtonCallback)
        rospy.Subscriber(self.PubNameTen, UInt8, self.controlPriorityCallback)
        rospy.Subscriber(self.PubNameEleven, ChassisState, self.chassisStateCallback)
        rospy.Subscriber(self.PubNameTwelve, UInt8 , self.guiDrivingStrategyCallback)
        rospy.Subscriber(self.PubNameTheerteen, UInt8 , self.guiSpeedLevelCallback)
        rospy.Subscriber(self.PubNameFourteen, Int16, self.guiVelocityCallback)
        rospy.Subscriber(self.PubNameFiveteen, Int16, self.guiTurnRatioCallback)
    
    def guiTurnRatioCallback(self, msg):
        self.guiTurnRatioActual = msg.data
        self.chassisSignal.emit()
        
    def guiVelocityCallback(self, msg):
        self.guiVelocityActual = msg.data
        self.chassisSignal.emit()
        
    def guiSpeedLevelCallback(self, msg):
        self.guiSpeedLevelActual = msg.data
        self.chassisSignal.emit()
        
    def guiDrivingStrategyCallback(self, msg):
        self.guiDrivingStrategyActual = msg.data
        self.chassisSignal.emit()

    def chassisStateCallback(self, msg):
        self.speedLevel = msg.speedLevel
        self.priorityDevice = msg.priorityDevice
        self.armingState = msg.armingState
        self.drivingStrategy = msg.drivingStrategy
        self.driveSpeed = msg.driveSpeed
        self.steerAngle = msg.steerAngle
        self.chassisSignal.emit()


    def drivingStrategyCallback(self, msg):
        self.drivingStrategyActual = msg.data
        self.chassisSignal.emit()

    def softStopCallback(self, msg):
        self.softStopActual = msg.data
        self.chassisSignal.emit()

    def hardStopCallback(self, msg):
        self.hardStopActual = msg.data
        self.chassisSignal.emit()
    
    def speedLevelCallback(self, msg):
        self.velocityActual = msg.data
        self.chassisSignal.emit()
    
    def velocityCallback(self, msg):
        self.velocityActual = msg.data
        self.chassisSignal.emit()
    
    def turnRatioCallback(self, msg):
        self.turnRatioActual = msg.data
        self.chassisSignal.emit()
    
    def safetyXCallback(self, msg):
        self.safetyXActual = msg.data
        self.chassisSignal.emit()
    
    def safetyYCallback(self, msg):
        self.safetyYActual = msg.data
        self.chassisSignal.emit()
    
    def safetyButtonCallback(self, msg):
        self.safetyButtonActual = msg.data
        self.chassisSignal.emit()

    def controlPriorityCallback(self, msg):
        self.controlPriorityActual = msg.data
        self.chassisSignal.emit()

    def returnCommunicateDrivingStrategy(self):
        return self.drivingStrategyActual
    
    def returnCommunicateSoftStop(self):
        return self.softStopActual
    
    def returnCommunicateHardStop(self):
        return self.hardStopActual
    
    def returnCommunicateSpeedLevel(self):
        return self.speedLevelActual
    
    def returnCommunicateVelocity(self):
        return self.velocityActual
    
    def returnCommunicateTurnRatio(self):
        return self.turnRatioActual
    
    def returnCommunicateSafetyX(self):
        return self.safetyXActual
    
    def returnCommunicateSafetyY(self):
        return self.safetyYActual
    
    def returnCommunicateSafetyButton(self):
        return self.safetyButtonActual
    
    def returnCommunicateControlPriority(self):
        return self.controlPriorityActual