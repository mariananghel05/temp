from tkinter import *
import subprocess

root = Tk()
#root.attributes("-fullscreen", True)
root.title("Astronomie")
root.minsize(1280, 800)
root.maxsize(1280, 800)
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
def stellarium():
    bashCommand = "stellarium -geometry 1280x800"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

def gaiaSky():
    pass
    #bashCommand = "stellarium -geometry 1280x800"
    #process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    #output, error = process.communicate()

def Celestia():
    pass
    #bashCommand = "stellarium -geometry 1280x800"
    #process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    #output, error = process.communicate()

def Cosmonium():
    pass
    #bashCommand = "stellarium -geometry 1280x800"
    #process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    #output, error = process.communicate()

def CommingSoon():
    pass
    #bashCommand = "stellarium -geometry 1280x800"
    #process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    #output, error = process.communicate()

#Apps buttons
stellarium = PhotoImage(file="stellarium.png")
GaiaSky = PhotoImage(file="GaiaSky.png")
Celestia = PhotoImage(file="Celestia.png")
Cosmonium = PhotoImage(file="Cosmonium.png")
CommingSoon = PhotoImage(file="CommingSoon.png")

label = Label(text="stellarium", background="#212133", foreground="#ffffff").grid(row=1, column=1)
button1 = Button(root, image=stellarium, cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=start_stellarium).grid(row=0, column=0)
button2 = Button(root, image=GaiaSky, cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=start_stellarium).grid(row=0, column=1)
button3 = Button(root, image=Celestia, cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=start_stellarium).grid(row=0, column=2)


button11 = Button(root, image=Cosmonium, cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=start_stellarium).grid(row=1, column=0)
button22 = Button(root, image=CommingSoon, cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=start_stellarium).grid(row=1, column=1)
button33 = Button(root, image=CommingSoon, cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=start_stellarium).grid(row=1, column=2)


button111 = Button(root, image=CommingSoon, cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=start_stellarium).grid(row=2, column=0)
button222 = Button(root, image=CommingSoon, cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=start_stellarium).grid(row=2, column=1)
button333 = Button(root, image=CommingSoon, cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=start_stellarium).grid(row=2, column=2)

shutdown = Button(root, image=CommingSoon, cursor="circle", background="#212133", activebackground="#212144",width=350, height=200, borderwidth=5, command=start_stellarium).grid(row=2, column=2)
root.mainloop()
