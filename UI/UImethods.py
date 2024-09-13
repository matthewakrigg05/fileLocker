import tkinter
from tkinter import messagebox


def unblockEarly(unlockedEarly):
    areYouSure = tkinter.messagebox.askyesno("FileLocker",
                                             "Are you sure you want to unlock your chosen apps/sites early?")
    if areYouSure:
        unlockedEarly.set(True)

