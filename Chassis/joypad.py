#!/usr/bin/env python
from chassis_publisher import chassisSending
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

import sys
from enum import Enum

class Direction(Enum):
    Left = 0
    Right = 1
    Up = 2
    Down = 3

class Joystick(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Joystick, self).__init__(parent)
        self.setMinimumSize(100, 100)
        self.movingOffset = QtCore.QPointF(0, 0)
        self.grabCenter = False
        self.__maxDistance = 50
        self.centerOfCircle = QtCore.QPointF(0, 0)
        self.chassisPublisher = chassisSending()
    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        bounds = QtCore.QRectF(-self.__maxDistance, -self.__maxDistance, self.__maxDistance * 2, self.__maxDistance * 2 ).translated(self._center())
        painter.drawEllipse(bounds)
        painter.setBrush(Qt.black)
        painter.drawEllipse(self._centerEllipse())

    def _centerEllipse(self):
        if self.grabCenter:
            return QtCore.QRectF(-20, -20, 40, 40).translated(self.movingOffset)
        return QtCore.QRectF(-20, -20, 40, 40).translated(self._center())

    def _center(self):
        return QtCore.QPointF(self.width()/2, self.height()/2)


    def _boundJoystick(self, point):
        limitLine = QtCore.QLineF(self._center(), point)
        if (limitLine.length() > self.__maxDistance):
            limitLine.setLength(self.__maxDistance)
        return limitLine.p2()

    @QtCore.pyqtSlot()
    def mousePressEvent(self, ev):
        self.grabCenter = self._centerEllipse().contains(ev.pos())
        self.chassisPublisher.joypadVelocity(int(self.movingOffset.x()))
        return super(Joystick, self).mousePressEvent(ev)

    @QtCore.pyqtSlot()
    def mouseReleaseEvent(self, event):
        self.grabCenter = False
        self.movingOffset = QtCore.QPointF(0, 0)
        self.update()
        self.chassisPublisher.joypadVelocity(int(self.movingOffset.y()))
        self.chassisPublisher.joypadRatio(int(self.movingOffset.x()))

    @QtCore.pyqtSlot()
    def mouseMoveEvent(self, event):
        leftMaxY = 40
        leftMinY = 140
        leftMaxX = 165
        leftMinX = 65
        rightMax = 255
        rightMin = -255

        if self.grabCenter:
            self.movingOffset = self._boundJoystick(event.pos())
            
            self.update()
            self.movingOffsetY = int(self.movingOffset.y())
            self.movingOffsetX = int(self.movingOffset.x())

        leftSpanX = leftMaxX - leftMinX
        
        rightSpan = rightMax - rightMin
        leftSpanY = leftMaxY - leftMinY

        valueScaledX = float(self.movingOffsetX - leftMinX) / float(leftSpanX)
        self.valueMappedX = float(rightMin + (valueScaledX * rightSpan))

        valueScaledY = float(self.movingOffsetY - leftMinY) / float(leftSpanY)
        self.valueMappedY = float(rightMin + (valueScaledY * rightSpan))
        
        
        print(valueScaledX)
        self.chassisPublisher.joypadVelocity(int(self.valueMappedY))
        self.chassisPublisher.joypadRatio(int(self.valueMappedX))
        
        
