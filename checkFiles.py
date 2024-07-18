import os
import subprocess


# check if the file containing names of lockable files exists
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
    file = open("./lockedFiles.txt", 'r')
    fileContents = set()
    Lines = file.readlines()

    for line in Lines:
        strippedLine = line[:-1]
        fileContents.add(strippedLine)

    return fileContents

