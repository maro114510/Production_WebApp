#!/usr/bin/env python
# -*- coding: utf8 -*-


import sys
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import api.models.db_model as model
import api.schemas.users as u_schema
import api.schemas.playlists as p_schema


async def get_user_playlists(db_session: AsyncSession):
    """_summary_

    Args:
            db_session (AsyncSession): AsyncSession

    Returns:
            list: UserPlaylist schemas list
    """
    result: Result = await (
        db_session.execute(
            select(
                model.UserPlaylist.id,
                model.UserPlaylist.user_name,
                model.UserPlaylist.playlist_original_id,
                model.UserPlaylist.created_at
            )
        )
    )
    return result.all()
# --- EoF ---


async def get_user_playlist_by_user(db_session: AsyncSession, user: str):
    """_summary_

    Args:
            db_session (AsyncSession): AsyncSession
            user (str): user name

    Returns:
            schema: UserPlaylist schema
    """
    result: Result = await (
        db_session.execute(
            select(
                model.UserPlaylist.id,
                model.UserPlaylist.user_name,
                model.UserPlaylist.playlist_original_id,
                model.UserPlaylist.created_at
            ).filter(
                model.UserPlaylist.user_name == user
            )
        )
    )
    return result.all()
# --- EoF ---


async def get_user_playlist_by_user_id(db_session: AsyncSession, user: str, playlist: str):
    """_summary_

    Args:
            db_session (AsyncSession): AsyncSession
            user (str): user name
            playlist (str): playlist original id

    Returns:
            schema: UserPlaylist schema
    """
    result: Result = await (
        db_session.execute(
            select(
                model.UserPlaylist.id,
                model.UserPlaylist.user_name,
                model.UserPlaylist.playlist_original_id,
            ).filter(
                model.UserPlaylist.user_name == user
            ).filter(
                model.UserPlaylist.playlist_original_id == playlist
            )
        )
    )
    return result.first()
# --- EoF ---


async def create_user_playlist(db: AsyncSession, user_info: u_schema.UserCreate, playlists: p_schema.PlaylistCreate):
    """_summary_

    Args:
            db (AsyncSession): AsyncSession
            user_info (u_schema.UserCreate): UserCreate schema
            playlists (p_schema.PlaylistCreate): PlaylistCreate schema

    Returns:
            schema: UserPlaylist schema
    """
    user_playlist = model.UserPlaylist(
        user_name=user_info.user_name,
        playlist_original_id=playlists.playlist_original_id
    )
    result: Result = await (
        db.execute(
            select(
                model.UserPlaylist.id,
            ).filter(
                model.UserPlaylist.user_name == user_info.user_name
            ).filter(
                model.UserPlaylist.playlist_original_id == playlists.playlist_original_id
            )
        )
    )

    if result.first():
        user_name = user_info.user_name
        playlist_original_id = playlists.playlist_original_id
        return f"{user_name}'s {playlist_original_id} is doubled."
    else:
        db.add(user_playlist)
        await db.commit()
        await db.refresh(user_playlist)
        return user_playlist
# --- EoF ---


async def delete_user_playlist(
    db_session: AsyncSession, user: str, playlist: str
):
    sql = """
	DELETE FROM user_playlists
	WHERE user_name = '%s'
	AND playlist_original_id = '%s';
	""" % (user, playlist)
    await db_session.execute(sql)
    await db_session.commit()
# --- EoF ---


# End of Script
