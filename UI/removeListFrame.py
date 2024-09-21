import os
from functools import partial
from tkinter import *
from tkinter import ttk
from lists import blockingList


class removeListFrame(Toplevel):

    def __init__(self, mainFrame):

        super().__init__()
        self.original_frame = mainFrame
        self.geometry("300x200")
        self.title("FileLocker: Remove Items")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", lambda arg=self: self.onClose())

        itemsBox = ttk.Combobox(self, state="readonly", values=os.listdir("./savedLists"))
        itemsBox.pack(side=TOP, anchor=N)

        removeButton = Button(self, text="Remove List", command=partial(self.handleRemoveInput, itemsBox))
        removeButton.pack(side=BOTTOM, anchor=S, pady=50)

    def onClose(self):
        self.destroy()
        self.original_frame.show()

    def handleRemoveInput(self, file):
        f = blockingList(file.get()[:-4])
        f.removeList()
        self.onClose()
