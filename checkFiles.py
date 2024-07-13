import os
import subprocess


# check if the file containing names of lockable files exists
def checkForTxt():
    filePath = './lockedFiles.txt'

    if not os.path.exists(filePath):
        open("lockedFiles.txt", 'w')
        print("TRUE")
    else:
        print("FALSE, file exists already")

def checkIfProcessRunning(program):
    n = 0
    prog = [line.split() for line in subprocess.check_output("tasklist").splitlines()]
    [prog.pop(e) for e in [0, 1, 2]]  # useless
    for task in prog:
        if task[0] == program:
            n = n + 1
    if n > 0:
        return True
    else:
        return False