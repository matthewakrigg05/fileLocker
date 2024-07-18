from checkFiles import lockedFilesContent


def clearList():
    file = open("./lockedFiles.txt", 'w')
    file.close()


def addToList():
    with open("./lockedFiles.txt", 'a') as file:
        itemAlreadyInFile = False

        fileContents = lockedFilesContent()

        fileToAdd = input(
            "Please write the .exe (as it would appear in the file explorer) name of the app you wish to add.\n")

        for item in fileContents:
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


def removeItem():
    fileContents = lockedFilesContent()

    toRemove = input("Please write the .exe name of the application you wish to remove from your list (ensure that your"
                     + " choice is written as it is in the text file)\n")

    for item in fileContents:

        if item == toRemove:
            fileContents.remove(toRemove)
            with open("./lockedFiles.txt", "r+") as f:
                lines = f.readlines()

                lines.pop(lines.index(item + "\n"))

                f.truncate()

                f.writelines(lines)
            break