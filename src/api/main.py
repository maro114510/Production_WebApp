#!/usr/bin/env python
# -*- coding: utf8 -*-

from fastapi import FastAPI

from api.routers import users, playlist, music

app = FastAPI(
	title="Youtube Diff Checker",
	description=
	"""
	バックエンド部分の処理
	""",
)

# routers
app.include_router(users.router)
app.include_router(playlist.router)
app.include_router(music.router)


# End of Script