from cgitb import text
from http import client
import pandas as pd
import tweepy
import re
from cleaning import clean


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

tweets = client.search_recent_tweets('india', max_results=20)
#print(tweets)

f = list()

for tweets in tweets.data:
   clean_text = re.sub("[^-9A-Za-z ]", "" , tweets.text)
   f.append(clean_text.lower())

print(clean(f))


#for tweet in tweets:
#    print()