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
    itemToAdd = fileToAdd.get()

    if not itemToAdd:
        tkinter.messagebox.showerror("Error", "No input was provided.")
        return Exception

    if ".exe" in itemToAdd:
        file = "textFiles/lockedApps.txt"
    else:
        file = "textFiles/lockedDomains.txt"

    with open(file, 'r+') as f:
        txt = f.readlines()

        for line in txt:
            if itemToAdd in line:
                itemAlreadyInFile = True
                break
            else:
                itemAlreadyInFile = False

        if itemAlreadyInFile:
            tkinter.messagebox.showerror("Error", "This item is already in this file!")
        else:
            f.write(itemToAdd + "\n")
            tkinter.messagebox.showinfo("Item Added", "Your item was successfully added to the correct file!")


def removeItem(contents):
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
    if not websites:
        tkinter.messagebox.showinfo("Websites", "You currently have no websites in your list.")
    else:
        tkinter.messagebox.showinfo("Websites", "Currently your websites list contains: " + ", ".join(websites).replace('\n', ''))


def showBlockedApps(apps=checkFiles.lockedAppsContent()):
    if not apps:
        tkinter.messagebox.showinfo("Apps", "You currently have no apps in your list.")
    else:
        tkinter.messagebox.showinfo("Apps", "Currently your apps list contains: " + ", ".join(apps).replace('\n', ''))
