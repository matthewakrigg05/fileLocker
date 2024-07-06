import os

def checkForTxt():
    filePath = './lockedFiles.txt'

    if not os.path.exists(filePath):
        open("lockedFiles.txt", 'w')
        print("TRUE")
    else:
        print("FALSE, file exists already")