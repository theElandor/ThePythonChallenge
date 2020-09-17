import urllib.request
url = "https://it.wikipedia.org/wiki/Pandemia_di_COVID-19_del_2019-2020"
uf = urllib.request.urlopen(url)
data = uf.read()
print(data)