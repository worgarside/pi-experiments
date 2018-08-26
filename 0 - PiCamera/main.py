# noinspection PyUnresolvedReferences
from picamera import PiCamera

camera = PiCamera()

camera.start_preview()
input('Press enter to exit ')
camera.stop_preview()
