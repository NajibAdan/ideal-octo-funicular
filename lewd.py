import feedparser
from pprint import  pprint
import wget
import os
import time

def download_and_open(i):
    if os.path.isfile("\Animu Torrents\\"+i.title+".torrent"):
        print i.title + ' has already been downloaded'
    else:
        print 'Downloading '+ i.title
        wget.download(i.link, "\Animu Torrents\\"+i.title+".torrent")
        os.startfile("\Animu Torrents\\"+i.title+".torrent")


while 1:
    time.sleep(10)
    url = "https://nyaa.si/rss?c=1_2&f=0"
    search_url = "https://nyaa.si/rss?c=1_2&f=0&q=%title%"
    feed = feedparser.parse(url).entries
    airing_shows = ["Fate","Shingeki no Bahamut","Kakegurui","Musekinin","Ballroom e Youkoso"]
    for  i in feed:
        for x in airing_shows:
            if x in i.title and "720" in i.title:
                download_and_open(i)
