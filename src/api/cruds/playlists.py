#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
from typing import Optional, Tuple
from unittest import result
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import api.models.db_model as model
import api.schemas.playlists as schema

async def get_playlists(db_session: AsyncSession):
	result: Result = await (
		db_session.execute(
			select(
				model.Playlist.playlist_id,
				model.Playlist.playlist_name,
				model.Playlist.playlist_original_id
			)
		)
	)
	return result.all()
#--- EoF ---

async def get_playlist_by_id(db_session: AsyncSession,playlist_id:int):
	result: Result = await (
		db_session.execute(
			select(
				model.Playlist.playlist_id,
				model.Playlist.playlist_name,
				model.Playlist.playlist_original_id,
			).filter(
				model.Playlist.playlist_id==playlist_id
			)
		)
	)
	return result.first()
#--- EoF ---

async def get_playlist_by_original_id(db_session: AsyncSession,playlist_original_id:str):
	result: Result = await (
		db_session.execute(
			select(
				model.Playlist.playlist_id,
				model.Playlist.playlist_name,
				model.Playlist.playlist_original_id
			).filter(
				model.Playlist.playlist_original_id==playlist_original_id
			)
		)
	)
	return result.first()
#--- EoF ---

async def create_playlist(
		db:AsyncSession, playlist_create:schema.PlaylistCreate
	):
	playlist = model.Playlist(
		playlist_name=playlist_create.playlist_name,
		playlist_original_id=playlist_create.playlist_original_id
	)
	db.add(playlist)
	await db.commit()
	await db.refresh(playlist)
	return playlist
#--- EoF ---

async def update_playlist(
		db: AsyncSession,playlist:str,original:schema.PlaylistCreate
	):
	result = await db.execute(
		select(
			model.Playlist
		).filter(
			model.Playlist.playlist_original_id==playlist
		)
	)
	buf = result.first()
	buf[0].playlist_name = original.playlist_name
	db.add(buf[0])
	await db.commit()
	await db.refresh(buf[0])
	return buf[0]
#--- EoF ---

async def delete_playlist(
		db_session: AsyncSession,original:model.Playlist
	):
	sql = "DELETE FROM playlists WHERE playlist_id = %s ;" % original.playlist_id
	await db_session.execute(sql)
	await db_session.commit()
#--- EoF ---



# End of Script