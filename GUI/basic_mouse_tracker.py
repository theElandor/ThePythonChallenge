import pyautogui
import time
pyautogui.PAUSE = 1.5
pyautogui.FAILSAFE = True
while True:
    x1,y1 = pyautogui.position()
    x2,y2 = pyautogui.position()
    if x1==x2 and y1 == y2:
        continue
    else:
        col = pyautogui.screenshot().getpixel((x2,y2))
        print(x2,y2,col)

