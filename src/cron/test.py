#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import datetime
import sqlite3
import requests

def main(argc, argv):
	DB_URL = "/Users/nohiraatsushinozomi/ghq/github.com/maro114510/Production_WebApp/src/database.db"

	conn = sqlite3.connect(DB_URL)
	cur = conn.cursor()
	cur.execute(
		"select * from playlists;"
	)

	box = [ i[2] for i in cur ]

	cur.execute(
		"""
		select * from n_playlist_music \
			where playlist_original_id = "%s"
		""" % box[1]
	)
	headers = {
		'accept': 'application/json',
		'content-type': 'application/x-www-form-urlencoded',
	}
	res = requests.post(f'https://2y5u90.deta.dev/{box[0]}', headers=headers).json()
	music_list = res.get("music_id_list")

	inlist = []
	dllist = []
	api = [i.get("video_id") for i in music_list]
	db = [ i[2] for i in cur ]

	inc = []
	for i in api:
		if i not in db:
			inc.append(i)
	dl = []
	for i in db:
		if i not in api:
			dl.append(i)
	for i in music_list:
		for j in inc:
			if i.get("video_id") == j:
				inlist.append(i)
			#-- if
		#-- for
	#-- for
	for i in cur:
		for j in dl:
			if i[2] == j:
				dllist.append(i)
			#-- if
		#-- for
	#-- for
	return 0
#--- EoF ---

# Entry Point

if __name__ == "__main__":
	sys.exit(main(len(sys.argv), sys.argv))
#-- if

# End of Script