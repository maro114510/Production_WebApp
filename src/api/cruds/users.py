#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
from typing import Optional, Tuple
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import api.models.db_model as model
import api.schemas.users as schema


async def get_users(db_session: AsyncSession):
    """_summary_

    Args:
            db_session (AsyncSession): AsyncSession

    Returns:
            list: User schema list
    """
    result: Result = await (
        db_session.execute(
            select(
                model.User.user_id,
                model.User.user_name,
                model.User.user_email,
                model.User.user_pw,
            )
        )
    )
    return result.all()
# --- EoF ---


async def get_user_by_id(db_session: AsyncSession, user_id: int):
    """_summary_

    Args:
            db_session (AsyncSession): AsyncSession
            user_id (int): user serial number

    Returns:
            schema: User schema
    """
    result: Result = await (
        db_session.execute(
            select(
                model.User.user_id,
                model.User.user_name,
                model.User.user_email,
                model.User.user_pw,
            ).filter(
                model.User.user_id == user_id
            )
        )
    )
    return result.first()
# --- EoF ---


async def get_user_by_name(db_session: AsyncSession, user_name: str):
    """_summary_

    Args:
            db_session (AsyncSession): AsyncSession
            user_name (str): user original name

    Returns:
            schema: User schema
    """
    result: Result = await (
        db_session.execute(
            select(
                model.User.user_id,
                model.User.user_name,
                model.User.user_email,
                model.User.user_pw
            ).filter(
                model.User.user_name == user_name
            )
        )
    )
    return result.first()
# --- EoF ---


async def create_user(
    db: AsyncSession, user_create: schema.UserCreate
):
    user = model.User(
        user_name=user_create.user_name,
        user_email=user_create.user_email,
        user_pw=user_create.user_pw
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user
# --- EoF ---


async def update_user(
    db: AsyncSession, user: schema.UserCreate, original: model.User
):
    """_summary_

    Args:
            db (AsyncSession): AsyncSession
            user (schema.UserCreate): UserCreate schema
            original (model.User): User schema

    Returns:
            schema: User schema
    """
    result = await db.execute(
        select(
            model.User
        ).filter(
            model.User.user_name == original.user_name
        )
    )
    buf = result.first()
    buf[0].user_name = user.user_name
    buf[0].user_email = user.user_email
    # original.user_name = user.user_name
    # original.user_email = user.user_email
    db.add(buf[0])
    await db.commit()
    await db.refresh(buf[0])
    return buf[0]
# --- EoF ---


async def delete_user(
    db_session: AsyncSession, original: model.User
):
    """_summary_

    Args:
            db_session (AsyncSession): AsyncSession
            original (model.User): User schema
    """
    sql = "delete from users where user_id = %s ;" % original.user_id
    await db_session.execute(sql)
    # await db_session.delete(original)
    await db_session.commit()
# --- EoF ---


# End of Script……………
