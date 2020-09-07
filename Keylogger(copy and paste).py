import pyperclip
import time
filename = 'notes.txt'
list = []
i = 0
while True:
    if pyperclip.paste() != 'None':
        value = pyperclip.paste()  ## u  copy the text from the clipboard

        if value not in list:
            list.append(value)
            i+= 1

        print(list)

        time.sleep(3)
    if i > 3:
        break
f = open(filename, "w+")  ## means we can both read and write
for x in list:
    f.write(x +" ")
f.close()



