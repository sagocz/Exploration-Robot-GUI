#!/usr/bin/env python
import time
import rospy
from std_msgs.msg import Int32, Int64, Bool
# from custom_msgs import ChassisState

t = 5
rospy.init_node('Containers')

rospy.Publisher("/containers/measurementOne", Int32, queue_size = 1)
rospy.Publisher("/containers/measurementTwo", Int32, queue_size = 1)
rospy.Publisher("/containers/measurementThree", Int32, queue_size = 1)

rospy.Subscriber("/containers/servoControlOne", Bool, queue_size = 1)
rospy.Subscriber("/containers/servoControlTwo", Bool, queue_size = 1)
rospy.Subscriber("/containers/servoControlThree", Bool, queue_size=1)
rospy.Subscriber("/containers/calibrationOne", Int64, queue_size = 1)
rospy.Subscriber("/containers/calibrationTwo", Int64, queue_size = 1)
rospy.Subscriber("/containers/calibrationThree", Int64, queue_size = 1)
# rate = rospy.Rate(1) # 3 Hz
 
while not rospy.is_shutdown():
       
    time.sleep(t)
    