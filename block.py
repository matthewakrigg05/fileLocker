import subprocess
import time
import tkinter.messagebox
from tkinter import *
import checkFiles


def validTimeToBlock(t):
    try:
        int(t)
    except ValueError:
        return False
    else:
        if t == 0:
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
    with open("C:\\Windows\\System32\\drivers\\etc\\hosts", 'w') as file:
        file.close()


def runBlock(root, timeGiven, apps, websites):
    if apps.get() == 0 and websites.get() == 0:
        tkinter.messagebox.showinfo("Error", "No options chosen to block")
    else:
        if validTimeToBlock(timeGiven.get()):
            toContinue = tkinter.messagebox.askyesno("FileLocker", "Are you sure you wish to continue?")
            timeNow = StringVar()

            if toContinue:
                timeToLock = timeGiven.get() * 60
                top = Toplevel(root)
                top.geometry("300x300")
                top.title("FileLocker: Blocking Apps")
                top.resizable(False, False)
                timer = Entry(top, width=10, textvariable=timeNow, justify=CENTER)
                timer.pack(side=TOP, anchor=N)

                if apps.get() == 1 and websites.get() == 1:
                    blockWebsites(checkFiles.lockedDomainsContent())

                    while timeToLock:
                        mins, secs = divmod(timeToLock, 60)
                        timeNow.set('{:02d}:{:02d}'.format(mins, secs))
                        time.sleep(1)
                        top.update()
                        closeAppIfDetected(checkFiles.lockedAppsContent())
                        timeToLock -= 1

                    unblockWebsites()

                elif apps.get() == 1 and websites.get() == 0:

                    while timeToLock:
                        mins, secs = divmod(timeToLock, 60)
                        timeNow.set('{:02d}:{:02d}'.format(mins, secs))
                        time.sleep(1)
                        top.update()
                        closeAppIfDetected(checkFiles.lockedAppsContent())
                        timeToLock -= 1

                elif websites.get() == 1 and apps.get() == 0:
                    blockWebsites(checkFiles.lockedDomainsContent())

                    while timeToLock:
                        mins, secs = divmod(timeToLock, 60)
                        timeNow.set('{:02d}:{:02d}'.format(mins, secs))
                        time.sleep(1)
                        top.update()
                        timeToLock -= 1

                    unblockWebsites()
        else:
             tkinter.messagebox.showinfo("Error", "Invalid time input!")
