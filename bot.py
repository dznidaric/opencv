import pyautogui
import time
import keyboard
import random
import win32api, win32con

while 1:
    if pyautogui.locateOnScreen('poklon.png', confidence=0.55) != None:
        print("vidljivo")
        time.sleep(0.5)
    else:
        print("nope")
        time.sleep(0.5)

        