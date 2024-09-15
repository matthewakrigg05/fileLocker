from tkinter import Tk
import checkFiles
from UI.mainFrame import FileLocker
from elevate import elevate


if __name__ == '__main__':
    elevate()
    print(checkFiles.checkTxtFiles())
    root = Tk()
    app = FileLocker(root)
    root.mainloop()
