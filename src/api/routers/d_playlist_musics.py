#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.db import get_db
import api.cruds.d_playlist_musics as cruds
import api.schemas.playlists as p_schema
import api.schemas.musics as m_schema
import api.cruds.musics as musics

router = APIRouter()


@router.get("/d_playlist_musics/", tags=["D_Playlist_Musics"])
async def read_d_playlist_musics(db: AsyncSession = Depends(get_db)):
    """_summary_

    Args:
            db (AsyncSession, optional): AsyncSession. Defaults to Depends(get_db).

    Returns:
            list: DeletePlaylistMusic schema list
    """
    return await cruds.get_playlist_musics(db)
# --- EoF ---


@router.get("/d_playlist_music1/", tags=["D_Playlist_Musics"])
async def read_d_playlist_musics_by_p(playlist_original_id: str, db: AsyncSession = Depends(get_db)):
    """_summary_

    Args:
            playlist_original_id (str): playlist original id
            db (AsyncSession, optional): AsyncSession. Defaults to Depends(get_db).

    Returns:
            schema: DeletePlaylistMusic schema
    """
    return await cruds.get_playlist_musics_by_playlist(db, playlist_original_id)
# --- EoF ---


@router.get("/d_playlist_music2/", tags=["D_Playlist_Musics"])
async def read_d_playlist_musics_by_p_m(playlist_original_id: str, music_original_id: str, db: AsyncSession = Depends(get_db)):
    """_summary_

    Args:
            playlist_original_id (str): playlist original id
            music_original_id (str): music original id
            db (AsyncSession, optional): AsyncSession. Defaults to Depends(get_db).

    Returns:
            schema: DeletePlaylistMusic schema
    """
    return await cruds.get_playlist_musics_by_p_m(
        db,
        playlist_original_id,
        music_original_id
    )
# --- EoF ---


@router.post("/d_playlist_music/", tags=["D_Playlist_Musics"])
async def create_playlist_music(
    playlist_info: p_schema.PlaylistCreate,
    music_in: m_schema.MusicCreate,
    db: AsyncSession = Depends(get_db)
):
    """_summary_

    Args:
            playlist_info (p_schema.PlaylistCreate): PlaylistCreate schema
            music_in (m_schema.MusicCreate): MusicCreate schema
            db (AsyncSession, optional): AsyncSession. Defaults to Depends(get_db).

    Returns:
            schema: DeletePlaylistMusic schema
    """
    r = await musics.get_musics(db)
    ids = [i.music_original_id for i in r]
    if music_in.music_original_id in ids:
        music_r = await cruds.create_playlist_music(db, playlist_info, music_in)
    else:
        music_d = await musics.create_music(db, music_in)
        music_r = await cruds.create_playlist_music(db, playlist_info, music_in)
    return music_r
# --- EoF ---


@router.delete("/d_playlist_music/", tags=["D_Playlist_Musics"])
async def delete_playlist_music(playlist_original_id: str, music_original_id: str, db: AsyncSession = Depends(get_db)):
    """_summary_

    Args:
            playlist_original_id (str): playlist original id
            music_original_id (str): music original id
            db (AsyncSession, optional): AsyncSession. Defaults to Depends(get_db).

    Raises:
            HTTPException: 404

    Returns:
            int: 0
    """
    playlist = await cruds.get_playlist_musics_by_p_m(
        db,
        playlist_original_id,
        music_original_id
    )
    if playlist:
        await cruds.delete_playlist_music(
            db,
            playlist_original_id,
            music_original_id
        )
    else:
        raise HTTPException(
            status_code=404
        )
    return 0
# --- EoF ---

# End of Script
