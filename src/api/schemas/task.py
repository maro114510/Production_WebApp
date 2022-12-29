#!/usr/bin/env python
# -*- coding: utf8 -*-

from typing import Optional

from pydantic import BaseModel, Field


class TaskBase( BaseModel ):
	title: Optional[ str ] = Field( None, example="クリーニングを取りに行く" )
#--- Class ---


class TaskCreate( TaskBase ):
	pass
#--- Class ---

class TaskCreateResponse( TaskCreate ):
	id: int

	class Config:
		orm_mode = True
	#--- Class ---
#--- Class ---

class Task( TaskBase ):
	id: int
	done: bool = Field( False, description="完了フラグ" )

	class Config:
		orm_mode = True
	#--- Class ---
#--- Class ---



# End of Script