from tkinter import *


def onClose(root):
    with open("C:\\Windows\\System32\\drivers\\etc\\hosts", 'w') as file:
        file.close()
    root.destroy()


def close_win(top):
    top.destroy()


def popUpBox(root):

    top = Toplevel(root)
    top.geometry("250x125")
    top.title("File locker: Add to list")

    entry = Entry(top, width=25)
    entry.pack(pady=25, side=TOP)

    button = Button(top, text="Add to List!", command=lambda: close_win(top))
    button.pack(pady=5, side=TOP)
