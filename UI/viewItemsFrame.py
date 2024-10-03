import os
from tkinter import *
from tkinter import ttk
from lists import blockingList


class viewItemsFrame(Toplevel):

    def __init__(self, mainFrame):
        super().__init__()
        self.original_frame = mainFrame
        self.geometry("250x125")
        self.title("FileLocker: View Items")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", lambda arg=self: self.onClose())

        self.label = Label(self, text="Please select a list that you wish to look at.")
        self.label.pack(side=TOP, anchor=N)

        if len(os.listdir("./savedLists")) == 0:
            self.label = Label(self, text="You currently have no lists.")
            self.label.pack(pady=5, side=TOP, anchor=NW)
        else:
            self.item = StringVar()
            self.combo = ttk.Combobox(self, state="readonly", values=os.listdir("./savedLists"), textvariable=self.item)
            self.combo.bind("<<ComboboxSelected>>", self.onChange)
            self.combo.pack(side=TOP, anchor=N, pady=5)

    def onChange(self, event):
        self.label.pack_forget()
        selection = self.combo.get()
        contentList = blockingList(selection)

        self.label = Label(self,
                           text=("In " + selection + " there is: " + contentList.getListContents()),
                           wraplength=250,
                           justify=LEFT)
        self.label.pack(side=BOTTOM, anchor=CENTER, pady=20)

    def onClose(self):
        self.destroy()
        self.original_frame.show()
