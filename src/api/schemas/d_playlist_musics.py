#!/usr/bin/env python
# -*- coding: utf8 -*-

from typing import Optional

from pydantic import BaseModel


class DeletedPlaylistMusicsSchema(BaseModel):
    """_summary_

    Args:
            BaseModel (class): Inherit pydantic's Basemodel class
    """
    id: int
    playlist_original_id: str
    music_original_id: str
    date: str
# -- class


# End of Script
