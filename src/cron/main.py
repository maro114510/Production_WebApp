#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import requests
from time import sleep
import datetime


def main(argc, argv):
	params = {
		"date":datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S'),
		"headers":{
			'accept': 'application/json',
		},
		"params":{},
		"json_data":{},
		"dl_list":[],
		"in_list":[],
		"playlist_original_id":""
	}

	catch_data(params)

	return 0
#--- EoF ---


def catch_data(params):
	try:
		# DBに格納されているプレイリスト全件取得
		response = requests.get('http://192.168.11.2:8000/playlists/', headers=params["headers"]).json()
		box = [ i.get("playlist_original_id") for i in response ]
		# print(box[0])

		# DBプレイリスト内の音楽を全件取得 
		#############
		# for文で回す必要あり
		#############
		for point in box:
			params["params"] = {}
			params["params"] = {
				'playlist_original_id': f'{point}',
			}
			params["playlist_original_id"] = box[0]
			response1 = requests.get('http://192.168.11.2:8000/n_playlist_music1/', params=params["params"], headers=params["headers"]).json()
			# print(response1[0])

			# APIによる現時点でのプレイリスト内の音楽情報を取得
			params["headers"]["content-type"] = "application/x-www-form-urlencode"
			res = requests.post(f'https://2y5u90.deta.dev/{point}', headers=params["headers"]).json()
			music_list = res.get("music_id_list")

			params["in_list"] = []
			params["dl_list"] = []

			api = [i.get("video_id") for i in music_list]
			# print(api[0])
			db = [ i.get("music_original_id") for i in response1 ]

			inc = []
			for i in api:
				if i not in db:
					inc.append(i)
				#-- if
			#-- for
			dl = []
			for i in db:
				if i not in api:
					dl.append(i)
				#-- if
			#-- for

			for i in music_list:
				for j in inc:
					if i.get("video_id") == j:
						params["in_list"].append(i)
					#-- if
				#-- for
			#-- for
			for i in response1:
				for j in dl:
					if i.get("music_original_id") == j:
						params["dl_list"].append(i)
					#-- if
				#-- for
			#-- for

			# print(params["dl_list"])

			new_data(params)
			dl_register(params)

			with open("/workspace/cron/log/execute.log", "a") as f:
				print(f"[{params['date']}] {point}", file=f)
			#-- with
		#-- for
	except Exception as e:
		with open("/workspace/cron/log/error.log", "a") as f:	
			print( f"[{params['date']}]"+"%s" % ( [e.args, ] ), file=f )
		#-- with
	#-- except
	return 0
#--- EoF ---

def dl_register(params):
	params["headers"] = {}
	params["headers"]["accept"] = "application/json"
	# print(params["headers"])

	if params["dl_list"]:
		for i in params["dl_list"]:
			data = i.get("music_original_id")
			json_data = {
				'playlist_info': {
					'playlist_name': 'string',
					'playlist_original_id': f'{params["playlist_original_id"]}',
				},
				'music_in': {
					'music_name': 'string',
					'music_original_id': f'{data}',
				},
			}
			response2 = requests.post('http://192.168.11.2:8000/d_playlist_music/', headers=params["headers"], json=json_data)
			# print( response2.status_code)

			d = {
				'playlist_original_id': f'{params["playlist_original_id"]}',
				'music_original_id': f'{data}',
			}

			# print(params["headers"])
			response3 = requests.delete('http://192.168.11.2:8000/n_playlist_music/', params=d, headers=params["headers"])
			# print(response3.status_code)
	return 0
#--- EoF ---

def new_data(params):
	params["headers"] = {}
	params["headers"]["accept"] = "application/json"

	for i in params["in_list"]:
		music_name = i.get("video_name")
		music_original_id = i.get("video_id")
		json_data = {
			'music_name': f'{music_name}',
			'music_original_id': f'{music_original_id}',
		}
		# print(json_data)

		response = requests.post('http://192.168.11.2:8000/musics/', headers=params["headers"], json=json_data)
		sleep(0.5)
	#-- for
	return 0
#--- EoF ---

# Entry Point

sys.exit(main(len(sys.argv), sys.argv))

# End of Script