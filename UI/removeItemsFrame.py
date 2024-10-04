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

        listPromt = Label(self, text="Please select a list that you wish to remove from:")
        listPromt.pack(side=TOP, anchor=N)

        itemsBox = ttk.Combobox(self, state="readonly", values=os.listdir("./savedLists"))
        itemsBox.pack(side=TOP, anchor=N)

        itemPrompt = Label(self, text="Then type the name of the item from that list that you wish to remove:",
                           justify=CENTER, wraplength=280)
        itemPrompt.pack(side=TOP, anchor=N)

        itemToRemove = StringVar()
        entry = Entry(self, width=20, textvariable=itemToRemove)
        entry.pack(pady=25, side=TOP)

        removeButton = Button(self, text="Remove Item", command=partial(self.handleRemoveInput, itemsBox, itemToRemove))
        removeButton.pack(side=BOTTOM, anchor=S, pady=15)

    def onClose(self):
        self.destroy()
        self.original_frame.show()

    def handleRemoveInput(self, file, itemToRemove):
        f = blockingList(file.get())
        f.removeFromList(itemToRemove.get(), self)

