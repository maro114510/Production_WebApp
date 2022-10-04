#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import api.schemas.users as schema
import api.cruds.users as user_crud
from api.db import get_db

router = APIRouter()


@router.get("/users/", tags=["Users"])
async def read_users(db: AsyncSession = Depends(get_db)):
	"""_summary_

	Args:
		db (AsyncSession, optional): AsyncSession. Defaults to Depends(get_db).

	Returns:
		list: User schemas list
	"""
	return await user_crud.get_users(db)
# --- EoF ---

@router.get("/users/{user_id}", tags=["Users"])
async def read_user(user_id:int,db: AsyncSession = Depends(get_db)):
	"""_summary_

	Args:
		user_id (int): user serial number
		db (AsyncSession, optional): AsyncSession. Defaults to Depends(get_db).

	Returns:
		schema: User schema
	"""
	return await user_crud.get_user_by_id(db,user_id=user_id)
# --- EoF ---


@router.get("/users/name/", tags=["Users"])
async def read_by_name(user_name:str,db: AsyncSession = Depends(get_db)):
	"""_summary_

	Args:
		user_name (str): user original name
		db (AsyncSession, optional): AsyncSession. Defaults to Depends(get_db).

	Returns:
		schema: User schema
	"""
	# return await user_crud.get_users(db)
	return await user_crud.get_user_by_name(db, user_name=user_name)
# --- EoF ---


@router.post("/users/", tags=["Users"])
async def create_user(user_in: schema.UserCreate, db: AsyncSession = Depends(get_db)):
	"""_summary_

	Args:
		user_in (schema.UserCreate): UserCreate schema
		db (AsyncSession, optional): AsyncSession. Defaults to Depends(get_db).

	Raises:
		HTTPException: 404

	Returns:
		schema: User schema
	"""
	# r = await user_crud.create_user(db, user_in)
	try:
		r = await user_crud.create_user(db, user_in)
	except Exception as e:
		raise HTTPException(
			status_code=404,
			detail=f"{user_in.user_name}, or {user_in.user_email} is duplicated."
		)
	# -- except
	return r
# --- EoF ---


@router.put("/users/{user_name}",
            tags=["Users"])
async def update_user(user_name: str, user_body: schema.UserCreate, db: AsyncSession = Depends(get_db)):
	"""_summary_

	Args:
		user_name (str): user original name
		user_body (schema.UserCreate): UserCreate schema
		db (AsyncSession, optional): AsyncSession. Defaults to Depends(get_db).

	Raises:
		HTTPException: 404

	Returns:
		schema: User schema
	"""
	user = await user_crud.get_user_by_name(db, user_name=user_name)
	if user is None:
		raise HTTPException(
			status_code=404,
			detail=f"{user_name} is not found.")
	# user = await user_crud.get_user_by_name(db, user_name=user_name)
	# return user.user_name
	return await user_crud.update_user(db, user_body, original=user)
# --- EoF ---


@router.delete("/users/user/", tags=["Users"])
async def delete_user(user_name: str, db: AsyncSession = Depends(get_db)):
	"""_summary_

	Args:
		user_name (str): user original name
		db (AsyncSession, optional): AsyncSession. Defaults to Depends(get_db).

	Raises:
		HTTPException: 404

	Returns:
		schema: User schema
	"""
	content = await user_crud.get_user_by_name(db, user_name=user_name)
	if content is None:
		raise HTTPException(
			status_code=404,
			detail=f"{user_name} is not found.")
	return await user_crud.delete_user(db, original=content)
# --- EoF ---


# End of Script
