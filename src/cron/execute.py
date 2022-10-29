#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import datetime
import sqlite3
import requests

def main(argc, argv):
	params = {
		"date":datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S'),
		"headers":{
			'accept': 'application/json',
			'content-type':"application/x-www-form-urlencode"
		},
		"params":{},
		"json_data":{},
		"dl_list":[],
		"in_list":[],
		"playlist_original_id":"",
		"DB_URL":"/Users/nohiraatsushinozomi/ghq/github.com/maro114510/Production_WebApp/src/database.db",
		"conn":None
	}

	params["conn"] = sqlite3.connect(params["DB_URL"])

	catch_data(params)

	if params["conn"] != None:
		params["conn"].close()
	#-- if

	return 0
#--- EoF ---

def catch_data(params):
	cur = params["conn"].cursor()
	try:
		# DBに格納されているプレイリスト全件取得
		cur.execute(
			"SELECT * FROM playlists;"
		)
		box = [ i[2] for i in cur ]

		# DBプレイリスト内の音楽を全件取得 
		#############
		# for文で回す必要あり
		#############
		for point in box:
			response1 = cur.execute(
				"""
				select * from n_playlist_music \
					where playlist_original_id = "%s"
				""" % point
			)
			# print(response1[0])

			# APIによる現時点でのプレイリスト内の音楽情報を取得
			res = requests.post(f'https://2y5u90.deta.dev/{point}', headers=params["headers"]).json()
			music_list = res.get("music_id_list")

			params["in_list"] = []
			params["dl_list"] = []
			params["playlist_original_id"] = point
			print(params["playlist_original_id"])

			api = [i.get("video_id") for i in music_list]
			# print(api[0])
			db = [ i[2] for i in cur ]

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
					if i[ 2 ] == j:
						params["dl_list"].append(i)
					#-- if
				#-- for
			#-- for

			print(len(params["in_list"]))
			# print(len(params["dl_list"]))

			new_data(params)
			dl_register(params)

			# with open("/workspace/cron/log/execute.log", "a") as f:
				# print(f"[{params['date']}] {point}", file=f)
			#-- with
		#-- for
	except Exception as e:
		# with open("/workspace/cron/log/error.log", "a") as f:	
			# print( f"[{params['date']}]"+"%s" % ( [e.args, ] ), file=f )
		#-- with
		print( "%s" % ( [e.args, ] ), file=sys.stderr )
	#-- except
	return 0
#--- EoF ---


def new_data(params):
	cur = params["conn"].cursor()

	for i in params["in_list"]:
		music_name = i.get("video_name")
		music_original_id = i.get("video_id")
		cur.execute("SELECT * FROM musics WHERE music_original_id='%s'" % music_original_id)

		list1 = cur.fetchone()

		if list1 is None:
			# print(type(list1))
			print(music_name)
			# cur.execute(
			# 	f"""
			# 	INSERT INTO musics (music_name, music_original_id) VALUES ( '{music_name}', '{music_original_id}' );
			# 	"""
			# )
	#-- for
	return 0
#--- EoF ---


def dl_register(params):
	cur = params["conn"].cursor()

	if params["dl_list"]:
		for i in params["dl_list"]:
			date = params["date"]
			pl = params["playlist_original_id"]
			cur.execute(
				f"""
				INSERT INTO d_playlist_music (music_original_id,playlist_original_id,created_at) VALUES ( "{i}", "{pl}", "{date}" );
				""" 
			)
			cur.execute(
				"""
					DELETE FROM d_playlist_music
					WHERE playlist_original_id = '%s'
					AND music_original_id = '%s';
				""" % (params["playlist_original_id"],i)
			)
			# print(response3.status_code)
	return 0
#--- EoF ---






# Entry Point

if __name__ == "__main__":
	sys.exit(main(len(sys.argv), sys.argv))
#-- if

# End of Script