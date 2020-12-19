import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


#color of snowflake: RGB: (255, 255, 255)
#color of present:   RGB: (129,   8,  12) RGB: (179,  22,  29) RGB: (249,  85, 111)

while keyboard.is_pressed('q') == False:

    pic = pyautogui.screenshot(region=(710,100,480,780))

    width, height = pic.size

    for x in range(0,height,15):
        for y in range(0,width,5):
            r,g,b = pic.getpixel((x,y))

            if b == 255:
                click(x+710,y+100)
                time.sleep(0.01)
                break
                