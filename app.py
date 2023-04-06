from types import SimpleNamespace
from tkinter import *
import subprocess
import os
import sys

App = SimpleNamespace(
    resolution = SimpleNamespace(x=1920, y=1080),

    )

root = Tk()
root.attributes("-fullscreen", True)
root.title("Astronomie")
root.minsize(App.resolution.x, App.resolution.y)
root.maxsize(App.resolution.x, App.resolution.y)

Bg = PhotoImage(file="Bg.png")
root.config(background="#212133",cursor="circle")

limg= Label(root, i=Bg).grid(rowspan=3, columnspan=3)

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)


#Apps functions
def start(method):
    root.withdraw()
    method()
    root.deiconify()
def stellarium_app():
    os.system("stellarium -geometry " + App.resolution.x +"x" + App.resolution.y)

def gaiaSky_app():
    os.system("gaiasky")

def Celestia_app():
    root.withdraw()
    os.system("xrandr --output HDMI-2")
    os.system("celestia")
    root.deiconify()

def Cosmonium_app():
    os.system("xterm -geometry " + App.resolution.x +"x" + App.resolution.y)

def CommingSoon_app():
    pass

#Apps buttons
stellarium = PhotoImage(file="stellarium.png")
GaiaSky = PhotoImage(file="GaiaSky.png")
Celestia = PhotoImage(file="Celestia.png")
Cosmonium = PhotoImage(file="Cosmonium.png")
CommingSoon = PhotoImage(file="CommingSoon.png")


button1 = Button(root, image=stellarium, cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=lambda: start(stellarium_app)).grid(row=0, column=0)
button2 = Button(root, image=GaiaSky, cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=lambda: start(gaiaSky_app)).grid(row=0, column=1)
button3 = Button(root, image=Celestia, cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=lambda: start(Celestia_app)).grid(row=0, column=2)


button11 = Button(root, image=Cosmonium, cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=lambda: start(Cosmonium_app)).grid(row=1, column=0)
#button22 = Button(root, image=CommingSoon, cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=lambda: start(CommingSoon_app)).grid(row=1, column=1)
#button33 = Button(root, image=CommingSoon, cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=CommingSoon_app).grid(row=1, column=2)


#button111 = Button(root, image=CommingSoon, cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=lambda: start(CommingSoon_app)).grid(row=2, column=0)
#button222 = Button(root, image=CommingSoon, cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=lambda: start(CommingSoon_app)).grid(row=2, column=1)
#button333 = Button(root, image=CommingSoon, cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=lambda: start(CommingSoon_app)).grid(row=2, column=2)

#shutdown = Button(root, image=CommingSoon, cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=lambda: start(CommingSoon_app)).grid(row=2, column=2)
root.mainloop()





