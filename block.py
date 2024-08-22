import subprocess
import time

import checkFiles


def timeToBlock(givenTime):
    while not givenTime.isnumeric():
        try:
            if givenTime.isnumeric():
                timeToBlock = time.time() + givenTime
                continue
        except ValueError:
            givenTime = (input("Please enter an integer value as your length of time.\n"))

    return timeToBlock


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

        elif not apps and websites:
            blockWebsites(checkFiles.lockedDomainsContent())
            time.sleep(timeGiven)
            unblockWebsites()

        else:
            return "No options selected"
