import tkinter as tk
from tkinter import filedialog, Text
from tkinter.ttk import *
import os

window = tk.Tk()
window.title("Student management system ")
files = []

def addFile():

    for widget in frame.winfo_children():
        widget.destroy()

    fileName=filedialog.askopenfilename(initialdir="/", title = "Select File", filetypes = (("executables","*.py"),("all file", "*.*")))
    files.append(fileName)
    print(fileName)

    for file in files:
        label=tk.Label(frame, text=file, bg ="gray")
        label.pack()

def runFile():
    for file in files:
        os.startfile(file)

canvas = tk.Canvas(window,height=700, width=700, bg="#263D42")
canvas.pack()

frame=tk.Frame(window, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

fileOpen=tk.Button(window, text="Choose files end with .py",padx=10, pady=5, fg="white", bg="#263D42" ,command = addFile)
fileOpen.pack()

fileOpen=tk.Button(window, text="Execuse File",padx=10, pady=5, fg="white", bg="#263D42", command = runFile)
fileOpen.pack()



window.mainloop()
