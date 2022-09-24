#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys

from typing import List, Tuple
from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.db import get_db

router = APIRouter()

# End of Script