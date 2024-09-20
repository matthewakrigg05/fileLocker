import os
import tkinter
from tkinter import messagebox


def createNewList(fileName):
    if not os.path.exists("savedLists/" + fileName):
        f = open("savedLists/" + fileName)
        f.close()
    else:
        tkinter.messagebox.showinfo("Error", "This file already exists!")
