import tweepy


#Twitter API credentials
consumer_key = "xhdyt2TNZcKb0vn8dDjsmDpdW"
consumer_secret = "S5i33XrS0CyqLxJUVLQhY7PVr5TwpTv7nJY3XnlbkKhQgKT9X5"
access_token = "UywoAnl6hnPVCymcnwciWp4ljdMKfub"
access_token_secret = "3CS4Vd4Lg9wZHMnIxYoh4u4Pij0nr7BZvUWumEToa5Idb"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


user = api.get_user('elonmusk')

def last_tweets():
    
