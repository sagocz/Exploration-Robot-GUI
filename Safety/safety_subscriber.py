#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool, Float64
from PyQt5.QtCore import QObject, pyqtSignal

class safetyReceiver(QObject):

    safetySignal = pyqtSignal()

    def __init__(self):
        super(safetyReceiver, self).__init__()

        self.hardStopActual = False
        self.motorsOffActual = False
        self.temperatureActual = 0
        self.redButtonActual = False
        self.softStopActual = False

        self.SubNameOne = "safety/hardStop"
        self.SubNameTwo = "safety/motorsOff"
        self.SubNameThree = "safety/redButton"
        self.SubNameFour = "safety/temperature"
        self.SubNameFive = "safety/softStop"

        rospy.Subscriber(self.SubNameOne, Bool, self.hardStopCallback)
        rospy.Subscriber(self.SubNameTwo, Bool, self.motorsOffCallback)
        rospy.Subscriber(self.SubNameThree, Bool, self.redButtonCallback)
        rospy.Subscriber(self.SubNameFour, Float64, self.temperatureCallback)
        rospy.Subscriber(self.SubNameFive, Bool, self.softStopCallback)

    def hardStopCallback(self, msg):
        self.hardStopActual = msg.data
        self.safetySignal.emit()
        

    def motorsOffCallback(self, msg):
        self.motorsOffActual = msg.data
        self.safetySignal.emit()

    def redButtonCallback(self, msg):
        self.redButtonActual = msg.data
        self.safetySignal.emit()
    
    def temperatureCallback(self, msg):
        self.temperatureActual = msg.data
        self.safetySignal.emit()
    
    def softStopCallback(self, msg):
        self.softStopActual = msg.data
        self.safetySignal.emit()
        