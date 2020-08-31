import urllib.request
import pickle
url = "http://www.pythonchallenge.com/pc/def/banner.p"
data = pickle.load(urllib.request.urlopen(url))
for line in data :
    print("".join([k*v for k , v in line]))



