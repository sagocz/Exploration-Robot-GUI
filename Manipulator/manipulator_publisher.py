#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool, Char, Int64, UInt8, Int8
from PyQt5.QtCore import QObject


class manipulatorSending(QObject):
    
    def __init__(self):
        super(manipulatorSending, self).__init__()
        self.PubNameFour = "gripper/command"
        self.PubNameFive = "manipulator/controlChoice"
        self.PubNameSix = "manipulator/firstAxis"
        self.PubNameSeven = "manipulator/secondAxis"
        self.PubNameEight = "manipulator/thirdAxis"
        self.PubNameNine = "manipulator/fourthAxis"
        self.PubNameTen = "manipulator/fifthAxis"        

        self.gripperCommandOrder = rospy.Publisher(self.PubNameFour, Char, queue_size = 1)       
        self.controlChoice = rospy.Publisher(self.PubNameFive, UInt8, queue_size = 1)
        self.positionOneValue = rospy.Publisher(self.PubNameSix, Int64, queue_size = 1)
        self.positionTwoValue = rospy.Publisher(self.PubNameSeven, Int64, queue_size = 1)
        self.positionThreeValue = rospy.Publisher(self.PubNameEight, Int64, queue_size = 1)
        self.positionFourValue = rospy.Publisher(self.PubNameNine, Int64, queue_size = 1)
        self.positionFiveValue = rospy.Publisher(self.PubNameTen, Int64, queue_size = 1)


    def gripperCommandSending(self, shouldCommandSend):
        if shouldCommandSend == "-":  
            self.gripperCommandOrder.publish(45)
        elif shouldCommandSend == "+":       
            self.gripperCommandOrder.publish(43)
        elif shouldCommandSend == "RESET":    
            self.gripperCommandOrder.publish(48)
        elif shouldCommandSend == "STRONG GRIP":    
            self.gripperCommandOrder.publish(49)
        elif shouldCommandSend == "WEAK GRIP":    
            self.gripperCommandOrder.publish(50)
        elif shouldCommandSend == "VOLTAGE MEASURE":    
            self.gripperCommandOrder.publish(51)
        elif shouldCommandSend == "OPENLY":    
            self.gripperCommandOrder.publish(52)
        elif shouldCommandSend == "ENCODER POS":    
            self.gripperCommandOrder.publish(53)    
        elif shouldCommandSend == "BEAM RESET":    
            self.gripperCommandOrder.publish(54)
    
    def controlChoiceSending(self, value):
        self.controlChoice.publish(value)
    
    def positionOneControl(self, value):
        self.positionOneValue.publish(value)
    
    def positionTwoControl(self, value):
        self.positionTwoValue.publish(value)
    
    def positionThreeControl(self, value):
        self.positionThreeValue.publish(value)
    
    def positionFourControl(self, value):
        self.positionFourValue.publish(value)
    
    def positionFiveControl(self, value):
        self.positionFiveValue.publish(value)