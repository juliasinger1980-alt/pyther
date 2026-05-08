import tkinter as tk
import keyboard
import os
import pyautogui

os.system("cls")

class window:
    def __init__(self, root):
        root.title("Test")
        root.geometry("1080x720")
        root.button =tk.Button(root, text="Resize", command=self.resize)
        root.button.pack(pady=20)
        root.input_x = tk.Entry(root)
        root.input_x.pack(pady=20)
        root.input_y = tk.Entry(root)
        root.input_y.pack(pady=20)

    def resize(self):
        x = root.input_x.get()
        y = root.input_y.get()
        root.geometry(f"{x}x{y}")



if __name__ == "__main__":
    root = tk.Tk()
    app = window(root)
    root.mainloop()