#!/usr/bin/env python
# -*- coding: utf8 -*-

from pydantic import BaseModel


class PlaylistBase(BaseModel):
    """_summary_

    Args:
            BaseModel (class): Inherit pydantic's Basemodel class
    """
    playlist_name: str
    playlist_original_id: str
# -- class


class PlaylistCreate(PlaylistBase):
    """_summary_

    Args:
            PlaylistBase (class): Inherits PlaylistBase class
    """
    pass
# -- class


class PlaylistCreateResponse(PlaylistCreate):
    """_summary_

    Args:
            PlaylistCreate (class): Inherits PlaylistCrea class
    """
    playlist_id: int

    class Config:
        orm_mode = True
# -- class


class Playlists(PlaylistCreate):
    """_summary_

    Args:
            PlaylistCreate (class): Inherits PlaylistCrea class
    """
    playlist_id: int
    notify: bool
    date: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
# -- class

# End of Script
