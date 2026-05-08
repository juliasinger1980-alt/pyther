import threading
import time
import keyboard

spam_aktivierer = threading.Event()
thread = None

def spam():
    while spam_aktivierer.is_set():
        keyboard.press_and_release("e")
        time.sleep(0.1)

def start():
    global thread
    if spam_aktivierer.is_set():
        return
    spam_aktivierer.set()
    thread = threading.Thread(target=spam, daemon=True)
    thread.start()

def stop():
    keyboard.release("e")
    spam_aktivierer.clear()

keyboard.add_hotkey("f6", start)
keyboard.add_hotkey("f7", stop)

keyboard.wait()