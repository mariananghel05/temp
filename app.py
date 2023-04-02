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
    bashCommand = "opera -e https://www.google.com/search?q=stellarium&sxsrf=APwXEdfSW8Ztg_qaoa3f2csBX-5nCYqXnQ%3A1680445890485&ei=wpEpZIyfHZCN9u8P3fWb8Ag&ved=0ahUKEwiMiPfitIv-AhWQhv0HHd36Bo4Q4dUDCA8&uact=5&oq=stellarium&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECCMQJzIICAAQgAQQywEyCAgAEIAEEMsBMggIABCABBDLATIICAAQgAQQywEyCAgAEIAEEMsBMggIABCABBDLATIFCAAQgAQyBQgAEIAEMgUIABCABDoLCAAQgAQQsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOgsILhCABBCxAxCDAToLCC4QigUQsQMQgwE6BggjECcQEzoHCC4QigUQQzoNCC4QigUQxwEQ0QMQQzoECAAQAzoTCC4QigUQsQMQgwEQxwEQ0QMQQzoICAAQgAQQsQM6CAguEIAEELEDOg4ILhCKBRCxAxCDARDUAjoNCC4QigUQsQMQgwEQQzoHCAAQigUQQzoFCC4QgAQ6CAguEIAEEMsBOg4ILhCABBDHARCvARDLAUoECEEYAFAAWLQRYIATaABwAXgAgAGaAYgBxQiSAQM0LjaYAQCgAQHAAQE&sclient=gws-wiz-serp"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()


logo = PhotoImage(file="stellarium.png")
label = Label(text="stellarium", background="#212133", foreground="#ffffff").grid(row=1, column=1)
button1 = Button(root, image=logo, cursor="circle", background="#212133", activebackground="#212144",width=500, height=250, borderwidth=5, command=start_stellarium).grid(row=1, column=1)
root.mainloop()
