#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool, String, Int32
from PyQt5.QtCore import QObject, pyqtSignal


class containersReceiver(QObject):
    
    containersSignal = pyqtSignal()
    def __init__(self):
        super(containersReceiver, self).__init__()

        self.containersMeasurementOne = 0
        self.containersMeasurementTwo = 0
        self.containersMeasurementThree = 0
        self.firstServoActual = False
        self.secondServoActual = False
        self.thirdServoActual = False

        rospy.Subscriber("containers/measurementOne", Int32, self.firstTensometricBeamMeasurementCallback)
        rospy.Subscriber("containers/measurementTwo", Int32, self.secondTensometricBeamMeasurementCallback)
        rospy.Subscriber("containers/measurementThree", Int32, self.thirdTensometricBeamMeasurementCallback)
        rospy.Subscriber("containers/servoControlOne", Bool, self.firstServoCallback)
        rospy.Subscriber("containers/servoControlTwo", Bool, self.secondServoCallback)
        rospy.Subscriber("containers/servoControlThree", Bool, self.thirdServoCallback)
    
    def firstServoCallback(self, msg):
        self.firstServoActual = msg.data
        self.containersSignal.emit()

    def secondServoCallback(self, msg):
        self.secondServoActual = msg.data
        self.containersSignal.emit()

    def thirdServoCallback(self, msg):
        self.thirdServoActual = msg.data
        self.containersSignal.emit()

    def firstTensometricBeamMeasurementCallback(self, msg):
        self.containersMeasurementOne = msg.data
        self.containersSignal.emit()

    def secondTensometricBeamMeasurementCallback(self, msg):
        self.containersMeasurementTwo = msg.data
        self.containersSignal.emit()

    def thirdTensometricBeamMeasurementCallback(self, msg):
        self.containersMeasurementThree = msg.data
        self.containersSignal.emit()
    