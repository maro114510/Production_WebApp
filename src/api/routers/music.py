#!/usr/bin/env python
# -*- coding: utf8 -*-

from fastapi import APIRouter

router = APIRouter()

@router.get("/musics/",tags=["Musics"])
async def read_musics():
    pass
#--- EoF ---

@router.get("/musics/{music_id}",tags=["Musics"])
async def read_music():
    pass
#--- EoF ---

@router.post("/musics/",tags=["Musics"])
async def create_music():
    pass
#--- EoF ---

@router.put("/musics/{music_id}",tags=["Musics"])
async def update_music():
    pass
#--- EoF ---

@router.delete("/musics/{music_id}",tags=["Musics"])
async def delete_music():
    pass
#--- EoF ---



# End of Script