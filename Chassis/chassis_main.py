#!/usr/bin/env python

import sys
from PyQt5 import QtWidgets, QtCore
import rospy
from chassis_controller import chassisController


class Window(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        rospy.init_node('ChassisGUI', anonymous = False)
        self.ui = chassisController()

    def showAndSetup(self):
        self.ui.setupUi(self)
        self.show()

    def KeyPressEvent(self, event):
        key = event.key()
        if key == QtCore.Qt.Key_Escape:
            self.close()
        

def main(argv):
    app = QtWidgets.QApplication(argv)
    window = Window()
    window.showAndSetup()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)