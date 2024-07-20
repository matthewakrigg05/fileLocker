import os
import subprocess


def checkForTxt():
    filePath = './lockedFiles.txt'

    if not os.path.exists(filePath):
        return True
    else:
        return False


def checkIfProcessRunning(program):
    activePrograms = str(subprocess.check_output('tasklist'))
    if program in activePrograms:
        return True
    else:
        return False


def lockedFilesContent():
    with open("./lockedFiles.txt", 'r') as file:
        fileContents = set()
        Lines = file.readlines()

        for line in Lines:
            strippedLine = line[:-1]
            fileContents.add(strippedLine)

    return fileContents

