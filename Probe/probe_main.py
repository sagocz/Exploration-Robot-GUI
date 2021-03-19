#!/usr/bin/env python

import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication 
from PyQt5.QtCore import QObject
import rospy
from probe_controller import probeController


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        rospy.init_node('LabProbeGUI', anonymous = False)
        self.ui = probeController()
    
    def showAndSetup(self):
        self.ui.setupUi(self)
        self.show()

def main(argv):           
    app = QtWidgets.QApplication(argv)
    window = Window()
    window.showAndSetup()
     
    sys.exit(app.exec_())

if __name__ == '__main__':
    main(sys.argv)
    
