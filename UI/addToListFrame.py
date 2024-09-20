import os
from functools import partial
from tkinter import *
from tkinter import ttk
from lists import blockingList


class addToListFrame(Toplevel):

    def __init__(self, mainFrame):
        super().__init__()
        self.original_frame = mainFrame
        self.geometry("250x125")
        self.title("FileLocker: Add to list")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", lambda arg=self: self.onClose())

        itemsBox = ttk.Combobox(self, state="readonly", values=os.listdir("./savedLists"))
        itemsBox.pack(side=TOP, anchor=N)

        itemToAdd = StringVar()
        entry = Entry(self, width=10, textvariable=itemToAdd)
        entry.pack(pady=25, side=TOP)

        button = Button(self, text="Add to List!", command=partial(self.handleInput, itemsBox, itemToAdd))
        button.pack(pady=5, side=TOP)

    def onClose(self):
        self.destroy()
        self.original_frame.show()

    def handleInput(self, file, item):
        f = blockingList(file)
        f.addToList(item, self)
