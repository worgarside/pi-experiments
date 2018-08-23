# noinspection PyUnresolvedReferences
import RPi.GPIO as GPIO
from time import sleep
from sys import stdout

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
for i in range(5):
    GPIO.output(21, True)
    print('.', end='')
    stdout.flush()
    sleep(0.5)
    GPIO.output(21, False)
    sleep(0.5)
print('!')
GPIO.cleanup()
