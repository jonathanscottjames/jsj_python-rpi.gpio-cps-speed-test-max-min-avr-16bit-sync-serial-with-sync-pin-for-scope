#!/usr/bin/env python3
# copyright jonathanscottjames@hotmail.com
#thanks git hub nerd Paradise pygame python stack Overflow Raspberry Pi especially tutorialspoint for their consistant dilligent series it's too close to the weekend i have to wrap it up. thanks to all for inspieration and love
import subprocess

print("ctrl + c to exit")
import RPi.GPIO as GPIO
from datetime import datetime
import sys, time, pygame
from pygame.locals import *

GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom
indataLines=0
indata=""
indat=1
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
    indat=indat*10+GPIO.input(2)
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    indat=indat*10+GPIO.input(2)
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    indat=indat*10+GPIO.input(2)
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    indat=indat*10+GPIO.input(2)
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    indat=indat*10+GPIO.input(2)
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    indat=indat*10+GPIO.input(2)
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    indat=indat*10+GPIO.input(2)
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    indat=indat*10+GPIO.input(2)
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    indat=indat*10+GPIO.input(2)
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    indat=indat*10+GPIO.input(2)
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    indat=indat*10+GPIO.input(2)
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    indat=indat*10+GPIO.input(2)
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    indat=indat*10+GPIO.input(2)
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    indat=indat*10+GPIO.input(2)
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    indat=indat*10+GPIO.input(2)
    GPIO.output(3, 1)
    GPIO.output(3, 0)
    indat=indat*10+GPIO.input(2)
    countington=countington+1
    indata=indata+str(indat)[1:]
    indat=1
    if timington<time.time():
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
            hor=0
        mindispstr=" mx="+str(maxington)+" mn="+str(minington)+" t="+str(timebase)+" avr="+(str(averagington)+"_____")[:5]+" cur="+str(countington)+" rt:"+str(time.time()-timingtonson)[:6]+'      '
        Window1.blit(pygame.font.Font('freesansbold.ttf',16).render(mindispstr,0,(255, 255, 255),(0,0,1)),(0,0))
        Window1.blit(pygame.font.Font('freesansbold.ttf',50).render((str(" "*(int(width/14)+1))),0,(1,1,1),(1,1,1)),(0,20))
        while indataLines<(len(indata)/width):# draw indata block
            Window1.blit(pygame.font.Font('freesansbold.ttf', 1).render(str("0"+indata[((width*indataLines)+1):(width*(indataLines+1))]),0,(0,0,1),(55+200*((indataLines%4)==3), 255, 55+200*((indataLines%4)==3))),(1,24+indataLines))
            indataLines=indataLines+1
        indataLines=0    
        for inkey in pygame.event.get(KEYDOWN):#check if a key is pressed check if it is esc
            if inkey.key == K_ESCAPE:          #pf esc key pressed terminat while loop
                off=1
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
        for inkey in pygame.event.get():
            if inkey.type == pygame.VIDEORESIZE:
                width,winhight  = inkey.size  # or event.w, event.h
#                width    = inkey.w
#                winhight = inkey.h
#                scrsize  = inkey.size  # or event.w, event.h
#                width    = inkey.w
#                winhight = inkey.h
                Window1=pygame.display.set_mode((width,winhight),pygame.RESIZABLE) #set control variable to window1 and set initial size and mode of gui window
            if inkey.type==pygame.QUIT: #check if window is "x"'ed or closed from task bar or alt+f4
                off=1
#        pygame.event.pump
        pygame.display.update()# tranmsferr buffer into display proscessor
#        pygame.display.flip()# tranmsferr buffer into display proscessor
        countington=0
        timington=time.time()+timebase
        indata=""
pygame.quit()
sys.exit()
GPIO.cleanup()
#pygame.event.pump	—	internally process pygame event handlers
#pygame.event.get	—	get events from the queue
#pygame.event.poll	—	get a single event from the queue
#pygame.event.wait	—	wait for a single event from the queue
#        width, winhight = pygame.display.get_surface().get_size()
#        pygame.event.wait()
#        pginit=pygame.init()
#        pevpu=pygame.event.pump()
#        pgepo=pygame.event.poll()
#        pgeg=pygame.event.get()
#        mindispstr="pginit="+str(pginit)+" epupp="+str(pevpu)+" mx="+str(maxington)+" mn="+str(minington)+" w="+str(width)+" t="+str(timebase)+" avr="+(str(averagington)+"_____")[:5]+" cur="+str(countington)+" rt:"+str(time.time()-timingtonson)[:6]+'      '
#        mindispst2=" eget="+str(pgeg)+" jsj w h="+str(width)+" "+str(winhight)+'_'*200
#        mindispst3="epoll-"+str(pgepo)+'_'*200
#        Window1.blit(pygame.font.Font('/usr/share/fonts/truetype/freefont/FreeMono.ttf',16).render(mindispstr,0,(255, 255, 255),(0,0,1)),(1, 1))
#        Window1.blit(pygame.font.Font('freesansbold.ttf',16).render(mindispstr,0,(255, 255, 255),(0,0,1)),(1,1))
#        Window1.blit(pygame.font.Font('freesansbold.ttf',16).render(mindispst2[:70],0,(255, 255, 255),(0,0,1)),(1,25))
#        Window1.blit(pygame.font.Font('freesansbold.ttf',16).render(mindispst3[71:140],0,(255, 255, 255),(0,0,1)),(1,50))
#        Window1.blit(pygame.font.Font('/usr/share/fonts/truetype/freefont/FreeMono.ttf',16).render(mindispstr,0,(255, 255, 255),(0,0,1)),(1, 1))


#        time.sleep(0.01)  # wait 10 ms to let the system have some time 

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

#            if event.type == pygame.VIDEORESIZE:
#                scrsize  = event.size  # or event.w, event.h
#                width    = event.w
#                winhight = event.h
#        if pygame.event.get(QUIT): #check if window is "x"'ed or closed from task bar or alt+f4
#            off=1
#        for inkey in pygame.event.get(KEYDOWN):#check if a key is pressed check if it is esc
#            if inkey.key == K_ESCAPE:          #pf esc key pressed terminat while loop
#                off=1
#            if inkey.key ==K_UP   :
#                timebase=timebase*10
#                average=0
#                countingb=0
#                maxington=0
#                minington=0
#            if inkey.key ==K_DOWN :
#                timebase=timebase/10
#                average=0
#                countingb=0
#                maxington=0
#                minington=0
