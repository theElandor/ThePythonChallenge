import zipfile
import re
comments = []
file = zipfile.ZipFile('channel.zip')
num = '90052'
while True:
    content = file.read(num + ".txt").decode("utf-8")
    comments.append(file.getinfo(num+".txt").comment.decode())
    print(content)
    number = re.findall("[0-9]+", content)
    if not number:
        break
    else:
        num = number.pop()
for comment in comments:
    print(comment, end = "")