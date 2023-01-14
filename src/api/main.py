#!/usr/bin/env python
# -*- coding: utf8 -*-

from fastapi import FastAPI

from api.routers import users, playlists, musics, user_playlists, playlist_musics, interface

app = FastAPI(
        title="Youtube Diff Checker",
        description="""
	バックエンド部分の処理
	""",
)


app.include_router( users.router )
app.include_router( playlists.router )
app.include_router( musics.router )
app.include_router( user_playlists.router )
app.include_router( playlist_musics.router )
app.include_router( interface.router )


# End of Script
