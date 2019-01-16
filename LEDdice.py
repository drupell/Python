'''
LEDdice.py
Programmer: David Rupell
Date: 1/16/2019
Description: Program waits for user to press a button. The roll button triggers
the rollDice() method that rolls a random number 1-6 and outputs the dice roll
to the screen and through LEDs. The other button shutsdown the program and
triggers the GPIO cleanup. This can be used as a class in a later program.
'''

from time import sleep
import RPi.GPIO as GPIO
import random

TOP_LEFT = 18
TOP_RIGHT = 16
MID_LEFT = 22
MIDDLE = 13
MID_RIGHT = 15
BOTTOM_LEFT = 37
BOTTOM_RIGHT = 11
ROLL_BTN = 33
PWR_BTN = 36

DEBUG = False

def gpio_setup():
    #Setup the wiring
    GPIO.setmode(GPIO.BOARD)
    #Setup Ports
    GPIO.setup(TOP_LEFT,GPIO.OUT)
    GPIO.setup(TOP_RIGHT,GPIO.OUT)
    GPIO.setup(MID_LEFT,GPIO.OUT)
    GPIO.setup(MIDDLE,GPIO.OUT)
    GPIO.setup(MID_RIGHT,GPIO.OUT)
    GPIO.setup(BOTTOM_LEFT,GPIO.OUT)
    GPIO.setup(BOTTOM_RIGHT,GPIO.OUT)
    GPIO.setup(ROLL_BTN,GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(PWR_BTN,GPIO.IN, pull_up_down=GPIO.PUD_UP) 
#one() - six() outputs the appropriate dice roll in text to the screen and
    #to the LEDs.
def one():
    GPIO.output(MIDDLE,1)
    print(" -----------")
    print("|           |")
    print("|           |")
    print("|     o     |")
    print("|           |")
    print("|           |")
    print(" -----------")
    sleep(2)
    ledOff()
def two():
    GPIO.output(TOP_LEFT,1)
    GPIO.output(BOTTOM_RIGHT,1)
    print(" -----------")
    print("|  o        |")
    print("|           |")
    print("|           |")
    print("|           |")
    print("|        o  |")
    print(" -----------")
    sleep(2)
    ledOff()
def three():
    GPIO.output(TOP_RIGHT,1)
    GPIO.output(MIDDLE,1)
    GPIO.output(BOTTOM_LEFT,1)
    print(" -----------")
    print("|        o  |")
    print("|           |")
    print("|     o     |")
    print("|           |")
    print("|  o        |")
    print(" -----------")
    sleep(2)
    ledOff()
def four():
    GPIO.output(TOP_LEFT,1)
    GPIO.output(TOP_RIGHT,1)
    GPIO.output(BOTTOM_LEFT,1)
    GPIO.output(BOTTOM_RIGHT,1)
    print(" -----------")
    print("|  o     o  |")
    print("|           |")
    print("|           |")
    print("|           |")
    print("|  o     o  |")
    print(" -----------")
    sleep(2)
    ledOff()
def five():
    GPIO.output(TOP_LEFT,1)
    GPIO.output(TOP_RIGHT,1)
    GPIO.output(MIDDLE,1)
    GPIO.output(BOTTOM_LEFT,1)
    GPIO.output(BOTTOM_RIGHT,1)
    print(" -----------")
    print("|  o     o  |")
    print("|           |")
    print("|     o     |")
    print("|           |")
    print("|  o     o  |")
    print(" -----------")
    sleep(2)
    ledOff()
def six():
    GPIO.output(TOP_LEFT,1)
    GPIO.output(TOP_RIGHT,1)
    GPIO.output(MID_LEFT,1)
    GPIO.output(MID_RIGHT,1)
    GPIO.output(BOTTOM_LEFT,1)
    GPIO.output(BOTTOM_RIGHT,1)
    print(" -----------")
    print("|  o     o  |")
    print("|           |")
    print("|  o     o  |")
    print("|           |")
    print("|  o     o  |")
    print(" -----------")
    sleep(2)
    ledOff()
#For making sure that every LED is off after each method
def ledOff():
    GPIO.output(TOP_LEFT,0)
    GPIO.output(TOP_RIGHT,0)
    GPIO.output(MID_LEFT,0)
    GPIO.output(MIDDLE,0)
    GPIO.output(MID_RIGHT,0)
    GPIO.output(BOTTOM_LEFT,0)
    GPIO.output(BOTTOM_RIGHT,0)
#roll is set to a random number 1-6 and is printed to the screen.
    #The appropriate method is called to output the roll again to the screen
    #and in LED format.
def rollDice():
    roll = random.randint(1, 6)
    print("Roll: " + str(roll))
    if roll == 1:
        one()
    elif roll == 2:
        two()
    elif roll == 3:
        three()
    elif roll == 4:
        four()
    elif roll == 5:
        five()
    else:
        six()
def main():
    gpio_setup()
    while GPIO.input(PWR_BTN): #Press pwr button to close program
        if DEBUG: print("Waiting on button press")
        if not GPIO.input(ROLL_BTN): #if button is pressed, roll dice
            rollDice()

try:
    main()
finally:
    GPIO.cleanup()
    print("ATN: Program terminated. GPIO cleanup complete.")
    
