#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import UInt8, Int16, Char, Bool

class ArmControlLogic:
    roll_threshold = 0.4
    tilt_threshold = 0.1
    spin_threshold = 0.1
    gripper_threshold = 0.5
    open_command = chr(43)
    close_command = chr(45)


    def __init__(self):
       
        rospy.init_node("armControlLogic", anonymous=False)
        self.motors_lock = True
        self.index = 1
        self.gripperPositionLock = 0
        self.lock = [0] * 2

        self.command = Char()
        self.pwm = [Int16()]*5
        self.motor_selection = UInt8()


        self.pwm0_pub = rospy.Publisher(name="manipulator/axisZeroPwm", data_class=Int16, queue_size=1)
        self.pwm1_pub = rospy.Publisher(name="manipulator/axisOnePwm", data_class=Int16, queue_size=1)
        self.pwm2_pub = rospy.Publisher(name="manipulator/axisTwoPwm", data_class=Int16, queue_size=1)
        self.pwm3_pub = rospy.Publisher(name="manipulator/axisThreePwm", data_class=Int16, queue_size=1)
        self.pwm4_pub = rospy.Publisher(name="manipulator/axisFourPwm", data_class=Int16, queue_size=1)
        self.pwm_pub = [self.pwm0_pub,self.pwm1_pub,self.pwm2_pub,self.pwm3_pub,self.pwm4_pub]

        self.motor_selection_pub = rospy.Publisher(name="manipulator/motorSelection",data_class=UInt8,queue_size=1)
        self.command_pub = rospy.Publisher(name="gripper/command",data_class=Char,queue_size=1)

        self.joy_sub = rospy.Subscriber(name="spacenav/joy", data_class=Joy,
                                          callback=self.joyCallback, queue_size=10)

        self.motorsLockSub = rospy.Subscriber(name="safety/motorsLock", data_class=Bool,
                                          callback=self.motors_lock_callback, queue_size=1)


    def map(self,value, leftMin=-0.68359375, leftMax=0.68359375, rightMin=-160, rightMax=160):
        # Figure out how 'wide' each range is
        leftSpan = float(leftMax) - float(leftMin)
        rightSpan = float(rightMax) - float(rightMin)

        # Convert the left range into a 0-1 range (float)
        valueScaled = (value - leftMin) / (leftSpan)

        # Convert the 0-1 range into a value in the right range.
        return rightMin + (valueScaled * rightSpan)

    def motors_lock_callback(self,lock):
        lock_state = lock.data
        if lock_state:
            self.motors_lock = True
        else:
            self.motors_lock = False

    
    def joyCallback(self, joy):

    # button logic for changing motor
        spin = -float(joy.axes[5])/3

        if self.index == 1:
            tilt = float(joy.axes[4])/1
        elif self.index == 2:
            tilt = float(joy.axes[4])/1.9
        elif self.index == 3:
            tilt = float(joy.axes[4])/3

        roll = -float(joy.axes[3])/1.5
        panUpDown = float(joy.axes[2])
        

        if(joy.buttons[0] == 1 and self.lock[0] == 0):
            self.index = self.index +1
            if self.index == 4:
                self.index = 1
            self.lock[0] = 1
        elif(joy.buttons[0] == 0):
            self.lock[0] = 0

    # button logic for self.locking gripper
        if(joy.buttons[1] == 1 and self.lock[1] == 0):
            self.gripperPositionLock = self.gripperPositionLock +1
            if self.gripperPositionLock == 2:
                self.gripperPositionLock = 0
            self.lock[1] = 1
        elif(joy.buttons[1] == 0):
            self.lock[1] = 0

    # spin BASE
        if(abs(spin) > ArmControlLogic.spin_threshold):
            self.pwm[0] = self.map(spin)
        else:
            self.pwm[0] = 0


    # tilt AXES
        if(abs(tilt) > ArmControlLogic.tilt_threshold):
            self.pwm[self.index] = self.map(tilt)
        else:
            self.pwm[self.index] = 0

    # roll AXES
        if(abs(roll) > ArmControlLogic.roll_threshold):
            self.pwm[4] = self.map(roll)
        else:
            self.pwm[4] = 0

    # panUpDown GRIPPER
        if not self.gripperPositionLock:
            if panUpDown > ArmControlLogic.gripper_threshold:
                self.command.data = 43
                self.command_pub.publish(self.command)
            elif panUpDown < ArmControlLogic.gripper_threshold * -1:
                self.command.data = 45
                self.command_pub.publish(self.command)


    def publish_pwms(self,event):
        axis = 0
        self.motor_selection_pub.publish(self.index)
        while axis < 5:
            self.pwm_pub[axis].publish(self.pwm[axis]) 
            axis += 1

    def spin(self):
        # while not rospy.is_shutdown():
        #     self.publish_pwms()
        #     rospy.sleep(0.2)
        rospy.spin()

if __name__ == '__main__':
    armControlLogic = ArmControlLogic()
    rospy.Timer(rospy.Duration(0.2),armControlLogic.publish_pwms)
    armControlLogic.spin()