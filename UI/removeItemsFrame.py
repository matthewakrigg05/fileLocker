from functools import partial
from tkinter import *
from tkinter import ttk

from checkFiles import allLockedContent
from manipulateList import removeItem


class removeItemsFrame(Toplevel):

    def __init__(self, mainFrame):

        super().__init__()
        self.original_frame = mainFrame
        self.geometry("300x200")
        self.title("FileLocker: Remove Items")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", lambda arg=self: self.onClose())

        itemsBox = ttk.Combobox(self, state="readonly", values=allLockedContent())
        itemsBox.pack(side=TOP, anchor=N, pady=30)

        removeButton = Button(self, text="Remove Item", command=partial(removeItem, itemsBox))
        removeButton.pack(side=BOTTOM, anchor=S, pady=50)

    def onClose(self):
        self.destroy()
        self.original_frame.show()