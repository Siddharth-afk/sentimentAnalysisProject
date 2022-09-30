from cgitb import text
from http import client
import pandas as pd
import tweepy

token = pd.read_csv("twitter_code.csv")

consumer_key = token['API'][0]
consumer_secret = token['API_Secret'][0]
access_token = token['Access_token'][0]
access_token_secret = token['Access_token_secret'][0]

auth = tweepy.OAuth1UserHandler(
   consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

client = tweepy.Client(bearer_token=token['Bearer'][0])

tweets = client.search_recent_tweets('banana', max_results=50)

for tweet in tweets:
    print(tweet[1])
