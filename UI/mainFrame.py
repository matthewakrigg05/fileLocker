import tkinter
from tkinter import *
from tkinter import messagebox
from functools import partial
from UI import UImethods
from UI.runBlockFrame import runBlockFrame
from block import validTimeToBlock


class FileLocker(object):

    def __init__(self, parent):
        self.root = parent
        self.root.title("File Locker")
        self.root.protocol("WM_DELETE_WINDOW", lambda arg=self.root: self.onClose())
        self.root.geometry("640x360")
        self.root.resizable(False, False)

        self.frame = Frame(parent)

        Label(self.frame, text="File Locker", justify=CENTER).grid(row=0, columnspan=2, sticky=N)

        Label(self.frame, text="Manipulate Lists").grid(row=1, column=0, padx=100)
        Button(self.frame, text="View Items", command=partial(UImethods.viewItemsPopUpBox, self.frame)).grid(row=2,
                                                                                                             column=0,
                                                                                                             pady=3)

        Button(self.frame, text="Add Items to lists", command=partial(UImethods.addToListPopUpBox, self.frame)).grid(
            row=3,
            column=0,
            pady=5)

        Button(self.frame, text="Remove Items from lists",
               command=partial(UImethods.removeItemsPopUpBox, self.frame)).grid(
            row=4, column=0, pady=5)

        Label(self.frame, text="Block Apps and Websites").grid(row=1, column=1, pady=5, padx=100)
        blockApps = IntVar()
        Checkbutton(self.frame, text="Block Apps", variable=blockApps, onvalue=1, offvalue=0).grid(row=2, column=1)

        blockSites = IntVar()
        Checkbutton(self.frame, text="Block Websites", variable=blockSites, onvalue=1, offvalue=0).grid(row=3, column=1)

        Label(self.frame, text="Amount of time you wish to block in minutes:").grid(row=4, column=1)
        lockTime = IntVar()
        timeToLock = (Entry(self.frame, textvariable=lockTime))
        timeToLock.grid(row=5, column=1, pady=2)

        Button(self.frame, text="Block!", command=partial(self.checkInputs, lockTime, blockApps,
                                                          blockSites)).grid(row=6, column=1, pady=50)

        self.frame.pack()

    def hide(self):
        self.root.withdraw()

    def openFrame(self, lockTime, blockApps, blockSites):
        self.hide()
        runBlockFrame(self, lockTime, blockApps, blockSites)

    def onCloseOtherFrame(self, otherFrame):
        otherFrame.destroy()
        self.show()

    def show(self):
        self.root.update()
        self.root.deiconify()

    def onClose(self):
        with open("C:\\Windows\\System32\\drivers\\etc\\hosts", 'w') as file:
            file.close()
        self.root.destroy()

    def checkInputs(self, lockTime, blockApps, blockSites):
        if blockApps.get() == 0 and blockSites.get == 0:
            tkinter.messagebox.showinfo("Error", "No options chosen to block")
        else:
            if validTimeToBlock(lockTime.get()):
                toContinue = tkinter.messagebox.askyesno("FileLocker", "Are you sure you wish to continue?")
                if toContinue:
                    self.openFrame(lockTime, blockApps, blockSites)
            else:
                tkinter.messagebox.showerror("Error", "Invalid time input!")
