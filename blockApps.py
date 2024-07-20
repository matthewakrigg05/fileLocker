import os


def blockApps():
    timeToLock = input("How long would you like to block your chosen apps for (in seconds)\n")

    while not timeToLock.isnumeric():
        try:
            if timeToLock.isnumeric():
                continue
            else:
                timeToLock = input("Please enter an integer value as your length of time.\n")
        except ValueError:
            timeToLock = (input("Please enter an integer value as your length of time.\n"))
blockApps()
