import requests
import bs4
from matplotlib import pyplot as plt
def welcome():
	print("CoronaVirus Live update.")
	
def remove_items(test_list , item, item2):
	res = [i for i in test_list if i != item and i != item2]
	return res

table_class = "table table-bordered table-condensed table-striped"
welcome()
URL = "https://www.ecdc.europa.eu/en/geographical-distribution-2019-ncov-cases"
res = requests.get(URL)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"html.parser")
rows_list=[]
nations_list=[]
sum_of_cases = []
sum_of_deaths = []
last_14_days=[]
table = soup.find(class_ = table_class)
print(type(table))
rows = table.find_all("tr")
for x in rows:
	for y in x:
		rows_list.append(str(y.string))
res = remove_items(rows_list,"\n","\xa0")
del res[0:5]
res.remove("Africa")
res.remove("America")
res.remove("Asia")
res.remove("Europe")
res.remove("Oceania")
res.remove("Total")
res.remove("Other")
for i in range(3):
	del res[-1]
for x in res:
	print(x)
##get the nations list
i = 0 
while i < len(res):
	nations_list.append(res[i])
	i = i + 4 
print(nations_list)
print("\n")

i = 1
while i < len(res):
	sum_of_cases.append(res[i])
	i = i + 4 
print(sum_of_cases)
print("\n")

i = 2
while i < len(res):
	sum_of_deaths.append(res[i])
	i = i + 4 
print(sum_of_deaths)
print("\n")

i = 3
while i < len(res):
	last_14_days.append(res[i])
	i = i + 4 
print(last_14_days)
print("\n")

##check if the lists are right
print(len(nations_list))
print(len(sum_of_cases))
print(len(sum_of_deaths))
print(len(last_14_days))

##plot the data
fig = plt.figure(figsize=(100, 100))
plt.bar(nations_list[:20],sum_of_cases[:20])
plt.show()
