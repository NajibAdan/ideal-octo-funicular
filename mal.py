import json
import requests
def placeholder():
    dict = {}
    username = raw_input('Enter MAL username: ')
    password = raw_input('Enter password: ')

    url = 'http://localhost:8000/2.1/animelist/' + username
    idurl = 'http://localhost:8000/2.1/anime/'
    r = requests.get(url,auth=(username,password))
    response = json.loads(r.text)
    for i in response['anime']:
        if i['status'] == 'currently airing' and i['watched_status'] == 'watching':
            dict[i['title']] = i['watched_episodes']+1
    return dict
