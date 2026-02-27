# Updated main.py

import threading

# Improved GUI component
from tkinter import Tk, Label, Button, messagebox

class App:
    def __init__(self, master):
        self.master = master
        master.title("AES Photocipher Tool")

        self.label = Label(master, text="Welcome to the AES Photocipher Tool")
        self.label.pack()

        self.run_button = Button(master, text="Run", command=self.run_with_thread)
        self.run_button.pack()

    def run_with_thread(self):
        thread = threading.Thread(target=self.run)
        thread.start()

    def run(self):
        try:
            # Your processing code goes here
            pass
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()