from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
import json

consumer_key = "TtiE7zqyR5dFnxnMK59YnOyv3"
consumer_secret ="5hY6yrcDirpxKuZzV4iBRegDmCHzR7GWu9iX7OumhRyG5FKzWG"
access_token = "2564580349-eNIvkUZSqBDn18pIzZDFumXNjTtVbj2u0BxdVyr"
access_token_secret = "MybINkpjcnZCTBe6EVLPtGVdO81wZk8jgI4ojArzyMCIk"

class MyStreamListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

    def on_status(self, status):
        print('full_text:', status.extended_tweet['full_text'])

class TweetScraper():

    def __init__(self):
        self.api = api

    def get_current_status_per_page(self,twitter_id):
        status_list = api.user_timeline(twitter_id)
        return [status._json['text'] for status in status_list]

    def get_all_status(self, twitter_id):
        for status in Cursor(api.user_timeline, twitter_id).items():
            print(status._json['text'])

if __name__ == '__main__':
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = API(auth)
    twitter_id = "Petrol_Price"

    tweet = TweetScraper()
    tweet.get_current_status_per_page(twitter_id)
    # tweet.get_all_status(twitter_id)
