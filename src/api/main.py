#!/usr/bin/env python
# -*- coding: utf8 -*-

from fastapi import FastAPI

from api.routers import musics, playlists, users, user_playlists, n_playlist_musics, d_playlist_musics, firtst_register

app = FastAPI(
        title="Youtube Diff Checker",
        description="""
	バックエンド部分の処理
	""",
)

# routers
app.include_router(users.router)
app.include_router(playlists.router)
app.include_router(musics.router)
app.include_router(user_playlists.router)
app.include_router(n_playlist_musics.router)
app.include_router(d_playlist_musics.router)
app.include_router(firtst_register.router)


# End of Script
