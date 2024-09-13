from functools import partial
from tkinter import *
from manipulateList import addToList


class addToListFrame(Toplevel):

    def __init__(self, mainFrame):
        super().__init__()
        self.original_frame = mainFrame
        self.geometry("250x125")
        self.title("FileLocker: Add to list")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.onClose())

        itemToAdd = StringVar()
        entry = Entry(self, width=25, textvariable=itemToAdd)
        entry.pack(pady=25, side=TOP)

        button = Button(self, text="Add to List!", command=partial(addToList, itemToAdd.get()))
        button.pack(pady=5, side=TOP)

    def onClose(self):
        self.destroy()
        self.original_frame.show()
