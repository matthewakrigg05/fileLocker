from functools import partial
from tkinter import *
from lists import blockingList


class newListFrame(Toplevel):

    def __init__(self, mainFrame):
        super().__init__()
        self.original_frame = mainFrame
        self.geometry("250x125")
        self.title("FileLocker: Add to list")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", lambda arg=self: self.onClose())

        label = Label(self, text="Please type the name of your new file:")
        label.pack(side=TOP, anchor=N)

        fileName = StringVar()
        entry = Entry(self, width=25, textvariable=fileName)
        entry.pack(pady=25, side=TOP)

        button = Button(self, text="Create file!", command=partial(self.handleInput, fileName))
        button.pack(pady=5, side=TOP)

    def onClose(self):
        self.destroy()
        self.original_frame.show()

    def handleInput(self, fileName):
        f = blockingList(fileName.get())
        f.createNewList()
        self.onClose()
