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
		"params":{}
	}

	catch_data(params)

	return 0
#--- EoF ---


def catch_data(params):
	try:
		# DBに格納されているプレイリスト全件取得
		response = requests.get('http://192.168.11.2:8000/playlists/', headers=params["headers"]).json()
		box = [ i.get("playlist_original_id") for i in response ]


		# DBプレイリスト内の音楽を全件取得 
		#############
		# for文で回す必要あり
		#############
		params["params"] = {
			'playlist_original_id': f'{box[0]}',
		}
		response1 = requests.get('http://192.168.11.2:8000/n_playlist_music1/', params=params["params"], headers=params["headers"])

		# APIによる現時点でのプレイリスト内の音楽情報を取得
		params["headers"]["content-type"] = "application/x-www-form-urlencode"
		res = requests.post(f'https://2y5u90.deta.dev/{box[0]}', headers=params["headers"]).json()
		# TODO 増減に応じた処理を切り出すところから（2022年10月1日）


		with open("/workspace/cron/log/execute.log", "a") as f:
			print(f"[{params['date']}] {box}", file=f)
		#-- with
	except Exception as e:
		with open("/workspace/cron/log/error.log", "a") as f:	
			print( f"[{params['date']}]"+"%s" % ( [e.args, ] ), file=f )
		#-- with
	#-- except
	return 0
#--- EoF ---


# Entry Point

sys.exit(main(len(sys.argv), sys.argv))

# End of Script