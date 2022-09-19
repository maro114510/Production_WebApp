#!/usr/bin/env python
# -*- coding: utf8 -*-

from fastapi import APIRouter

router = APIRouter()

@router.get("/playlists/",tags=["Playlists"])
async def read_playlists():
    pass
#--- EoF ---

@router.get("/playlists/{playlist_id}",tags=["Playlists"])
async def read_playlist():
    pass
#--- EoF ---

@router.post("/playlists/",tags=["Playlists"])
async def create_playlist():
    pass
#--- EoF ---

@router.put("/playlists/{playlist_id}",tags=["Playlists"])
async def update_playlist():
    pass
#--- EoF ---

@router.delete("/playlists/{playlist_id}",tags=["Playlists"])
async def delete_playlist():
    pass
#--- EoF ---



# End of Script