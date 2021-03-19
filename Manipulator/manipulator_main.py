#!/usr/bin/env python
import sys
import rospy
from PyQt5 import QtWidgets
from manipulator_controller import manipulatorController


class Window(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        rospy.init_node('ManipulatorGUI', anonymous = False)
        self.ui = manipulatorController()

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