import feedparser
from pprint import  pprint
import wget
import os

def download_and_open(i):
    wget.download(i.link, "Torrents/"+i.title+".torrent")
    os.startfile(".\Torrents\\"+i.title+".torrent")

url = "https://nyaa.si/rss?c=1_2&f=0"
search_url = "https://nyaa.si/rss?c=1_2&f=0&q=%title%"
feed = feedparser.parse(url).entries
airing_shows = ["Fate","Shingeki no Bahamut","Kakegurui","Musekinin"]
for  i in feed:
    for x in airing_shows:
        if x in i.title and "720" in i.title:
            pprint(i.title)
            download_and_open(i)
