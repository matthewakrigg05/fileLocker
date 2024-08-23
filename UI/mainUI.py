from tkinter import *
from functools import partial
import block
import checkFiles
import manipulateList
from UI import UImethods


class FileLocker:

    def __init__(self, root):
        root.title("File Locker")
        root.geometry("640x360")
        root.resizable(False, False)
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)
        root.rowconfigure(0, weight=2)
        root.rowconfigure(1, weight=2)
        root.rowconfigure(2, weight=1)
        root.rowconfigure(3, weight=1)
        root.rowconfigure(4, weight=1)
        root.rowconfigure(5, weight=0)

        Label(root, text="File Locker", justify=CENTER).grid(row=0, columnspan=2, sticky=N)

        Label(root, text="Manipulate Lists").grid(row=1, column=0, pady=5)
        Button(root, text="View Items", command=partial(manipulateList.showList, checkFiles.lockedContent())).grid(
            row=2, column=0, pady=10)

        Button(root, text="Add Items to lists", command=partial(UImethods.addToListPopUpBox, root)).grid(row=3,
                                                                                                         column=0,
                                                                                                         pady=5)

        Button(root, text="Remove Items from lists").grid(row=4, column=0, pady=5)

        Button(root, text="Saved Lists", justify=CENTER).grid(row=5, column=0, pady=5)

        Label(root, text="Block Apps and Websites").grid(row=1, column=1, pady=2)
        blockAppsCheck = Checkbutton(root, text="Block Apps", variable=BooleanVar(), onvalue=True, offvalue=False).grid(
            row=2,
            column=1,
            pady=5)

        blockWebsitesCheck = Checkbutton(root, text="Block Websites", variable=BooleanVar(), onvalue=True,
                                         offvalue=False).grid(row=3,
                                                              column=1,
                                                              pady=5)

        Label(root, text="Amount of time you wish to block in minutes:").grid(row=4, column=1, pady=2)
        timeToLock = (Entry(root))
        timeToLock.grid(row=5, column=1, pady=2)

        Button(root, text="Block!", command=partial(block.runBlock, timeToLock.get(), blockAppsCheck,
                                                    blockWebsitesCheck)).grid(row=6,
                                                                              column=1,
                                                                              pady=5)

        mainloop()


root = Tk()
root.protocol("WM_DELETE_WINDOW", lambda arg=root: UImethods.onClose(arg))
FileLocker(root)
