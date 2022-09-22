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
	datalist = [{'video_name': '【CoC狂気山脈】狂気！ンゴ灰那山脈！【後編】PL：周央 サンゴ、黛 灰、健屋 花那','video_id': 'oTq9AIzx_wk'},{'video_name': '【クトゥルフ神話TRPG配信】茶瀬木高校オカルト部 その２ #ンゴ灰那部','video_id': '69ynXHdTPWg'},{'video_name': '新約・きさらぎ駅／出演：朝日奈丸佳、森永千才、ベルモンド・バンデラス、周央サンゴ','video_id': 'm2IxsOmtAM4'},{'video_name': '【こひな卓】刹夏【#ンゴ刹那】', 'video_id': '6aD-Sm1TXko'},
	]
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

	if box:
		musics = [ model.Music( music_name=d["video_name"],music_original_id=d["video_id"] ) for d in box ]
		db.add_all(musics)
		await db.commit()
		# await db.refresh(musics)
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