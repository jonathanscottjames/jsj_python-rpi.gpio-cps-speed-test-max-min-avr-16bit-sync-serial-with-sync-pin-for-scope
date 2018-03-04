#!/usr/bin/env python27
import RPi.GPIO as GPIO
from datetime import datetime
import time

GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom
countingb=0
countington=0
timington=time.time()
averagington=0
average=0
maxington=0
minington=0

GPIO.setwarnings(False)  #this supresses error messages to avoid clutter
GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP) #set pull up resistor so grounding will change it
GPIO.setup(3, GPIO.OUT)  #set gpio 4 to output mode
GPIO.setup(4, GPIO.OUT)  #set gpio 4 to output mode
#GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#************** end setup *****************************
#   `

timington = time.time()+1
while True:
    GPIO.output(4, 1)
    GPIO.output(4, 0)
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    countington=countington+1
    if ((timington)<time.time()):
        print(countington, end=" ")
        countingb=countingb+1
        average=average+countington
        if average>2000000000:
            average=countington
            countingb=1
        averagington=average/countingb
        if(countington>maxington):
            maxington=countington
            print(" ")
            print ("max=",maxington," min=",minington," avr=",averagington)
        if(minington==0):
            minington=countington
        if(countington<minington):
            minington=countington
            print(" ")
            print ("max=",maxington," min=",minington," avr=",averagington)
        countington=0
        timington=time.time()+1

            
            
        

#        time.sleep(0.01)  # wait 10 ms to give CPU chance to do other things

# GPIO.input(2) #this returns the value of gpio2 0 for low 1 for high

#GPIO.cleanup()
#===================================================================
#examples :

#if GPIO.input(channel):
#    print('Input was HIGH')
#else:
#    print('Input was LOW')
#..........................................
#
#while GPIO.input(channel) == GPIO.LOW:
#    time.sleep(0.01)  # wait 10 ms to give CPU chance to do other things
#
#..........................................
#
# wait for up to 5 seconds for a rising edge (timeout is in milliseconds)
#channel = GPIO.wait_for_edge(channel, GPIO_RISING, timeout=5000)
#if channel is None:
#    print('Timeout occurred')
#else:
#    print('Edge detected on channel', channel)
#..........................................
#GPIO.add_event_detect(channel, GPIO.RISING)  # add rising edge detection on a channel
#do_something()
#if GPIO.event_detected(channel):
#    print('Button pressed')
#..........................................
#def my_callback(channel):
#    print('This is a edge event callback function!')
#    print('Edge detected on channel %s'%channel)
#    print('This is run in a different thread to 
