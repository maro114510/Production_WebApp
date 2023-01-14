#!/usr/bin/env python
# -*- coding: utf8 -*-

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field



class FullUserInfo( BaseModel ):
	uid: int
	user_name: Optional[ str ] = Field( None, example="youtuber" )
	user_email: Optional[ str ] = Field( None, example="youtube@mail" )
	user_pw: str
	status: int
	created_at: datetime
	modified_at: datetime
#--- FullUserInfo ---


# End of Script