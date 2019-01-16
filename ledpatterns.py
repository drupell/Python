'''
ledpatterns.py
Programmer: David Rupell
Date: 1/16/2019
Description: Allows user to select from a list of pre-programmed LED patterns
and displays them for atleast one full cycle. User may exit the pattern loops
by pressing the power button to get back to the prompt or go to the next
pattern. Some patterns take user input fo sleep time, but will default to
.5 seconds if the input is not valid.
'''
from time import sleep
import RPi.GPIO as GPIO
import random #only used in chaos lighting [chaos()]

#Channels
BLU = 11 #Blue
YLW = 13 #Yellow
GRN = 15 #Green
RED = 16 #Red
PWR_BTN = 7 #Used to exit patterns
Colors = (BLU, YLW, GRN, RED) #List of colors for random picking

def gpio_setup():
    #Setup the wiring
    GPIO.setmode(GPIO.BOARD)
    #Setup Ports
    GPIO.setup(BLU,GPIO.OUT)
    GPIO.setup(YLW,GPIO.OUT)
    GPIO.setup(GRN,GPIO.OUT)
    GPIO.setup(RED,GPIO.OUT)
    GPIO.setup(PWR_BTN,GPIO.IN,pull_up_down=GPIO.PUD_UP)
#Asks user which pattern they want to execute and returns answer
def prompt():
    print("\nWhich output would you like to see?")
    print("1. Alternating flash")
    print("2. Siren flash")
    print("3. LED cycle (custom speed)")
    print("4. Loading bar")
    print("5. All flash")
    print("6. Choas lights")
    print("7. Double alternating flash")
    print("8. LED pendulum")
    print("9. Cycle all patterns")
    print("Enter desired number. If you wish to exit, type 'quit'...")
    return input("IN > ")
#Alternates between yellow and red. Flashing.
def altFlash():
    print("Alternate flash on. Press pwr button to quit.")
    while GPIO.input(PWR_BTN):
        GPIO.output(YLW,1)
        sleep(.5)
        GPIO.output(YLW,0)
        GPIO.output(RED,1)
        sleep(.5)
        GPIO.output(RED,0)
    ledOff()
#Fast alternate between blue and red like a siren.
def siren():
    print("Siren flash on. Press pwr button to quit.")
    while GPIO.input(PWR_BTN):
        GPIO.output(BLU,1)
        sleep(.2)
        GPIO.output(RED,1)
        GPIO.output(BLU,0)
        sleep(.2)
        GPIO.output(RED,0)
    ledOff()
#Checks to see if user input is a number. If it is, we use it as the
    #sleep time between GPIO outputs. If not, we default to .5 sec sleep time
    #and cycle through the colors.
def cycle():
    try:
        val = float(input("How many seconds should the individual LEDs stay on?" +
                  " (Default = .5)\nIN > "))
    except:
        print("Input was not a number. Defaulting to .5 second intervals.")
        val = .5
    print("Cycle colors on. Press pwr button to quit.")
    while GPIO.input(PWR_BTN):
        GPIO.output(GRN,1)
        sleep(val)
        GPIO.output(GRN,0)
        GPIO.output(YLW,1)
        sleep(val)
        GPIO.output(YLW,0)
        GPIO.output(BLU,1)
        sleep(val)
        GPIO.output(BLU,0)
        GPIO.output(RED,1)
        sleep(val)
        GPIO.output(RED,0)
    ledOff()
#Similar to a loading bar. Lights up each LED one at a time, and turns
    #them off one at a time.
def load():
    print("Loading bar on. Press pwr button to quit.")
    while GPIO.input(PWR_BTN):
        GPIO.output(GRN,1)
        sleep(.5)
        GPIO.output(YLW,1)
        sleep(.5)
        GPIO.output(BLU,1)
        sleep(.5)
        GPIO.output(RED,1)
        sleep(.5)
        GPIO.output(GRN,0)
        sleep(.5)
        GPIO.output(YLW,0)
        sleep(.5)
        GPIO.output(BLU,0)
        sleep(.5)
        GPIO.output(RED,0)
        sleep(.5)
    ledOff()
