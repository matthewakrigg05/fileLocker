import os


def checkTxtFiles():
    if not os.path.exists('textFiles/lockedApps.txt'):
        with open('textFiles/lockedApps.txt') as f:
            f.close()

    if not os.path.exists('textFiles/lockedDomains.txt'):
        with open('textFiles/lockedDomains.txt', 'w') as f:
            f.close()


def allLockedContent():
    return lockedAppsContent() + lockedDomainsContent()


def lockedAppsContent():
    fileContents = []

    with open("textFiles/lockedApps.txt", 'r') as file:
        Lines = file.readlines()

        for line in Lines:
            fileContents.append(line.strip("\n"))

    return fileContents


def lockedDomainsContent():
    fileContents = []

    with open("textFiles/lockedDomains.txt", "r") as file:
        lines = file.readlines()

        for line in lines:
            fileContents.append(line.strip("\n"))

    return fileContents
