import requests
import bs4
import time

print("Benvenuto nello spacecity cinema scraper!")
print("Ecco i film in arrivo allo spacecity cinema: ")
print("---------------------------------------------")
links = []
i = 0
film_list = []
res = requests.get("https://spacecity.it")
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"html.parser")
films = soup.find_all("img", class_ = "m18-csoon-playbill")
for film in films:
	film_list.append(str(film['alt']))
for x in film_list:
	i+=1;
	print(str(i) +") "+ x)