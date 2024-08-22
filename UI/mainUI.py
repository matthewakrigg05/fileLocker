from tkinter import *
from functools import partial

import blockApps
import checkFiles


def onClose():
    with open("C:\\Windows\\System32\\drivers\\etc\\hosts", 'w') as file:
        file.close()
    root.destroy()


class FileLocker:

    def __init__(self, root):
        root.title("File Locker")
        root.geometry("640x360")
        root.resizable(False, False)

        Label(root, text="File Locker").grid(row=0, column=1, pady=2)

        Label(root, text="Manipulate Lists").grid(row=1, column=0, pady=5)
        Button(root, text="View Items").grid(row=2, column=0, pady=5)
        Button(root, text="Add Items to list").grid(row=3, column=0, pady=5)
        Button(root, text="Remove Items from lists").grid(row=4, column=0, pady=5)
        Button(root, text="Saved Lists", justify=CENTER).grid(row=5, column=0, pady=5)

        Label(root, text="Block Apps and Websites").grid(row=1, column=2, pady=2)
        Checkbutton(root, text="Block Apps", variable=BooleanVar(), onvalue=True, offvalue=False).grid(row=2,
                                                                                                       column=2,
                                                                                                       pady=5)
        Checkbutton(root, text="Block Websites", variable=BooleanVar(), onvalue=True, offvalue=False).grid(row=3,
                                                                                                           column=2,
                                                                                                           pady=5)
        Label(root, text="Amount of time you wish to block:").grid(row=4, column=2, pady=2)
        timeToBlock = Entry(root).grid(row=5, column=2, pady=2)

        Button(root, text="Block!", command=partial(blockApps.closeAppIfDetected, checkFiles.lockedAppsContent())).grid(row=6,
                                                                                                               column=2,
                                                                                                               pady=5)

        mainloop()


root = Tk()
root.protocol("WM_DELETE_WINDOW", onClose)
FileLocker(root)

