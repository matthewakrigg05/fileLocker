import os
from functools import partial
from tkinter import *
from tkinter import ttk
from manipulateList import addToList


class addToListFrame(Toplevel):

    def __init__(self, mainFrame):
        super().__init__()
        self.original_frame = mainFrame
        self.geometry("250x125")
        self.title("FileLocker: Add to list")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", lambda arg=self: self.onClose())

        itemsBox = ttk.Combobox(self, state="readonly", values=os.listdir("./textFiles"))
        itemsBox.pack(side=TOP, anchor=N, pady=30)

        itemToAdd = StringVar()
        entry = Entry(self, width=25, textvariable=itemToAdd)
        entry.pack(pady=25, side=TOP)

        button = Button(self, text="Add to List!", command=partial(addToList, itemToAdd))
        button.pack(pady=5, side=TOP)

    def onClose(self):
        self.destroy()
        self.original_frame.show()
