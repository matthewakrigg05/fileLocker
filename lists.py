import tkinter
from tkinter import messagebox


class blockingList:

    def __init__(self, fileName):
        self.filePath = "textFiles/" + fileName.get()

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

    def addToList(self, fileToAdd, frame):
        if not fileToAdd.get():
            tkinter.messagebox.showerror("Error", "No input was provided.")
            return Exception

        if fileToAdd in self.getListContents():
            tkinter.messagebox.showerror("Error", "This item is already in this file!")
        else:
            with open(self.filePath, "a+") as f:
                f.write(fileToAdd.get() + "\n")
                frame.onClose()
                tkinter.messagebox.showinfo("Item Added", "Your item was successfully added to the correct file!")

    def removeFromList(self, fileToRemove, frame):
        removed = False

        for item in self.getListContents():
            if item != fileToRemove.get():
                with open(self.filePath, "r+") as f:
                    f.write(item + "\n")
            else:
                f.truncate()
                removed = True

        if removed:
            tkinter.messagebox.showinfo("Success", "Your chosen item was successfully removed from your list!")
            frame.onClose()
        else:
            tkinter.messagebox.showerror("Error", "Item could not be removed")
