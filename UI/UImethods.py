import tkinter
from functools import partial
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import checkFiles
from checkFiles import allLockedContent
from manipulateList import addToList, removeItem


def unblockEarly(unlockedEarly):
    areYouSure = tkinter.messagebox.askyesno("FileLocker",
                                             "Are you sure you want to unlock your chosen apps/sites early?")
    if areYouSure:
        unlockedEarly.set(True)


def removeItemsPopUpBox(root):
    top = Toplevel(root)
    top.geometry("300x200")
    top.title("FileLocker: Remove Items")
    top.resizable(False, False)

    itemsBox = ttk.Combobox(top, state="readonly", values=allLockedContent())
    itemsBox.pack(side=TOP, anchor=N, pady=30)

    removeButton = Button(top, text="Remove Item", command=partial(removeItem, itemsBox))
    removeButton.pack(side=BOTTOM, anchor=S, pady=50)
