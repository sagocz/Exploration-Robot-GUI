#!/usr/bin/env python
import time
import rospy
from std_msgs.msg import Int16, UInt8
# from custom_msgs import ChassisState

t = 5
rospy.init_node('Spacenav')

rospy.Publisher("manipulator/axisZeroDesired", Int16, queue_size = 1)
rospy.Publisher("manipulator/axisOneDesired", Int16, queue_size = 1)
rospy.Publisher("manipulator/axisTwoDesired", Int16, queue_size = 1)
rospy.Publisher("manipulator/axisThreeDesired", Int16, queue_size = 1)
rospy.Publisher("manipulator/axisFourDesired", Int16, queue_size = 1)
rospy.Publisher("manipulator/motorSelection", UInt8, queue_size = 1)
# rospy.Subscriber("/probe/manualControl", Bool, queue_size = 1)
# rospy.Subscriber("/probe/autoControl", Bool, queue_size = 1)
# rospy.Subscriber("/probe/autoProcessStart", Bool, queue_size=1)
# rospy.Subscriber("/probe/manualVelocity", Int64, queue_size = 1)
# rospy.Subscriber("/probe/probeLiftLow", UInt8, queue_size = 1)
# rospy.Subscriber("/probe/drillLiftLow", UInt8, queue_size = 1)
# rate = rospy.Rate(1) # 3 Hz
 
while not rospy.is_shutdown():
       
    time.sleep(t)
    