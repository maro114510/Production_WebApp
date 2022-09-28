#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import requests
from time import sleep
import datetime

def main(argc, argv):
	date = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
	try:
		headers = {
			'accept': 'application/json',
		}
		response = requests.get('http://192.168.11.4:8000/playlists/', headers=headers).json()
		box = [ i.get("playlist_original_id") for i in response ]
		with open("/workspace/cron/log/execute.log", "a") as f:
			print(f"[{date}] {box}", file=f)
		#-- with
		# response1 = requests.get()
	except Exception as e:
		with open("/workspace/cron/log/error.log", "a") as f:	
			print( f"[{date}]"+"%s" % ( [e.args, ] ), file=f )
		#-- with
	#-- except
	return 0
#--- EoF ---

def catch_data():
	return 0
#--- EoF ---


# Entry Point

sys.exit(main(len(sys.argv), sys.argv))

# End of Script