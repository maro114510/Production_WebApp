#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
from typing import List
from fastapi import APIRouter, HTTPException

from api.cruds.playlist_musics import PlaylistMusics
from api.libs.plalylist_url_handling import Format

ins = PlaylistMusics()
f_ins = Format()
router = APIRouter()


@router.get( "/playlist_musics", tags=[ "PlaylistMusics" ] )
async def list_playlist_musics() -> List[ dict ]:
	return ins.get_all_playlist_musics_full_info()
#--- EoF ---

@router.get( "/playlist_musics/playlist_musics", tags=[ "PlaylistMusics" ] )
async def get_playlit_musics_byId( p_org_id: str ) -> List[ dict ]:
	return ins.get_one_playlist_musics_info( p_org_id )
#--- EoF ---

@router.get( "/playlist_musics/d/playlist_musics", tags=[ "PlaylistMusics" ] )
async def get_playlit_musics_byId( p_org_id: str ) -> List[ dict ]:
	return ins.get_del_playlist_musics_info( p_org_id )
#--- EoF ---

@router.post( "/playlist_musics", tags=[ "PlaylistMusics" ] )
async def create_playlist_musics( 
	p_org_id: str,
	m_org_id: str,
) -> int:
	try:
		ins.playlist_musics_insert(
			p_org_id,
			m_org_id,
		)
	except Exception as e:
		print( "%s" % ( [e.args, ] ), file=sys.stderr )
		raise HTTPException(
			status_code=404,
			detail="Either the user's email address or the user's password is duplicated. Please change it.",
		)
	#-- except
	return 0
#--- EoF ---

@router.post( "/playlist_musics/bulk", tags=[ "PlaylistMusics" ] )
async def create_playlist_musics_bulk( url: str ) -> int:
	p_org_id = f_ins.generate_playlist_id( url )
	try:
		music_list = f_ins.to_playlist_musics( url )
		f_list = [
			[
				p_org_id,
				i[ "video_id" ],
				p_org_id,
				i[ "video_id" ],
			] 
			for i in music_list
		]
		ins.playlist_musics_bulk_insert( f_list )
	except Exception as e:
		print( "%s" % ( [e.args, ] ), file=sys.stderr )
		raise HTTPException(
			status_code=404,
			detail="Either the user's email address or the user's password is duplicated. Please change it.",
		)
	#-- except
	return 0
#--- EoF ---

@router.delete( "/playlist_musics", tags=[ "PlaylistMusics" ] )
async def delete_task(
	p_org_id: str,
	m_org_id: str,
) -> int:
	try:
		ins.delete_playlist_musics(
			p_org_id,
			m_org_id
		)
	except Exception as e:
		print( "%s" % ( [e.args, ] ), file=sys.stderr )
		raise HTTPException(
			status_code=404,
			detail="Sorry, Try again.",
		)
	#-- except
	return 0
#--- EoF ---




# End of Script