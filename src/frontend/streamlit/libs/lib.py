#!/usr/bin/env python
#-*- coding: utf8 -*-

import sys
import re
import requests
import pandas as pd
from datetime import datetime


class Lib():
	def __init__( self ):
		self.headers = {
			"accept": "application/json",
		}
		self.domein = "http://192.168.11.2:8000"
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
			f"{self.domein}/users/user",
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
			f"{self.domein}/user_playlists/user_playlists",
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
				f"{self.domein}/playlists/playlist",
				params=params,
				headers=self.headers
			).json()
			p_date = self.format_date( res2.get( "created_at" ) )
			d[ "Playlist Name" ] = res2.get( "playlist_name" )
			d[ "Record start date" ] = p_date
			playlist_box.append( d )
		#-- for
		pb = pd.DataFrame( playlist_box )
		return pb
	#--- EoF ---

	def get_delete_music( self, uid ):
		params = {
			"uid": f"{uid}",
		}
		res1 = requests.get(
			f"{self.domein}/user_playlists/user_playlists",
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
				f"{self.domein}/playlist_musics/d/playlist_musics",
				params=params,
				headers=self.headers
			).json()

			for j in res2:
				p_org_id = j.get( "p_org_id" )
				params = {
					"p_org_id": f"{p_org_id}",
				}
				res3 = requests.get(
					f"{self.domein}/playlists/playlist",
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
					f"{self.domein}/musics/music",
					params=params,
					headers=self.headers
				).json()
				d[ "Music Name" ] = res4.get( "music_name" )
				d[ "Playlist Name" ] = res3.get( "playlist_name" )
				d[ "Deleted date" ] = p_date
				del_box.append( d )
			#-- for
		#-- for
		del_b = pd.DataFrame( del_box )
		return del_b
	#--- EoF ---

	def first_register( self, uid, url ):
		headers = self.headers
		headers[ "content-type" ] = "application/x-www-form-urlencoded"
		params = {
			"uid": f"{uid}",
			"url": f"{url}"
		}
		res = requests.post(
			f"{self.domein}/register/all",
			params=params,
			headers=headers
		).json()
		return res
	#--- EoF ---

	def format_date( self, dt ):
		buf = datetime.strptime( dt, "%Y-%m-%dT%H:%M:%S.%f" )
		return buf.strftime( "%Y/%m/%d" )
	#--- EoF ---

	def get_row_data( self, url ):
		headers = {
			"accept": "application/json",
			"content-type": "application/x-www-form-urlencoded",
		}
		playlist_id = self.generate_playlist_id( url )
		res = requests.post(
			f"https://2y5u90.deta.dev/{playlist_id}",
			headers=headers).json()
		return res
	#--- EoF ---

	def generate_playlist_id( self, url ):
		"""_summary_
		Args:
				url (str): playlist url
		Returns:
				str: playlist original id
		"""
		pattern = "(.*)list=(.*)"
		u = re.search( pattern, url )
		playlist_id = u.group( 2 )
		return playlist_id
	#--- EoF ---

	def register_uer( self, d ):
		params = {
			"user_name": d[ "user_name" ],
			"user_email": d[ "user_email" ],
			"user_pw": d[ "user_pw" ],
		}
		response = requests.post(
			f"{self.domein}/users/",
			headers=self.headers,
			params=params
		)
		return response
	#--- EoF ---
#--- Lib ---


# Entry Point

if __name__ == "__main__":
	ins = Lib()
	sys.exit( ins.main( len( sys.argv ), sys.argv ) )
#-- if



# End of Script