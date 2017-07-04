import xmltodict
import requests
from pprint import pprint

url = "https://myanimelist.net/api/anime/search.xml?q=bleach"
r = requests.get(url, auth =(username,password))
result= xmltodict.parse(r.content)
for i in result['anime']['entry']:
    print(i['title'])
