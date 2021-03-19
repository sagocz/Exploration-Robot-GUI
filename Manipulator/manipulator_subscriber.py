#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16, String, Float64, UInt8
from PyQt5.QtCore import QObject, pyqtSignal


class manipulatorReceiver(QObject):
    
    manipulatorSignal = pyqtSignal()
    def __init__(self):
        super(manipulatorReceiver, self).__init__()
        self.SubNameOne = "manipulator/axisZeroDesired"
        self.SubNameTwo = "manipulator/axisOneDesired"
        self.SubNameThree = "manipulator/axisTwoDesired"
        self.SubNameFour = "manipulator/axisThreeDesired"
        self.SubNameFive = "manipulator/axisFourDesired"
        self.SubNameEight = "manipulator/motorSelection"
        self.SubNameNine = "gripper/distance"
        self.SubNameTen = "gripper/force"
        self.SubNameEleven = "gripper/encoder"
        

        self.manipulatorAxisOneActual = 0
        self.manipulatorAxisTwoActual = 0
        self.manipulatorAxisThreeActual = 0
        self.manipulatorAxisFourActual = 0
        self.manipulatorAxisFiveActual = 0
        self.manipulatorCurrentActiveAxis = 0
        self.gripperDistanceActual = 0
        self.gripperEncoderActual = 0
        self.gripperForceActual = 0
        
        rospy.Subscriber(self.SubNameOne, Float64, self.axisOneActualCallback)
        rospy.Subscriber(self.SubNameTwo, Float64, self.axisTwoActualCallback)
        rospy.Subscriber(self.SubNameThree, Float64, self.axisThreeActualCallback)
        rospy.Subscriber(self.SubNameFour, Float64, self.axisFourActualCallback)
        rospy.Subscriber(self.SubNameFive, Float64, self.axisFiveActualCallback)
        rospy.Subscriber(self.SubNameEight, UInt8, self.manipulatorActualActiveAxisCallback)
        rospy.Subscriber(self.SubNameNine, Int16, self.gripperDistanceCallback)
        rospy.Subscriber(self.SubNameTen, Int16, self.gripperForceCallback)
        rospy.Subscriber(self.SubNameEleven, Int16, self.gripperEncoderCallback)
    
    def axisOneActualCallback(self, msg):
        self.manipulatorAxisOneActual = msg.data
        self.manipulatorSignal.emit()
    
    def axisTwoActualCallback(self, msg):
        self.manipulatorAxisTwoActual = msg.data
        self.manipulatorSignal.emit()
    
    def axisThreeActualCallback(self, msg):
        self.manipulatorAxisThreeActual = msg.data
        self.manipulatorSignal.emit()
    
    def axisFourActualCallback(self, msg):
        self.manipulatorAxisFourActual = msg.data
        self.manipulatorSignal.emit()
    
    def axisFiveActualCallback(self, msg):
        self.manipulatorAxisFiveActual = msg.data
        self.manipulatorSignal.emit()
    
    def gripperForceCallback(self,msg):
        self.gripperForceActual = msg.data
        self.manipulatorSignal.emit()
    
    def gripperDistanceCallback(self,msg):
        self.gripperDistanceActual = msg.data
        self.manipulatorSignal.emit()
    
    def gripperEncoderCallback(self,msg):
        self.gripperEncoderActual = msg.data
        self.manipulatorSignal.emit()

    def manipulatorActualActiveAxisCallback(self, msg):
        self.manipulatorCurrentActiveAxis = msg.data
        self.manipulatorSignal.emit()