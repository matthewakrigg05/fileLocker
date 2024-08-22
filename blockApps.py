import subprocess
import time


def timeToBlock(timeToLock):

    while not timeToLock.isnumeric():
        try:
            if timeToLock.isnumeric():
                timeToBlock = time.time() + timeToLock
                continue
        except ValueError:
            timeToLock = (input("Please enter an integer value as your length of time.\n"))

    return timeToBlock


def closeAppIfDetected(appsToClose, timeToLock):
    while time.time() < timeToLock:
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
