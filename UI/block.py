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
    with open("C:\\Windows\\System32\\drivers\\etc\\hosts", 'w') as file:
        file.close()


def unblockEarly(top, unlockedEarly):
    areYouSure = tkinter.messagebox.askyesno("FileLocker", "Are you sure you want to unlock your chosen apps/sites early?")
    if areYouSure:
        unlockedEarly = True
        unblockWebsites()
        top.destroy()
    else:
        unlockedEarly = False
