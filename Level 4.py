import urllib.request, urllib.error, urllib.parse
import re
## 84)16044
## 163)66831
##164) peak

num = "12345"
for x in range(400):
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+num
    response = urllib.request.urlopen(url)
    webContent = response.read().decode()
    number = re.findall("[0-9]+",webContent)
    num = number.pop()
    print(str(x)+")"+num)