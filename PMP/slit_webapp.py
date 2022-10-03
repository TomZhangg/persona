import streamlit as st
import pandas as pd
from PDP.twitter.twitterConstants import api_key, api_secrets, access_token, access_secret
from PDP.twitter.twitterScraper import authenticate, twitterScraper


scraper = twitterScraper(api_key, api_secrets, access_token, access_secret)

search = st.text_input(label='@add_twitter_account')
if search != '':
	try:
		name, screen_name, followers_count, idols_count = scraper.extract_public_traits(search)
		st.write(f'{name}, {screen_name}, {followers_count}, {idols_count}')
		st.dataframe(pd.DataFrame())
	except:
		st.write('invalid')



#st.write(f"{name}, {screen_name}, {followers_count}, {idols_count}")
# pd.Data