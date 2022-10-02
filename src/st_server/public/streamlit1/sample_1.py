#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys

import streamlit as st
import time
import numpy as np
import pandas as pd
import requests
import hashlib

from views.user import *

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
	page_title="test_page",
	page_icon="https://licensecounter.jp/devops-hub/docker%20%281%29.png",
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
#-- if

elif page == "USER":
	user_name = st.sidebar.text_input('Input User Name')
	user_password = st.sidebar.text_input('Input User pauser_password',type="password")
	if st.sidebar.checkbox('LOGIN'):
		r = get_user_info(user_name)
		# st.write(r)
		user_hashed_pw = r.get('user_pw')
		# st.write(user_hashed_pw)
		hashed_pwd = make_hashes(user_password)
		result_ = check_hashes(user_password,user_hashed_pw)
		if result_:
			un = r.get('user_name')
			user_page(un)
		#-- if
		else:
			st.warning('パスワードが違います')
		#-- else
	#-- if
#-- elif

elif page == "PLAYLIST":
	with st.form(key="URL"):
		url:str = st.text_input("Playlist URL")
		submit_button = st.form_submit_button(label="送信")
	#-- with

elif page == "USER REGISTER":
	st.markdown("### Create User")
	with st.form(key="USER"):
		user_name = st.text_input("User Name",help="ユーザー名の登録")
	#-- with