#!/usr/bin/env python
# -*- coding: utf8 -*-

from typing import List
from fastapi import APIRouter

import api.schemas.playlists as schema

router = APIRouter()


@router.get("/playlists/", tags=["Playlists"])
async def read_playlists():
    return []
# --- EoF ---


@router.get("/playlists/{playlist_id}", tags=["Playlists"])
async def read_playlist():
    return 0
# --- EoF ---


@router.post("/playlists/", tags=["Playlists"])
async def create_playlist():
    return 0
# --- EoF ---


@router.put("/playlists/{playlist_id}", tags=["Playlists"])
async def update_playlist():
    return 0
# --- EoF ---


@router.delete("/playlists/{playlist_id}",
               tags=["Playlists"], response_model=int)
async def delete_playlist(playlist_id: int):
    return playlist_id
# --- EoF ---


# End of Script
