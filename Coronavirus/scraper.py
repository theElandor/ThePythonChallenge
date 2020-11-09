import requests
import bs4
from matplotlib import pyplot as plt
def welcome():
	print("Welcome to Matteo's CoronaVirus live update center!")
	print("Press cntrl+c to end the program.")
def calculate_percentage(cases , deaths):
	cases = float(cases)
	deaths = float(deaths)
	result = (deaths/cases)*100
	return round(result,3)
	
def remove_items(test_list , item, item2):
	res = [i for i in test_list if i != item and i != item2]
	return res
def print_data(name,nations_list,sum_of_cases,sum_of_deaths,last_14_days):
	try:
		i = nations_list.index(name)
		print("Nation: "+ name)
		print("- sum of cases: "+ sum_of_cases[i])
		print("- sum of deaths: "+ sum_of_deaths[i])
		print("- cases occurred in the last 14 days: "+ last_14_days[i])
		percentage = calculate_percentage(sum_of_cases[i],sum_of_deaths[i])
		print("- deaths/cases: " + str(percentage)+"%")
	except ValueError:
		print("Nome non valido.")

def max_cases(nations_list , sum_of_cases):
	mass = sum_of_cases[0]
	for i in range(0,len(sum_of_cases)):
		if int(sum_of_cases[i]) > int(mass):
			mass = sum_of_cases[i]
	index = sum_of_cases.index(str(mass))
	print(nations_list[index]+" : "+ str(mass) +"\n")


def max_deaths(nations_list , sum_of_deaths):
	mass = sum_of_cases[0]
	for i in range(0,len(sum_of_deaths)):
		if int(sum_of_deaths[i]) > int(mass):
			mass = sum_of_deaths[i]
	index = sum_of_deaths.index(str(mass))
	print(nations_list[index]+" : "+ str(mass) +"\n")
	
def find_nation_by_name(initials , nations_list):
	results = []
	for nation in nations_list:
		if(nation.startswith(initials)):
			results.append(nation)
	for result in results:
		print(result)

def debug():  ##print list lenght and all the data from the lists
	pass

table_class = "table table-bordered table-condensed table-striped"
URL = "https://www.ecdc.europa.eu/en/geographical-distribution-2019-ncov-cases"
print("Connecting to database...")
res = requests.get(URL)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"html.parser")
rows_list=[]
nations_list=[]
sum_of_cases = []
sum_of_deaths = []
last_14_days=[]
table = soup.find("table")
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
##get the nations list
i = 0 
while i < len(res):
	nations_list.append(res[i])
	i = i + 4 
i = 1
while i < len(res):
	sum_of_cases.append(res[i])
	i = i + 4 
i = 2
while i < len(res):
	sum_of_deaths.append(res[i])
	i = i + 4 
i = 3
while i < len(res):
	last_14_days.append(res[i])
	i = i + 4 


welcome()
while True:
	print("-----------------MAIN MENU-----------------")
	print("1) Press 1 to search the name of a country.")
	print("2) Press 2 to be updated on a specific country.")
	print("3) Press 3 to get the nation with the highest number of cases.")
	print("4) Press 4 to get the nation with the highest number of deaths.")
	print("0) Press 0 to quit.")
	print("-------------------------------------------")
	choice = int(input())
	if choice == 1:
		initials = input("Insert the starting letter: ")
		find_nation_by_name(initials,nations_list)
	elif choice == 2:
		name = input("Enter a country: ")
		print_data(name,nations_list,sum_of_cases,sum_of_deaths,last_14_days)
	elif choice == 3:
		max_cases(nations_list, sum_of_cases)
	elif choice == 4:
		max_deaths(nations_list, sum_of_deaths)
	elif choice == 0:
		break
	else:
		print("Unvalid selection.")


