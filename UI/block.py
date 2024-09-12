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


def runBlock(root, timeGiven, apps, websites):
    if apps.get() == 0 and websites.get() == 0:
        tkinter.messagebox.showinfo("Error", "No options chosen to block")
    else:
        if validTimeToBlock(timeGiven.get()):
            toContinue = tkinter.messagebox.askyesno("FileLocker", "Are you sure you wish to continue?")

            if toContinue:
                timeNow = StringVar()
                unlockedEarly = False
                timeToLock = timeGiven.get() * 60

                top = Toplevel(root)
                top.geometry("300x300")
                top.title("Blocking Apps...")
                top.resizable(False, False)
                timer = Entry(top, width=10, textvariable=timeNow, justify=CENTER)
                unblockEarlyButton = Button(top, text="Unblock", justify=CENTER, command=partial(unblockEarly, top, unlockedEarly))
                timer.pack(side=TOP, anchor=N)
                unblockEarlyButton.pack(side=BOTTOM, anchor=S)

                if websites.get() == 1:
                    blockWebsites(checkFiles.lockedDomainsContent())

                    if apps.get() == 1:
                        while timeToLock > -1:
                            if not unlockedEarly:
                                mins, secs = divmod(timeToLock, 60)
                                timeNow.set('{:02d}:{:02d}'.format(mins, secs))
                                time.sleep(1)
                                top.update()
                                closeAppIfDetected(checkFiles.lockedAppsContent())
                                timeToLock -= 1
                            else:
                                break
                    else:
                        while timeToLock > -1:
                            if not unlockedEarly:
                                mins, secs = divmod(timeToLock, 60)
                                timeNow.set('{:02d}:{:02d}'.format(mins, secs))
                                time.sleep(1)
                                top.update()
                                timeToLock -= 1
                            else:
                                break

                    unblockWebsites()

                else:
                    while timeToLock > -1:
                        if not unlockedEarly:
                            mins, secs = divmod(timeToLock, 60)
                            timeNow.set('{:02d}:{:02d}'.format(mins, secs))
                            time.sleep(1)
                            top.update()
                            closeAppIfDetected(checkFiles.lockedAppsContent())
                            timeToLock -= 1
                        else:
                            break

                timeNow.set('00:00')
                tkinter.messagebox.showinfo("Complete!", "Your timer is completed! Good Work!")

        else:
            tkinter.messagebox.showerror("Error", "Invalid time input!")
