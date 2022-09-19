#!/usr/bin/env python
# -*- coding: utf8 -*-

from typing import List
from fastapi import APIRouter

import api.schemas.musics as schema

router = APIRouter()

@router.get("/musics/",tags=["Musics"],response_model=List[schema.Musics])
async def read_musics():
	pass
#--- EoF ---

@router.get("/musics/{music_id}",tags=["Musics"],response_model=schema.Musics)
async def read_music():
	pass
#--- EoF ---

@router.post("/musics/",tags=["Musics"],response_model=schema.MusicCreateResponse)
async def create_music():
	pass
#--- EoF ---

@router.put("/musics/{music_id}",tags=["Musics"],response_model=schema.MusicCreateResponse)
async def update_music():
	pass
#--- EoF ---

@router.delete("/musics/{music_id}",tags=["Musics"],response_model=None)
async def delete_music():
	pass
#--- EoF ---



# End of Script