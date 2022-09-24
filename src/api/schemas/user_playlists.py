#!/usr/bin/env python
# -*- coding: utf8 -*-

from typing import Optional

from pydantic import BaseModel

class UserPlaylistSchema(BaseModel):
	"""_summary_

	Args:
		BaseModel (class): Inherit pydantic's Basemodel class
	"""
	id:int
	user_name:str
	playlist_original_id:str
#-- class


# End of Script