from tkinter import *
import tkinter.messagebox
import checkFiles
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
    top.title("FileLocker: Add to list")

    itemToAdd = StringVar(root)
    entry = Entry(top, width=25, textvariable=itemToAdd)
    entry.pack(pady=25, side=TOP)

    button = Button(top, text="Add to List!", command=lambda: [close_win(top), addToList(itemToAdd.get())])
    button.pack(pady=5, side=TOP)


def viewItemsPopUpBox(root):
    top = Toplevel(root)
    top.geometry("250x125")
    top.title("FileLocker: View Items")
    top.resizable(False, False)

    content = checkFiles.lockedContent()
    if len(content) == 0:
        label = Label(top, text="You currently have no applications in your list.")
        label.pack(pady=5, side=TOP, anchor=NW)
    else:
        label = Label(top,
                      text=("Currently your list contains: " + ", ".join(content).replace('\n', '')),
                      wraplength=250,
                      justify=LEFT)
        label.pack(side=TOP,  anchor=NW)
