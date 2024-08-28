from tkinter import Tk
import checkFiles
from UI.mainUI import FileLocker
from elevate import elevate


def main():
    elevate()
    checkFiles.checkTxtFiles()
    root = Tk()
    FileLocker(root)


if __name__ == '__main__':
    main()
