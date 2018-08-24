# noinspection PyUnresolvedReferences
import RPi.GPIO as GPIO
from time import sleep
from sys import stdout

PINOUT = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(PINOUT, GPIO.OUT)

GPIO.output(PINOUT, True)
input("Press Enter to continue...")
GPIO.output(PINOUT, False)
GPIO.cleanup()
