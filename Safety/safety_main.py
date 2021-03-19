#!/usr/bin/env python

import sys
from PyQt5 import QtWidgets
import rospy
from safety_controller import safetyController

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        rospy.init_node('SafetyGUI', anonymous = False)
        self.ui = safetyController()
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