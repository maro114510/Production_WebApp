#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import hashlib
from typing import List
from fastapi import APIRouter, HTTPException

import api.schemas.task as ts
from api.cruds.insert import Insert
from api.cruds.read import Read

router = APIRouter()


@router.get( "/users" )
async def list_users():
	read_ins = Read()
	return read_ins.execute()
#--- EoF ---


@router.post( "/users" )
async def create_user( 
	name: str,
	email: str,
	passwd: str
) -> int:
	insert_ins = Insert()
	try:
		insert_ins.execute(
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


@router.put( "/users/{task_id}", response_model=ts.TaskCreateResponse )
async def update_task( task_id: int, body: ts.TaskCreate ):
	return ts.TaskCreateResponse( id=task_id, **body.dict() )
#--- EoF ---


@router.delete( "/users/{task_id}", response_model=None )
async def delete_task( task_id: int ):
	return 
#--- EoF ---




# End of Script