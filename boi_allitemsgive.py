from pynput import keyboard
from pynput.keyboard import Controller, Key
import time
import threading

def main():
    continue_e = threading.Event()

    def wait(key):
        if key == keyboard.Key.enter:
            continue_e.set()
    
    kb = Controller()
    lsn = keyboard.Listener(on_press=wait)
    lsn.start()

    for i in range(1, 300):
        kb.type(f"giveitem c{i}")
        time.sleep(0.05)
        continue_e.clear()
        continue_e.wait()
        time.sleep(0.1)

        


def on_press(key):
    if key == keyboard.Key.f3:
        threading.Thread(target=main, daemon= True).start()


listener = keyboard.Listener(on_press=on_press)

listener.start()

listener.join()
