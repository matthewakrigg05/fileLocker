import os
import subprocess


def timeToBlock():
    timeToLock = input("How long would you like to block your chosen apps for (in seconds)\n")

    while not timeToLock.isnumeric():
        try:
            if timeToLock.isnumeric():
                continue
            else:
                timeToLock = input("Please enter an integer value as your length of time.\n")
        except ValueError:
            timeToLock = (input("Please enter an integer value as your length of time.\n"))

    return timeToLock


def closeAppIfDetected(appsToClose):

    for apps in appsToClose:
        subprocess.call("TASKKILL /F /IM " + apps, shell=True)
    """
    needs:  how long to check for
    check the apps running -> if it is close it, if not, wait x time and check again.
    :return:
    """
