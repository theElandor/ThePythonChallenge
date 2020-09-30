#this script will uninstall all my python packages
import pyautogui
import time


speed = 0.1
filename = "installed.txt"
time.sleep(2)
pyautogui.press("winleft")
pyautogui.typewrite("cmd", interval = speed)
pyautogui.press("enter")

with open(filename , "r") as file:
	data = file.read()
	names = data.split()
	for name in names:
		pyautogui.typewrite("python -m pip uninstall ",interval = speed)
		pyautogui.typewrite(name ,interval = speed)
		pyautogui.press("enter")
		time.sleep(2)
		pyautogui.press("y")
		pyautogui.press("enter")
