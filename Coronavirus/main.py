from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
import requests
import bs4

def remove_items(test_list, item, item2):
    res = [i for i in test_list if i != item and i != item2]
    return res
def get_data(data, name,nations_list,sum_of_cases,sum_of_deaths,last_14_days):  ##nation data is going to be a string
    i = nations_list.index(name)
    data.append(name)
    data.append(sum_of_cases[i])
    data.append(sum_of_deaths[i])
    data.append(last_14_days[i])



table_class = "table table-bordered table-condensed table-striped"
URL = "https://www.ecdc.europa.eu/en/geographical-distribution-2019-ncov-cases"
print("Connecting to database...")
res = requests.get(URL)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")
rows_list = []
nations_list = []
sum_of_cases = []
sum_of_deaths = []
last_14_days = []
nation_data=[]
table = soup.find("table")
rows = table.find_all("tr")
for x in rows:
    for y in x:
        rows_list.append(str(y.string))
res = remove_items(rows_list, "\n", "\xa0")
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


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/send', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        recv = request.form["nm"]
        print("Command received: "+ str(recv))
        return redirect(url_for('compute', command=recv))  ##u have to use the function
    else:
        return render_template("input.html")
@app.route('/send_nation', methods=["POST", "GET"])
def get_nation():
    if request.method=="POST":
        recv = request.form["nm"]
        print("Nation received: "+str(recv))
        nation_data = []
        get_data(nation_data, recv, nations_list, sum_of_cases, sum_of_deaths, last_14_days)
        return render_template('show_nation.html', my_data=nation_data)
    else:
        return render_template("get_nation.html")


@app.route("/command/<command>")
def compute(command):
    if command == str(1):
        return render_template('com.html', nations_list=nations_list)
    if command == str(2):
        return redirect(url_for('get_nation'))

        pass

    else:
        return "<h1> Invalid command </h1>"


@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == '__main__':
    app.run(debug=True)


