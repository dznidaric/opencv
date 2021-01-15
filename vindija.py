import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(5)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


#boja vrpce RGB: (  0,  34,  64)

while keyboard.is_pressed('q') == False:

    pic = pyautogui.screenshot(region=(680,150,580,500))

    width, height = pic.size

    for x in range(0,width,5):
        for y in range(0,height,5):
            r,g,b = pic.getpixel((x,y))

            if b == 64 or b==0 or b==102 or b==180:
                click(x+680,y+150)
                click(x+680,y+170)
                time.sleep(0.01)
                break


