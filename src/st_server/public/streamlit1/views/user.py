#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
from urllib.error import HTTPError
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
	st.dataframe(d_r)

	st.markdown("### Register new playlist")
	with st.form(key="key"):
		url = st.text_input("Input playlist url",)
		submit_button = st.form_submit_button(label="submit")
	#-- with
	# TODO ユーザ登録の現況を見るところから（2022年10月2日）
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