#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
from typing import Optional, Tuple
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
			select(model.Playlist).filter(model.Playlist.playlist_id==playlist_id)
		)
	)
	playlist: Optional[Tuple[model.Playlist]] = result.first()
	return playlist[0] if playlist is not None else None
#--- EoF ---

async def get_playlist_by_original_id(db_session: AsyncSession,playlist_original_id:str):
	result: Result = await (
		db_session.execute(
			select(model.Playlist).filter(model.Playlist.playlist_original_id==playlist_original_id)
		)
	)
	playlist: Optional[Tuple[model.Playlist]] = result.first()
	return playlist[0] if playlist is not None else None
#--- EoF ---

async def create_playlist(
		db:AsyncSession, playlist_create:schema.PlaylistCreate
	):
	playlist = model.Playlist(
		playlist_name=playlist_create.playlist_name,
		playlist_original_id=playlist_create.playlist_original_id,
	)
	db.add(playlist)
	await db.commit()
	await db.refresh(playlist)
	return playlist
#--- EoF ---

async def update_playlist(
		db: AsyncSession,playlist:schema.PlaylistCreate,original:model.Playlist
	):
	original.playlist_name = playlist.playlist_name
	original.playlist_original_id = playlist.playlist_original_id
	db.add(original)
	await db.commit()
	await db.refresh(original)
	return original
#--- EoF ---

async def delete_playlist(
		db_session: AsyncSession,original:model.Playlist
	):
	await db_session.delete(original)
	await db_session.commit()
#--- EoF ---



# End of Script