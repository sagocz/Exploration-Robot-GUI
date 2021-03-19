#!/usr/bin/env python

import rospy
from std_msgs.msg import UInt8, Int64, Float64
from PyQt5.QtCore import QObject, pyqtSignal


class probeReceiver(QObject):
    
    labProbeSignal = pyqtSignal()
    def __init__(self):
        super(probeReceiver, self).__init__()
        
        self.humidityActual = 9999
        self.temperatureActual = 9999
        self.processStateActual = 10
        self.soilTemperatureActual = 9999
        self.rpmActual = 9999
        self.probeStateActual = 10
        
        rospy.Subscriber("probe/humidity", Float64, self.humidityCallback)
        rospy.Subscriber("probe/temperature", Float64, self.temperatureCallback)
        rospy.Subscriber("probe/processState", UInt8, self.processStateCallback)
        rospy.Subscriber("probe/soilTemperature", Float64, self.soilTemperatureCallback)
        rospy.Subscriber("probe/rpm", Int64, self.rpmCallback)
        rospy.Subscriber("probe/probeState", UInt8, self.probeStateCallback)
        
           
    def humidityCallback(self, msg):
        self.humidityActual = msg.data
        self.labProbeSignal.emit()
    
    def temperatureCallback(self, msg):
        self.temperatureActual = msg.data
        self.labProbeSignal.emit()
    
    def processStateCallback(self, msg):
        self.processStateActual = msg.data
        self.labProbeSignal.emit()
    
    def soilTemperatureCallback(self, msg):
        self.soilTemperatureActual = msg.data
        self.labProbeSignal.emit()
    
    def rpmCallback(self, msg):
        self.rpmActual = msg.data
        self.labProbeSignal.emit()
    
    def probeStateCallback(self, msg):
        self.probeStateActual = msg.data
        self.labProbeSignal.emit()