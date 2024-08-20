import tkinter as tk


class FileLocker:

    def __init__(self, root):
        root.title("File Locker")
        root.geometry("640x360")
        root.resizable(False, False)

        mainFrame = tk.Frame(root, width=640, height=360)
        mainFrame.grid(row=0, column=0)

        label = tk.Label(mainFrame, text="File Locker", justify="center")
        label.place(relx=0.5, rely=0.05, anchor=tk.CENTER)


root = tk.Tk()
FileLocker(root)
root.mainloop()
