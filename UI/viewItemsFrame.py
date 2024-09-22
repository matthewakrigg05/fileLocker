import os
from tkinter import *

from lists import blockingList


class viewItemsFrame(Toplevel):

    def __init__(self, mainFrame):
        super().__init__()
        self.original_frame = mainFrame
        self.geometry("250x125")
        self.title("FileLocker: View Items")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", lambda arg=self: self.onClose())

        if len(os.listdir("./savedLists")) == 0:
            label = Label(self, text="You currently have no lists.")
            label.pack(pady=5, side=TOP, anchor=NW)
        else:
            for file in os.listdir("./savedLists"):
                l = blockingList(file)

                label = Label(self,
                              text=("In " + file + " there is: " + l.getListContents()),
                              wraplength=250,
                              justify=LEFT)
                label.pack(side=TOP, anchor=W)

    def onClose(self):
        self.destroy()
        self.original_frame.show()
