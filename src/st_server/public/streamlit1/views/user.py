#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import streamlit as st
import requests


def user_page(un):
	st.markdown(f"## Welcome,{un}!")
	st.markdown("### Your register playlist")
	st.markdown("### Your registerd diff")

	st.markdown("### Register new playlist")
	with st.form(key="oppai"):
		url = st.text_input("Input playlist url",)
		submit_button = st.form_submit_button(label="submit")
	#-- with
	# TODO ユーザ登録の現況を見るところから（2022年10月2日）
#--- EoF ---

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