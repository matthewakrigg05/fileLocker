from checkFiles import lockedFilesContent


def addToList():
    file = open("./lockedFiles.txt", 'w')

    fileContents = lockedFilesContent()
    """
    fileToAdd = input(
        "Please write the .exe (as it would appear in the file explorer) name of the app you wish to add.\n")
"""
    print(fileContents)
    file.close()


addToList()
