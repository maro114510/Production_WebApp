#!/usr/bin/env python
# -*- coding: utf8 -*-

from tkinter import E
import requests
from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import api.schemas.playlists as p_schema
import api.schemas.users as u_schema
import api.cruds.playlists as playlist_crud
import api.cruds.musics as music_crud
import api.cruds.n_playlist_musics as npm_cruds
import api.cruds.user_playlists as up_cruds
from api.db import get_db
from api.lib.library import generate_playlist_id

router = APIRouter()


@router.post("/register/", tags=["Register"])
async def create_bulk(
    user: u_schema.UserCreate,
    url: str,
    db: AsyncSession = Depends(get_db)
):
    """_summary_

    Args:
            user (u_schema.UserCreate): UserCreate schema
            url (str): playlist url
            db (AsyncSession, optional): AsyncSession. Defaults to Depends(get_db).

    Raises:
            HTTPException: 400
            HTTPException: 400
            HTTPException: 400
            HTTPException: 400
            HTTPException: 400

    Returns:
            list: empty list
    """

    # ユーザ・プレイリストテーブルの登録
    playlist_original_id = generate_playlist_id(url)
    headers = {
        'accept': 'application/json',
        'content-type': 'application/x-www-form-urlencoded',
    }
    # res = requests.post(f'https://2y5u90.deta.dev/{playlist_original_id}', headers=headers).json()
    try:
        res = requests.post(
            f'https://2y5u90.deta.dev/{playlist_original_id}',
            headers=headers).json()
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=e
        )
    # -- except
    playlist_name = res.get("playlistname")

    playlist_s = p_schema.PlaylistCreate(
        playlist_name=playlist_name,
        playlist_original_id=playlist_original_id
    )

    try:
        await playlist_crud.create_playlist(db, playlist_s)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=e
        )
    # -- except
    # await up_cruds.create_user_playlist(db,user,playlist_s)
    try:
        await up_cruds.create_user_playlist(db, user, playlist_s)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=e
        )
    # -- except
    playlist_in = p_schema.PlaylistCreate(
        playlist_name=f"{playlist_name}",
        playlist_original_id=f"{playlist_original_id}"
    )
    try:
        r = await playlist_crud.get_playlists(db)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=e)
    # -- except
    # プレイリスト内の音楽登録
    music_list = res.get("music_id_list")

    # npmテーブルの登録
    try:
        r = await npm_cruds.create_playlist_musics(db, music_list, playlist_in)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=e)
    # -- except
    return r
# --- EoF ---


# End of Script
