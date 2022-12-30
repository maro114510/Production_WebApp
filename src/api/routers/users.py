#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import hashlib
from typing import List
from fastapi import APIRouter, HTTPException

from api.cruds.users import Users

ins = Users()
router = APIRouter()


@router.get( "/users", tags=[ "Users" ] )
async def list_users() -> List[ dict ]:
	return ins.get_all_users_full_info()
#--- EoF ---


@router.get( "/users/user", tags=[ "Users" ] )
async def get_user_info(
	user_name: str,
	user_email: str
) -> dict:
	return ins.get_one_user_info(
		user_name,
		user_email
	)
#--- EoF ---

@router.post( "/users", tags=[ "Users" ] )
async def create_user( 
	name: str,
	email: str,
	passwd: str
) -> int:
	try:
		ins.user_insert(
			name,
			email,
			hashlib.md5( passwd.encode() ).hexdigest()
		)
	except Exception as e:
		print( "%s" % ( [e.args, ] ), file=sys.stderr )
		raise HTTPException(
			status_code=404,
			detail="Either the user's email address or the user's password is duplicated. Please change it.",
		)
	#-- except
	return 0
#--- EoF ---


@router.put( "/users/update", tags=["Users"] )
async def update_task(
	old_user_name,
	old_user_email,
	user_name: str,
	user_email: str,
	user_pw: str
) -> int:
	try:
		ins.update_user_info(
			old_user_name,
			old_user_email,
			hashlib.md5( user_pw.encode() ).hexdigest(),
			user_name,
			user_email,
		)
	except Exception as e:
		print( "%s" % ( [e.args, ] ), file=sys.stderr )
		raise HTTPException(
			status_code=404,
			detail="Sorry, Try again.",
		)
	#-- except
	return 0
#--- EoF ---


@router.delete( "/users/delete", tags=["Users"] )
async def delete_task(
	user_name: str,
	user_email: str
) -> int:
	try:
		ins.delete_user(
			user_name,
			user_email,
		)
	except Exception as e:
		print( "%s" % ( [e.args, ] ), file=sys.stderr )
		raise HTTPException(
			status_code=404,
			detail="Sorry, Try again.",
		)
	#-- except
	return 0
#--- EoF ---




# End of Script