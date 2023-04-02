from tkinter import *
import subprocess

root = Tk()
root.attributes("-fullscreen", True)
root.title("Astronomie")
root.minsize(1280, 800)
root.maxsize(1280, 800)
root.config(background="#212133",cursor="circle")


# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

def start_stellarium():
    bashCommand = "stellarium -geometry 1280x800"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()


logo = PhotoImage(file="stellarium.png")
label = Label(text="stellarium", background="#212133", foreground="#ffffff").grid(row=1, column=1)
button1 = Button(root, image=logo, cursor="circle", background="#212133", activebackground="#212144",width=500, height=250, borderwidth=5, command=start_stellarium).grid(row=1, column=1)
root.mainloop()
