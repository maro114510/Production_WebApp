#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
from fastapi import APIRouter, HTTPException

from api.cruds.playlists import Playlists

ins = Playlists()
router = APIRouter()


@router.get( "/playlists/", tags=[ "Playlists" ] )
async def list_playlists():
	return ins.get_all_playlists_full_info()
#--- EoF ---


@router.get( "/playlists/playlist", tags=[ "Playlists" ] )
async def get_playlist_info( p_org_id: str ):
	return ins.get_one_playlist_info( p_org_id )
#--- EoF ---

@router.post( "/playlists/", tags=[ "Playlists" ] )
async def create_playlist( 
	playlist: str,
	p_org_id: str
) -> int:
	try:
		ins.insert_playlist(
			playlist,
			p_org_id
		)
	except Exception as e:
		print( "%s" % ( [e.args, ] ), file=sys.stderr )
		raise HTTPException(
			status_code=404,
			detail="",
		)
	#-- except
	return 0
#--- EoF ---





# End of Script