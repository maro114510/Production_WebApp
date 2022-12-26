#!/usr/bin/env python
# -*- coding: utf8 -*-

from typing import List
from fastapi import APIRouter

import api.schemas.task as ts

router = APIRouter()


@router.get( "/tasks", response_model=List[ ts.Task ] )
async def list_tasks():
	return [
		ts.Task( id=1, title="oneoneone" )
	]
#--- EoF ---


@router.post( "/tasks", response_model=ts.TaskCreateResponse )
async def create_task( body: ts.TaskCreate ):
	return ts.TaskCreateResponse( id=1, **body.dict() )
#--- EoF ---


@router.put( "/tasks/{task_id}", response_model=ts.TaskCreateResponse )
async def update_task( task_id: int, body: ts.TaskCreate ):
	return ts.TaskCreateResponse( id=task_id, **body.dict() )
#--- EoF ---


@router.delete( "/tasks/{task_id}", response_model=None )
async def delete_task( task_id: int ):
	return 
#--- EoF ---




# End of Script