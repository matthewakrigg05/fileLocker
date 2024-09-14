import tkinter
from tkinter import messagebox


class blockingList:

    def __init__(self, filePath):
        self.filePath = filePath

    def getListContents(self):
        fileContents = []

        with open(self.filePath, 'r') as file:
            Lines = file.readlines()

            for line in Lines:
                fileContents.append(line.strip("\n"))

        return fileContents

    def clearListContents(self):
        appsFile = open(self.filePath, 'w')
        appsFile.close()

    def addToList(self, fileToAdd):

        if not fileToAdd.get():
            tkinter.messagebox.showerror("Error", "No input was provided.")
            return Exception

        with open(self.filePath, 'r+') as f:
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

    def removeFromList(self, fileToRemove):

        with open(self.filePath, "r+") as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if line.strip("\n") != fileToRemove.get():
                    file.write(line)
            file.truncate()
            removed = True

        if removed:
            tkinter.messagebox.showinfo("Success", "Your chosen item was successfully removed from your list!")
        else:
            tkinter.messagebox.showerror("Error", "Item could not be removed")
