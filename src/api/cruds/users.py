#!/usr/bin/env python
# -*- coding: utf8 -*-

from operator import mod
import sys
from typing import Optional, Tuple
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import api.models.db_model as model
import api.schemas.users as schema

async def get_users(db_session: AsyncSession):
	result: Result = await (
		db_session.execute(
			select(
				model.User.user_id,
				model.User.user_email,
				model.User.user_pw,
			)
		)
	)
	return result.all()
#--- EoF ---

async def get_user_by_id(db_session: AsyncSession,user_id:int):
	result: Result = await (
		db_session.execute(
			select(model.User).filter(model.User.user_id==user_id)
		)
	)
	user: Optional[Tuple[model.User]] = result.first()
	return user[0]
#--- EoF ---

async def get_user_by_name(db_session: AsyncSession,user_name:str):
	result: Result = await (
		db_session.execute(
			select(model.User).filter(model.User.user_name==user_name)
		)
	)
	user: Optional[Tuple[model.User]] = result.first()
	return user[0] if user is not None else None
#--- EoF ---

async def create_user(
		db:AsyncSession, user_create:schema.UserCreate
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
#--- EoF ---

async def update_user(
		db: AsyncSession,user:schema.UserCreate,original:model.User
	):
	original.user_name = user.user_name
	original.user_email = user.user_email
	original.user_pw = user.user_pw
	db.add(original)
	await db.commit()
	await db.refresh(original)
	return original
#--- EoF ---

async def delete_user(
		db_session: AsyncSession,original:model.User
	):
	await db_session.delete(original)
	await db_session.commit()
#--- EoF ---



# End of Script