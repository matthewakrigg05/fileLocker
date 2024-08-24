from tkinter import *

from manipulateList import addToList


def onClose(root):
    with open("C:\\Windows\\System32\\drivers\\etc\\hosts", 'w') as file:
        file.close()
    root.destroy()


def close_win(top):
    top.destroy()


def addToListPopUpBox(root):
    top = Toplevel(root)
    top.geometry("250x125")
    top.title("File locker: Add to list")

    itemToAdd = StringVar(root)
    entry = Entry(top, width=25, textvariable=itemToAdd)
    entry.pack(pady=25, side=TOP)

    button = Button(top, text="Add to List!", command=lambda: [close_win(top), addToList(itemToAdd.get())])
    button.pack(pady=5, side=TOP)
