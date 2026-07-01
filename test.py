import pyautogui
import keyboard
import time
import subprocess
import os

os.system("cls")
street_light = [("green", 2, "apple"),
                ("yellow", 1, "banana"),
                ("red", 2, "cherry")]

while True:
    for item in street_light:
        c,s,f = item
        os.system("cls")
        print(c)
        time.sleep(s)
