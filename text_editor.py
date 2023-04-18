import os

def open_file(filename):
    with open(filename, "r") as f:
        return f.read()

def save_file(filename, text):
    with open(filename, "w") as f:
        f.write(text)

def pypad():
    while True:
        filename = input("Enter filename: ")

        if not os.path.isfile(filename):
            print(f"File {filename} does not exist.")
            continue

        print(open_file(filename))

        choice = input("Do you want to edit this file? (y/n): ")
        if choice.lower() == "y":
            text = input("Enter text: ")
            save_file(filename, text)
        else:
            break
