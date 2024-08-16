import os
import subprocess


def checkForFilesTxt():
    if not os.path.exists('lockedApps.txt'):
        with open('lockedApps.txt') as f:
            f.close()
    else:
        return False


def checkForWebTxt():
    if not os.path.exists('./webDomains.txt'):
        with open('./webDomains.txt', 'w') as f:
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
    with open("lockedApps.txt", 'r') as file:
        filesContents = set()
        Lines = file.readlines()

        for line in Lines:
            strippedLine = line[:-1]
            filesContents.add(strippedLine)

    with open("./webDomains.txt", 'r') as file:
        domains = set()
        Lines = file.readlines()

        for line in Lines:
            strippedLine = line[:-1]
            domains.add(strippedLine)

    return filesContents