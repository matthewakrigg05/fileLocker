import os
import subprocess

def checkForFilesTxt():
    if not os.path.exists('./lockedFiles.txt'):
        with open('./lockedFiles.txt') as f:
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


def lockedFilesContent():
    with open("./lockedFiles.txt", 'r') as file:
        fileContents = set()
        Lines = file.readlines()

        for line in Lines:
            strippedLine = line[:-1]
            fileContents.add(strippedLine)

    return fileContents