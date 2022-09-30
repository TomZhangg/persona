import pandas as pd
import tweepy
from twitterConstants import api_key, api_secrets, access_token, access_secret



class twitterScraper:
	def load_resources(self, api_key, api_secrets, access_token, access_secret):
		auth = tweepy.OAuthHandler(api_key,api_secrets)
		auth.set_access_token(access_token,access_secret)
		api = tweepy.API(auth)
		try:
		    api.verify_credentials()
		    user = api.get_user(screen_name='AndrewYang')	
		    print('Successful Authentication')
		    return api, user
		except:
		    print('Failed authentication')
		    return -1

	def extract_base_traits(self, user, api):
		name = user.name
		screen_name = user.screen_name
		followers_count = user.followers_count
		return name, screen_name, followers_count


scraper = twitterScraper()

api, user = scraper.load_resources(api_key, api_secrets, access_token, access_secret)
name, screen_name, followers_count = scraper.extract_base_traits(user, api)
 


# class personaTwitter:
# 	def __init__(self, name, screen_name, followers_count):
# 		self.name = name
# 		self.screen_name = screen_name
# 		self.followers_count = followers_count




# me = personaTwitter(name, screen_name, followers_count)
# print(f'{me.name} | @{me.screen_name}: {me.followers_count} followers')



