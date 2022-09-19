#!/usr/bin/env python
# -*- coding: utf8 -*-

from pydantic import BaseModel


class MusicBase(BaseModel):
    music_name: str
    music_original_id: str
# -- class


class MusicCreate(MusicBase):
    pass
# -- class


class MusicCreateResponse(MusicCreate):
    music_id: int

    class Config:
        orm_mode = True
# -- class


class Musics(MusicCreate):
    music_id: int
    date: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
# -- class

# End of Script
