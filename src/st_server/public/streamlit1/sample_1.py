#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys

import streamlit as st
import time
import numpy as np
import pandas as pd
import hashlib

from views.user import *
from views.playlist import *
from views.user_register import *
from views.home import home_page

from libs.lib import register_uer

def make_hashes(password):
	return hashlib.md5(str.encode(password)).hexdigest()
#--- EoF ---

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	#-- if
	else:
		return False
	#-- else
#--- EoF ---


st.set_page_config(
	page_title="Youtube Diff Checker",
	page_icon="./img/youtube_profile_image.png",
	layout="wide",
	menu_items={
		"Get help":None,
		"Report a Bug":None,
		"About":None
	}
)

page_list = ["HOME","USER","USER REGISTER","PLAYLIST"]
page = st.sidebar.selectbox('Choose your page',page_list)

if page == "HOME":
	st.subheader('HOME')
	home_page()
#-- if

elif page == "USER":
	user_name = st.sidebar.text_input('Input User Name')
	user_password = st.sidebar.text_input('Input User pauser_password',type="password")
	if st.sidebar.checkbox('LOGIN'):
		r = get_user_info(user_name)
		if r == None:
			st.error(f"{user_name} is not found")
			st.text("Prease register")
		#-- if
		else:
			user_hashed_pw = r.get('user_pw')
			# st.write(user_hashed_pw)
			hashed_pwd = make_hashes(user_password)
			result_ = check_hashes(user_password,user_hashed_pw)
			if result_:
				un = r.get('user_name')
				user_page(un)
			#-- if
			else:
				st.warning('Your password is wrong.')
			#-- else
		#-- else
	#-- if
#-- elif

elif page == "PLAYLIST":
	st.markdown("### Info")
	st.write("The song contents of the playlist you want to check can be displayed at once.")
	with st.form(key="URL"):
		url:str = st.text_input("Playlist URL")
		submit_button = st.form_submit_button(label="Submit")
		if submit_button:
			playlist_info_page(url)
		#-- if
	#-- with
#-- elif

elif page == "USER REGISTER":
	st.markdown("### Create User")
	with st.form(key="USER"):
		d = {}

		user_name = st.text_input("User Name",help="Username you wish to register")
		d["user_name"] = user_name
		user_email = st.text_input("User Email",help="Email address you would like us to notify you about")
		d["user_email"] = user_email
		user_pw = st.text_input('User Password',help="Register password in alphanumeric characters",type="password")
		d["user_pw"] = user_pw

		submit_button = st.form_submit_button(label="Submit")
		if submit_button:
			r = register_uer(d)
			if r.status_code == 200:
				st.success(
					f"""Hello, {user_name}!
					Registration is complete!
					"""
				)
			#-- if
			elif r.status_code == 404:
				st.error(f"You registered {user_name}, or {user_email} is duplicated.Sorry, please change to a different name and email.")
			#-- elif
			else:
				st.error(
					"""
					I am sorry.
					Unexpected error. Please contact the developer.
					"""
				)
			#-- else
		#-- if
	#-- with
#-- elif


# End of Script