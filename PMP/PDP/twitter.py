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

	def extract_public_traits(self, user):
		name = user.name
		screen_name = user.screen_name
		followers_count = user.followers_count
		return name, f'@{screen_name}', followers_count


	def extract_private_traits(self, user, api):
		followers = api.get_followers()
		followers_list = []

		for follower in followers:
			followers_list.append(list(self.extract_public_traits(follower)))

		return followers_list




scraper = twitterScraper()

api, user = scraper.load_resources(api_key, api_secrets, access_token, access_secret)
name, screen_name, followers_count = scraper.extract_public_traits(user)

followers = scraper.extract_private_traits(user, api)
