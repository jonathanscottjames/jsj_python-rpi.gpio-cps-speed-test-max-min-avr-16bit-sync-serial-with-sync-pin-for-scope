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
winhight=480
off=0
pygame.init()#initialize gui window

Window1=pygame.display.set_mode((width,winhight),pygame.RESIZABLE) #set control variable to window1 and set initial size and mode of gui window
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
        hor=hor+1
        pygame.draw.line(Window1,(0,255,1),(hor+1,1), (hor+1,winhight),1)
        pygame.draw.line(Window1,(0,0,1),  (hor,1),   (hor  , winhight),1)
        pygame.draw.line(Window1,(100,255,100),(hor, (winhight/2)-(previouscountington-averagington) ), (hor, (winhight/2)-(countington-averagington)) , 1)
        previouscountington=countington
        if (hor+1)>width:
            pygame.draw.line(Window1,(0,0,1),(hor+1,1), (hor+1, winhight) , 1)
            hor=1

        indata=indata+"___________"*120
        mindispstr="mx="+str(maxington)+" mn="+str(minington)+" w="+str(width)+" t="+str(timebase)+" avr="+(str(averagington)+'0')[:5]+" cur="+str(countington)+" rt:"+str(time.time()-timingtonson)[:6]+'  '
        Window1.blit(pygame.font.Font('freesansbold.ttf',16).render(mindispstr,0,(255, 255, 255),(0,0,1)),(1, 1))
        Window1.blit(pygame.font.Font('freesansbold.ttf', 1).render(str(indata[:600]     ),0,(255, 255, 255),(0,0,1)),(1,20))
        Window1.blit(pygame.font.Font('freesansbold.ttf', 1).render(str(indata[601:1200] ),0,(255, 255, 255),(0,0,1)),(1,22))
        Window1.blit(pygame.font.Font('freesansbold.ttf', 1).render(str(indata[1201:1800]),0,(255, 255, 255),(0,0,1)),(1,24))
        Window1.blit(pygame.font.Font('freesansbold.ttf', 1).render(str(indata[1801:2400]),0,(55, 255, 55),(0,0,1)),(1,26))
        Window1.blit(pygame.font.Font('freesansbold.ttf', 1).render(str(indata[2401:3000]),0,(255, 255, 255),(0,0,1)),(1,28))
        Window1.blit(pygame.font.Font('freesansbold.ttf', 1).render(str(indata[3001:3600]),0,(255, 255, 255),(0,0,1)),(1,30))
        Window1.blit(pygame.font.Font('freesansbold.ttf', 1).render(str(indata[3601:4200]),0,(255, 255, 255),(0,0,1)),(1,32))
        Window1.blit(pygame.font.Font('freesansbold.ttf', 1).render(str(indata[4201:4800]),0,(55, 255, 55),(0,0,1)),(1,34))
        Window1.blit(pygame.font.Font('freesansbold.ttf', 1).render(str(indata[4801:5400]),0,(255, 255, 255),(0,0,1)),(1,36))
        Window1.blit(pygame.font.Font('freesansbold.ttf', 1).render(str(indata[5401:6000]),0,(255, 255, 255),(0,0,1)),(1,38))
        Window1.blit(pygame.font.Font('freesansbold.ttf', 1).render(str(indata[6001:6600]),0,(255, 255, 255),(0,0,1)),(1,40))
        Window1.blit(pygame.font.Font('freesansbold.ttf', 1).render(str(indata[6601:7200]),0,(55, 255, 55),(0,0,1)),(1,42))
        Window1.blit(pygame.font.Font('freesansbold.ttf', 1).render(str(indata[7201:7800]),0,(255, 255, 255),(0,0,1)),(1,44))
        Window1.blit(pygame.font.Font('freesansbold.ttf', 1).render(str(indata[7801:8400]),0,(255, 255, 255),(0,0,1)),(1,46))
        Window1.blit(pygame.font.Font('freesansbold.ttf', 1).render(str(indata[8401:9000]),0,(255, 255, 255),(0,0,1)),(1,48))
        Window1.blit(pygame.font.Font('freesansbold.ttf', 1).render(str(indata[9001:9600]),0,(55, 255, 55),(0,0,1)),(1,50))
        Window1.blit(pygame.font.Font('freesansbold.ttf', 1).render(str(indata[9601:10200]),0,(255, 255, 255),(0,0,1)),(1,52))
        Window1.blit(pygame.font.Font('freesansbold.ttf', 1).render(str(indata[10201:10800]),0,(255, 255, 255),(0,0,1)),(1,54))
        Window1.blit(pygame.font.Font('freesansbold.ttf', 1).render(str(indata[10801:11400]),0,(255, 255, 255),(0,0,1)),(1,56))
        Window1.blit(pygame.font.Font('freesansbold.ttf', 1).render(str(indata[11401:12000]),0,(55, 255, 55),(0,0,1)),(1,58))
        Window1.blit(pygame.font.Font('freesansbold.ttf', 1).render(str(indata[12001:12600]),0,(255, 255, 255),(0,0,1)),(1,60))
        if pygame.event.get(QUIT): #check if window is "x"'ed or closed from task bar or alt+f4'ed
            off=1
        for inkey in pygame.event.get(KEYDOWN):#check if a key is pressed check if it is esc
            if inkey.key ==K_UP   :
                timebase=timebase*10
                average=0
                countingb=0
                maxington=0
                minington=0
            if inkey.key ==K_DOWN :
                timebase=timebase/10
                average=0
                countingb=0
                maxington=0
                minington=0
            if inkey.key ==K_LEFT :
                width=Width+1
                Window1=pygame.display.set_mode((width,winhight),pygame.RESIZABLE) #set control variable to window1 and set initial size and mode of gui window
            if inkey.key ==K_RIGHT:
                width=width+1
                Window1=pygame.display.set_mode((width,winhight),pygame.RESIZABLE)
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
