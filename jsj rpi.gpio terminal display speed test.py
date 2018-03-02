#!/usr/bin/env python27
import RPi.GPIO as GPIO
from datetime import datetime
import time

GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom
countingb=0
countington=0
timington=time.time()
averagington=0
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
    GPIO.output(3, 1) # set gpio 3 to high
    GPIO.output(3, 0) # set gpio 3 to low
    GPIO.output(3, 1) # set gpio 3 to high
    GPIO.output(3, 0) # set gpio 3 to low
    GPIO.output(3, 1) # set gpio 3 to high
    GPIO.output(3, 0) # set gpio 3 to low
    GPIO.output(3, 1) # set gpio 3 to high
    GPIO.output(3, 0) # set gpio 3 to low
    GPIO.output(3, 1) # set gpio 3 to high
    GPIO.output(3, 0) # set gpio 3 to low
    GPIO.output(3, 1) # set gpio 3 to high
    GPIO.output(3, 0) # set gpio 3 to low
    GPIO.output(3, 1) # set gpio 3 to high
    GPIO.output(3, 0) # set gpio 3 to low
    GPIO.output(3, 1) # set gpio 3 to high
    GPIO.output(3, 0) # set gpio 3 to low
    GPIO.output(3, 1) # set gpio 3 to high
    GPIO.output(3, 0) # set gpio 3 to low
    GPIO.output(3, 1) # set gpio 3 to high
    GPIO.output(3, 0) # set gpio 3 to low
    GPIO.output(3, 1) # set gpio 3 to high
    GPIO.output(3, 0) # set gpio 3 to low
    GPIO.output(3, 1) # set gpio 3 to high
    GPIO.output(3, 0) # set gpio 3 to low
    GPIO.output(3, 1) # set gpio 3 to high
    GPIO.output(3, 0) # set gpio 3 to low
    GPIO.output(3, 1) # set gpio 3 to high
    GPIO.output(3, 0) # set gpio 3 to low
    GPIO.output(3, 1) # set gpio 3 to high
    GPIO.output(3, 0) # set gpio 3 to low
    GPIO.output(3, 1) # set gpio 3 to high
    GPIO.output(3, 0) # set gpio 3 to low
    GPIO.output(4, 1) # set gpio 3 to low
    GPIO.output(4, 0) # set gpio 3 to low
    countington=countington+1
    if ((timington)<time.time()):
        print(countington, end=" ")
        if(averagington==0):
            averagington=countington
        averagington=((averagington + countington)/2)
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
#    print('This is run in a different thread to your main program')
#
#def my_callback_one(channel):
#    print('Callback one')
#
#def my_callback_two(channel):
#    print('Callback two')
#
#GPIO.add_event_detect(channel, GPIO.RISING)
#GPIO.add_event_callback(channel, my_callback_one)
#GPIO.add_event_callback(channel, my_callback_two)
#.........................................
## add rising edge detection on a channel, ignoring further edges for 200ms for switch bounce handling
#GPIO.add_event_detect(channel, GPIO.RISING, callback=my_callback, bouncetime=200)
#..........................................
#chan_list = [11,12]    # add as many channels as you want!
#                       # you can tuples instead i.e.:
#                       #   chan_list = (11,12)
#GPIO.setup(chan_list, GPIO.OUT)
#..........................................
#chan_list = [11,12]                             # also works with tuples
#GPIO.output(chan_list, GPIO.LOW)                # sets all to GPIO.LOW
#GPIO.output(chan_list, (GPIO.HIGH, GPIO.LOW))   # sets first HIGH and second LOW
#..........................................
#GPIO.output(12, not GPIO.input(12))             # toggle gpio channel
#..........................................
#end of list
