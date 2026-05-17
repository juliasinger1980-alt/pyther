from cProfile import label
import threading
import keyboard
import tkinter as tk
import tkinter.font as tkFont
import time
import os

os.system("clear")

def record_keys():
    keyboard.start_recording()
    time.sleep(15)  # Record fuer 15 secs
    recorded = keyboard.stop_recording()
    time.sleep(1)
    return recorded

class Anzeige:
    def __init__(self, root):
        #keyboard.add_hotkey('q', self.stop)
        root.bind("<KeyPress-q>", lambda e: self.stop())
        self.test = True
        self.root = root
        self.root.title("Keyboard Recorder")
        self.root.geometry("400x200")
        self.root.configure(bg="#351C13")
        self.root.attributes("-topmost", True)
        self.label = tk.Label(root, text = "Press 'Start Recording' to record your keystrokes for 15 seconds.", bg="#351C13", fg="white", font=tkFont.Font(size=12), wraplength = 380)
        self.label.pack(pady = 20,fill =tk.BOTH, expand=True)
        self.label.bind("<Configure>", lambda e: self.label.config(wraplength=e.width))
        self.button = tk.Button(root, text="Start Recording", command=self.start_recording, bg="#4E2617", fg="white", font=tkFont.Font(size=12))
        self.button.pack(pady = 10)
        self.inputs = tk.Label(root, bg="#351C13", fg="white", font=tkFont.Font(size=12), wraplength=380)
        self.inputs.pack(fill =tk.BOTH, expand=True)
        self.inputs.bind("<Configure>", lambda e: self.inputs.config(wraplength=e.width))
        self.exit = tk.Label(root, bg="#351C13", fg="white", font=tkFont.Font(size=12))
        self.exit.pack()

    def playing_loop(self):
        while self.test:
            keyboard.play(self.recorded)
            time.sleep(2)

    def start_recording(self):
        self.recorded = record_keys()
        self.inputs.config(text=str(self.recorded))
        self.root.update()
        threading.Thread(target=self.playing_loop, daemon=True).start()
        
    def stop(self):
        self.test = False
        self.exit.config(text="Exiting...")
        self.root.update()
    

if __name__ == "__main__":
    root = tk.Tk()
    app = Anzeige(root)
    root.mainloop()


