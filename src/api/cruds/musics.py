#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
from typing import Optional, Tuple, List
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import api.models.db_model as model
import api.schemas.musics as schema


async def get_musics(db_session: AsyncSession):
    result: Result = await (
        db_session.execute(
            select(
                model.Music.music_id,
                model.Music.music_name,
                model.Music.music_original_id,
            )
        )
    )
    return result.all()
# --- EoF ---


async def get_music_by_id(db_session: AsyncSession,music_id:int):
	result: Result = await (
		db_session.execute(
			select(
				model.Music.music_id,
				model.Music.music_name,
				model.Music.music_original_id,
			).filter(
				model.Music.music_id==music_id
			)
		)
	)

	return result.first() 
#--- EoF ---


async def get_music_by_name(db_session: AsyncSession,music_name:str):
	result: Result = await (
		db_session.execute(
			select(
				model.Music.music_id,
				model.Music.music_name,
				model.Music.music_original_id,
			).filter(
				model.Music.music_name==music_name
			)
		)
	)
	return result.first()
#--- EoF ---

async def get_music_by_original_id(db_session: AsyncSession,music_original_id:str):
	result: Result = await (
		db_session.execute(
			select(
				model.Music.music_id,
				model.Music.music_name,
				model.Music.music_original_id,
			).filter(
				model.Music.music_original_id==music_original_id
			)
		)
	)
	music: Optional[Tuple[model.Music]] = result.first()
	return music[0] if music is not None else None
#--- EoF ---


async def create_music(
		db:AsyncSession, music_create:schema.MusicCreate
	):
	music = model.Music(
		music_name=music_create.music_name,
		music_original_id=music_create.music_original_id
	)
	db.add(music)
	await db.commit()
	await db.refresh(music)
	return music
#--- EoF ---

async def create_musics(
		db:AsyncSession, music_list:list):
	box = []

	for i in music_list:
		id = i.get("video_id")
		r = await (db.execute(select(
				model.Music.music_id,
			).filter(
				model.Music.music_original_id==id
			)))
		r = r.first()
		if r is None:
			box.append(i)
		#-- if
	#-- for

	if box:
		musics = [ model.Music( music_name=d["video_name"],music_original_id=d["video_id"] ) for d in box ]
		db.add_all(musics)
		await db.commit()
		# await db.refresh(musics)
	#-- if
	return box
#--- EoF ---


async def update_music(
		db: AsyncSession,music:schema.MusicCreate,original:model.Music
	):
	original.music_name = music.music_name
	db.add(original)
	await db.commit()
	await db.refresh(original)
	return original
#--- EoF ---

async def delete_music(
		db_session: AsyncSession,original:model.Music
	):
	await db_session.delete(original)
	await db_session.commit()
#--- EoF ---



# End of Script