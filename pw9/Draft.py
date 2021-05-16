import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import os

window = tk.Tk()
window.title("Student management system .grid()")
canvas = tk.Canvas(window,height=700, width=700, bg="#263D42").grid()
frame=tk.Frame(window, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

#tk.Frame(window,width=750,height=550, bg="green").grid()
# sub = tk.Toplevel(window)
# sub.title("Students ")
# sub.geometry("600x400")



#tk.Label(window, text="Username").grid(column=0, row=0, sticky=tk.EW, padx=3, pady=3)
#tk.Label(window, text="Password").grid(column=0, row=1, sticky=tk.EW, padx=3, pady=3)
#tk.Entry(window, width=20).grid(column=1, row=0,  sticky =tk.EW,pady =2)
#tk.Entry(window, width=20).grid(column=1, row=1,  sticky =tk.EW,pady =2)
openFile=tk.Button(window, text="Make your choice!").grid(column=1, row=3, sticky=tk.EW, padx=3, pady=3)
# default window

# tk.Frame(window, width=50,height=50,bg="green").pack()
# tk.Frame(window, width=25,height=25,bg="blue").pack()

# secondary window with fill
#
# tk.Frame(sub, width=100,height=100,bg="red").pack(fill=tk.X)
# tk.Frame(sub, width=50,height=50,bg="green").pack(fill=tk.X)

window.mainloop()
