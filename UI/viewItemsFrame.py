import checkFiles
from tkinter import *


class viewItemsFrame(Toplevel):

    def __init__(self, mainFrame):
        super().__init__()
        self.original_frame = mainFrame
        self.geometry("250x125")
        self.title("FileLocker: View Items")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", lambda arg=self: self.onClose())

        if len(checkFiles.allLockedContent()) == 0:
            label = Label(self, text="You currently have no applications in your list.")
            label.pack(pady=5, side=TOP, anchor=NW)
        else:
            label = Label(self,
                          text=("Currently your lists contain: " + ", ".join(checkFiles.allLockedContent()).replace('\n', '')),
                          wraplength=250,
                          justify=LEFT)
            label.pack(side=TOP, anchor=CENTER)

    def onClose(self):
        self.destroy()
        self.original_frame.show()
