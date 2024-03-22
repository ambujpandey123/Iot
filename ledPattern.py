import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

led1 = 29
led2 = 31
led3 = 33
led4 = 35
led5 = 36
led6 = 37
led7 = 38
led8 = 40

GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(led4, GPIO.OUT)
GPIO.setup(led5, GPIO.OUT)
GPIO.setup(led6, GPIO.OUT)
GPIO.setup(led7, GPIO.OUT)
GPIO.setup(led8, GPIO.OUT)

GPIO.output(led1, False)
GPIO.output(led2, False)
GPIO.output(led3, False)
GPIO.output(led4, False)
GPIO.output(led5, False)
GPIO.output(led6, False)
GPIO.output(led7, False)
GPIO.output(led8, False)

def ledpattern(ledVal1, ledVal2, ledVal3, ledVal4, ledVal5, ledVal6, ledVal7, ledVal8):
    GPIO.output(led1, ledVal1)
    GPIO.output(led2, ledVal2)
    GPIO.output(led3, ledVal3)
    GPIO.output(led4, ledVal4)
    GPIO.output(led5, ledVal5)
    GPIO.output(led6, ledVal6)
    GPIO.output(led7, ledVal7)
    GPIO.output(led8, ledVal8)

def patternOne():
    for i in range(0, 3):
        ledpattern(1, 0, 1, 0, 1, 0, 1, 0)
        time.sleep(1)
        ledpattern(0, 1, 0, 1, 0, 1, 0, 1)
        time.sleep(1)

def patternTwo():
    for i in range(0, 5):
        ledpattern(1, 0, 0, 0, 0, 0, 0, 0)
        time.sleep(0.1)
        ledpattern(0, 1, 0, 0, 0, 0, 0, 0)
        time.sleep(0.1)
        ledpattern(0, 0, 1, 0, 0, 0, 0, 0)
        time.sleep(0.1)
        ledpattern(0, 0, 0, 1, 0, 0, 0, 0)
        time.sleep(0.1)
        ledpattern(0, 0, 0, 0, 1, 0, 0, 0)
        time.sleep(0.1)
        ledpattern(0, 0, 0, 0, 0, 1, 0, 0)
        time.sleep(0.1)
        ledpattern(0, 0, 0, 0, 0, 0, 1, 0)
        time.sleep(0.1)
        ledpattern(0, 0, 0, 0, 0, 0, 0, 1)
        time.sleep(0.1)

def patternThree():
    for i in range(0, 5):
        ledpattern(0, 0, 0, 0, 0, 0, 0, 1)
        time.sleep(0.1)
        ledpattern(0, 0, 0, 0, 0, 0, 1, 0)
        time.sleep(0.1)
        ledpattern(0, 0, 0, 0, 0, 1, 0, 0)
        time.sleep(0.1)
        ledpattern(0, 0, 0, 0, 1, 0, 0, 0)
        time.sleep(0.1)
        ledpattern(0, 0, 0, 1, 0, 0, 0, 0)
        time.sleep(0.1)
        ledpattern(0, 0, 1, 0, 0, 0, 0, 0)
        time.sleep(0.1)
        ledpattern(0, 1, 0, 0, 0, 0, 0, 0)
        time.sleep(0.1)
        ledpattern(1, 0, 0, 0, 0, 0, 0, 0)
        time.sleep(0.1)

def patternFour():
    for i in range(0, 5):
        ledpattern(0, 1, 1, 1, 1, 1, 1, 1)
        time.sleep(0.1)
        ledpattern(1, 0, 1, 1, 1, 1, 1, 1)
        time.sleep(0.1)
        ledpattern(1, 1, 0, 1, 1, 1, 1, 1)
        time.sleep(0.1)
        ledpattern(1, 1, 1, 0, 1, 1, 1, 1)
        time.sleep(0.1)
        ledpattern(1, 1, 1, 1, 0, 1, 1, 1)
        time.sleep(0.1)
        ledpattern(1, 1, 1, 1, 1, 0, 1, 1)
        time.sleep(0.1)
        ledpattern(1, 1, 1, 1, 1, 1, 0, 1)
        time.sleep(0.1)
        ledpattern(1, 1, 1, 1, 1, 1, 1, 0)
        time.sleep(0.1)

def patternFive():
    for i in range(0, 5):
        ledpattern(1, 1, 1, 1, 1, 1, 1, 0)
        time.sleep(0.1)
        ledpattern(1, 1, 1, 1, 1, 1, 0, 1)
        time.sleep(0.1)
        ledpattern(1, 1, 1, 1, 1, 0, 1, 1)
        time.sleep(0.1)
        ledpattern(1, 1, 1, 1, 0, 1, 1, 1)
        time.sleep(0.1)
        ledpattern(1, 1, 1, 0, 1, 1, 1, 1)
        time.sleep(0.1)
        ledpattern(1, 1, 0, 1, 1, 1, 1, 1)
        time.sleep(0.1)
        ledpattern(1,0, 1, 1, 1, 1, 1, 1)
        time.sleep(0.1)
        ledpattern(0,1, 1, 1, 1, 1, 1, 1)
        time.sleep(0.1)

try:
    while True:
        patternOne()
        patternTwo()
        patternThree()
        patternFour()
        patternFive()
finally:
    GPIO.cleanup()

