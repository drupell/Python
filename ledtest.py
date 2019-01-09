#!/usr/bin/python3
'''
David Rupell
ledtest.py
Description: Using breadboard wiring and a rapspi, the program cycles through
colors red, green, and blue outputting the color through the LED. Works with
one RGB module or three separate modules for R G and B.
'''

import time
import RPi.GPIO as GPIO

#RGB LED module
#Works with separate red, green, and blue LEDs too

RGB_ENABLE = 1 #0  May need to swap depending on LEDs used or swap anode
RGB_DISABLE = 0 #1 connection to pin 1. This configuration works well though

RGB_RED = 16
RGB_GREEN = 18
RGB_BLUE = 22 #22
RGB = [RGB_RED,RGB_GREEN,RGB_BLUE]

def led_setup():
    #wiring setup
    GPIO.setmode(GPIO.BOARD)
    #Ports
    for val in RGB:
        GPIO.setup(val, GPIO.OUT)

def main():
    led_setup()
    for val in RGB:
        GPIO.output(val,RGB_ENABLE)
        print("LED ON")
        time.sleep(5)
        GPIO.output(val,RGB_DISABLE)
        print("LED OFF")

try:
    main()
finally:
    GPIO.cleanup()
    print("ATN: GPIO cleanup complete.")
