#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool, UInt8, Int16
from PyQt5.QtCore import QObject


class chassisSending(QObject):
    
    def __init__(self):
        super(chassisSending, self).__init__()
        self.PubNameOne = "gui/priorityDevice"
        self.PubNameTwo = "gui/drivingStrategy"
        self.PubNameThree = "gui/speedLevel"
        self.PubNameFour = "gui/velocity"
        self.PubNameFive = "gui/turnRatio"
        self.PubNameSix = "gui/safetyButton"

        self.priorityDevice = rospy.Publisher(self.PubNameOne, UInt8, queue_size=1)
        self.drivingStrategy = rospy.Publisher(self.PubNameTwo, UInt8, queue_size=1)
        self.speedLevel = rospy.Publisher(self.PubNameThree, UInt8, queue_size=1)
        self.velocity = rospy.Publisher(self.PubNameFour, Int16, queue_size=1)
        self.turnRatio = rospy.Publisher(self.PubNameFive, Int16, queue_size=1)
        self.safetyButton = rospy.Publisher(self.PubNameSix, Bool, queue_size=1)

    def controlPriority(self, priority):
        self.priorityDevice.publish(priority)
        
    def driveModeControl(self, driveMode):
        self.drivingStrategy.publish(driveMode)

    def speedLevelControl(self, speedMode):
        self.speedLevel.publish(speedMode)
    
    def joypadVelocity(self, velocityValue):
        self.velocity.publish(velocityValue)
    
    def joypadRatio(self, ratioValue):
        self.turnRatio.publish(ratioValue)

    def safetyArmGui(self, armGuiControl):
        self.safetyButton.publish(armGuiControl)