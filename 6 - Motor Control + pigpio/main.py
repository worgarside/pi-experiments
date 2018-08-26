import pigpio
from time import sleep
from math import ceil
from enum import Enum, unique, auto


@unique
class Direction(Enum):
    CLOCKWISE = auto()
    ANTICLOCKWISE = auto()


PINS_OUT = [21, 26, 19, 13]
PINS_IN = [17, 5, 6]
DELAY = 0.0005  # 0.05 >= d >= 0.0005
PRINT_SPACE = ' '
ANGLE_DIVISOR = 0.703125
pi = pigpio.pi()


def activate(*pins):
    [pi.write(p, 1) for p in pins]
    sleep(DELAY)
    [pi.write(p, 0) for p in pins]


def cycle_pins():
    for i in range(len(PINS_OUT) * 2):
        if i % 2 == 0:
            j = int(i / 2)
            activate(PINS_OUT[j], PINS_OUT[(j + 1) % len(PINS_OUT)])
        else:
            activate(PINS_OUT[ceil(i / 2) % len(PINS_OUT)])


def degs_to_steps(angle):
    return ceil(angle / ANGLE_DIVISOR)


def run_motor(*_):
    while pi.read(17):
        cycle_pins()


if __name__ == '__main__':
    if not 0.05 >= DELAY >= 0.0005:
        raise ValueError('DELAY out of bounds. Motor will not function.')

    for pin in PINS_OUT:
        pi.set_mode(pin, pigpio.OUTPUT)

    for pin in PINS_IN:
        pi.set_mode(pin, pigpio.INPUT)
        pi.set_pull_up_down(pin, pigpio.PUD_DOWN)

    pi.callback(17, pigpio.EITHER_EDGE, run_motor)

    input('Press enter to exit ')
    pi.stop()
