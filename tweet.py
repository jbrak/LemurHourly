import json
import tweepy
from time import sleep

with open('auth.json') as f:
  data = json.load(f)

consumer_key = data["consumer_key"]
consumer_secret = data["consumer_secret"]
access_token = data["access_token"]
access_token_secret = data["access_token_secret"]

#print(data)
#print(consumer_key,"\n", access_token)

#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)
#api = tweepy.API(auth)

def tweet():
    try:
        api.update_status("Hello World")
    except:
        sleep(600)
        tweet()
