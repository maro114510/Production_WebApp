#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import re
from datetime import datetime
import requests
import streamlit as st
import pandas as pd


class Lib():
	def __init__( self ):
		self.headers = {
			"accept": "application/json",
		}
	#--- EoF ---

	def execute( self ):
		print( "OK" )
	#--- EoF ---

	def main( self, argc, argv ):
		self.execute()
		return 0
	#--- EoF ---

	def get_user_info( self, user_name, user_email ):
		params = {
			"user_name": f"{user_name}",
			"user_email": f"{user_email}",
		}

		response = requests.get(
			"http://192.168.11.2:8000/users/user",
			params=params,
			headers=self.headers
		).json()
		return response
	#--- EoF ---

	def get_users_playlist( self, uid ):
		params = {
			"uid": f"{uid}",
		}
		res1 = requests.get(
			"http://192.168.11.2:8000/user_playlists/user_playlists",
			params=params,
			headers=self.headers,
		).json()

		playlist_box = []

		for i in res1:
			d = {}
			p_org_id = i.get( "p_org_id" )
			params = {
				"p_org_id": f"{p_org_id}",
			}
			res2 = requests.get(
				"http://192.168.11.2:8000/playlists/playlist",
				params=params,
				headers=self.headers
			).json()
			p_date = self.format_date( res2.get( "created_at" ) )
			d[ "Playlist Name" ] = res2.get( "playlist_name" )
			d[ "Record start date" ] = p_date
			playlist_box.append( d )
		# -- for
		pb = pd.DataFrame( playlist_box )
		pb.index = pd.RangeIndex( start=1 )
		return pb
	#--- EoF ---

	def get_delete_music( self, uid ):
		params = {
			"uid": f"{uid}",
		}
		res1 = requests.get(
			"http://192.168.11.2:8000/user_playlists/user_playlists",
			params=params,
			headers=self.headers,
		).json()

		del_box = []

		for i in res1:
			p_org_id = i.get( "p_org_id" )
			params = {
				"p_org_id": f"{p_org_id}",
			}
			res2 = requests.get(
				"http://192.168.11.2:8000/playlist_musics/d/playlist_musics",
				params=params,
				headers=self.headers
			).json()

			for j in res2:
				p_org_id = j.get( "p_org_id" )
				params = {
					"p_org_id": f"{p_org_id}",
				}
				res3 = requests.get(
					"http://192.168.11.2:8000/playlists/playlist",
					params=params,
					headers=self.headers
				).json()

				p_date = self.format_date( j.get( "created_at" ) )
				d = {}
				m_org_id = j.get( "m_org_id" )
				params = {
					"m_org_id": f"{m_org_id}",
				}
				res4 = requests.get(
					"http://192.168.11.2:8000/musics/music",
					params=params,
					headers=self.headers
				).json()
				d[ "Music Name" ] = res4.get( "music_name" )
				d[ "Playlist Name" ] = res3.get( "playlist_name" )
				d[ "Deleted date" ] = p_date
				del_box.append( d )
			# -- for
		# -- for
		del_b = pd.DataFrame( del_box )
		return del_b
	#--- EoF ---

	def format_date( self, dt ):
		buf = datetime.strptime( dt, "%Y-%m-%dT%H:%M:%S.%f" )
		return buf.strftime( "%Y/%m/%d" )
	#--- EoF ---
#--- Lib ---


# Entry Point

if __name__ == "__main__":
	ins = Lib()
	sys.exit( ins.main( len( sys.argv ), sys.argv ) )
#-- if



# End of Script