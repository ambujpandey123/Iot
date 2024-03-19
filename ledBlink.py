import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)
ledpin=15 # Gpio pin no 15
GPIO.setup(ledpin, GPIO.OUT) 

Try:
   while True:
   GPIO.output(ledpin, True) # Turn on GPIO.HIGH
   sleep(1)
   GPIO.output(18, False) 
   sleep(1)