#Flashes all LEDs at once
def allFlash():
    print("All flash on. Press pwr button to quit.")
    while GPIO.input(PWR_BTN):
        GPIO.output(GRN,1)
        GPIO.output(YLW,1)
        GPIO.output(BLU,1)
        GPIO.output(RED,1)
        sleep(.5)
        GPIO.output(GRN,0)
        GPIO.output(YLW,0)
        GPIO.output(BLU,0)
        GPIO.output(RED,0)
        sleep(.5)
    ledOff()
#Picks a random color and a random state(on or off) and uses that as
    #output to GPIO.
def chaos():
    print("Chaos lights on. Press pwr button to quit.")
    while GPIO.input(PWR_BTN):
        color = Colors[random.randint(0, len(Colors)-1)]
        state = random.randint(0,1)
        GPIO.output(color, state)
        sleep(.1)
    ledOff()
#Alternates between Green and Blue OR Yellow and Red.
def dblAlt():
    print("Double alternating flash on. Press pwr button to quit.")
    while GPIO.input(PWR_BTN):
        GPIO.output(GRN,1)
        GPIO.output(BLU,1)
        sleep(.5)
        GPIO.output(GRN,0)
        GPIO.output(BLU,0)
        GPIO.output(YLW,1)
        GPIO.output(RED,1)
        sleep(.5)
        GPIO.output(YLW,0)
        GPIO.output(RED,0)
    ledOff()
#Cycles through colors quickly - forwards, then backwards. Takes user input
    #for sleep time.
def pendulum():
    try:
        val = float(input("How many seconds should the individual LEDs stay on?" +
                  " (Default = .5)\nIN > "))
    except:
        print("Input was not a number. Defaulting to .5 second intervals.")
        val = .5
    print("Pendulum on. Press pwr button to quit.")
    while GPIO.input(PWR_BTN):
        GPIO.output(GRN,1)
        sleep(val)
        GPIO.output(GRN,0)
        GPIO.output(YLW,1)
        sleep(val)
        GPIO.output(YLW,0)
        GPIO.output(BLU,1)
        sleep(val)
        GPIO.output(BLU,0)
        GPIO.output(RED,1)
        sleep(val)
        GPIO.output(RED,0)
        GPIO.output(BLU,1)
        sleep(val)
        GPIO.output(BLU,0)
        GPIO.output(YLW,1)
        sleep(val)
        GPIO.output(YLW,0)
    ledOff()
#Cycles through all the patterns. Press and hold pwr button to go to next.
def cyclePatterns():
    altFlash()
    sleep(.2)
    siren()
    sleep(.2)
    cycle()
    sleep(.2)
    load()
    sleep(.2)
    allFlash()
    sleep(.2)
    chaos()
    sleep(.2)
    dblAlt()
    sleep(.2)
    pendulum()

#shows a quick pattern to show user that LEDs are shutting off       
def ledOff():
    GPIO.output(GRN,1)
    GPIO.output(YLW,1)
    GPIO.output(BLU,1)
    GPIO.output(RED,1)
    sleep(.5)
    GPIO.output(GRN,0)
    GPIO.output(YLW,0)
    GPIO.output(BLU,0)
    GPIO.output(RED,0)
    sleep(.1)
    GPIO.output(GRN,1)
    GPIO.output(YLW,1)
    GPIO.output(BLU,1)
    GPIO.output(RED,1)
    sleep(.2)
    GPIO.output(GRN,0)
    GPIO.output(YLW,0)
    GPIO.output(BLU,0)
    GPIO.output(RED,0)
#Runs the show. Prints the welcome message and asks which output user wants,
    #then executes the proper method.
def run():
    print("LED Pattern Tester\n"+
          "Selected pattern will run one atleast one full cycle.\nPress and "+
          "hold pwr button to exit a pattern or press it at the\nend of the " +
          "pattern's cycle.\nKeep this in mind if considering long pause times.")
    ans = prompt()
    while ans[0].lower() != 'q':
        if ans == '1':
            altFlash()
        elif ans == '2':
            siren()
        elif ans == '3':
            cycle()
        elif ans == '4':
            load()
        elif ans == '5':
            allFlash()
        elif ans == '6':
            chaos()
        elif ans == '7':
            dblAlt()
        elif ans == '8':
            pendulum()
        elif ans == '9':
            cyclePatterns()
        else:
            print("\nInput not recognized. Try again\n")
        ans = prompt()

def main():
    gpio_setup()
    run()       

try:
    main()
finally:
    GPIO.cleanup()
    print("ATN: Program terminated. GPIO cleanup complete.")
