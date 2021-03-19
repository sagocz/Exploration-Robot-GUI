#!/usr/bin/env python
import time
import rospy
from std_msgs.msg import Int32, UInt8, Bool, Int16, Float64
# from custom_msgs import ChassisState
# self.PubNameOne = "pad/drivingStrategy"
# self.PubNameTwo = "pad/softStop"
# self.PubNameThree = "pad/hardStop"
# self.PubNameFour = "pad/speedLevel"
# self.PubNameFive = "pad/velocity"
# self.PubNameSix = "pad/turnRatio"
# self.PubNameSeven = "pad/safetyX"
# self.PubNameEight = "pad/safetyY"
# self.PubNameNine = "pad/safetyButton"
# self.PubNameTen = "chassis/controlPriority"
t = 5
rospy.init_node('Safety')

hardStop = rospy.Publisher("/safety/hardStop", Bool, queue_size = 1)
motorsOff = rospy.Publisher("/safety/motorsOff", Bool, queue_size = 1)
redButton = rospy.Publisher("/safety/redButton", Bool, queue_size = 1)
temperature = rospy.Publisher("/safety/temperature", Float64, queue_size = 1)
softStop = rospy.Publisher("/safety/softStop", Bool, queue_size = 1)


rospy.Subscriber("/gui/softStop", Bool, queue_size = 1)
rospy.Subscriber("/safety/motorsLock", Bool, queue_size = 1)
rospy.Subscriber("/gui/hardStop", Bool, queue_size=1)

# rate = rospy.Rate(1) # 3 Hz
 
while not rospy.is_shutdown():
    # hardStop.publish(True)
    # time.sleep(t)
    # softStop.publish(True)
    # time.sleep(5)
    # redButton.publish(True)
    
    time.sleep(t)
    # hardStop.publish(True)
    # temperature.publish(55)
    # time.sleep(t)
    # temperature.publish(65)
    # time.sleep(t)
    # temperature.publish(78)
    # time.sleep(t)``
    # temperature.publish(85)
    # time.sleep(t)
    # temperature.publish(95)
    # time.sleep(t)
    # temperature.publish(58)