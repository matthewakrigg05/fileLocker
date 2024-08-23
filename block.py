import subprocess
import time
import tkinter.messagebox
import checkFiles


def validTimeToBlock(t):
    try:
        if t.isnumeric():
            return True
    except ValueError:
        return False


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


def runBlock(timeGiven, apps, websites):
    if validTimeToBlock(timeGiven):
        toContinue = input("Are you sure you wish to continue? (Y/N)")
        if toContinue == "Y" or toContinue == "y":
            timeToLock = time.time() + timeGiven

            if apps and websites:
                blockWebsites(checkFiles.lockedDomainsContent())

                while time.time() < time:
                    closeAppIfDetected(checkFiles.lockedAppsContent())

                unblockWebsites()

            elif apps and not websites:
                while time.time() < timeToLock:
                    closeAppIfDetected(checkFiles.lockedAppsContent())

            elif websites and not apps:
                blockWebsites(checkFiles.lockedDomainsContent())
                time.sleep(timeGiven)
                unblockWebsites()

            else:
                return "No options selected"
    else:
        tkinter.messagebox.showinfo("Error", "Invalid time input!")
