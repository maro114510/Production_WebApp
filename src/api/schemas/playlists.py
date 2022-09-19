#!/usr/bin/env python
# -*- coding: utf8 -*-

from pydantic import BaseModel

class PlaylistBase(BaseModel):
    playlist_name:str 
    playlist_original_id:str

class PlaylistCreate(PlaylistBase):
    pass

class PlaylistCreateResponse(PlaylistCreate):
    playlist_id:int
    class Config:
        orm_mode = True

class Playlists(PlaylistCreate):
    playlist_id:int
    notify:bool
    date:str
    class Config:
        orm_mode = True
        allow_population_by_field_name = True

# End of Script