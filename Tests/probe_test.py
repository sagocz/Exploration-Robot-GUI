#!/usr/bin/env python
import time
import rospy
from std_msgs.msg import Float64, Int64, Bool, UInt8
# from custom_msgs import ChassisState

t = 5
rospy.init_node('Probe')

rospy.Publisher("/probe/humidity", Float64, queue_size = 1)
rospy.Publisher("/probe/temperature", Float64, queue_size = 1)
rospy.Publisher("/probe/processState", UInt8, queue_size = 1)
rospy.Publisher("/probe/soilTemperature", Float64, queue_size = 1)
rospy.Publisher("/probe/rpm", Int64, queue_size = 1)
rospy.Publisher("/probe/probeState", UInt8, queue_size = 1)
rospy.Subscriber("/probe/controlChoice", UInt8, queue_size = 1)
rospy.Subscriber("/probe/autoProcessStart", Bool, queue_size=1)
rospy.Subscriber("/probe/manualVelocity", Int64, queue_size = 1)
rospy.Subscriber("/probe/probeLiftLow", UInt8, queue_size = 1)
rospy.Subscriber("/probe/drillLiftLow", UInt8, queue_size = 1)
# rate = rospy.Rate(1) # 3 Hz
 
while not rospy.is_shutdown():
       
    time.sleep(t)
    