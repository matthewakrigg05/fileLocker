import os
import tkinter
from tkinter import messagebox


class blockingList:

    def __init__(self, fileName):
        self.fileName = fileName
        self.filePath = "./savedLists/" + fileName

    def getListContents(self):
        fileContents = []

        with open(self.filePath, 'r') as file:
            Lines = file.readlines()

            for line in Lines:
                fileContents.append(line.strip("\n"))

        if not fileContents:
            return False
        else:
            return ", ".join(fileContents).replace('\n', '')

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
        with open(self.filePath, "r+") as f:
            lines = f.readlines()
            f.seek(0)
            for item in lines:
                if item.strip("\n") != fileToRemove:
                    f.write(item)
            removed = True
            f.truncate()

        if removed:
            tkinter.messagebox.showinfo("Success", "Your chosen item was successfully removed from your list!")
            frame.onClose()
        else:
            tkinter.messagebox.showerror("Error", "Item could not be removed")

    def createNewList(self):
        if not os.path.exists(self.filePath + ".txt"):
            f = open(self.filePath + ".txt", "w")
            f.close()
            tkinter.messagebox.showinfo("Success", "Your file has been created!")
        else:
            tkinter.messagebox.showinfo("Error", "This file already exists!")

    def removeList(self):
        if os.path.exists(self.filePath + ".txt"):
            os.remove(self.filePath + ".txt")
            tkinter.messagebox.showinfo("Success", "Your file has been removed!")
        else:
            tkinter.messagebox.showinfo("Error", "This file could not be removed")
