import checkFiles


def clearList():
    file = open("lockedApps.txt", 'w')
    file.close()


def addToList(contents):
    with open("lockedApps.txt", 'a') as file:
        itemAlreadyInFile = False

        fileToAdd = input(
            "Please write the .exe (as it would appear in the file explorer) name of the app you wish to add.\n")

        for item in contents:
            if item == fileToAdd:
                itemAlreadyInFile = True
                break

        if itemAlreadyInFile:
            print("This item is already in this file!")
        else:
            file.write(fileToAdd + "\n")
            print("Item added to list!")


def removeItem(contents):
    removed = False
    toRemove = input("Please write the .exe name of the application you wish to remove from your list (ensure that your"
                     + " choice is written as it is in the text file)\n")

    for item in contents:
        strippedLine = item.strip("\n")
        if strippedLine == toRemove:
            contents.remove(toRemove)

            with open("lockedApps.txt", "r+") as f:
                lines = f.readlines()

            with open("lockedApps.txt", "w") as f:
                for line in lines:
                    if line.strip("\n") != toRemove:
                        f.write(line)

            removed = True
            break

    if not removed:
        print("Item could not be removed, make sure the case matches and the item does exist in the list.")
    else:
        print("Item successfully removed from list.")


def showList(content):
    if len(content) == 0:
        print("You currently have no applications in your list.")
    else:
        print("Currently your list contains: " + ", ".join(content).replace('\n', ''))


def showBlockedWebsites(websites):
    if len(websites) == 0:
        print("You currently have no websites in your list.")
    else:
        print("Currently your websites list contains: " + ", ".join(websites).replace('\n', ''))


def showBlockedApps(apps):
    if len(apps) == 0:
        print("You currently have no apps in your list.")
    else:
        print("Currently your apps list contains: " + ", ".join(apps).replace('\n', ''))