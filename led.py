#!/usr/bin/python3
'''
David Rupell
led.py
Description: Using breadboard wiring and a rapspi, the program looks for a
button press to determine what to do. The first button turns on the LED while
it is pressed. The other button (if held down) breaks the loop and,
in effect, ends the program. If you press both at the same time, a yellow LED
lights up. If you press the first btn and then the second, both light up.
'''

from time import sleep
import RPi.GPIO as GPIO
#Make False to get rid of most onscreen messages
DEBUG = True
#GPIO Channels for where the wires are connected to the board
RED_LED = 16
YELLOW_LED = 13
BTN = 18
KILL_BTN = 7

def gpio_setup():
    #Setup the wiring
    GPIO.setmode(GPIO.BOARD)
    #Setup Ports
    GPIO.setup(BTN,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(KILL_BTN,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(RED_LED,GPIO.OUT)
    GPIO.setup(YELLOW_LED,GPIO.OUT)

def ledButton():
    sleep(.1)
    if GPIO.input(KILL_BTN):
        if DEBUG: print("BTN PRESS DETECTED")
        GPIO.output(YELLOW_LED,0) #make sure only red is showing
        GPIO.output(RED_LED,1)
        sleep(.1)

def killButton():
    sleep(.4)
    Exit = False
    if GPIO.input(KILL_BTN):
        if(DEBUG): print("Ignore short press on kill.")
    elif GPIO.input(BTN): #LED Button is not pressed, proceed with shtdwn
        if(DEBUG): print("Kill button pressed") #(Only if button was held >.25sec
        Exit = True
    return Exit

def bothInput():
    if DEBUG: print("2 inputs detected")
    GPIO.output(YELLOW_LED,1)
    sleep(.1)

def run():
    print("Start")
    while True:
        if DEBUG: print("Waiting for button press...")
        #Button Press
        while not GPIO.input(BTN): #while led button is pressed
            if not GPIO.input(KILL_BTN): #if the kill button is pressed too,
                bothInput() #go to bothInput fct.
            else: #otherwise, light up LED
                ledButton()
        #turn LEDs back off
        GPIO.output(RED_LED,0)
        GPIO.output(YELLOW_LED,0)
        #Kill Button pressed
        if not GPIO.input(KILL_BTN): #if kill button is pressed
            sleep(.1) #(give user time to press other button)
            if not GPIO.input(BTN): #and so is the led button,
                bothInput()
            else: #otherwise close program if button is held
                if killButton(): break
        sleep(.1)

def main():
    gpio_setup()
    run()

try:
    main()
finally:
    GPIO.cleanup()
    print("ATN: Program terminated. GPIO cleanup complete.")
