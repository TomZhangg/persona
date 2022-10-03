import streamlit as st
import pandas as pd
from PDP.twitter.twitterConstants import api_key, api_secrets, access_token, access_secret
from PDP.twitter.twitterScraper import authenticate, twitterScraper

@st.cache(allow_output_mutation=True)
def load_twitterScraper(api_key, api_secrets, access_token, access_secret):
	return twitterScraper(api_key, api_secrets, access_token, access_secret)

scraper = load_twitterScraper(api_key, api_secrets, access_token, access_secret)
twitter_df = pd.DataFrame(columns=['name', 'tag', 'followers count', 'idols count'])


twitter_search1 = st.text_input(label='@add_twitter_account1')
if twitter_search1 != '':
	try:
		name, screen_name, followers_count, idols_count = scraper.extract_public_traits(twitter_search1)
		temp_df = pd.DataFrame(data=[[name, screen_name, followers_count, idols_count]], 
											columns=['name', 'tag', 'followers count', 'idols count'])
		st.dataframe(temp_df)
	except:
		st.write('invalid')



twitter_search2 = st.text_input(label='@add_twitter_account2')
if twitter_search2 != '':
	try:
		name, screen_name, followers_count, idols_count = scraper.extract_public_traits(twitter_search2)
		temp_df = pd.DataFrame(data=[[name, screen_name, followers_count, idols_count]], 
											columns=['name', 'tag', 'followers count', 'idols count'])
		st.dataframe(temp_df)
	except:
		st.write('invalid')