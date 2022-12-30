#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import hashlib
from fastapi import APIRouter, HTTPException

from api.cruds.users import Users

ins = Users()
router = APIRouter()


@router.get( "/users", tags=[ "Users" ] )
async def list_users():
	return ins.get_all_users_full_info()
#--- EoF ---


@router.get( "/users", tags=[ "Users" ] )
async def get_user_info():
	# read_ins = Read()
	# return read_ins.execute()
	return 0
#--- EoF ---

@router.post( "/users", tags=[ "Users" ] )
async def create_user( 
	name: str,
	email: str,
	passwd: str
) -> int:
	# try:
	# 	ins.user_insert(
	# 		name,
	# 		email,
	# 		hashlib.md5( passwd.encode() ).hexdigest()
	# 	)
	# except Exception as e:
	# 	print( "%s" % ( [e.args, ] ), file=sys.stderr )
	# 	raise HTTPException(
	# 		status_code=404,
	# 		detail="Either the user's email address or the user's password is duplicated. Please change it.",
	# 	)
	# #-- except
	return 0
#--- EoF ---


# @router.put( "/users/{user_name}", tags=["Users"] )
# async def update_task( user_name: int, body: ts.TaskCreate ):
# 	return ts.TaskCreateResponse( id=user_name, **body.dict() )
# #--- EoF ---


@router.delete( "/users/{user_name}", tags=["Users"] )
async def delete_task( user_name: int ):
	return 
#--- EoF ---




# End of Script