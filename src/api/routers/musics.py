#!/usr/bin/env python
# -*- coding: utf8 -*-

import requests
from fastapi import APIRouter,Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import api.schemas.musics as schema
import api.cruds.musics as music_crud
from api.db import get_db
from api.lib.library import generate_playlist_id

router = APIRouter()


@router.get("/musics/", tags=["Musics"])
async def read_musics(db: AsyncSession = Depends(get_db)):
	"""_summary_

	Args:
		db (AsyncSession, optional): _description_. Defaults to Depends(get_db).

	Returns:
		object: List[schema.Musics]
	"""
	return await music_crud.get_musics(db)
# --- EoF ---


@router.get("/music/{music_id}",
            tags=["Musics"])
async def read_music_by_id(music_id:int,db: AsyncSession = Depends(get_db)):
	"""_summary_

	Args:
		music_id (int): music id (serial number)
		db (AsyncSession, optional): _description_. Defaults to Depends(get_db).

	Returns:
		object: schema.Musics
	"""
	return await music_crud.get_music_by_id(db,music_id)
# --- EoF ---

@router.get("/musics/{music_original_id}",
            tags=["Musics"])
async def read_music_by_original_id(music_original_id:str,db: AsyncSession = Depends(get_db)):
	"""_summary_

	Args:
		music_original_id (str): music original id
		db (AsyncSession, optional): _description_. Defaults to Depends(get_db).

	Returns:
		object: schema.Musics
	"""
	return await music_crud.get_music_by_original_id(db,music_original_id)
# --- EoF ---

@router.get("/musics/{music_name}",
            tags=["Musics"])
async def read_music_by_name(music_name:str,db: AsyncSession = Depends(get_db)):
	"""_summary_

	Args:
		music_name (str): music name(video name)
		db (AsyncSession, optional): _description_. Defaults to Depends(get_db).

	Returns:
		object: schema.Musics
	"""
	return await music_crud.get_music_by_name(db,music_name)
# --- EoF ---

@router.post("/musics/", tags=["Musics"])
async def create_music(music_in:schema.MusicCreate,db: AsyncSession = Depends(get_db)):
	"""_summary_

	Args:
		music_in (schema.MusicCreate): _description_
		db (AsyncSession, optional): _description_. Defaults to Depends(get_db).

	Raises:
		HTTPException: _description_

	Returns:
		_type_: _description_
	"""
	# r = await music_crud.create_music(db,music_in)
	try:
		r = await music_crud.create_music(db,music_in)
	except Exception as e:
		raise HTTPException(
			status_code=404,
			detail=f"{music_in.music_name}, or {music_in.music_original_id} is duplicated.")
	# -- except
	return r
# --- EoF ---

@router.post("/musics-list/", tags=["Musics"])
async def create_musics(url:str,db: AsyncSession = Depends(get_db)):
	headers = {
		'accept': 'application/json',
		'content-type': 'application/x-www-form-urlencoded',
	}
	playlist_id = generate_playlist_id(url)
	res = requests.post(f'https://2y5u90.deta.dev/{playlist_id}', headers=headers).json()
	music_list = res.get("music_id_list")

	try:
		r = await music_crud.create_musics(db,music_list)
	except Exception as e:
		raise HTTPException(
			status_code=404)
	# -- except
	return r
# --- EoF ---


@router.put("/musics/{music_id}",
            tags=["Musics"])
async def update_music(music_original_id:str,music_body:schema.MusicCreate,db: AsyncSession = Depends(get_db)):
	music = await music_crud.get_music_by_original_id(db,music_original_id= music_original_id)
	if music is None:
		raise HTTPException(
			status_code=404,
			detail=f"{music_original_id} is not found.")
	return await music_crud.update_music(db, music_body, original=music)
# --- EoF ---


@router.delete("/musics/{music_id}", tags=["Musics"], response_model=None)
async def delete_music(music_original_id:str,db: AsyncSession = Depends(get_db)):
	music = await music_crud.get_music_by_original_id(db,music_original_id=music_original_id)
	if music is None:
		raise HTTPException(
			status_code=404,
			detail=f"{music_original_id} is not found.")
	return await music_crud.delete_music(db,original=music)

# --- EoF ---


# End of Script
