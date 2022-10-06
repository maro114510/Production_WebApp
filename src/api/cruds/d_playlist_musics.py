#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import api.models.db_model as model
import api.schemas.playlists as p_schema
import api.schemas.musics as m_schema

async def get_playlist_musics(db:AsyncSession):
	"""_summary_

	Args:
		db (AsyncSession): asynchronous session

	Returns:
		list: Retrieved Intermediate Table (Playlist - Music)
	"""
	result: Result = await (
		db.execute(
			select(
				model.DeletedPlaylistMusic.id,
				model.DeletedPlaylistMusic.playlist_original_id,
				model.DeletedPlaylistMusic.music_original_id,
				model.DeletedPlaylistMusic.created_at,
			)
		)
	)
	return result.all()
#--- EoF ---

async def get_playlist_musics_by_playlist(db:AsyncSession,playlist_original_id:str):
	"""_summary_

	Args:
		db (AsyncSession): asynchronous session
		playlist_original_id (str): playlist original id

	Returns:
		list: List of music included in the playlist
	"""
	result: Result = await (
		db.execute(
			select(
				model.DeletedPlaylistMusic.id,
				model.DeletedPlaylistMusic.playlist_original_id,
				model.DeletedPlaylistMusic.music_original_id,
				model.DeletedPlaylistMusic.created_at,
			).filter(
				model.DeletedPlaylistMusic.playlist_original_id==playlist_original_id
			)
		)
	)
	return result.all()
#--- EoF ---

async def get_playlist_musics_by_p_m(
		db:AsyncSession,playlist_original_id:str,music_original_id:str
	):
	"""_summary_

	Args:
		db (AsyncSession): asynchronous session
		playlist_original_id (str): playlist original id
		music_original_id (str): music original id

	Returns:
		schema: DeletedPlaylistMusic
	"""
	result: Result = await (
		db.execute(
			select(
				model.DeletedPlaylistMusic.id,
				model.DeletedPlaylistMusic.playlist_original_id,
				model.DeletedPlaylistMusic.music_original_id,
				model.DeletedPlaylistMusic.created_at,
			).filter(
				model.DeletedPlaylistMusic.playlist_original_id==playlist_original_id
			).filter(
				model.DeletedPlaylistMusic.music_original_id==music_original_id
			)
		)
	)
	return result.first()
#--- EoF ---

async def create_playlist_music(
		db:AsyncSession,
		playlist_info:p_schema.PlaylistCreate,
		music:m_schema.MusicCreate
	):
	"""_summary_

	Args:
		db (AsyncSession): asynchronous session
		playlist_original_id (str): playlist original id
		music (m_schema.MusicCreate): MusicCreate schema

	Returns:
		schema: DeletedPlaylistMusic schema
	"""
	playlist_music = model.DeletedPlaylistMusic(
		playlist_original_id = playlist_info.playlist_original_id,
		music_original_id = music.music_original_id
	)
	db.add(playlist_music)
	await db.commit()
	await db.refresh(playlist_music)
	return playlist_music
#--- EoF ---

async def delete_playlist_music(
		db:AsyncSession,
		playlist:str,
		music:str
	):
	"""_summary_

	Args:
		db (AsyncSession): asynchronous session
		playlist (str): playlist original id
		music (str): music original id
	"""

	sql = """
	DELETE FROM d_playlist_music
	WHERE playlist_original_id = '%s'
	AND music_original_id = '%s';
	""" % ( playlist, music )
	await db.execute(sql)
	await db.commit()
#--- EoF ---




# End of Script