#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import streamlit as st

from libs.lib import *


def home_page():
	st.title("Welcome to Youtube Diff Checker!!")
	st.caption("This application is currently under development.")
	
	#st.markdown("## !!!!!  The user registration function is currently unavailable.")
	st.header("Overview of this application😀")
	st.subheader("Capture the missing songs in your playlist")

	# TODO ランダムでおすすめ曲の表示をする
	st.write("#### This is my favorite song.")
	with st.expander("Open to see"):
		st.video("https://youtu.be/CH7gf1rg49Y")
	#-- with

	col1,col2 = st.columns(2)
	col1.subheader("Content")
	col1.write(
		"""
		* **This application is a web application that requires user registration.**
		* Register a playlist URL and we will monitor the playlist daily.
		* You can also view the songs and song IDs included in the playlist without having to register as a user!
		* We are working on a future feature that will allow users to be notified by registered email.
		"""
	)
	col2.subheader("Background of Production")
	col2.write(
		"""
		* I am a heavy user of Youtube
		* There are about 10 hours of viewing time per day
		* The playlists alone exceed 100 and I can no longer manage my music and videos!
		* I'm sure you've felt uncomfortable listening to music on your playlist too
		* That is because the music is private or deleted.
		* If the number of songs in a playlist you normally listen to is small, you can quickly see what has disappeared, but this is not the case.
		* So we decided to create this web application.
		"""
	)
	
	tag1, tag2 = st.tabs(["About tech", "About me"])
	tag1.subheader("About the technologies and frameworks used")
	tag1.write(
		"""
		* Python 3.9
		* FastAPI 0.85
		* uvicorn
		* SQLAlchemy 1.4
		* Docker
		* MySQL
		* Streamlit
		* Nginx
		* YoutubeAPI
		"""
	)
	tag2.subheader("Contact Developer")
	tag2.write(
		"""
		* Email : parcels-dollar.0p@icloud.com
		* Facebook : https://www.facebook.com/profile.php?id=100074151648343
		* github : https://github.com/maro114510 
		"""
	)

	st.text(" © 2022 Atsuki Nohira ")

	return 0
#--- EoF ---



# End of Script
