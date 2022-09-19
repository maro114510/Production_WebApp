#!/usr/bin/env python
# -*- coding: utf8 -*-

from typing import List
from fastapi import APIRouter

import  api.schemas.users as schema

router = APIRouter()

@router.get("/users/",tags=["Users"],response_model=List[schema.Users])
async def read_users(body:schema.UserCreate):
	return [schema.Users(user_id=1,**body.dict())]
#--- EoF ---

@router.get("/users/{user_id}",tags=["Users"],response_model=schema.Users)
async def read_user(user_id:int,body:schema.UserCreate):
	return schema.Users(user_id=user_id,**body.dict())
#--- EoF ---

@router.post("/users/",tags=["Users"],response_model=schema.UserCreateResponse)
async def create_user(body:schema.UserCreate):
	return schema.UserCreateResponse(
		user_id=1,
		**body.dict()
	)
#--- EoF ---

@router.put("/users/{user_id}",tags=["Users"],response_model=schema.UserCreateResponse)
async def update_user(user_id:int,body:schema.UserCreate):
	return schema.UserCreateResponse(user_id=user_id,**body.dict())
#--- EoF ---

@router.delete("/users/{user_id}",tags=["Users"],response_model=int)
async def delete_user(user_id:int):
	return 0
#--- EoF ---



# End of Script