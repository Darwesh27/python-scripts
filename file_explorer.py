import os
from tkinter import *

class FileExplorer:
    def __init__(self, master):
        self.master = master
        self.master.title("File Explorer")
        self.frame = Frame(self.master)
        self.frame.pack()
        self.create_widgets()

    def create_widgets(self):
        self.path_label = Label(self.frame, text="Path: ")
        self.path_label.grid(row=0, column=0)
        self.path_entry = Entry(self.frame, width=50)
        self.path_entry.grid(row=0, column=1)
        self.path_entry.insert(END, os.getcwd())
        self.listbox = Listbox(self.frame, width=70, height=20)
        self.listbox.grid(row=1, column=0, columnspan=2)
        self.scrollbar = Scrollbar(self.frame, orient=VERTICAL)
        self.scrollbar.grid(row=1, column=2, sticky=N+S)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        self.show_files()

    def show_files(self):
        self.listbox.delete(0, END)
        path = self.path_entry.get()
        if not os.path.exists(path):
            messagebox.showerror("Error", "Invalid Path")
            return
        files = os.listdir(path)
        for file in files:
            self.listbox.insert(END, file)


# driver code
def explore():
    root = Tk()
    fe = FileExplorer(root)
    root.mainloop()
