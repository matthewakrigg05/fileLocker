from checkFiles import lockedFilesContent


def clearList():
    file = open("./lockedFiles.txt", 'w')
    file.close()


def addToList():
    file = open("./lockedFiles.txt", 'a')
    itemAlreadyInFile = False

    fileContents = lockedFilesContent()

    fileToAdd = input(
        "Please write the .exe (as it would appear in the file explorer) name of the app you wish to add.\n")

    for item in fileContents:
        print(item)
        if item == fileToAdd:
            itemAlreadyInFile = True
            break

    if itemAlreadyInFile:
        print("This item is already in this file!")
    elif not fileContents:
        file.write(fileToAdd + "\n")
        print("Item added to list!")
    else:
        file.write(fileToAdd + "\n")
        print("Item added to list!")

    file.close()
