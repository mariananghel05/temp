from types import SimpleNamespace
from tkinter import *
import subprocess
import os
import sys

#Variables definition
root = Tk()

Props = SimpleNamespace(
    Background = PhotoImage(file="Bg.png"),
    Resolution = SimpleNamespace(x=1920, y=1080),
    Output = "HDMI-2",
    Apps = SimpleNamespace(
        Stellarium = SimpleNamespace(
            icon = PhotoImage(file="stellarium.png")
            ),
        GaiaSky = SimpleNamespace(
            icon = PhotoImage(file="GaiaSky.png")
            ),
        Celestia = SimpleNamespace(
            icon = PhotoImage(file="Celestia.png"),
            Resolution = SimpleNamespace(x=1152, y=864)
            ),
        Cosmonium = SimpleNamespace(
            icon = PhotoImage(file="Cosmonium.png")
            ),
        CommingSoon = SimpleNamespace(
            icon = PhotoImage(file="CommingSoon.png")
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
    os.system("stellarium -geometry {}x{}".format(Props.resolution.x, Props.resolution.y))

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




button1 = Button(root, image=Props.Apps.Stellarium.icon, cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=lambda: start(Stellarium)).grid(row=0, column=0)
button2 = Button(root, image=Props.Apps.GaiaSky.icon, cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=lambda: start(GaiaSky)).grid(row=0, column=1)
button3 = Button(root, image=Props.Apps.Celestia.icon, cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=lambda: start(Celestia)).grid(row=0, column=2)


button11 = Button(root, image=Props.Apps.Cosmonium.icon , cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=lambda: start(Cosmonium)).grid(row=1, column=0)
button22 = Button(root, image=Props.Apps.CommingSoon.icon , cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=lambda: start(CommingSoon)).grid(row=1, column=1)
#button33 = Button(root, image=Props.Apps.CommingSoon.icon , cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=CommingSoon).grid(row=1, column=2)


#button111 = Button(root, image=Props.Apps.CommingSoon.icon , cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=lambda: start(CommingSoon)).grid(row=2, column=0)
#button222 = Button(root, image=Props.Apps.CommingSoon.icon , cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=lambda: start(CommingSoon)).grid(row=2, column=1)
#button333 = Button(root, image=Props.Apps.CommingSoon.icon , cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=lambda: start(CommingSoon)).grid(row=2, column=2)

#shutdown = Button(root, image=Props.Apps.CommingSoon.icon , cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=lambda: start(CommingSoon)).grid(row=2, column=2)
root.mainloop()





