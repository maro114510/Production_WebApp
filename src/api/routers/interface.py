#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
from typing import List
from fastapi import APIRouter, HTTPException

from api.cruds.playlists import Playlists
from api.cruds.musics import Musics
from api.cruds.user_playlists import UserPlaylists
from api.cruds.playlist_musics import PlaylistMusics
from api.libs.plalylist_url_handling import Format


p_ins = Playlists()
m_ins = Musics()
up_ins = UserPlaylists()
pm_ins = PlaylistMusics()
f_ins = Format()

router = APIRouter()

@router.post( "/register/all", tags=[ "Register" ] )
async def register_all( uid: int, url: str ):
	### プレイリストの情報を取得
	p_org_id = f_ins.generate_playlist_id( url )
	playlist_info = f_ins.get_plane_data( url )
	playlist_name = playlist_info[ "playlistname" ]
	musics = playlist_info[ "music_id_list" ]

	### プレイリストの登録
	try:
		p_ins.insert_playlist(
			playlist_name,
			p_org_id
		)
	except Exception as e:
		print( "%s" % ( [e.args, ] ), file=sys.stderr )
		raise HTTPException(
			status_code=404,
			detail="",
		)
	#-- except

	### ユーザープレイリストの登録
	try:
		montana = up_ins.user_playlists_insert(
			uid,
			p_org_id
		)
		if montana == 1:
			return 1
		#-- if
	except Exception as e:
		print( "%s" % ( [e.args, ] ), file=sys.stderr )
		raise HTTPException(
			status_code=455,
			detail="Either the uid or the p_org_id is duplicated. Please change it.",
		)
	#-- except

	### 音楽の登録
	try:
		music_list = [ [ i[ "video_name" ], i[ "video_id" ], i[ "video_id" ] ] for i in musics ]
		m_ins.musics_insert(
			music_list
		)
	except Exception as e:
		print( "%s" % ( [e.args, ] ), file=sys.stderr )
		raise HTTPException(
			status_code=404,
			detail="",
		)
	#-- except

	### PlaylistMusicの登録
	try:
		f_list = [
			[
				p_org_id,
				i[ "video_id" ],
				p_org_id,
				i[ "video_id" ],
			] 
			for i in musics
		]
		pm_ins.playlist_musics_bulk_insert( f_list )
	except Exception as e:
		print( "%s" % ( [e.args, ] ), file=sys.stderr )
		raise HTTPException(
			status_code=404,
			detail="Either the user's email address or the user's password is duplicated. Please change it.",
		)
	#-- except

	return 0
#--- EoF ---


# End of Script