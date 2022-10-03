import pandas as pd
import tweepy

#
#from twitterConstants import api_key, api_secrets, access_token, access_secret

def authenticate(api_key, api_secrets, access_token, access_secret):
	auth = tweepy.OAuthHandler(api_key,api_secrets)
	auth.set_access_token(access_token,access_secret)
	api = tweepy.API(auth)
	try:
	    api.verify_credentials()
	    print('Successful Authentication')
	    return api
	except:
	    print('Failed authentication')
	    return -1

class twitterScraper:
	def __init__(self, api_key, api_secrets, access_token, access_secret):
		self.api_key = api_key
		self.api_secrets = api_secrets
		self.access_token = access_token
		self.access_secret = access_secret
		self.api = authenticate(api_key,api_secrets,access_token, access_secret)


	def extract_public_traits(self, tag):
		user = self.api.get_user(screen_name=tag)

		name = user.name
		screen_name = user.screen_name
		followers_count = user.followers_count
		idols_count = user.friends_count
		return name, f'@{screen_name}', followers_count, idols_count


	#TODO: implememnt private extract features

	# def extract_private_traits(self, user, api):
	# 	followers = api.get_followers()
	# 	followers_list = []

	# 	for follower in followers:
	# 		followers_list.append(list(self.extract_public_traits(follower)))

	# 	return followers, pd.DataFrame(followers_list)




# scraper = twitterScraper(api_key, api_secrets, access_token, access_secret)

# print(scraper.extract_public_traits('elonmusk'))



# api, user = scraper.authenticate(api_key, api_secrets, access_token, access_secret)
# name, screen_name, followers_count, idols_count = scraper.extract_public_traits(user)

# print(name, screen_name, followers_count, idols_count)


#print(dir(user))
# f, followers = scraper.extract_private_traits(user, api)
# print(followers)

# print()
# print('follower ids')
# print(f[0].follower_ids)

# print()
# print('followers')
# print(f[0].followers)

# print()
# print('following')
# print(f[0].following)