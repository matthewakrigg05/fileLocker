import tkinter.messagebox

import checkFiles


def clearLists():
    appsFile = open("textFiles/lockedApps.txt", 'w')
    appsFile.close()

    websiteFile = open("textFiles/lockedDomains.txt", "w")
    websiteFile.close()


def clearApps():
    appsFile = open("textFiles/lockedApps.txt", 'w')
    appsFile.close()


def clearWebsites():
    websiteFile = open("textFiles/lockedDomains.txt", "w")
    websiteFile.close()


def addToList(fileToAdd):
    if not fileToAdd:
        print("No input")
        return Exception

    if ".exe" in fileToAdd:
        file = "textFiles/lockedApps.txt"
    else:
        file = "textFiles/lockedDomains.txt"

    with open(file, 'a') as f:
        itemAlreadyInFile = False

        for item in file:
            if item == fileToAdd:
                itemAlreadyInFile = True
                break

        if itemAlreadyInFile:
            print("This item is already in this file!")
            return False
        else:
            f.write(fileToAdd + "\n")
            print("Item added to list!")
            return True


def removeItem(contents):
    removed = False

    if ".exe" in contents.get():
        file = "textFiles/lockedApps.txt"
    else:
        file = "textFiles/lockedDomains.txt"

    with open(file, "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if line.strip("\n") != contents.get():
                file.write(line)
        file.truncate()
        removed = True

    if removed:
        tkinter.messagebox.showinfo("Success", "Your chosen item was successfully removed from your list!")
    else:
        tkinter.messagebox.showerror("Error", "Item could not be removed")


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
