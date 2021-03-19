#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool, Int64, String
from PyQt5.QtCore import QObject


class containersSending(QObject):
    
    def __init__(self):
        super(containersSending, self).__init__()
        self.PubNameOne = "containers/servoControlOne"
        self.PubNameTwo = "containers/servoControlTwo"
        self.PubNameThree = "containers/servoControlThree"
        self.PubNameFour = "containers/calibrationOne"
        self.PubNameFive = "containers/calibrationTwo"
        self.PubNameSix = "containers/calibrationThree"       
        
        self.containerOneFlagSending = rospy.Publisher(self.PubNameOne, Bool, queue_size=1)
        self.containerTwoFlagSending = rospy.Publisher(self.PubNameTwo, Bool, queue_size=1)
        self.containerThreeFlagSending = rospy.Publisher(self.PubNameThree, Bool, queue_size=1)
        self.containerOneCalibSending = rospy.Publisher(self.PubNameFour, Int64, queue_size=1)
        self.containerTwoCalibSending = rospy.Publisher(self.PubNameFive, Int64, queue_size=1)
        self.containerThreeCalibSending = rospy.Publisher(self.PubNameSix, Int64, queue_size=1)     


    def containerOne(self, shouldMoveOne):
        self.containerOneFlagSending.publish(shouldMoveOne)
        
    def containerTwo(self, shouldMoveTwo):
        self.containerTwoFlagSending.publish(shouldMoveTwo)
    
    def containerThree(self, shouldMoveThree):
        self.containerThreeFlagSending.publish(shouldMoveThree)

    def calibrationOne(self, calibOneValue):
        self.containerOneCalibSending.publish(calibOneValue)

    def calibrationTwo(self, calibTwoValue):
        self.containerTwoCalibSending.publish(calibTwoValue)

    def calibrationThree(self, calibThreeValue):
        self.containerThreeCalibSending.publish(calibThreeValue)        
