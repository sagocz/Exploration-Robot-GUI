#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32, UInt8, Bool, Int16
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

rospy.init_node('tutorialek')

drivingStrategy = rospy.Publisher("/pad/drivingStrategy", UInt8, queue_size = 1)
softStop = rospy.Publisher("/pad/softStop", Bool, queue_size = 1)
hardStop = rospy.Publisher("/pad/hardStop", Bool, queue_size = 1)
speedLevel = rospy.Publisher("/pad/speedLevel", UInt8, queue_size = 1)
velocity = rospy.Publisher("/pad/velocity", Int16, queue_size = 1)
turnRatio = rospy.Publisher("/pad/turnRatio", Int16, queue_size = 1)
safetyX = rospy.Publisher("/pad/safetyX", UInt8, queue_size = 1)
safetyY = rospy.Publisher("/pad/safetyY", UInt8, queue_size = 1)
safetyButton = rospy.Publisher("/pad/safetyButton", Bool, queue_size = 1)
controlPriority = rospy.Publisher("/chassis/controlPriority", UInt8, queue_size = 1)
    # self.state = rospy.Publisher(self.PubNameEleven, ChassisState, queue_size = 1)

rate = rospy.Rate(1) # 3 Hz
 
while not rospy.is_shutdown():
    drivingStrategy.publish(3)
    softStop.publish(False)
    hardStop.publish(False)
    speedLevel.publish(1)
    velocity.publish(65)
    turnRatio.publish(80)
    safetyX.publish(95)
    safetyY.publish(76)
    safetyButton.publish(True)
    controlPriority.publish(1)