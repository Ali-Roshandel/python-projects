from tkinter import *
import tkinter.messagebox as msg
from tkinter.ttk import Combobox


class CarView:
    def __init__(self):
        win = Tk()
        win.title("Car Information")
        win.geometry("300x250")

        Label(win, text="Name").place(x=20, y=20)
        self.name = StringVar()
        Entry(win, textvariable=self.name).place(x=80, y=20)

        Label(win, text="Color").place(x=20, y=50)
        self.color = StringVar()
        car_cmb = Combobox(win, textvariable=self.color, width=17)
        car_cmb["values"] = ["Red", "Black", "White"]
        car_cmb["state"] = "readonly"
        car_cmb.set("Choose Color...")
        car_cmb.place(x=80, y=50)







        win.mainloop()
