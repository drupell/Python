#! /usr/bin/python3

import pyautogui as mouse
print("Press Ctrl+C to quit.")
try:
    while True:
        x, y = mouse.position()
        pos = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(pos, end='')
        print('\b'*len(pos),end='',flush=True)

except KeyboardInterrupt:
    print("\nDone.")
