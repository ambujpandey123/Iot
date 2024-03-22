import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO
from telepot.loop import MessageLoop
red=23 # connect red led at pin 23 of raspberry pi
now=datetime.datetime.now()
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(red,GPIO.OUT)
GPIO.output(red,0)
def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print ('Got command: %s' %command)
    if 'On' in command:
        message="Turn On"
        message=message+" red"
        GPIO.output(red,1)
        bot.sendMessage(chat_id,message)
    if 'Off' in command:
        message="Turn Off"
        message=message+" red"
        GPIO.output(red,0)
        bot.sendMessage(chat_id, message)
bot = telepot.Bot('626665131:AAHsNzQbqSj9GZ9-w2t4I') #paste your bot tokan here.
print(bot.getMe())
MessageLoop(bot,action).run_as_thread()
print ('I am listening...')
while 1:
    time.sleep(10)
