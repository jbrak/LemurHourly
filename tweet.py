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
bearer_token = data["bearer_token"]

#print(data)
#print(consumer_key,"\n", access_token)

#Creating V1.1 API object
auth = tweepy.OAuth1UserHandler(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret)
api = tweepy.API(auth)

#Creating V2 Client Object
client = tweepy.Client(bearer_token,
                    access_token=access_token,
                    access_token_secret=access_token_secret,
                    consumer_key=consumer_key,
                    consumer_secret=consumer_secret)

def tweet(accumulator = 0):
    try:
        #Using V1.1 API to create media object
        media = api.media_upload(randomFile())
        #Using V2 API to tweet image
        client.create_tweet(media_ids=[media.media_id_string])

    except Exception as e:
        sleep(300)
        accumulator += 1
        if accumulator < 5:
            tweet(accumulator)
        else:
            print("This tweet has been canceled due to ", e)