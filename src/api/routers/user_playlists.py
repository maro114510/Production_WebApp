#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import hashlib
from typing import List
from fastapi import APIRouter, HTTPException

from api.cruds.user_playlists import UserPlaylists

ins = UserPlaylists()
router = APIRouter()


@router.get("/user_playlists", tags=["UserPlaylists"])
async def list_user_playlists() -> List[dict]:
    return ins.get_all_user_playlists_full_info()
# --- EoF ---


@router.get("/user_playlists/user_playlists", tags=["UserPlaylists"])
async def get_user_playlists_info(uid: int):
    return ins.get_user_playlists_byUid(uid)
# --- EoF ---


@router.get("/user_playlists/d/user_playlists", tags=["UserPlaylists"])
async def get_d_user_playlists_info(uid: int):
    return ins.get_one_user_playlists_d_info(uid)
# --- EoF ---


@router.post("/user_playlists", tags=["UserPlaylists"])
async def create_user_playlists(
        uid: int,
        p_org_id: str
):
    try:
        ins.user_playlists_insert(
            uid,
            p_org_id
        )
    except Exception as e:
        print("%s" % ([e.args, ]), file=sys.stderr)
        raise HTTPException(
            status_code=455,
            detail="Either the uid or the p_org_id is duplicated. Please change it.",
        )
    # -- except
    return 0
# --- EoF ---


@router.delete("/user_playlists", tags=["UserPlaylists"])
async def delete_user_playlists(
        uid: int,
        p_org_id: str
) -> int:
    try:
        ins.delete_user_playlist(uid, p_org_id)
    except Exception as e:
        print("%s" % ([e.args, ]), file=sys.stderr)
        raise HTTPException(
            status_code=404,
            detail="Sorry, Try again.",
        )
    # -- except
    return 0
# --- EoF ---


@router.put("/user_playlists", tags=["UserPlaylists"])
async def update_user_playlists(
        uid: int,
        p_org_id
):
    try:
        judge = ins.update_user_playlist(
            uid,
            p_org_id
        )
        if judge != 0:
            print("NO EFFECT")
        # -- if
    except Exception as e:
        print("%s" % ([e.args, ]), file=sys.stderr)
        raise HTTPException(
            status_code=404,
            detail="Sorry, Try again.",
        )
    # -- except
    return 0
# --- EoF ---


# End of Script
