#!/usr/bin/env python

from enum import IntEnum


class DrivingStrategy(IntEnum):

    RC = 0
    Xbox = 1
    Gui = 2


class SpeedLevel(IntEnum):
    Slow = 0
    Fast = 1
    Turbo = 2


class DrivingType(IntEnum):

    Tank = 0
    Rotary = 1
    Twist = 2
    Stop = 3


class ArmingState(IntEnum):

    Disarmed = 0
    Started = 1
    InProgress = 2
    Failed = 3
    Armed = 4
