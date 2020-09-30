from selenium import webdriver
import pyautogui
import time
import requests

time.sleep(1)
browser = webdriver.Chrome()
browser.get('http://www.amazon.it/')
bar = browser.find_element_by_id("twotabsearchtextbox")
bar.click()
pyautogui.typewrite("Laptop" , interval = 0.1)
pyautogui.press("enter")
time.sleep(1)
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
price = browser.find_element_by_link_text("400 - 600 EUR")
price.click()







