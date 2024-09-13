from tkinter import Tk
import checkFiles
from UI.mainUI import FileLocker
from elevate import elevate


if __name__ == '__main__':
    elevate()
    checkFiles.checkTxtFiles()
    root = Tk()
    app = FileLocker(root)
    root.mainloop()
