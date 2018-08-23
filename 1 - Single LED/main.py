# noinspection PyUnresolvedReferences
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(21, GPIO.OUT)
for i in range(50):
    GPIO.output(21, True)
    time.sleep(1)
    GPIO.output(21, False)
    time.sleep(1)
GPIO.cleanup()
