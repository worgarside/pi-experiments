"""
Simple controller for 28BYJ-48 motor with ULN2003A
512 steps = 360deg
"""

# noinspection PyUnresolvedReferences
import RPi.GPIO as GPIO
from time import sleep
from math import ceil
from enum import Enum, unique, auto


@unique
class StepMode(Enum):
    HALF = auto()
    FULL = auto()


@unique
class Direction(Enum):
    CLOCKWISE = auto()
    ANTICLOCKWISE = auto()


PINOUT = [21, 26, 19, 13]
DELAY = 0.001  # 0.05 >= d >= 0.0008
PRINT_SPACE = ' '
ANGLE_DIVISOR = 0.703125
GPIO.setmode(GPIO.BCM)

STEP_MODE: float = StepMode.HALF
DIRECTION = Direction.CLOCKWISE


def activate(*pins):
    [GPIO.output(p, True) for p in pins]
    sleep(DELAY * STEP_MODE.value)
    [GPIO.output(p, False) for p in pins]


def cycle_pins():
    ordered_pins = PINOUT if DIRECTION == Direction.CLOCKWISE else PINOUT[::-1]

    if STEP_MODE == StepMode.HALF:
        for i in range(len(ordered_pins) * 2):
            if i % 2 == 0:
                j = int(i / 2)
                activate(ordered_pins[j], ordered_pins[(j + 1) % len(ordered_pins)])
            else:
                activate(ordered_pins[ceil(i / 2) % len(ordered_pins)])
    elif STEP_MODE == StepMode.FULL:
        for i in range(len(ordered_pins)):
            activate(ordered_pins[i], ordered_pins[(i + 1) % len(ordered_pins)])
    else:
        raise AttributeError('Invalid StepMode')


def degs_to_steps(angle):
    return ceil(angle / ANGLE_DIVISOR)


if __name__ == '__main__':
    if not 0.05 >= DELAY >= 0.0008:
        raise ValueError('DELAY out of bounds. Motor will not function.')

    for pin in PINOUT:
        GPIO.setup(pin, GPIO.OUT)
    try:
        for step in range(degs_to_steps(3600)):
            cycle_pins()
    except KeyboardInterrupt:
        print()

    GPIO.cleanup()
