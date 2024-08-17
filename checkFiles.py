import os
import subprocess


def checkForFilesTxt():
    if not os.path.exists('lockedApps.txt'):
        with open('lockedApps.txt') as f:
            f.close()
    else:
        return False


def checkForWebTxt():
    if not os.path.exists('lockedDomains.txt'):
        with open('lockedDomains.txt', 'w') as f:
            f.close()
    else:
        return False


def checkIfProcessRunning(program):
    activePrograms = str(subprocess.check_output('tasklist'))
    if program in activePrograms:
        return True
    else:
        return False


def lockedContent():
    filesContents = []

    with open("lockedApps.txt", 'r') as file:
        Lines = file.readlines()

        for line in Lines:
            strippedLine = line.strip("\n")
            filesContents.append(strippedLine)

    with open("lockedDomains.txt", 'r') as file:
        Lines = file.readlines()

        for line in Lines:
            strippedLine = line.strip("\n")
            filesContents.append(strippedLine)

    return filesContents

print(lockedContent())
