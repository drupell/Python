#!/user/bin/python3
'''
shtdwn.py by David Rupell
Description: Uses breadboard wiring and button to shutdown/reboot pi with a
button press that lasts longer than 3 seconds. Functions with an LED to show
system is on or off.
Referenced - Raspberry Pi 3 Cookbook for Python Programmers

**Note: Designed on Raspberry Pi 3. Needs flite installed to announce shutdown
verbally. Copy script to ~/bin and add it to cronab to run script automatically.
    mkdir ~/bin
    mv shtdwn.py ~/bin/shtdwn.py
    crontab -e
'''
    
import time #required for sleep
import RPi.GPIO as GPIO #used to work with GPIO pins
import os #required for terminal commands like flite and shutdown

# Shutdown
DEBUG=True #True for simulation/debugging
SNDON=True

#BTN CONFIG - Set GPIO Ports
GPIO_MODE=GPIO.BOARD
SHTDWN_BTN = 7 
LED = 12 

def gpio_setup():
    #Setup the wiring
    GPIO.setmode(GPIO_MODE)
    #Setup Ports
    GPIO.setup(SHTDWN_BTN,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(LED,GPIO.OUT)

def doShutdown():
    if DEBUG: print("Press detected")
    time.sleep(3)
    if GPIO.input(SHTDWN_BTN):
        if(DEBUG):print("Ignore the shutdown (<3sec)") #Press must be >3 secs
    else:
        if(DEBUG):print("DEBUG: Action would shutdown the RPi Now")
        GPIO.output(LED,0) #Flash the led to signify shutdown
        time.sleep(0.5)
        GPIO.output(LED,1)
        #flite is text to speak. Need flite installed. '.' characters increase
        #pause duration and are not spoken.
        if(SNDON):os.system("flite -t 'Warning commencing power"
                            + "down 3....... 2........... 1'") 
        if not DEBUG:os.system("sudo shutdown -h now")
        if(DEBUG):GPIO.cleanup()
        if(DEBUG):exit()

def main():
    gpio_setup()
    GPIO.output(LED,1) #LED on while system is on
    while True:
        if(DEBUG): print("Waiting for >3sec button press")
        if GPIO.input(SHTDWN_BTN) == False:
            doShutdown()
        time.sleep(1)

try:
    main()
finally:
    GPIO.cleanup()
    print("ATN: GPIO cleanup complete")
    
        
