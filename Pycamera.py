from time import sleep
from picamera import PiCamera
camera = PiCamera()
camera.resolution = (1280, 720) # selecting resolution 1280x720 px
camera.start_preview()
# Camera warm-up time
sleep(2)
camera.capture('/home/pi/Pictures/newImage.jpg') #capture and save image at specified location
camera.stop_preview()


#$ sudo raspistill -o /home/pi/Desktop/image.jpg