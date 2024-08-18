import checkFiles


def clearLists():
    appsFile = open("lockedApps.txt", 'w')
    appsFile.close()

    websiteFile = open("lockedDomains.txt", "w")
    websiteFile.close()


def clearApps():
    appsFile = open("lockedApps.txt", 'w')
    appsFile.close()


def clearWebsites():
    websiteFile = open("lockedDomains.txt", "w")
    websiteFile.close()


def addToList(file, contents):

    match file:
        case "./lockedApps.txt":
            fileToAdd = input(
                "Please write the .exe (as it would appear in the file explorer) name of the app you wish to add.\n")

        case "./lockedDomains.txt":
            fileToAdd = input("Please input the website in the form example.com to add it to the list\n")

    with open(file, 'a') as file:
        itemAlreadyInFile = False

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


def showBlockedWebsites(websites=checkFiles.lockedDomainsContent()):
    if len(websites) == 0:
        print("You currently have no websites in your list.")
    else:
        print("Currently your websites list contains: " + ", ".join(websites).replace('\n', ''))


def showBlockedApps(apps=checkFiles.lockedAppsContent()):
    if len(apps) == 0:
        print("You currently have no apps in your list.")
    else:
        print("Currently your apps list contains: " + ", ".join(apps).replace('\n', ''))
        