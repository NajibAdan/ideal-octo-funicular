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
    url = "https://nyaa.si/rss?c=1_2&f=0"
    for x in airing_shows.keys():
        search_url = "https://nyaa.si/rss?c=1_2&f=0&q="
        search_url = search_url + x
        feed = feedparser.parse(search_url).entries
        for i in feed:
            show = x+' '+str(airing_shows[x])
            if show in i.title and '720p' in i.title:
                print(repr(i.title)) + 'torrent found'
                download_and_open(i.title)
            else:
                print 'No new torrents found'
                time.sleep(10)
