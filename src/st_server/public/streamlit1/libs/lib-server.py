#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import re
import requests
import streamlit as st
import pandas as pd


def get_users_playlist(un):
	headers = {
		'accept': 'application/json',
		'content-type': 'application/x-www-form-urlencoded',
	}
	params = {
		'user': f'{un}',
	}
	response1 = requests.post('http://www.youtube-diff-checker.com:8000/user_playlists/userinfo', params=params, headers=headers).json()

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
		response2 = requests.get('http://www.youtube-diff-checker.com:8000/playlist/original', params=params, headers=headers).json()
		#date = list(i.get("created_at"))[:17]
		#date[4] = "年"
		#date[7] = "月"
		#date[10] = "日"
		#date[13] = "時"
		#date[16] = "分"
		#date = "".join(date)
		#d["create_at"] = date
		d["playlist_name"] = response2.get("playlist_name")
		playlist_box.append(d)
	#-- for
	pb = pd.DataFrame(playlist_box)
	return pb
#--- EoF ---


def get_delete_music(un):
	headers = {
		'accept': 'application/json',
		'content-type': 'application/x-www-form-urlencoded',
	}
	params = {
		'user': f'{un}',
	}
	response1 = requests.post('http://www.youtube-diff-checker.com:8000/user_playlists/userinfo', params=params, headers=headers).json()

	del_box = []

	for i in response1:
		playlist_original_id = i.get("playlist_original_id")
		headers = {
			'accept': 'application/json',
		}
		params = {
			'playlist_original_id': f'{playlist_original_id}',
		}
		response2 = requests.get('http://www.youtube-diff-checker.com:8000/d_playlist_music1/', params=params, headers=headers).json()
		for j in response2:
			headers = {
				'accept': 'application/json',
			}
			d = {}
			music_original_id = j.get("music_original_id")
			response3 = requests.get(f'http://www.youtube-diff-checker.com:8000/musics/{music_original_id}', headers=headers).json()
			params = {
    				'playlist_original_id': 'PLSFrP_aW8Lfwohd6WIMTjz4XIU3jgpiyG',
			}
			response4 = requests.get('http://www.youtube-diff-checker.com:8000/playlist/original', headers=headers, params=params).json()
			playlist_name = response4.get("playlist_name")
			d["playlist_id"] = playlist_name
			d["music_name"] = response3.get("music_name")
			del_box.append(d)
		#-- for
	#-- for
	del_b = pd.DataFrame(del_box)
	return del_b
#--- EoF ---


def register(un,url):
	headers = {
		'accept': 'application/json',
	}
	params = {
		'url': f'{url}',
	}
	json_data = {
		'user_name': f'{un}',
		'user_email': 'user@gmail.com',
		'user_pw': 'string',
	}
	response = requests.post('http://www.youtube-diff-checker.com:8000/register/', params=params, headers=headers, json=json_data)
	return response
#--- EoF ---

def generate_playlist_id(url):
	"""_summary_

	Args:
		url (str): playlist url

	Returns:
		str: playlist original id
	"""
	pattern = "(.*)list=(.*)"
	u = re.search(pattern,url)
	playlist_id = u.group(2)
	return playlist_id
# --- EoF ---

def get_row_data(url):
	headers = {
		'accept': 'application/json',
		'content-type': 'application/x-www-form-urlencoded',
	}
	playlist_id = generate_playlist_id(url)
	res = requests.post(f'https://2y5u90.deta.dev/{playlist_id}', headers=headers).json()
	return res
#--- EoF ---

def register_uer(d):
	headers = {
		'accept': 'application/json',
	}
	json_data = {
		'user_name': d["user_name"],
		'user_email': d["user_email"],
		'user_pw': d["user_pw"],
	}
	response = requests.post('http://www.youtube-diff-checker.com:8000/users/', headers=headers, json=json_data)
	return response
#--- EoF ---


# End of Script
