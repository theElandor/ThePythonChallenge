import pyperclip
import time
filename = 'prova.txt'
words = []
i = 0
while True:
    if pyperclip.paste() != 'None':
        value = pyperclip.paste()  ## u  copy the text from the clipboard

        if value not in words:
            words.append(value)
            i += 1

        print(words)

        time.sleep(3)
    if i > 3:
        break
f = open(filename, "w+")  ## means we can both read and write
for x in words:
    f.write(x +" ")
f.close()
