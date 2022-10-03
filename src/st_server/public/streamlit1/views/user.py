#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import streamlit as st
import requests

from libs.lib import *


def user_page(un):
	st.markdown(f"## Welcome, {un}!")
	st.markdown("### Your register playlist")
	try:
		r = get_users_playlist(un)
	except Exception as e:
		st.warning(
		"""
		Sorry, something is wrong and I can't display it.
		Please try again in a few hours.
		"""
		)
	#-- except
	st.table(r)
	st.markdown("### Your registerd diff")
	try:
		d_r = get_delete_music(un)
	except Exception as e:
		st.warning(
		"""
		Sorry, something is wrong and I can't display it.
		Please try again in a few hours.
		"""
		)
	#-- except
	st.dataframe(d_r)

	st.markdown("### Register new playlist")
	with st.form(key="key"):
		url = st.text_input("Input playlist url",)
		submit_button = st.form_submit_button(label="submit")
		if submit_button:
			res = register(un,url)
			if res.status_code == 200:
				if len(res.json()) == 0:
					st.info("The playlist with the URL you sent is already registered")
				#-- if
				else:
					st.success("Registration Complete")
				#-- else
			#-- if
			else:
				st.error(
					"""
					Registration failed.
					Please check if the URL is correct and the communication environment is correct.
					"""
				)
			#-- else
		#-- if
	#-- with
#--- EoF ---

@st.cache
def get_user_info(user_name):
	headers = {
		'accept': 'application/json',
	}

	params = {
		'user_name': f'{user_name}',
	}

	response = requests.get('http://192.168.11.2:8000/users/name/', params=params, headers=headers).json()
	return response
#--- EoF ---



# End of Script