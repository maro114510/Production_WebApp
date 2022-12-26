#!/usr/bin/env python
# -*- coding: utf8 -*-

from fastapi import APIRouter

router = APIRouter()


@router.put( "/tasks/{task_id}/done", response_model=None )
async def mark_task_as_done( task_id: int ):
	return
#--- EoF ---

@router.delete( "/tasks/{task_id}/done", response_model=None)
async def unmark_task_as_done():
	return
#--- EoF ---


# End of Script