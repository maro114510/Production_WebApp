#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.db import get_db
import api.cruds.user_playlists as cruds
import api.schemas.users as u_schema
import api.schemas.playlists as p_schema
import api.cruds.playlists as playlists

router = APIRouter()

@router.get("/user_playlists/", tags=["UserPlaylist"])
async def read_user_playlists(db: AsyncSession = Depends(get_db)):
	"""_summary_

	Args:
		db (AsyncSession, optional): AsyncSession. Defaults to Depends(get_db).

	Returns:
		list: UserPlaylist schema list
	"""
	return await cruds.get_user_playlists(db)
# --- EoF ---

@router.post("/user_playlists/userinfo", tags=["UserPlaylist"])
async def read_user_by_name(user:str, db: AsyncSession = Depends(get_db)):
	"""_summary_

	Args:
		user (str): user original name
		db (AsyncSession, optional): AsyncSession. Defaults to Depends(get_db).

	Returns:
		schema: UserPlaylist schema
	"""
	return await cruds.get_user_playlist_by_user(db,user)
# --- EoF ---

@router.post("/user_playlists/", tags=["UserPlaylist"])
async def create_user_playlists(user_info:u_schema.UserCreate ,playlist_in:p_schema.PlaylistCreate, db: AsyncSession = Depends(get_db)):
	"""_summary_

	Args:
		user_info (u_schema.UserCreate): UserCreate schema
		playlist_in (p_schema.PlaylistCreate): PlaylistCreate schema
		db (AsyncSession, optional): AsyncSession. Defaults to Depends(get_db).

	Returns:
		schema: UserPlaylist schema
	"""
	r = await playlists.get_playlists(db)
	ids = [ i.playlist_original_id for i in r ]
	if playlist_in.playlist_original_id in ids:
		playlist_r = await cruds.create_user_playlist(db,user_info,playlist_in)
	else:
		playlist_d = await playlists.create_playlist(db,playlist_in)
		playlist_r = await cruds.create_user_playlist(db,user_info,playlist_in)
	return playlist_r
# --- EoF ---

@router.delete("/user_playlists/playlist", tags=["UserPlaylist"])
async def delete_user_playlist(user_name: str,playlist:p_schema.PlaylistCreate , db: AsyncSession = Depends(get_db)):
	"""_summary_

	Args:
		user_name (str): user original name
		playlist (p_schema.PlaylistCreate): PlaylistCreate schema
		db (AsyncSession, optional): AsyncSession. Defaults to Depends(get_db).

	Raises:
		HTTPException: 404

	Returns:
		schema: UserPlaylist schema
	"""
	user = await cruds.get_user_playlist_by_user_id(db,user_name,playlist.playlist_original_id)
	if user:
		await cruds.delete_user_playlist(db,user,playlist.playlist_original_id)
	else:
		raise HTTPException(
			status_code=404)
	return user
# --- EoF ---



# End of Script