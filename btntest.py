#!/usr/bin/python3
#btntest.py
#Programmed and wired with help from Ch9 of rpi3 cook book for python programmers
#page248 - David Rupell
import time
import os
import RPi.GPIO as GPIO

#Button Config
BTN = 12
DEBUG = False

def gpio_setup():
    #Setup the wiring
    GPIO.setmode(GPIO.BOARD)
    #Setup Ports
    GPIO.setup(BTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def main():
    gpio_setup()
    count = 0
    btn_closed = True
    while True:
        btn_val = GPIO.input(BTN)
        if btn_val and btn_closed:
            print("Open")
            btn_closed = False
        elif btn_val == False and btn_closed==False:
            count+=1
            print("Button press %s" % count)
            #if(btn_val == False):
                #uncomment the following lines to turn this into a powerdown button
            #if(DEBUG):print("In debug. Would have shutdown rpi.") #
            #if not DEBUG: os.system("sudo shutdown -h now") #
            os.system("flite -t '%s'" % count)  
            btn_closed=True
        time.sleep(0.1)

try:
    main()
finally:
    GPIO.cleanup()
    print("Closed Everything. End")
#End
