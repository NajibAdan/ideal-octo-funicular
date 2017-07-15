import feedparser
from pprint import  pprint
import wget
import os
import time
import mal
def download_and_open(i):
    if os.path.isfile("\Animu Torrents\\"+i.title+".torrent"):
        print i.title + ' has already been downloaded'
    else:
        print 'Downloading '+ i.title
        wget.download(i.link, "Animu Torrents\\"+i.title+".torrent")
        os.startfile(".\Animu Torrents\\"+i.title+".torrent")
airing_shows = mal.placeholder()
while 1:

    time.sleep(10)
    url = "https://nyaa.si/rss?c=1_2&f=0"
    search_url = "https://nyaa.si/rss?c=1_2&f=0&q=%title%"
    feed = feedparser.parse(url).entries
    for  i in feed:
        for x in airing_shows.keys():
            if show in i.title and "720" in i.title:
                download_and_open(i)
