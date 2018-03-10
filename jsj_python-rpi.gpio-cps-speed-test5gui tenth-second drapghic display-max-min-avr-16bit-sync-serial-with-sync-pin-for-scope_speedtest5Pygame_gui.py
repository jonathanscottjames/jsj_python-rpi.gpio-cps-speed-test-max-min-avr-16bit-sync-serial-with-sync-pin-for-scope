#!/usr/bin/env python3
# copyright jonathanscottjames@hotmail.com
#thanks git hub nerd Paradise pygame python stack Overflow Raspberry Pi especially tutorialspoint for their consistant dilligent series it's too close to the weekend i have to wrap it up. thanks to all for inspieration and love
print("ctrl + c to exit")
import RPi.GPIO as GPIO
from datetime import datetime
import sys, time, pygame
from pygame.locals import *


GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom
countingb=0
countington=0
timington=time.time()
timingtonson=time.time()
averagington=0
average=0
maxington=0
minington=0
hor=0
previouscountington=1
off=0
pygame.init()#initialize gui window

Window1=pygame.display.set_mode((640,480),pygame.RESIZABLE) #set control variable to window1 and set initial size and mode of gui window
pygame.display.set_caption('press esc or click "x" or press alt+f4 to exit')#set gui window title bat caption

GPIO.setwarnings(False)  #this supresses error messages to avoid clutter
GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP) #set pull up resistor so grounding will change it
GPIO.setup(3, GPIO.OUT)  #set gpio 4 to output mode
GPIO.setup(4, GPIO.OUT)  #set gpio 4 to output mode
#GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#************** end setup *****************************

timington = time.time()+1
while not off:
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
        currentdispstr=str(countington)
        countingb=countingb+1
        average=average+countington
        if average>2000000000:
            average=countington
            countingb=1
        averagington=average/countingb
        if(countington>maxington):
            maxington=countington

        if(minington==0):
            minington=countington                                   
        if(countington<minington):                                 
            minington=countington                                 
            #print (" max=",maxington,"vmin=",minington,"avr=",averagington, "runtime:",time.time()-timingtonson)
       #line(Surface, color, start_pos, end_pos, width=1) -> Rect
       #line(Window1,(255,255,255), (), (), width=1)
        hor=hor*(hor<600)+1
        #if maxington-minington
        pygame.draw.line(Window1,(1,1,1),(hor+1,1), (hor+1, 480) , 1)
        pygame.draw.line(Window1,(100,255,100),(hor, 240-(previouscountington-averagington) ), (hor+1, 240-(countington-averagington)) , 1)
        previouscountington=countington
        mindispstr=str(("max=",maxington,"min=",minington,"avr=",averagington, "runtime:",time.time()-timingtonson))
        Window1.blit(pygame.font.Font('freesansbold.ttf', 16).render(str('#'*len(mindispstr)),0,(1,1,1),(1,1,1)),(1, 1))
        Window1.blit(pygame.font.Font('freesansbold.ttf', 16).render(mindispstr,0,(255, 255, 255)),(1, 1))


#       Window1.blit(pygame.font.Font('freesansbold.ttf', 16).render(str(' '*40),0,(1,1,1),(1,1,1)),(400, 30))
#       Window1.blit(pygame.font.Font('freesansbold.ttf', 16).render(str(time.time()),0,(255, 255, 255)),(400, 30))
        
        if pygame.event.get(QUIT): #check if window is "x"'ed or closed from task bar or alt+f4'ed
            off=1
        for inkey in pygame.event.get(KEYDOWN):#check if a key is pressed check if it is esc
            if inkey.key == K_ESCAPE:          #pf esc key pressed terminat while loop
                off=1
        pygame.display.update()# tranmsferr buffer into display proscessor
        countington=0
        timington=time.time()+.1
            
pygame.quit()
sys.exit()










            
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

# Write your code here :-)
