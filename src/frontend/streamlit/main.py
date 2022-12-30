#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys

import hashlib
import streamlit as st

from views.home import Home
from views.user import User
from libs.lib import Lib

lib_ins = Lib()
home_ins = Home()
user_ins = User()


st.set_page_config(
	page_title="Youtube Diff Checker",
	page_icon="./img/youtube_profile_image.png",
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
	# -- if
	else:
		return False
	# -- else
# --- EoF ---


if page == "HOME":
	st.subheader("HOME")
	home_ins.home_page()
# -- if
elif page == "USER":
	user_name = st.sidebar.text_input("Input User Name")
	user_email = st.sidebar.text_input("Input User Email")
	user_password = st.sidebar.text_input(
		"Input User pauser_password", type="password")
	if st.sidebar.checkbox("LOGIN"):
		r = lib_ins.get_user_info(
			user_name,
			user_email
		)
		user_hashed_pw = r.get( "user_pw" )
		hashed_pw = make_hashes( user_password )
		st.write( hashed_pw )
		result =  check_hashes( hashed_pw, user_hashed_pw )
		if result:
			un = r.get( "user_name" )
			uid = r.get( "uid" )
			user_ins.user_page( un, uid )
		# -- if
		else:
			st.warning("Your password is wrong.")
		# -- else
	# -- if
# -- elif








# End of Script