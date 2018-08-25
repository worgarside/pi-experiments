# noinspection PyUnresolvedReferences
import RPi.GPIO as GPIO


def cb(pin):
    GPIO.output(21, GPIO.input(pin))


if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(21, GPIO.OUT)
    GPIO.add_event_detect(17, GPIO.BOTH)
    GPIO.add_event_callback(17, cb)

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print()

    GPIO.cleanup()
