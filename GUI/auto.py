import pyautogui
import time
pyautogui.PAUSE = 1.5
pyautogui.FAILSAFE = True
time.sleep(3)
pyautogui.click()
distance = 200
while distance > 0:
    pyautogui.dragRel(distance , 0, duration = 0.1)
    distance = distance -5
    pyautogui.dragRel(0, distance, duration = 0.1)
    pyautogui.dragRel(-distance , 0, duration = 0.1)
    distance = distance-5
    pyautogui.dragRel(0, -distance,duration = 0.1)
