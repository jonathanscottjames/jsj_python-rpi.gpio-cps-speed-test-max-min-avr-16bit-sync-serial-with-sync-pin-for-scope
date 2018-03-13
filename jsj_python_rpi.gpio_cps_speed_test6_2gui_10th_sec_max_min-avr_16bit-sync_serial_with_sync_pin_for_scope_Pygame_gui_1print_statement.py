#!/usr/bin/env python3
# copyright jonathanscottjames@hotmail.com
#thanks git hub nerd Paradise pygame python stack Overflow Raspberry Pi especially tutorialspoint for their consistant dilligent series it's too close to the weekend i have to wrap it up. thanks to all for inspieration and love
print("ctrl + c to exit")
import RPi.GPIO as GPIO
from datetime import datetime
import sys, time, pygame
from pygame.locals import *
           

GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom
indata=""
countingb=0
countington=0
timebase=.1
timington=time.time()
timingtonson=time.time()
averagington=0
average=0
maxington=0
minington=0
hor=0
previouscountington=1
width=640
off=0
pygame.init()#initialize gui window

Window1=pygame.display.set_mode((width,480),pygame.RESIZABLE) #set control variable to window1 and set initial size and mode of gui window
pygame.display.set_caption('press esc or click "x" or press alt+f4 to exit')#set gui window title bat caption

GPIO.setwarnings(False)  #this supresses error messages to avoid clutter
GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP) #set pull up resistor so grounding will change it
GPIO.setup(3, GPIO.OUT)  #set gpio 4 to output mode
GPIO.setup(4, GPIO.OUT)  #set gpio 4 to output mode
#GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#************** end setup *****************************

timington = time.time()+timebase
while not off:
    GPIO.output(4, 1)
    GPIO.output(4, 0)
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    indata=(str(indata)+str(GPIO.input(2)))
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    indata=indata+str(GPIO.input(2))
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    indata=indata+str(GPIO.input(2))
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    indata=indata+str(GPIO.input(2))
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    indata=indata+str(GPIO.input(2))
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    indata=indata+str(GPIO.input(2))
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    indata=indata+str(GPIO.input(2))
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    indata=indata+str(GPIO.input(2))
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    indata=indata+str(GPIO.input(2))
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    indata=indata+str(GPIO.input(2))
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    indata=indata+str(GPIO.input(2))
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    indata=indata+str(GPIO.input(2))
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    indata=indata+str(GPIO.input(2))
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    indata=indata+str(GPIO.input(2))
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    indata=indata+str(GPIO.input(2))
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    indata=indata+str(GPIO.input(2))
    countington=countington+1
    if ((timington)<time.time()):
        countingb=countingb+1
        average=average+countington
        if average>2000000000:
            average=countington
            countingb=1
        averagington=average/countingb
        if(countington>maxington): maxington=countington
        if(minington==0):          minington=countington                                   
        if(countington<minington): minington=countington                                 
        hor=hor*(hor<width-10)+1
        pygame.draw.line(Window1,(0,0,1),(hor+1,1), (hor+1, 480) , 1)
        pygame.draw.line(Window1,(100,255,100),(hor, 240-(previouscountington-averagington) ), (hor+1, 240-(countington-averagington)) , 1)
        previouscountington=countington
        indata=indata+"_"*1200
        mindispstr="mx="+str(maxington)+" mn="+str(minington)+" w="+str(width)+" t="+str(timebase)+" avr="+(str(averagington)+'0')[:5]+" cur="+str(countington)+" rt:"+str(time.time()-timingtonson)[:6]+'  '
        Window1.blit(pygame.font.Font('freesansbold.ttf',16).render(mindispstr,0,(255, 255, 255),(0,0,1)),(1, 1))
        Window1.blit(pygame.font.Font('freesansbold.ttf', 5).render(str(indata[:200]     ),0,(255, 255, 255),(0,0,1)),(1, 20))
        Window1.blit(pygame.font.Font('freesansbold.ttf', 5).render(str(indata[201:400]  ),0,(255, 255, 255),(0,0,1)),(1, 25))
        Window1.blit(pygame.font.Font('freesansbold.ttf', 5).render(str(indata[401:600]  ),0,(255, 255, 255),(0,0,1)),(1, 30))
        Window1.blit(pygame.font.Font('freesansbold.ttf', 5).render(str(indata[601:800]  ),0,(255, 255, 255),(0,0,1)),(1, 35))
        Window1.blit(pygame.font.Font('freesansbold.ttf', 5).render(str(indata[801:1000] ),0,(255, 255, 255),(0,0,1)),(1, 40))
        Window1.blit(pygame.font.Font('freesansbold.ttf', 5).render(str(indata[1001:1200]),0,(255, 255, 255),(0,0,1)),(1, 45))
        if pygame.event.get(QUIT): #check if window is "x"'ed or closed from task bar or alt+f4'ed
            off=1
        for inkey in pygame.event.get(KEYDOWN):#check if a key is pressed check if it is esc
            if inkey.key ==K_UP   :timebase=timebase*10
            if inkey.key ==K_DOWN :timebase=timebase/10
            if inkey.key ==K_LEFT :
                width=Width+1
                Window1=pygame.display.set_mode((width,480),pygame.RESIZABLE) #set control variable to window1 and set initial size and mode of gui window
            if inkey.key ==K_RIGHT:
                width=width+1
                Window1=pygame.display.set_mode((width,480),pygame.RESIZABLE)
            if inkey.key == K_ESCAPE:          #pf esc key pressed terminat while loop
                off=1
        pygame.display.update()# tranmsferr buffer into display proscessor
        countington=0
        timington=time.time()+timebase
        indata=""
            
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
