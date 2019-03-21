'''
Programmed by: David Rupell
Description: Uses pyautogui and tkinter modules to track mouse position on
screen and output coordinates in a GUI window.
'''
import pyautogui as mouse
import tkinter as TK
from time import sleep

def update_label():
    x, y = mouse.position() #gets position of mouse
    xcoord.config(text=x,font=12) #updates appropriate labels
    ycoord.config(text=y,font=12)
    root.after(1, update_label) #after [some time] update the labels again
    #The int value in the after fct represents time in 1/1000 of a second
def square():
    xValue=x.get()
    yValue=y.get()
    distance=dist.get()
    interval=time.get()
    click=check.get()
    curr=current.get()
    rev=reverse.get()
    if click:
        if not curr:
            mouse.moveTo(xValue,yValue,duration=interval)
        else:
            sleep(1)
            xNew, yNew = mouse.position()
            x.set(xNew)
            y.set(yNew)
        if not rev:
            mouse.dragRel(distance,0,duration=interval)
            mouse.dragRel(0,distance,duration=interval) 
            mouse.dragRel(-distance,0,duration=interval)
            mouse.dragRel(0,-distance,duration=interval)
        elif rev:
            mouse.dragRel(-distance,0,duration=interval)
            mouse.dragRel(0,distance,duration=interval) 
            mouse.dragRel(distance,0,duration=interval)
            mouse.dragRel(0,-distance,duration=interval)
    else:
        if not curr:
            mouse.moveTo(xValue,yValue,duration=interval)
        else:
            sleep(1)
            xNew, yNew = mouse.position()
            x.set(xNew)
            y.set(yNew)
        if not rev:
            mouse.moveRel(distance,0,duration=interval)
            mouse.moveRel(0,distance,duration=interval) 
            mouse.moveRel(-distance,0,duration=interval)
            mouse.moveRel(0,-distance,duration=interval)
        elif rev:
            mouse.moveRel(-distance,0,duration=interval)
            mouse.moveRel(0,distance,duration=interval) 
            mouse.moveRel(distance,0,duration=interval)
            mouse.moveRel(0,-distance,duration=interval)

def clicking():
    sleep(3)
    xCurrent, yCurrent= mouse.position()
    clicksNum=clickCount.get()
    time=clickTime.get()
    mouse.click(x=xCurrent,y=yCurrent,clicks=clicksNum,interval=time)

            

root=TK.Tk() #root is the parent object that the rest of the labels will belong to
root.title("Where's My Mouse?") #sets title of application
mouse.FAILSAFE = False
#Declare entry variables
x=TK.IntVar()
y=TK.IntVar()
dist=TK.IntVar()
time=TK.DoubleVar()
current=TK.BooleanVar()
check=TK.BooleanVar()
reverse=TK.BooleanVar()
clickCount=TK.IntVar()
clickTime=TK.IntVar()

#Setup labels
title=TK.Label(root,text = "Mouse Position:",font=12)
xLabel=TK.Label(root,text='X:',font=12,width=5)
xcoord=TK.Label(root,width=10)
yLabel=TK.Label(root,text='Y:',font=12,width=5)
ycoord=TK.Label(root,width=10)
xel=TK.Label(root,text='Start X value:')
yel=TK.Label(root,text='Start Y value:')
distEL=TK.Label(root,text='Square side length:')
timeEL=TK.Label(root,text='Time between move:')
clickEL=TK.Label(root,text='How many clicks?')
clickTimeEL=TK.Label(root,text='Interval between clicks:')
clickConsole=TK.Label(root,text='NOTE: You will have 3 seconds to position your cursor')
subtitle=TK.Label(root,text="\nEnter starting coordinates below, then select desired function.\n")
subtitleClick=TK.Label(root,text="\nClicker",font=12)

#Setup Button
button=TK.Button(root,text="GO",command=square)
clickButton=TK.Button(root,text="Ready to click",command=clicking)

#Setup entry
xEnter=TK.Entry(root,textvariable=x,width=5)
yEnter=TK.Entry(root,textvariable=y,width=5)
currentBox=TK.Checkbutton(root, text="OR use current position (1s after clicking go)",variable=current)
distEnter=TK.Entry(root,textvariable=dist,width=5)
timeEnter=TK.Entry(root,textvariable=time,width=5) 
clickBox=TK.Checkbutton(root,text="Click & drag?",variable=check)
revBox=TK.Checkbutton(root,text="Reverse? (R->L)",variable=reverse)
clickEnter=TK.Entry(root,textvariable=clickCount,width=3)
clickTimeEnter=TK.Entry(root,textvariable=clickTime,width=3)

#Format display
title.grid(row=0,columnspan=5)
xLabel.grid(row=1,column=0)
xcoord.grid(row=1,column=1)
yLabel.grid(row=1,column=2)
ycoord.grid(row=1,column=3)
subtitle.grid(row=2,columnspan=5)
xel.grid(row=3, column=0,sticky=TK.W)
xEnter.grid(row=3,column=1)
yel.grid(row=3, column=2)
yEnter.grid(row=3,column=3)
currentBox.grid(row=4,columnspan=5)
distEL.grid(row=5,column=0)
distEnter.grid(row=5,column=1)
timeEL.grid(row=5,column=2)
timeEnter.grid(row=5, column=3)
clickBox.grid(row=5,column=4,sticky=TK.W)
revBox.grid(row=6, column=4,sticky=TK.W)
button.grid(row=6,column=2,sticky=TK.W)
subtitleClick.grid(row=7,columnspan=5)
clickEL.grid(row=8,column=0,sticky=TK.W)
clickEnter.grid(row=8,column=1)
clickTimeEL.grid(row=8,column=2)
clickTimeEnter.grid(row=8,column=3)
clickButton.grid(row=8,column=4)
clickConsole.grid(row=9,columnspan=2)

#update information
update_label()



