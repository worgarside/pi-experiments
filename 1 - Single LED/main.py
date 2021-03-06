# noinspection PyUnresolvedReferences
import RPi.GPIO as GPIO
from time import sleep
from sys import stdout

PINOUT = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(PINOUT, GPIO.OUT)
for i in range(5):
    GPIO.output(PINOUT, True)
    print('.', end='')
    stdout.flush()
    sleep(0.5)
    GPIO.output(PINOUT, False)
    sleep(0.5)
print('!')
GPIO.cleanup()
