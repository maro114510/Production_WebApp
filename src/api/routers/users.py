#!/usr/bin/env python
# -*- coding: utf8 -*-

from fastapi import APIRouter

router = APIRouter()

@router.get("/users/",tags=["Users"])
async def read_users():
    pass
#--- EoF ---

@router.get("/users/{user_id}",tags=["Users"])
async def read_user():
    pass
#--- EoF ---

@router.post("/users/",tags=["Users"])
async def create_user():
    pass
#--- EoF ---

@router.put("/users/{user_id}",tags=["Users"])
async def update_user():
    pass
#--- EoF ---

@router.delete("/users/{user_id}",tags=["Users"])
async def delete_user():
    pass
#--- EoF ---



# End of Script