#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import requests
import streamlit as st
import pandas as pd

@st.cache
def get_users_playlist(un):
	headers = {
		'accept': 'application/json',
		'content-type': 'application/x-www-form-urlencoded',
	}
	params = {
		'user': f'{un}',
	}
	response1 = requests.post('http://192.168.11.2:8000/user_playlists/userinfo', params=params, headers=headers).json()

	playlist_box = []

	for i in response1:
		d = {}
		playlist_original_id = i.get("playlist_original_id")
		headers = {
			'accept': 'application/json',
		}
		params = {
			'playlist_original_id': f'{playlist_original_id}',
		}
		response2 = requests.get('http://192.168.11.2:8000/playlist/original', params=params, headers=headers).json()
		date = list(i.get("created_at"))[:17]
		date[4] = "年"
		date[7] = "月"
		date[10] = "日"
		date[13] = "時"
		date[16] = "分"
		date = "".join(date)
		d["create_at"] = date
		d["playlist_name"] = response2.get("playlist_name")
		playlist_box.append(d)
	#-- for
	pb = pd.DataFrame(playlist_box)
	return pb
#--- EoF ---

@st.cache
def get_delete_music(un):
	headers = {
		'accept': 'application/json',
		'content-type': 'application/x-www-form-urlencoded',
	}
	params = {
		'user': f'{un}',
	}
	response1 = requests.post('http://192.168.11.2:8000/user_playlists/userinfo', params=params, headers=headers).json()

	del_box = []

	for i in response1:
		playlist_original_id = i.get("playlist_original_id")
		headers = {
			'accept': 'application/json',
		}
		params = {
			'playlist_original_id': f'{playlist_original_id}',
		}
		response2 = requests.get('http://192.168.11.2:8000/d_playlist_music1/', params=params, headers=headers).json()
		for j in response2:
			headers = {
				'accept': 'application/json',
			}
			d = {}
			music_original_id = j.get("music_original_id")
			response3 = requests.get(f'http://192.168.11.2:8000/musics/{music_original_id}', headers=headers).json()
			date = list(i.get("created_at"))[:17]
			date[4] = "年"
			date[7] = "月"
			date[10] = "日"
			date[13] = "時"
			date[16] = "分"
			date = "".join(date)
			d["Confirm deletion"] = date
			d["music_name"] = response3.get("music_name")
			del_box.append(d)
		#-- for
	#-- for
	del_b = pd.DataFrame(del_box)
	return del_b

#--- EoF ---