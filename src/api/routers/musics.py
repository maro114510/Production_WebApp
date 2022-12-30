#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
from typing import List
from fastapi import APIRouter, HTTPException

from api.cruds.musics import Musics

ins = Musics()
router = APIRouter()


@router.get( "/musics", tags=[ "Musics" ] )
async def list_musics() -> List[ dict ]:
	return 0
#--- EoF ---




# End of Script