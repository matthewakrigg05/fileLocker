from tkinter import Tk
import checkFiles
from UI.mainUI import FileLocker


def main():
    checkFiles.checkTxtFiles()
    root = Tk()
    FileLocker(root)


if __name__ == '__main__':
    main()
