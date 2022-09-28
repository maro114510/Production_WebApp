#!/usr/bin/env python
# -*- coding: utf8 -*-

import requests
from fastapi import APIRouter,Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import api.schemas.playlists as p_schema
import api.schemas.users as u_schema
import api.cruds.playlists as playlist_crud
import api.cruds.musics as music_crud
import api.cruds.n_playlist_musics as npm_cruds
import api.cruds.user_playlists as up_cruds
from api.db import get_db
from api.lib.library import generate_playlist_id

router = APIRouter()

@router.post("/register/",tags=["Register"])
async def create_bulk(
		user:u_schema.UserCreate,
		url:str,
		db:AsyncSession = Depends(get_db)
	):

	# ユーザ・プレイリストテーブルの登録
	playlist_original_id = generate_playlist_id(url)
	headers = {
		'accept': 'application/json',
		'content-type': 'application/x-www-form-urlencoded',
	}
	playlist_id = generate_playlist_id(url)
	res = requests.post(f'https://2y5u90.deta.dev/{playlist_id}', headers=headers).json()
	playlist_name = res.get("playlistname")
	playlist_in = p_schema.PlaylistCreate(
		playlist_name=f"{playlist_name}",
		playlist_original_id=f"{playlist_original_id}"
	)
	r = await playlist_crud.get_playlists(db)
	ids = [ i.playlist_original_id for i in r ]
	# if playlist_original_id in ids:
	# 	playlist_r = await up_cruds.create_user_playlist(db,user,playlist_in)
	# 	if type(playlist_r) == str:
	# 		raise HTTPException(
	# 			status_code=400,
	# 			detail=playlist_r
	# 		)
	# else:
	# 	playlist_d = await playlist_crud.create_playlist(db,playlist_in)
	# 	playlist_r = await up_cruds.create_user_playlist(db,user,playlist_in)
	# 	if type(playlist_r) == str:
	# 		raise HTTPException(
	# 			status_code=400,
	# 			detail=playlist_r
	# 		)
	# プレイリスト内の音楽登録
	music_list = res.get("music_id_list")

	# npmテーブルの登録
	# r = await npm_cruds.create_playlist_musics(db,music_list,playlist_in)
	try:
		r = await npm_cruds.create_playlist_musics(db,music_list,playlist_in)
	except Exception as e:
		raise HTTPException(
			status_code=400,
			detail=e)
	# # -- except
	return music_list
# --- EoF ---


# End of Script