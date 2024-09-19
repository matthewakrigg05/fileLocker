import os
from functools import partial
from tkinter import *
from tkinter import ttk
from lists import blockingList


class removeItemsFrame(Toplevel):

    def __init__(self, mainFrame):

        super().__init__()
        self.original_frame = mainFrame
        self.geometry("300x200")
        self.title("FileLocker: Remove Items")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", lambda arg=self: self.onClose())

        itemsBox = ttk.Combobox(self, state="readonly", values=os.listdir("./textFiles"))
        itemsBox.pack(side=TOP, anchor=N)

        itemToRemove = StringVar()
        entry = Entry(self, width=10, textvariable=itemToRemove)
        entry.pack(pady=25, side=TOP)

        removeButton = Button(self, text="Remove Item", command=partial(self.handleRemoveInput, itemsBox, itemToRemove))
        removeButton.pack(side=BOTTOM, anchor=S, pady=50)

    def onClose(self):
        self.destroy()
        self.original_frame.show()

    def handleRemoveInput(self, file, itemToRemove):
        f = blockingList(file.get())
        f.removeFromList(itemToRemove.get(), self)

