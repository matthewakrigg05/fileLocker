import subprocess
import time


def timeToBlock():
    timeToLock = input("How long would you like to block your chosen apps for (in minutes)\n")

    while not timeToLock.isnumeric():
        try:
            if timeToLock.isnumeric():
                continue
            else:
                timeToLock = input("Please enter an integer value as your length of time.\n")
        except ValueError:
            timeToLock = (input("Please enter an integer value as your length of time.\n"))

    return int(timeToLock) * 60


def closeAppIfDetected(appsToClose):

    for apps in appsToClose:
        subprocess.call("TASKKILL /F /IM " + apps, shell=True)

    time.sleep(5)
