#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import requests

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.db import get_db
import api.cruds.n_playlist_musics as cruds
import api.schemas.playlists as p_schema
import api.schemas.musics as m_schema
import api.cruds.musics as musics

router = APIRouter()

@router.get("/n_playlist_musics/",tags=["N_Playlist_Musics"])
async def read_n_playlist_musics(db:AsyncSession = Depends(get_db)):
	"""_summary_

	Args:
		db (AsyncSession, optional): AsyncSession. Defaults to Depends(get_db).

	Returns:
		list: PlaylistMusic schema list
	"""
	return await cruds.get_playlist_musics(db)
# --- EoF ---

@router.get("/n_playlist_music1/",tags=["N_Playlist_Musics"])
async def read_n_playlist_musics_by_p(playlist_original_id:str,db:AsyncSession = Depends(get_db)):
	"""_summary_

	Args:
		playlist_original_id (str): playlist original id
		db (AsyncSession, optional): AsyncSession. Defaults to Depends(get_db).

	Returns:
		list: PlaylistMusic schemas list
	"""
	return await cruds.get_playlist_musics_by_playlist(db,playlist_original_id)
# --- EoF ---

@router.get("/n_playlist_music2/",tags=["N_Playlist_Musics"])
async def read_n_playlist_musics_by_p_m(playlist_original_id:str,music_original_id:str,db:AsyncSession = Depends(get_db)):
	"""_summary_

	Args:
		playlist_original_id (str): playlist original id
		music_original_id (str): music orignal id
		db (AsyncSession, optional): AsyncSession. Defaults to Depends(get_db).

	Returns:
		schema: PlaylistMusic schema
	"""
	return await cruds.get_playlist_musics_by_p_m(
		db,
		playlist_original_id,
		music_original_id
	)
# --- EoF ---

@router.post("/n_playlist_music/",tags=["N_Playlist_Musics"])
async def create_playlist_music(
		playlist_info:p_schema.PlaylistCreate,
		music_in:m_schema.MusicCreate,
		db: AsyncSession = Depends(get_db)
	):
	"""_summary_

	Args:
		playlist_info (p_schema.PlaylistCreate): playlistCreate schema
		music_in (m_schema.MusicCreate): MusicCreate schema
		db (AsyncSession, optional): AsyncSession. Defaults to Depends(get_db).

	Returns:
		schema: PlaylistMusic schema
	"""
	r = await musics.get_musics(db)
	ids = [ i.music_original_id for i in r ]
	if music_in.music_original_id in ids:
		music_r = await cruds.create_playlist_music(db,playlist_info,music_in)
	else:
		music_d = await musics.create_music(db,music_in)
		music_r = await cruds.create_playlist_music(db,playlist_info,music_in)
	return music_r
# --- EoF ---

@router.post("/n_playlist_musics/",tags=["N_Playlist_Musics"])
async def create_playlist_musics(
		playlist_info:p_schema.PlaylistCreate,
		db: AsyncSession = Depends(get_db)
	):
	"""_summary_

	Args:
		playlist_info (p_schema.PlaylistCreate): PlaylistCreate schema
		db (AsyncSession, optional): AsyncSession. Defaults to Depends(get_db).

	Raises:
		HTTPException: 404

	Returns:
		list: created list
	"""
	headers = {
		'accept': 'application/json',
		'content-type': 'application/x-www-form-urlencoded',
	}
	playlist_id = playlist_info.playlist_original_id
	res = requests.post(f'https://2y5u90.deta.dev/{playlist_id}', headers=headers).json()
	music_list = res.get("music_id_list")
	try:
		r = await cruds.create_playlist_musics(db,music_list,playlist_info)
	except Exception as e:
		raise HTTPException(
			status_code=403)
	# -- except
	return r
# --- EoF ---


@router.delete("/n_playlist_music/",tags=["N_Playlist_Musics"])
async def delete_playlist_music(playlist_original_id:str,music_original_id:str,db:AsyncSession = Depends(get_db)):
	"""_summary_

	Args:
		playlist_original_id (str): playlist orignal id
		music_original_id (str): music original id
		db (AsyncSession, optional): AsyncSession. Defaults to Depends(get_db).

	Raises:
		HTTPException: 404

	Returns:
		int: 0
	"""
	playlist = await cruds.get_playlist_musics_by_p_m(
		db,
		playlist_original_id,
		music_original_id
	)
	if playlist:
		await cruds.delete_playlist_music(
			db,
			playlist_original_id,
			music_original_id
		)
	else:
		raise HTTPException(
			status_code=404
		)
	return 0
# --- EoF ---


# End of Script