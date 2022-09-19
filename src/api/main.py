#!/usr/bin/env python
# -*- coding: utf8 -*-

from fastapi import FastAPI

from api.routers import musics, playlists, users

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



# End of Script
