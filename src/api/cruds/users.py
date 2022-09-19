#!/usr/bin/env python
# -*- coding: utf8 -*-


import sys
from sqlalchemy import text
from sqlalchemy.orm import Session, sessionmaker,joinedload
from sqlalchemy.ext.asyncio import AsyncSession

import api.models.db_model as model
import api.schemas.users as schema

async def get_user(db_session: Session, user_id: int):
    return db_session.query(model.User).filter(model.User.user_id == user_id).first()


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



# End of Script