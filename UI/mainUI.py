from tkinter import *
from functools import partial
from UI import UImethods, block


class FileLocker:

    def __init__(self, window):
        window.title("File Locker")
        window.protocol("WM_DELETE_WINDOW", lambda arg=window: UImethods.onClose(arg))
        window.geometry("640x360")
        window.resizable(False, False)
        window.columnconfigure(0, weight=1)
        window.columnconfigure(1, weight=1)
        window.rowconfigure(0, weight=2)
        window.rowconfigure(1, weight=2)
        window.rowconfigure(2, weight=1)
        window.rowconfigure(3, weight=1)
        window.rowconfigure(4, weight=1)
        window.rowconfigure(5, weight=0)

        Label(window, text="File Locker", justify=CENTER).grid(row=0, columnspan=2, sticky=N)

        Label(window, text="Manipulate Lists").grid(row=1, column=0)
        Button(window, text="View Items", command=partial(UImethods.viewItemsPopUpBox, window)).grid(row=2, column=0,
                                                                                                     pady=3)

        Button(window, text="Add Items to lists", command=partial(UImethods.addToListPopUpBox, window)).grid(row=3,
                                                                                                             column=0,
                                                                                                             pady=5)

        Button(window, text="Remove Items from lists", command=partial(UImethods.removeItemsPopUpBox, window)).grid(
            row=4, column=0, pady=5)

        Label(window, text="Block Apps and Websites").grid(row=1, column=1, pady=5)
        blockApps = IntVar()
        Checkbutton(window, text="Block Apps", variable=blockApps, onvalue=1, offvalue=0).grid(row=2, column=1)

        blockSites = IntVar()
        Checkbutton(window, text="Block Websites", variable=blockSites, onvalue=1, offvalue=0).grid(row=3, column=1)

        Label(window, text="Amount of time you wish to block in minutes:").grid(row=4, column=1)
        lockTime = IntVar()
        timeToLock = (Entry(window, textvariable=lockTime))
        timeToLock.grid(row=5, column=1, pady=2)

        Button(window, text="Block!", command=partial(block.runBlock, window, lockTime, blockApps,
                                                      blockSites)).grid(row=6, column=1, pady=50)

        mainloop()
