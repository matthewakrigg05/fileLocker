from tkinter import Tk
from UI.mainFrame import FileLocker
from elevate import elevate


if __name__ == '__main__':
    elevate()
    root = Tk()
    app = FileLocker(root)
    root.mainloop()
