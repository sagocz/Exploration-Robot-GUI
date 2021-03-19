#!/usr/bin/env python

from enum import IntEnum


class probeState(IntEnum):

    up = 0
    stop = 1
    down = 2


class processState(IntEnum):
    StepOne = 0
    StepTwo = 1
    StepThree = 2
    StepFour = 3
    StepFive = 4
    StepSix = 5
    StepSeven = 6

class controlChoice(IntEnum):

    auto = 0
    manual = 1