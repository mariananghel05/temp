from types import SimpleNamespace
from tkinter import *
import subprocess
import os
import sys
import time

#Variables definition
root = Tk()

Props = SimpleNamespace(
    Background = PhotoImage(file="Images/Bg.png"),
    Resolution = SimpleNamespace(x=1920, y=1080),
    Output = "HDMI-2",
    Apps = SimpleNamespace(
        Stellarium = SimpleNamespace(
            icon = PhotoImage(file="Images/Stellarium.png")
            ),
        GaiaSky = SimpleNamespace(
            icon = PhotoImage(file="Images/GaiaSky.png")
            ),
        Celestia = SimpleNamespace(
            icon = PhotoImage(file="Images/Celestia.png"),
            Resolution = SimpleNamespace(x=1152, y=864)
            ),
        Cosmonium = SimpleNamespace(
            icon = PhotoImage(file="Images/Cosmonium.png")
            ),
        CommingSoon = SimpleNamespace(
            icon = PhotoImage(file="Images/ShutDown.png")
            ),
        ShutDown = SimpleNamespace(
            icon = PhotoImage(file="Images/ShutDown.png")
            ),
        )
    )


#TKinter Layout and Creation
root.attributes("-fullscreen", True)
root.title("Astronomie")

root.minsize(Props.Resolution.x, Props.Resolution.y)
root.maxsize(Props.Resolution.x, Props.Resolution.y)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

root.config(background="#212133",cursor="circle")
limg= Label(root, i=Props.Background).grid(rowspan=3, columnspan=3)




#Apps functions
def start(method):
    root.withdraw()
    method()
    root.deiconify()
def Stellarium():
    os.system("stellarium -geometry {}x{}".format(Props.Resolution.x, Props.Resolution.y))

def GaiaSky():
    os.system("gaiasky")

def Celestia():
    root.withdraw()
    os.system("xrandr --output HDMI-2 --mode {}x{}".format(Props.Apps.Celestia.Resolution.x, Props.Apps.Celestia.Resolution.y))
    os.system("celestia")
    root.deiconify()

def Cosmonium():
    os.system("xterm -geometry {}x{} -e xrandr | grep connected.primary | grep -oE '[0-9]{3,4}x[0-9]{3,4}'".format(Props.Resolution.x, Props.Resolution.y))

def CommingSoon():
    exit()


def ShutDown():
    passwd = Toplevel()
    #passwd.attributes("-fullscreen", True)
    passwd.title("Shutdown - Window")

    passwd.minsize(Props.Resolution.x, Props.Resolution.y)
    passwd.maxsize(Props.Resolution.x, Props.Resolution.y)
    #passwd.minsize(500, 200)
    #passwd.maxsize(500, 200)

    passwd.columnconfigure(0, weight=1)
    passwd.columnconfigure(1, weight=1)
    passwd.columnconfigure(2, weight=1)
    passwd.rowconfigure(0, weight=1)
    passwd.rowconfigure(1, weight=1)
    passwd.rowconfigure(2, weight=1)

    passwd.config(background="#212133",cursor="circle")
    limg= Label(passwd, i=Props.Background).grid(rowspan=3, columnspan=3)
    #Info = Label(passwd,text="Password!", anchor="s").grid(row=0, column=1)
    entry = Entry(passwd, show="*")
    entry.grid(row=2, column=1)
    button = Button(passwd, image=Props.Apps.ShutDown.icon , cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=lambda: (os.system("shutdown now"), time.sleep(0.5), root.destroy(),time.sleep(0.5), exit())  if entry.get() == "123654!@" else passwd.destroy()).grid(row=2, column=2)
   #exit() 



button1 = Button(root, image=Props.Apps.Stellarium.icon, cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=lambda: start(Stellarium)).grid(row=0, column=0)
button2 = Button(root, image=Props.Apps.GaiaSky.icon, cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=lambda: start(GaiaSky)).grid(row=0, column=1)
button3 = Button(root, image=Props.Apps.Celestia.icon, cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=lambda: start(Celestia)).grid(row=0, column=2)


button22 = Button(root, image=Props.Apps.ShutDown.icon , cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=ShutDown).grid(row=2, column=2)
#button33 = Button(root, image=Props.Apps.CommingSoon.icon , cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=CommingSoon).grid(row=1, column=2)


#button111 = Button(root, image=Props.Apps.CommingSoon.icon , cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=lambda: start(CommingSoon)).grid(row=2, column=0)
#button222 = Button(root, image=Props.Apps.CommingSoon.icon , cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=lambda: start(CommingSoon)).grid(row=2, column=1)
#button333 = Button(root, image=Props.Apps.CommingSoon.icon , cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=lambda: start(CommingSoon)).grid(row=2, column=2)

#shutdown = Button(root, image=Props.Apps.CommingSoon.icon , cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=lambda: start(CommingSoon)).grid(row=2, column=2)
root.mainloop()





