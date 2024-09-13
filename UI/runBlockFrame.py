import time
import tkinter
from tkinter import *
from tkinter import messagebox
from functools import partial
import checkFiles
from UI.UImethods import unblockEarly
from block import blockWebsites, closeAppIfDetected, unblockWebsites


class runBlockFrame(Toplevel):

    def __init__(self, mainFrame, lockTime, blockApps, blockSites):
        Toplevel.__init__(self)
        self.original_frame = mainFrame
        self.geometry("300x300")
        self.title("Blocking Apps...")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", lambda arg=self: self.onClose())

        lockTime = lockTime.get() * 60
        blockApps = blockApps.get()
        blockSites = blockSites.get()

        timeNow = StringVar()
        unlockedEarly = BooleanVar()

        timer = Entry(self, width=10, textvariable=timeNow, justify=CENTER)
        unblockEarlyButton = Button(self, text="Unblock", justify=CENTER,
                                    command=partial(unblockEarly, unlockedEarly))
        timer.pack(side=TOP, anchor=N)
        unblockEarlyButton.pack(side=BOTTOM, anchor=S)

        self.runBlock(lockTime, blockApps, blockSites, unlockedEarly, timeNow)

    def onClose(self):
        with open("C:\\Windows\\System32\\drivers\\etc\\hosts", 'w') as file:
            file.close()
        self.destroy()
        self.original_frame.show()

    def runBlock(self, timeGiven, apps, websites, unlockedEarly, timeNow):
        if websites == 1:
            blockWebsites(checkFiles.lockedDomainsContent())

            if apps == 1:
                while timeGiven > -1:
                    if not unlockedEarly.get():
                        mins, secs = divmod(timeGiven, 60)
                        timeNow.set('{:02d}:{:02d}'.format(mins, secs))
                        time.sleep(1)
                        self.update()
                        closeAppIfDetected(checkFiles.lockedAppsContent())
                        timeGiven -= 1
                    else:
                        self.onClose()
                        break

                if timeGiven == -1:
                    timeNow.set('00:00')
                    tkinter.messagebox.showinfo("Complete!", "Your timer is completed! Good Work!")

            else:
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
            if timeGiven == -1:
                timeNow.set('00:00')
                tkinter.messagebox.showinfo("Complete!", "Your timer is completed! Good Work!")

        else:
            while timeGiven > -1:
                if not unlockedEarly.get():
                    mins, secs = divmod(timeGiven, 60)
                    timeNow.set('{:02d}:{:02d}'.format(mins, secs))
                    time.sleep(1)
                    self.update()
                    closeAppIfDetected(checkFiles.lockedAppsContent())
                    timeGiven -= 1
                else:
                    self.onClose()
                    break

            if timeGiven == -1:
                timeNow.set('00:00')
                tkinter.messagebox.showinfo("Complete!", "Your timer is completed! Good Work!")
