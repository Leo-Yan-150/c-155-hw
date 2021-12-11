from tkinter import *
import random
root=Tk()
root.title("Mutidimensional Arrays")

root.geometry("500x500")

cc=""
colours = ["maroon1","lawn green","magenta2","purple1","springgreen2","chocolate1", "deep pink","cyan"]

def c():
    cc = colours[random.randint(0,7)]
    root.configure(background = cc)

btn=Button(root, text="change", command=c)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()

#this code is totoally not scuffed and totally not copied off of byju's future school