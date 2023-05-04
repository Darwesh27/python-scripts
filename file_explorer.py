import os
import tkinter as tk
from tkinter import filedialog, messagebox

class FileExplorerGUI:
    def __init__(self, master):
        self.master = master
        master.title("File Explorer")

        # create and pack the widgets
        self.current_path_label = tk.Label(master, text="Current Path:")
        self.current_path_label.pack(side="top")

        self.path_var = tk.StringVar(value=os.getcwd())
        self.path_entry = tk.Entry(master, textvariable=self.path_var)
        self.path_entry.pack(side="top", fill="x")
        self.path_entry.bind("<Return>", self.change_directory)

        self.frame = tk.Frame(master)
        self.frame.pack(side="top", fill="both", expand=True)

        self.scrollbar = tk.Scrollbar(self.frame, orient="vertical")
        self.scrollbar.pack(side="right", fill="y")

        self.canvas = tk.Canvas(self.frame, yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar.config(command=self.canvas.yview)

        self.button_frame = tk.Frame(master)
        self.button_frame.pack(side="top", fill="x")

        self.back_button = tk.Button(self.button_frame, text="< Back", command=self.go_back)
        self.back_button.pack(side="left")


        # history list
        self.history = []
        self.history_pos = -1

        self.load_directory()

    def load_directory(self):

        # update history list
        print("The history is ", self.history)
        path = self.path_var.get()
        if path != self.history[-1] if self.history else True:
            self.history = self.history[:self.history_pos + 1] + [path]
            self.history_pos = len(self.history) - 1

        self.canvas.delete("all")
        path = self.path_var.get()
        current_y = 0
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if os.path.isdir(file_path):
                button = tk.Button(self.canvas, text=filename,
                                   command=lambda file_path=file_path: self.open_directory(file_path))
                self.canvas.create_window((0, current_y), window=button, anchor="nw")
            else:
                label = tk.Label(self.canvas, text=filename)
                self.canvas.create_window((0, current_y), window=label, anchor="nw")
            widget_height = button.winfo_height() if os.path.isdir(file_path) else label.winfo_height()
            current_y += 30



        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def change_directory(self, event):
        print("changing dir")
        path = self.path_var.get()
        if os.path.isdir(path):
            os.chdir(path)
            self.path_var.set(os.getcwd())  # update the path variable
            self.load_directory()
        else:
            messagebox.showerror("Error", "Invalid path")

    def open_directory(self, path):
        os.chdir(path)
        self.path_var.set(os.getcwd())  # update the path variable

        # Check if path is different from the current history position
        if path != self.history[self.history_pos]:
            # Append the new path to the history and update the history position
            self.history = self.history[:self.history_pos + 1] + [path]
            self.history_pos = len(self.history) - 1

        self.load_directory()

    def go_back(self):
        if self.history_pos > 0:
            self.history_pos -= 1
            self.path_var.set(self.history[self.history_pos])
            self.load_directory()

    def go_forward(self):
        if self.history_pos < len(self.history) - 1:
            self.history_pos += 1
            path = self.history[self.history_pos]
            self.path_var.set(path)
            self.load_directory()
        else:
            print("Can't go forward")




# driver code
def explore():
    root = tk.Tk()
    file_explorer = FileExplorerGUI(root)
    root.mainloop()
