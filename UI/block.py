import subprocess
import time
import tkinter.messagebox
from functools import partial
from tkinter import *
import checkFiles


def validTimeToBlock(t):
    try:
        int(t)
    except ValueError:
        return False
    else:
        if t <= 0:
            return False
        else:
            return True


def closeAppIfDetected(appsToClose):
    for apps in appsToClose:
        if apps in str(subprocess.check_output('tasklist')):
            subprocess.call("TASKKILL /F /IM " + apps, shell=True)


def blockWebsites(websitesToBlock):
    for website in websitesToBlock:
        with open("C:\\Windows\\System32\\drivers\\etc\\hosts", 'w') as file:
            file.write("127.0.0.1" + " " + website + " www." + website)


def unblockWebsites():
    with open("C:\\Windows\\System32\\drt  ivers\\etc\\hosts", 'w') as file:
        file.close()


def unblockEarly(top):
    unblockWebsites()
    top.destroy()


def runBlock(root, timeGiven, apps, websites):
    if apps.get() == 0 and websites.get() == 0:
        tkinter.messagebox.showinfo("Error", "No options chosen to block")
    else:
        if validTimeToBlock(timeGiven.get()):
            toContinue = tkinter.messagebox.askyesno("FileLocker", "Are you sure you wish to continue?")
            timeNow = StringVar()
            unlockedEarly = False

            if toContinue:
                timeToLock = timeGiven.get() * 60
                top = Toplevel(root)
                top.geometry("300x300")
                top.title("FileLocker: Blocking Apps")
                top.resizable(False, False)
                timer = Entry(top, width=10, textvariable=timeNow, justify=CENTER)
                unblockEarlyButton = Button(top, text="Unblock", justify=CENTER, command=partial(unblockEarly, top))
                timer.pack(side=TOP, anchor=N)

                if apps.get() == 1 and websites.get() == 1:
                    blockWebsites(checkFiles.lockedDomainsContent())

                    while timeToLock > 0:
                        mins, secs = divmod(timeToLock, 60)
                        timeNow.set('{:02d}:{:02d}'.format(mins, secs))
                        time.sleep(1)
                        top.update()
                        closeAppIfDetected(checkFiles.lockedAppsContent())
                        timeToLock -= 1

                    time.sleep(1)
                    timeNow.set('00:00')
                    unblockWebsites()

                elif apps.get() == 1 and websites.get() == 0:

                    while timeToLock > 0:
                        mins, secs = divmod(timeToLock, 60)
                        timeNow.set('{:02d}:{:02d}'.format(mins, secs))
                        time.sleep(1)
                        top.update()
                        closeAppIfDetected(checkFiles.lockedAppsContent())
                        timeToLock -= 1

                    time.sleep(1)
                    timeNow.set('00:00')

                elif websites.get() == 1 and apps.get() == 0:
                    blockWebsites(checkFiles.lockedDomainsContent())

                    while timeToLock > 0:
                        mins, secs = divmod(timeToLock, 60)
                        timeNow.set('{:02d}:{:02d}'.format(mins, secs))
                        time.sleep(1)
                        top.update()
                        timeToLock -= 1

                    time.sleep(1)
                    timeNow.set('00:00')
                    unblockWebsites()
        else:
            tkinter.messagebox.showerror("Error", "Invalid time input!")
