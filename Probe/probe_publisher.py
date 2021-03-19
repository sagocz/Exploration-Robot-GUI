#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool, Char, Int64, UInt8
from PyQt5.QtCore import QObject


class probeSending(QObject):
    
    def __init__(self):
        super(probeSending, self).__init__()
        self.PubNameOne = "probe/controlChoice"
        self.PubNameTwo = "probe/autoProcessStart"        
        self.PubNameThree = "probe/manualVelocity"
        self.PubNameFour = "probe/probeLiftLow"
        self.PubNameFive = "probe/drillLiftLow"

        self.probeControlChoice = rospy.Publisher(self.PubNameOne, UInt8, queue_size=1)
        self.probeProcess = rospy.Publisher(self.PubNameTwo, Bool, queue_size=1)       
        self.probeVelocity = rospy.Publisher(self.PubNameThree, Int64, queue_size=1)      
        self.probeLiftLow = rospy.Publisher(self.PubNameFour, UInt8, queue_size=1)       
        self.drillLiftLow = rospy.Publisher(self.PubNameFive, UInt8, queue_size=1)

    def probeControlChoiceSend(self, value):
        self.probeControlChoice.publish(value)
    
    def probeProcessStart(self, processCommand):
        self.probeProcess.publish(processCommand)
    
    def probeVelocitySend(self, velocityValue):
        velocityToInt = int(velocityValue)
        self.probeVelocity.publish(velocityToInt)
        
    def probeLiftLowControl(self, value):
        self.probeLiftLow.publish(value)
    
    def drillLiftLowControl(self, value):
        self.drillLiftLow.publish(value)
    