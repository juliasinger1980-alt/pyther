import threading
import time
import keyboard

spam_active = threading.Event()
spam_thread = None


def Spam():
    while spam_active.is_set():
        keyboard.press_and_release("e")
        time.sleep(0.1)


def Start():
    global spam_thread
    if spam_active.is_set():
        return

    spam_active.set()
    spam_thread = threading.Thread(target=Spam, daemon=True)
    spam_thread.start()
    print("E autoclicker started. Press F7 to stop.")


def Stop():
    spam_active.clear()
    keyboard.release("e")
    print("E autoclicker stopped.")

keyboard.add_hotkey("f6", Start)
keyboard.add_hotkey("f7", Stop)

print("Press F6 to start the E autoclicker and F7 to stop it.")
keyboard.wait()
