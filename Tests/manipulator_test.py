#!/usr/bin/env python
import time
import rospy
from std_msgs.msg import Int16, UInt8, Char, Int64, Float64
# from custom_msgs import ChassisState

t = 5
rospy.init_node('Manipulator')


rospy.Publisher("manipulator/axisZeroDesired", Float64, queue_size = 1)
rospy.Publisher("manipulator/axisOneDesired", Float64, queue_size = 1)
rospy.Publisher("manipulator/axisTwoDesired", Float64, queue_size = 1)
rospy.Publisher("manipulator/axisThreeDesired", Float64, queue_size = 1)
rospy.Publisher("manipulator/axisFourDesired", Float64, queue_size = 1)
rospy.Subscriber("manipulator/motorSelection", UInt8, queue_size = 1)
rospy.Publisher("gripper/distance", Int16, queue_size = 1)
rospy.Publisher("gripper/force", Int16, queue_size = 1)
rospy.Publisher("gripper/encoder", Int16, queue_size = 1)
rospy.Subscriber("gripper/command", Char, queue_size = 1)
rospy.Subscriber("manipulator/controlChoice", UInt8, queue_size = 1)
rospy.Subscriber("manipulator/firstAxis", Int64, queue_size = 1)
rospy.Subscriber("manipulator/secondAxis", Int64, queue_size = 1)
rospy.Subscriber("manipulator/thirdAxis", Int64, queue_size = 1)
rospy.Subscriber("manipulator/fourthAxis", Int64, queue_size = 1)
rospy.Subscriber("manipulator/fifthAxis", Int64, queue_size = 1)
rospy.Subscriber("manipulator/axisZeroPwm", Int16, queue_size = 1)
rospy.Subscriber("manipulator/axisOnePwm", Int16, queue_size = 1)
rospy.Subscriber("manipulator/axisTwoPwm", Int16, queue_size = 1)
rospy.Subscriber("manipulator/axisThreePwm", Int16, queue_size = 1)
rospy.Subscriber("manipulator/axisFourPwm", Int16, queue_size = 1)
# rate = rospy.Rate(1) # 3 Hz
 
while not rospy.is_shutdown():
       
    time.sleep(t)
    