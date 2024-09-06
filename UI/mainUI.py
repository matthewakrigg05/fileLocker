from tkinter import *
from functools import partial
import block
from UI import UImethods


class FileLocker:

    def __init__(self, root):
        root.title("File Locker")
        root.protocol("WM_DELETE_WINDOW", lambda arg=root: UImethods.onClose(arg))
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

        Label(root, text="Manipulate Lists").grid(row=1, column=0)
        Button(root, text="View Items", command=partial(UImethods.viewItemsPopUpBox, root)).grid(row=2, column=0, pady=3)

        Button(root, text="Add Items to lists", command=partial(UImethods.addToListPopUpBox, root)).grid(row=3,
                                                                                                         column=0,
                                                                                                         pady=5)

        Button(root, text="Remove Items from lists", command=partial(UImethods.removeItemsPopUpBox, root)).grid(row=4, column=0, pady=5)

        Label(root, text="Block Apps and Websites").grid(row=1, column=1, pady=5)
        blockApps = IntVar()
        Checkbutton(root, text="Block Apps", variable=blockApps, onvalue=1, offvalue=0).grid(row=2, column=1)

        blockSites = IntVar()
        Checkbutton(root, text="Block Websites", variable=blockSites, onvalue=1, offvalue=0).grid(row=3, column=1)

        Label(root, text="Amount of time you wish to block in minutes:").grid(row=4, column=1)
        lockTime = IntVar()
        timeToLock = (Entry(root, textvariable=lockTime))
        timeToLock.grid(row=5, column=1, pady=2)

        Button(root, text="Block!", command=partial(block.runBlock, root, lockTime, blockApps,
                                                    blockSites)).grid(row=6, column=1, pady=50)

        mainloop()
