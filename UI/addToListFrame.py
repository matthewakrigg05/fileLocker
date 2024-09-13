from functools import partial
from tkinter import *

from manipulateList import addToList


class addToListFrame(Toplevel):

    def __init__(self, mainFrame):
        super().__init__()
        self.original_frame = mainFrame
        self.geometry("250x125")
        self.title("FileLocker: Add to list")

        itemToAdd = StringVar()
        entry = Entry(self, width=25, textvariable=itemToAdd)
        entry.pack(pady=25, side=TOP)

        button = Button(self, text="Add to List!", command=partial(addToList, itemToAdd.get()))
        button.pack(pady=5, side=TOP)
