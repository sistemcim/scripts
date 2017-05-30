#!/usr/bin/python
#

import Tkinter
import time
import tkMessageBox

top=Tkinter.Tk()

#print "\nTkinter Module"
#print dir(Tkinter)
#print "\nTime Module"
#print dir(time)
#print "\ntkMessageBox Module"
#print dir(tkMessageBox)

def getTime():
    "This function returns epoch time in readable form"
    t=time.localtime()
    #time.asctime(t)
    return time.strftime("%b %d %Y %H:%M:%S",t)

def showMessage(event):
    "This function shows hello message"
    tkMessageBox.showinfo( "Hello Python", "Hello World")
    print "********************** Local Namespace Names *******************"
    print locals()
    print "********************** Global Namespace Names *******************"
    print globals()
    
def exitProgram(event):
    "This function exits the program"
    exit()
    
myButton=Tkinter.Button(top,text=getTime())
myButton.bind('<Button-1>', showMessage)
myButton.pack()

exitButton=Tkinter.Button(top,text="Exit")
exitButton.bind('<Double-Button-1>', exitProgram)
exitButton.pack()

top.mainloop()
