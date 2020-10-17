import requests
import bs4
from selenium import webdriver
import time



links = []
res = requests.get("https://spacecity.it")
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")
elems = soup.select('img')
i = 1
for elem in elems:
	link = (elem.get("src"))
	links.append(link)
for x in links:
	if x.endswith("jpg"):
		re = requests.get(x)
		file = open("C:\\Users\\Lugli\\Desktop\\programmazione\\Images\\sample"+str(i)+".jpg","wb")
		file.write(re.content)
		time.sleep(1)
		file.close()
		i+=1
