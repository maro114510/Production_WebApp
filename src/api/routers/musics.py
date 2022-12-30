#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
from typing import List
from fastapi import APIRouter, HTTPException

from api.cruds.musics import Musics
from api.libs.plalylist_url_handling import Format

ins = Musics()
f_ins = Format()
router = APIRouter()


@router.get( "/musics", tags=[ "Musics" ] )
async def list_musics() -> List[ dict ]:
	return ins.get_all_musics_full_info()
#--- EoF ---

@router.get( "/musics/music", tags=[ "Musics" ] )
async def get_music_info( m_org_id: str ):
	return ins.get_one_music_info( m_org_id )
#--- EoF ---

@router.post( "/musics", tags=[ "Musics" ] )
async def create_music(
	music_name: str,
	m_org_id: str
):
	try:
		ins.music_insert_one(
			music_name,
			m_org_id,
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

@router.post( "/musics/bulk", tags=[ "Musics" ] )
async def create_musics(
	url: str
):
	try:
		music_list = f_ins.get_row_data( url )
		ins.musics_insert(
			music_list
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