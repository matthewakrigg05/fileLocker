import os

# check if the file containing names of lockable files exists
def checkForTxt():
    filePath = './lockedFiles.txt'

    if not os.path.exists(filePath):
        open("lockedFiles.txt", 'w')
        print("TRUE")
    else:
        print("FALSE, file exists already")