#!/usr/bin/env python
#-*- coding: utf8 -*-

import sys

import hashlib
import streamlit as st

from views.home import Home
from views.user import User
from views.playlist import Playlist
from libs.lib import Lib

lib_ins = Lib()
home_ins = Home()
user_ins = User()
p_ins = Playlist()


st.set_page_config(
	page_title="Youtube Diff Checker",
	# page_icon="./img/youtube_profile_image.png",
	layout="wide",
	menu_items={
		"Get help": None,
		"Report a Bug": None,
		"About": None
	}
)

page_list = [ "HOME", "USER", "USER REGISTER", "PLAYLIST" ]
page = st.sidebar.selectbox( "Choose your page", page_list )

def make_hashes( password: str ):
	return hashlib.md5( password.encode() ).hexdigest()
#--- EoF ---

def check_hashes( password, hashed_text ):
	if password == hashed_text:
		return hashed_text
	#-- if
	else:
		return False
	#-- else
#--- EoF ---


if page == "HOME":
	st.subheader("HOME")
	home_ins.home_page()
#-- if
elif page == "USER":
	user_name = st.sidebar.text_input("Input User Name")
	user_email = st.sidebar.text_input("Input User Email")
	user_password = st.sidebar.text_input("Input User pauser_password", type="password")
	if user_password == "" or user_name == "" or user_email == "":
		st.warning( "Please fill in all the fields." )
	#-- if
	if st.sidebar.checkbox("LOGIN"):
		try:
			r = lib_ins.get_user_info(
				user_name,
				user_email
			)
			user_hashed_pw = r.get( "user_pw" )
			hashed_pw = make_hashes( user_password )
			result =  check_hashes( hashed_pw, user_hashed_pw )
			if result:
				un = r.get( "user_name" )
				uid = r.get( "uid" )
				user_ins.user_page( un, uid )
			#-- if
			else:
				st.warning( "Your password is wrong." )
			#-- else
		except Exception as e:
			st.error( e )
		#-- except
	#-- if
#-- elif

elif page == "PLAYLIST":
	st.markdown("### Info")
	st.write(
		"The song contents of the playlist you want to check can be displayed at once."
	)
	with st.form( key = "URL" ):
		url: str = st.text_input( "Playlist URL" )
		submit_button = st.form_submit_button( label = "Submit" )
		if submit_button:
			p_ins.playlist_info_page( url )
		#-- if
	#-- with
#-- elif

elif page == "USER REGISTER":
	st.markdown( "### Create User" )
	with st.form( key = "USER" ):
		d = {}

		user_name = st.text_input(
			"User Name", help = "Username you wish to register"
		)
		d[ "user_name" ] = user_name
		user_email = st.text_input(
			"User Email",
			help="Email address you would like us to notify you about"
		)
		d[ "user_email" ] = user_email
		user_pw = st.text_input(
			"User Password",
			help="Register password in alphanumeric characters",
			type="password"
		)
		d[ "user_pw" ] = user_pw

		submit_button = st.form_submit_button( label = "Submit" )
		if submit_button:
			try:
				r = lib_ins.register_uer( d )
				if r.status_code == 200:
					st.success(
						f"""Hello, {user_name}!
						Registration is complete!
						"""
					)
				#-- if
				elif r.status_code == 404:
					st.error(
						f"You registered {user_name}, or {user_email} is duplicated.Sorry, please change to a different name and email."
					)
				#-- elif
			except Exception as e:
				st.error(
					"""
					I am sorry.
					Unexpected error. Please contact the developer.
					"""
				)
			#-- else
		#-- if
		else:
			st.warning( "Please fill in all the fields." )
		#-- else
	#-- with
#-- elif







# End of Script