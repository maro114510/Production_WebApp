#!/usr/bin/env python
# -*- coding: utf8 -*-

import requests
from fastapi import APIRouter,Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import api.schemas.playlists as schema
import api.cruds.playlists as playlist_crud
from api.db import get_db
from api.lib.library import generate_playlist_id

router = APIRouter()


@router.get("/playlists/", tags=["Playlists"])
async def read_playlists(db: AsyncSession = Depends(get_db)):
    return await playlist_crud.get_playlists(db)
# --- EoF ---

@router.get("/playlists/{playlist_id}", tags=["Playlists"])
async def read_playlist_by_id(playlist_id:int,db: AsyncSession = Depends(get_db)):
    return await playlist_crud.get_playlist_by_id(db,playlist_id)
# --- EoF ---

@router.get("/playlist/original", tags=["Playlists"])
async def read_playlist_by_original_id(playlist_original_id:str,db: AsyncSession = Depends(get_db)):
	return await playlist_crud.get_playlist_by_original_id(db,playlist_original_id)
# --- EoF ---

@router.post("/playlists/", tags=["Playlists"])
async def create_playlist(url:str, db: AsyncSession = Depends(get_db)):
	headers = {
		'accept': 'application/json',
		'content-type': 'application/x-www-form-urlencoded',
	}
	playlist_id = generate_playlist_id(url)
	res = requests.post(f'https://2y5u90.deta.dev/{playlist_id}', headers=headers)
	if res.status_code != 200:
		HTTPException(status_code=500)
	res = res.json()
	playlist_name = res.get("playlistname")
	playlist_in = schema.PlaylistCreate(
		playlist_name=playlist_name,
		playlist_original_id=playlist_id
	)
	# r = await playlist_crud.create_playlist(db,playlist_in)
	try:
		r = await playlist_crud.create_playlist(db,playlist_in)
	except Exception as e:
		i = playlist_in.get("playlist_original_id")
		raise HTTPException( status_code=404,detail=f"{i} is duplicated." )
	#-- except
	return r
# --- EoF ---

@router.put("/playlists/{playlist_original_id}", tags=["Playlists"])
async def update_playlist(playlist_original_id: str, playlist_body:schema.PlaylistCreate,db: AsyncSession = Depends(get_db)):
	playlist = await playlist_crud.get_playlist_by_original_id(db,playlist_original_id=playlist_original_id)
	if playlist is None:
		raise HTTPException(status_code=404,detail=f"{playlist_original_id} is not found.")
	return await playlist_crud.update_playlist(db,playlist_original_id,original=playlist_body)
# --- EoF ---


@router.delete("/playlists/{playlist_id}",
            tags=["Playlists"])
async def delete_playlist(playlist_original_id:str,db: AsyncSession = Depends(get_db)):
	playlist = await playlist_crud.get_playlist_by_original_id(db,playlist_original_id=playlist_original_id)
	if playlist is None:
		raise HTTPException(status_code=404,detail=f"{playlist_original_id} is not found.")
	return await playlist_crud.delete_playlist(db,original=playlist)
# --- EoF ---


# End of Script
