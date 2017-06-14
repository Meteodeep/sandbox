from subprocess import call
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()


Upload = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload /home/pi/Desktop/image.jpg photo00001.jpg"
call ([Upload], shell=True)
