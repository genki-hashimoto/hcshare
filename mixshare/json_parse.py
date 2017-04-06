import json
import urllib

API_URL = "https://api.mixcloud.com/"

def check_country(username):
  html = urllib.request.urlopen(API_URL+username)
  jsonfile = json.loads(html.read().decode('utf-8'))
  if jsonfile['country'] != 'Japan':
    return False
  else:
    return True

def json_parse(url):
  html = urllib.request.urlopen(API_URL+url)
  jsonfile = json.loads(html.read().decode('utf-8'))
  if check_country(jsonfile['user']['username']):
    favorite = jsonfile['favorite_count']
    repost = jsonfile['repost_count']
    play = jsonfile['play_count']
    return [favorite,repost,play]
  else:
    return False
