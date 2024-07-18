from checkFiles import lockedFilesContent


def addToList():
    file = open("./lockedFiles.txt", 'a')
    itemAlreadyInFile = False

    fileContents = lockedFilesContent()
    fileContentsString = ", ".join(fileContents).replace('\n', '')

    if not fileContents:
        print("You currently have no items in your file")
    else:
        print("Currently in your file you have: " + fileContentsString)

    fileToAdd = input(
        "Please write the .exe (as it would appear in the file explorer) name of the app you wish to add.\n")

    for item in fileContents:
        print(item)
        if item == fileToAdd:
            itemAlreadyInFile = True
            break

    if itemAlreadyInFile == True:
        print("This item is already in this file!")
    elif not fileContents:
        file.write(fileToAdd + "\n")
        print("Item added to list!")
    else:
        file.write(fileToAdd + "\n")
        print("Item added to list!")

    file.close()


addToList()