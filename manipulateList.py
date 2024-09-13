import tkinter.messagebox


def clearLists():
    clearApps()
    clearWebsites()


def clearApps():
    appsFile = open("textFiles/lockedApps.txt", 'w')
    appsFile.close()


def clearWebsites():
    websiteFile = open("textFiles/lockedDomains.txt", "w")
    websiteFile.close()


def addToList(fileToAdd):

    if not fileToAdd.get():
        tkinter.messagebox.showerror("Error", "No input was provided.")
        return Exception

    if ".exe" in fileToAdd.get():
        file = "textFiles/lockedApps.txt"
    else:
        file = "textFiles/lockedDomains.txt"

    with open(file, 'r+') as f:
        txt = f.readlines()

        for line in txt:
            if fileToAdd.get() in line:
                itemAlreadyInFile = True
                break
            else:
                itemAlreadyInFile = False

        if itemAlreadyInFile:
            tkinter.messagebox.showerror("Error", "This item is already in this file!")
        else:
            f.write(fileToAdd.get() + "\n")
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
