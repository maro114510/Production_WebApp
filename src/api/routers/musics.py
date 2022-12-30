#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
from typing import List
from fastapi import APIRouter, HTTPException

from api.cruds.musics import Musics

ins = Musics()
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
	musics: list
):
	try:
		# ins.music_insert_one(
		# 	music_name,
		# 	m_org_id,
		# )
		pass
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