#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import re
import requests

class Format():
	def __init__( self ):
		pass
	#--- EoF ---

	def execute( self ):
		self.get_row_data( "https://youtube.com/playlist?list=PLSFrP_aW8LfyUx0QG9b8pJQyg5_wjSUm8" )
		# print( "OK" )
	#--- EoF ---

	def main( self, argc, argv ):
		self.execute()
		return 0
	#--- EoF ---

	def generate_playlist_id( self, url ):
		"""_summary_
		Args:
				url (str): playlist url
		Returns:
				str: playlist original id
		"""
		pattern = "(.*)list=(.*)"
		u = re.search(pattern, url)
		playlist_id = u.group(2)
		return playlist_id
	# --- EoF ---

	def get_row_data( self, url ):
		headers = {
			"accept": "application/json",
			"content-type": "application/x-www-form-urlencoded",
		}
		playlist_id = self.generate_playlist_id(url)
		res = requests.post(
			f"https://2y5u90.deta.dev/{playlist_id}",
			headers=headers
		).json()
		pos = [ [ i[ "video_name" ], i[ "video_id" ], i[ "video_id" ] ] for i in res[ "music_id_list" ] ]
		# print( pos )
		return pos
	# --- EoF ---

	def to_playlist_musics( self, url ):
		headers = {
			"accept": "application/json",
			"content-type": "application/x-www-form-urlencoded",
		}
		playlist_id = self.generate_playlist_id(url)
		res = requests.post(
			f"https://2y5u90.deta.dev/{playlist_id}",
			headers=headers
		).json()

		return res[ "music_id_list" ]
	# --- EoF ---
#--- Format ---


# Entry Point

if __name__ == "__main__":
	ins = Format()
	sys.exit( ins.main( len( sys.argv ), sys.argv ) )
#-- if



# End of Script