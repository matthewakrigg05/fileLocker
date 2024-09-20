import time
import tkinter
from tkinter import *
from tkinter import messagebox
from functools import partial
from UI.UImethods import unblockEarly
from block import blockWebsites, closeAppIfDetected, unblockWebsites


class runBlockFrame(Toplevel):

    def __init__(self, mainFrame, lockTime, toBlock):
        super().__init__()
        self.original_frame = mainFrame
        self.geometry("300x150")
        self.title("Blocking Apps...")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", lambda arg=self: self.onClose())

        lockTime = lockTime.get() * 60
        toBlock = toBlock.get()
        timeNow = StringVar()
        unlockedEarly = BooleanVar()

        timer = Entry(self, width=10, textvariable=timeNow, justify=CENTER)
        timer.pack(side=TOP, anchor=N, pady=20)

        unblockEarlyButton = Button(self, text="Unblock", justify=CENTER,
                                    command=partial(unblockEarly, unlockedEarly))
        unblockEarlyButton.pack(side=BOTTOM, anchor=S, pady=20)

        self.runBlock(lockTime, toBlock, unlockedEarly, timeNow)

    def onClose(self):
        with open("C:\\Windows\\System32\\drivers\\etc\\hosts", 'w') as file:
            file.close()
        self.destroy()
        self.original_frame.show()

    def runBlock(self, timeGiven, toBlock, unlockedEarly, timeNow):
        toBlock = "savedLists/" + toBlock
        apps = []
        sites = []

        with open(toBlock, "r") as file:
            lines = file.readlines()

            for line in lines:
                if ".exe" in line:
                    apps.append(line)
                else:
                    sites.append(line)

        if len(sites) != 0 and len(apps) != 0:
            blockWebsites(sites)
            while timeGiven > -1:
                if not unlockedEarly.get():
                    mins, secs = divmod(timeGiven, 60)
                    timeNow.set('{:02d}:{:02d}'.format(mins, secs))
                    time.sleep(1)
                    self.update()
                    closeAppIfDetected(apps)
                    timeGiven -= 1
                else:
                    self.onClose()
                    break
            unblockWebsites()

        elif len(sites) != 0 and len(apps) == 0:
            blockWebsites(sites)
            while timeGiven > -1:
                if not unlockedEarly.get():
                    mins, secs = divmod(timeGiven, 60)
                    timeNow.set('{:02d}:{:02d}'.format(mins, secs))
                    time.sleep(1)
                    self.update()
                    timeGiven -= 1
                else:
                    self.onClose()
                    break
            unblockWebsites()

        else:
            while timeGiven > -1:
                if not unlockedEarly.get():
                    mins, secs = divmod(timeGiven, 60)
                    timeNow.set('{:02d}:{:02d}'.format(mins, secs))
                    time.sleep(1)
                    self.update()
                    closeAppIfDetected(apps)
                    timeGiven -= 1
                else:
                    self.onClose()
                    break

        if timeGiven == -1:
            timeNow.set('00:00')
            tkinter.messagebox.showinfo("Complete!", "Your timer is completed! Good Work!")

        self.destroy()
        self.original_frame.show()
