#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
from typing import List
from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import api.schemas.users as schema
import api.cruds.users as user_crud
import api.models.db_model as model
from api.db import get_db

router = APIRouter()

@router.get("/users/", tags=["Users"], response_model=List[schema.Users])
async def read_users(body: schema.UserCreate):
    return [schema.Users(user_id=1, **body.dict())]
# --- EoF ---


@router.get("/users/{user_id}", tags=["Users"], response_model=schema.Users)
async def read_user(user_id: int, body: schema.UserCreate):
    return schema.Users(user_id=user_id, **body.dict())
# --- EoF ---


@router.post("/users/", tags=["Users"])
async def create_user(user_in:schema.UserCreate, db: AsyncSession = Depends(get_db)):
	try:
		r = await user_crud.create_user(db,user_in)
	except Exception as e:
		raise HTTPException( status_code=404,detail=f"{user_in.user_name}, or {user_in.user_email} is duplicated." )
	#-- except
	return r
# --- EoF ---


@router.put("/users/{user_id}",
            tags=["Users"],
            response_model=schema.UserCreateResponse)
async def update_user(user_id: int, body: schema.UserCreate):
    return schema.UserCreateResponse(user_id=user_id, **body.dict())
# --- EoF ---


@router.delete("/users/{user_id}", tags=["Users"], response_model=int)
async def delete_user(user_id: int):
    return 0
# --- EoF ---


# End of Script
