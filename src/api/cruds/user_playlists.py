#!/usr/bin/env python
# -*- coding: utf8 -*-

from operator import mod
import sys
from typing import Optional, Tuple
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import api.models.db_model as model
import api.schemas.users as u_schema
import api.schemas.playlists as p_schema

async def get_user_playlists(db_session: AsyncSession):
	result: Result = await (
		db_session.execute(
			select(
				model.UserPlaylist.id,
				model.UserPlaylist.user_name,
				model.UserPlaylist.playlist_original_id,
			)
		)
	)
	return result.all()
#--- EoF ---

async def get_user_playlist_by_user(db_session: AsyncSession,user:str):
	result: Result = await (
		db_session.execute(
			select(
				model.UserPlaylist.id,
				model.UserPlaylist.user_name,
				model.UserPlaylist.playlist_original_id,
			).filter(
				model.UserPlaylist.user_name==user
			)
		)
	)
	return result.all()
#--- EoF ---

async def get_user_playlist_by_user_id(db_session: AsyncSession,user:str,playlist:str):
	result: Result = await (
		db_session.execute(
			select(
				model.UserPlaylist.id,
				model.UserPlaylist.user_name,
				model.UserPlaylist.playlist_original_id,
			).filter(
				model.UserPlaylist.user_name==user
			).filter(
				model.UserPlaylist.playlist_original_id==playlist
			)
		)
	)
	return result.first()
#--- EoF ---

async def create_user_playlist(db:AsyncSession,user_info:u_schema.UserCreate ,playlists:p_schema.PlaylistCreate):
	user_playlist = model.UserPlaylist(
		user_name=user_info.user_name,
		playlist_original_id=playlists.playlist_original_id
	)
	db.add(user_playlist)
	await db.commit()
	await db.refresh(user_playlist)
	return user_playlist
#--- EoF ---


async def delete_user_playlist(
		db_session: AsyncSession,user:str,playlist:str
	):
	result: Result = await (
		db_session.execute(
			select(
				model.UserPlaylist.id,
				model.UserPlaylist.user_name,
				model.UserPlaylist.playlist_original_id,
				model.UserPlaylist.user,
				model.UserPlaylist.playlist,
			).filter(
				model.UserPlaylist.user_name==user
			).filter(
				model.UserPlaylist.playlist_original_id==playlist
			)
		)
	)
	r = result.mappings()
	# return r
	await db_session.delete(r)
	await db_session.commit()
#--- EoF ---



# End of Script
