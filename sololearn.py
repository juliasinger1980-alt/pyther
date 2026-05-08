import pyautogui
import keyboard
import time
import os

os.system("cls")
time.sleep(2)

target_color = (105, 76, 111)  # grayish target
target_color2 = (75, 63, 96)

test = True
while test:
    
    #keyboard.press("w")
    time.sleep(0.05)

    x, y = pyautogui.position()
    for dx in range(-10, 11):
        for dy in range(-10, 11):

            if pyautogui.pixelMatchesColor(x + dx, y + dy, target_color, tolerance=80) or pyautogui.pixelMatchesColor(x + dx, y - dy, target_color2, tolerance=80 ): 
                print("jump")
                keyboard.press_and_release("space")
                time.sleep(0.2)

            if keyboard.is_pressed("q"):
                test = False
                keyboard.release("w")
                keyboard.release("space")
                print("exiting")
    
    time.sleep(0.01)