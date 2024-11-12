import os
def clean():
    os.system('cls')
clean()

import tkinter as tk
from tkinter import ttk

from tkinter import *

root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)


def go_home():
    frame2.pack_forget()
    frame1.pack()


def go_second():
    frame1.pack_forget()
    frame2.pack()


root.title("páginas")

btn_page2 = Button(frame1, text="Página 2", command=go_second)
btn_page2.pack()

btn_home = Button(frame2, text="inicial", command=go_home)
btn_home.pack()

frame1.pack()

root.mainloop()