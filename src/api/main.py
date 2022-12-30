#!/usr/bin/env python
# -*- coding: utf8 -*-

from fastapi import FastAPI

from api.routers import users, playlists, musics

app = FastAPI()


app.include_router( users.router )
app.include_router( playlists.router )
app.include_router( musics.router )


# End of Script