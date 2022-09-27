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
	result: Result = await (
		db.execute(
			select(
				model.NormalPlaylistMusic.id,
				model.NormalPlaylistMusic.playlist_original_id,
				model.NormalPlaylistMusic.music_original_id,
				model.NormalPlaylistMusic.created_at,
			)
		)
	)
	return result.all()
#--- EoF ---

async def get_playlist_musics_by_playlist(db:AsyncSession,playlist_original_id:str):
	result: Result = await (
		db.execute(
			select(
				model.NormalPlaylistMusic.id,
				model.NormalPlaylistMusic.playlist_original_id,
				model.NormalPlaylistMusic.music_original_id,
				model.NormalPlaylistMusic.created_at,
			).filter(
				model.NormalPlaylistMusic.playlist_original_id==playlist_original_id
			)
		)
	)
	return result.all()
#--- EoF ---

async def get_playlist_musics_by_p_m(
		db:AsyncSession,playlist_original_id:str,music_original_id:str
	):
	result: Result = await (
		db.execute(
			select(
				model.NormalPlaylistMusic.id,
				model.NormalPlaylistMusic.playlist_original_id,
				model.NormalPlaylistMusic.music_original_id,
				model.NormalPlaylistMusic.created_at,
			).filter(
				model.NormalPlaylistMusic.playlist_original_id==playlist_original_id
			).filter(
				model.NormalPlaylistMusic.music_original_id==music_original_id
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
	playlist_music = model.NormalPlaylistMusic(
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
	sql = """
	DELETE FROM n_playlist_music
	WHERE playlist_original_id = '%s'
	AND music_original_id = '%s';
	""" % ( playlist, music )
	await db.execute(sql)
	await db.commit()
#--- EoF ---




# End of Script