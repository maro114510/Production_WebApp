#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import hashlib
from typing import List
from fastapi import APIRouter, HTTPException

from api.cruds.user_playlists import UserPlaylists

ins = UserPlaylists()
router = APIRouter()


@router.get( "/user_playlists", tags=[ "UserPlaylists" ] )
async def list_user_playlists() -> List[ dict ]:
	return 0
#--- EoF ---