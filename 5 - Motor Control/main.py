# noinspection PyUnresolvedReferences
import RPi.GPIO as GPIO
from time import sleep
from math import ceil

PINOUT = [21, 26, 19, 13]
DELAY = 0.0008  # 0.05 >= d >= 0.0008
PRINT_SPACE = ' '
ANGLE_DIVISOR = 0.703125
GPIO.setmode(GPIO.BCM)


def activate(*pins):
    [GPIO.output(p, True) for p in pins]
    sleep(DELAY)
    [GPIO.output(p, False) for p in pins]


def cycle_pins():
    for i in range(len(PINOUT) * 2):
        if i % 2 == 0:
            j = int(i / 2)
            activate(PINOUT[j], PINOUT[(j + 1) % len(PINOUT)])
        else:
            activate(PINOUT[ceil(i / 2) % len(PINOUT)])


def degs_to_steps(angle):
    return ceil(angle / ANGLE_DIVISOR)


def run_motor(pin_num):
    while GPIO.input(pin_num):
        cycle_pins()


if __name__ == '__main__':
    if not 0.05 >= DELAY >= 0.0008:
        raise ValueError('DELAY out of bounds. Motor will not function.')

    for pin in PINOUT:
        GPIO.setup(pin, GPIO.OUT)
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(17, GPIO.BOTH)
    GPIO.add_event_callback(17, run_motor)

    input('Press enter to exit ')
    GPIO.cleanup()
