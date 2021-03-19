#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool, Int8
from PyQt5.QtCore import QObject

class safetySending(QObject):

    def __init__(self):
        super(safetySending, self).__init__()

        self.PubNameOne = "gui/softStop"
        self.PubNameTwo = "safety/motorsLock"
        self.PubNameThree = "gui/hardStop"

        self.softStopOrder = rospy.Publisher(self.PubNameOne, Bool, queue_size = 1)
        self.motorsLockOrder = rospy.Publisher(self.PubNameTwo, Bool, queue_size = 1)
        self.hardStopOrder = rospy.Publisher(self.PubNameThree, Bool, queue_size=1)

    def softStopPublisher(self, value):
        self.softStopOrder.publish(value)
    
    def motorsLockPublisher(self, shouldLockMotors):
        self.motorsLockOrder.publish(shouldLockMotors)

    def hardStopPublisher(self, value):
        self.hardStopOrder.publish(value)
    
    