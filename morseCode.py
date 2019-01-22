'''
David Rupell
morseCode.py
Date: 1/22/2019
Description: Morse code translator capable of translating button presses to
letters, morse code text to letters, and letters to morse code.
'''
from time import sleep
import RPi.GPIO as GPIO

BTN = 33
SPC_BTN = 36
BOTTOM_LEFT = 37

DEBUG = False
MORSE_CODE = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 
              'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---',
              'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---',
              'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 
              'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--',
              'Z':'--..', '1':'.----', '2':'..---', '3':'...--', 
              '4':'....-', '5':'.....', '6':'-....', '7':'--...',
              '8':'---..', '9':'----.', '0':'-----', ', ':'--..--',
              '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-'}
CHARACTERS = {'.-':'A', '-...':'B', '-.-.':'C', '-..':'D', '.':'E', 
              '..-.':'F', '--.':'G', '....':'H', '..':'I', '.---':'J',
              '-.-':'K', '.-..':'L', '--':'M', '-.':'N', '---':'O',
              '.--.':'P', '--.-':'Q', '.-.':'R', '...':'S', '-':'T', 
              '..-':'U', '...-':'V', '.--':'W', '-..-':'X', '-.--':'Y',
              '--..':'Z', '.----':'1', '..---':'2', '...--':'3', 
              '....-':'4', '.....':'5', '-....':'6', '--...':'7',
              '---..':'8', '----.':'9', '-----':'0', '--..--':', ',
              '.-.-.-':'.', '..--..':'?', '-..-.':'/', '-....-':'-'} 

def gpio_setup():
    #Setup the wiring
    GPIO.setmode(GPIO.BOARD)
    #Setup Ports
    GPIO.setup(BTN,GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(SPC_BTN,GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BOTTOM_LEFT,GPIO.OUT)
# interface() is a friendly user interface to help users get to the method
# they're looking. The method runs most of the program.
def interface():
    done = False
    while not done:
        print("What would you like to do?")
        print("0. Exit program")
        print("1. Translate button pushes to letters")
        print("2. Translate a sentence to morse code")
        print("3. Translate morse code to a sentence")
        print("4. Help")
        ans = input("IN ---> ")
        if ans == '0':
            done = True
            print("Shutting down...")
        elif ans == '1':
            buttonTranslate()
        elif ans == '2':
            print("Message: " +
              toMorseCode(input("What would you like to translate?\nIN ---> ")))
        elif ans == '3':
            message = toCharacters(input("What would you like to translate?\nIN---> "))
            print("Message: " + message)
        elif ans == '4':
            Help()
        else:
            print("Entered value is not an available option. Enter the number of"
              + "your choice only.")
            interface()
#(1) buttonTranslate() takes GPIO input through two buttons. One is used to
        #input a '.' or '-' while the other is used to separate letters or
        # words. Then, the message is passed through to the toCharacters()
        # method to decode the message. Uesr can end transmission by pressing
        # both buttons at the same time.
def buttonTranslate():
    string = ''
    done = False
    while not done:
        pressTime = 0
        while not GPIO.input(BTN):
            if not GPIO.input(SPC_BTN):
                done = True
            else:
                GPIO.output(BOTTOM_LEFT,1)
                sleep(.1)
                pressTime+=1
        if DEBUG and pressTime != 0: print("Pressed for: " + str(pressTime))
        GPIO.output(BOTTOM_LEFT,0)
        if not GPIO.input(SPC_BTN) and not done:
            print(' ', end='')
            string += ' '
            sleep(.3)
            if not GPIO.input(SPC_BTN):
                print('/ ', end='')
                string += '/ '
            sleep(.3)
        if pressTime <= 2 and pressTime != 0 and not done:
            print('.', end='')
            string += '.'
        elif pressTime > 2 and not done:
            print('-', end='')
            string += '-'
        sleep(.05)
    print("\nMessage: " + toCharacters(string))
            
#(2) toMorseCode() takes a string input and converts it to morse code. Replacing
    #spaces with '/' and unknown characters with '*'
def toMorseCode(string):
    string = string.upper()
    message = ''
    for character in string:
        if character != ' ':
            try:
                message+= MORSE_CODE[character] + ' '
            except:
                message+= '* ' #if letter not recognized, replace with *
        else:
            message+= '/ '
    return message
#(3) toCharacters takes a string input and decodes it replacing '/' with a space
# and unknown characters with '*'
def toCharacters(string):
    message = ''
    letters = string.split(' ')
    for letter in letters:
        if letter == '/':
            message+= ' '
        else:
            try:
                message += CHARACTERS[letter]
            except:
                message += '*' #if code not recognized, replace with *
    return message
    
def Help():
    print("When using the translate button push function:\n\tPress the first button"
          +" for a normal button press.\n\tPress the second button to separate"
          +" letters and hold it down to separate\n\twords.\n"
          +"When translating to or from morse code:\n\tUnknown characters will"
          +" appear as '*'.\n\tIf you got this after translating from button"
          +" presses, make sure there\n\twere no double spaces and all characters"
          +" were input properly.\n\tIf input was correct, the characters may"
          +" not currently be supported.\n.... .- ...- . / ..-. ..- -. ")


def main():
    gpio_setup()
    print("Welcome to the morse code translator!")
    interface()
    

try:
    main()
finally:
    GPIO.cleanup()
    print("\nATN: Program terminated. GPIO cleanup complete.")
