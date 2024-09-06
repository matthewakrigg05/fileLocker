import time
from functools import partial
from tkinter import *
from tkinter import ttk
import checkFiles
from block import runBlock
from checkFiles import allLockedContent
from manipulateList import addToList, removeItem


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

    content = checkFiles.allLockedContent()
    if len(content) == 0:
        label = Label(top, text="You currently have no applications in your list.")
        label.pack(pady=5, side=TOP, anchor=NW)
    else:
        label = Label(top,
                      text=("Currently your lists contain: " + ", ".join(content).replace('\n', '')),
                      wraplength=250,
                      justify=LEFT)
        label.pack(side=TOP,  anchor=CENTER)


def removeItemsPopUpBox(root):
    top = Toplevel(root)
    top.geometry("300x200")
    top.title("FileLocker: Remove Items")
    top.resizable(False, False)

    itemsBox = ttk.Combobox(top, state="readonly", values=allLockedContent())
    itemsBox.pack(side=TOP, anchor=N, pady=30)

    removeButton = Button(top, text="Remove Item", command=partial(removeItem, itemsBox))
    removeButton.pack(side=BOTTOM, anchor=S, pady=50)
