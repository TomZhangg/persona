import streamlit as st
import pandas as pd
from PDP.twitter.twitterConstants import api_key, api_secrets, access_token, access_secret
from PDP.twitter.twitterScraper import authenticate, twitterScraper


@st.cache(allow_output_mutation=True)
def load_twitterScraper(api_key, api_secrets, access_token, access_secret):
	return twitterScraper(api_key, api_secrets, access_token, access_secret)


#st.title('Persona')





scraper = load_twitterScraper(api_key, api_secrets, access_token, access_secret)

if 'twitter_df' not in st.session_state:
	st.session_state.twitter_df = pd.DataFrame(columns=['name', 'tag', 'followers count', 'idols count'])


display_twitter = st.checkbox('Twitter', value=False)

if display_twitter:

	twitter_search1 = st.text_input(label='@add_twitter_account')
	if twitter_search1 != '':
		try:
			name, screen_name, followers_count, idols_count = scraper.extract_public_traits(twitter_search1)
			temp_df = pd.DataFrame(data=[[name, screen_name, followers_count, idols_count]], 
												columns=['name', 'tag', 'followers count', 'idols count'])
			st.session_state.twitter_df = st.session_state.twitter_df.append(temp_df)
		except:
			st.write('invalid')

	if len(st.session_state.twitter_df) > 0:
		st.session_state.twitter_df = st.session_state.twitter_df.tail(3)
		st.table(st.session_state.twitter_df.reset_index(drop=True))

else:
	pass




display_insta = st.checkbox('Instagram', value=False)

if display_insta:
	insta_search1 = st.text_input(label='@add_instagram_account')




display_tiktok = st.checkbox('TikTok', value=False)

display_twitch = st.checkbox('Twitch', value=False)

display_youtube= st.checkbox('YouTube', value=False)



# twitter_search2 = st.text_input(label='@add_twitter_account2')
# if twitter_search2 != '':
# 	try:
# 		name, screen_name, followers_count, idols_count = scraper.extract_public_traits(twitter_search2)
# 		temp_df = pd.DataFrame(data=[[name, screen_name, followers_count, idols_count]], 
# 											columns=['name', 'tag', 'followers count', 'idols count'])
# 		st.dataframe(temp_df)
# 	except:
# 		st.write('invalid')