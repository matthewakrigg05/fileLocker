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
        subprocess.call("TASKKILL /F /IM " + apps, shell=True)

    time.sleep(5)


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

            if toContinue:
                timeToLock = timeGiven.get()
                top = Toplevel(root)
                top.geometry("150x150")
                top.title("FileLocker: Blocking Apps")
                top.resizable(False, False)

                if apps.get() == 1 and websites.get() == 1:
                    blockWebsites(checkFiles.lockedDomainsContent())

                    while timeToLock:
                        closeAppIfDetected(checkFiles.lockedAppsContent())
                        mins, secs = divmod(timeGiven, 60)
                        timer = '{:02d}:{:02d}'.format(mins, secs)
                        Label(top, text=timer + "\r")
                        time.sleep(1)
                        timeGiven -= 1

                    unblockWebsites()

                elif apps.get() == 1 and websites.get() == 0:

                    while timeToLock:
                        closeAppIfDetected(checkFiles.lockedAppsContent())
                        mins, secs = divmod(timeGiven, 60)
                        timer = '{:02d}:{:02d}'.format(mins, secs)
                        Label(top, text=timer + "\r")
                        time.sleep(1)
                        timeGiven -= 1

                elif websites.get() == 1 and apps.get() == 0:
                    blockWebsites(checkFiles.lockedDomainsContent())

                    while timeToLock:
                        mins, secs = divmod(timeGiven, 60)
                        timer = '{:02d}:{:02d}'.format(mins, secs)
                        Label(top, text=timer + "\r")
                        time.sleep(1)
                        timeGiven -= 1

                    unblockWebsites()
        else:
            tkinter.messagebox.showinfo("Error", "Invalid time input!")
