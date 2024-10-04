import os
from functools import partial
from tkinter import *
from tkinter import ttk
from lists import blockingList


class addToListFrame(Toplevel):

    def __init__(self, mainFrame):
        super().__init__()
        self.original_frame = mainFrame
        self.geometry("300x150")
        self.title("FileLocker: Add to list")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", lambda arg=self: self.onClose())

        prompt = Label(self, text="Please select a list that you would like to add to:", justify=CENTER, wraplength=250)
        prompt.pack(side=TOP, anchor=N)

        itemsBox = ttk.Combobox(self, state="readonly", values=os.listdir("./savedLists"))
        itemsBox.pack(side=TOP, anchor=N)

        itemPrompt = Label(self, text="Please type the name of the app/site that you wish to block:", justify=CENTER,
                           wraplength=250)
        itemPrompt.pack(side=TOP, anchor=N)

        itemToAdd = StringVar()
        entry = Entry(self, width=10, textvariable=itemToAdd)
        entry.pack(pady=5, side=TOP)

        button = Button(self, text="Add to List!", command=partial(self.handleInput, itemsBox, itemToAdd))
        button.pack(pady=5, side=TOP)

    def onClose(self):
        self.destroy()
        self.original_frame.show()

    def handleInput(self, file, item):
        f = blockingList(file)
        f.addToList(item, self)
