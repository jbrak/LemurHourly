import json
import tweepy
from time import sleep
from randomFile import randomFile

with open('auth.json') as f:
  data = json.load(f)

consumer_key = data["consumer_key"]
consumer_secret = data["consumer_secret"]
access_token = data["access_token"]
access_token_secret = data["access_token_secret"]

#print(data)
#print(consumer_key,"\n", access_token)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def tweet(accumulator = 0):
    try:
        api.update_with_media(randomFile())
    except Exception as e:
        sleep(300)
        accumulator += 1
        if accumulator < 5:
            tweet(accumulator)
        else:
            print("This tweet has been canceled due to ", e)
