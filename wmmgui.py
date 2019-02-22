'''
Programmed by: David Rupell
Description: Uses pyautogui and tkinter modules to track mouse position on
screen and output coordinates in a GUI window.
'''
import pyautogui as mouse
import tkinter as TK

def update_label():
    x, y = mouse.position() #gets position of mouse
    xpos = 'X: ' + str(x).rjust(4)
    ypos = 'Y: ' + str(y).rjust(4)
    xcoord.config(text=xpos,font=(12)) #updates appropriate labels
    ycoord.config(text=ypos,font=(12))
    root.after(1, update_label) #after [some time] update the labels again
    #The int value in the after fct represents time in 1/1000 of a second    
        
root=TK.Tk() #root is the parent object that the rest of the labels will belong to
root.title("Where's My Mouse?") #sets title of application
#Setup labels
title=TK.Label(root,text = "Mouse Position:",font=(12))
xcoord=TK.Label(root,width=20)
ycoord=TK.Label(root,width=20)
#Format display
title.grid(row=0,columnspan=2)
xcoord.grid(row=1,column=0)
ycoord.grid(row=1,column=1)
#update information
update_label()



