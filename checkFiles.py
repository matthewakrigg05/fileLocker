import os


def checkTxtFiles():
    return os.listdir("textFiles")


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
