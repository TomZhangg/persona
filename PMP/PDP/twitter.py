import pandas as pd
import tweepy
from twitterConstants import api_key, api_secrets, access_token, access_secret


def load_resources(api_key, api_secrets, access_token, access_secret):
	auth = tweepy.OAuthHandler(api_key,api_secrets)
	auth.set_access_token(access_token,access_secret)
	api = tweepy.API(auth)
	try:
	    api.verify_credentials()
	    user = api.get_user(screen_name='53reborn')	
	    print('Successful Authentication')
	    return api, user
	except:
	    print('Failed authentication')
	    return -1


api, user = load_resources(api_key, api_secrets, access_token, access_secret)

 
class personaTwitter:
	def __init__(self, name, followers_count):
		self.name = name
		self.followers_count = followers_count


# home_tweets = api.home_timeline()
# for tweet in public_tweets:
# 	print(tweet)
# 	break

me = personaTwitter(user.screen_name, user.followers_count)

friends = api.get_friends()
print(friends[0].name)
print(friends[0].screen_name)
print(me.name)
print(me.followers_count)