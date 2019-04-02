from picamera import PiCamera
import time
from subprocess import call
from time import sleep
camera = PiCamera()
camera.brightness=60
camera.resolution=(500,500)
camera.start_preview()
sleep(0.5)
strt=time.strftime('%Y-%m-%d-%H-%M-%S')
camera.capture('./test/'+strt+'.jpg')
camera.stop_preview()