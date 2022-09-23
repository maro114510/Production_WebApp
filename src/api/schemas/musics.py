#!/usr/bin/env python
# -*- coding: utf8 -*-

from pydantic import BaseModel


class MusicBase(BaseModel):
	"""_summary_

	Args:
		BaseModel (class): pydantic basemodel
	"""
	music_name: str
	music_original_id: str
# -- class


class MusicCreate(MusicBase):
	"""_summary_

	Args:
		MusicBase (class): Inherits MusicBase class
	"""
	pass
# -- class


class MusicCreateResponse(MusicCreate):
	"""_summary_

	Args:
		MusicCreate (class): Inherit MusicCreate class
	"""
	music_id: int

	class Config:
		orm_mode = True
# -- class


class Musics(MusicCreate):
	"""_summary_

	Args:
		MusicCreate (_type_): Inherit MusicCreate class
	"""
	music_id: int
	date: str

	class Config:
		orm_mode = True
		allow_population_by_field_name = True
# -- class

# End of Script
