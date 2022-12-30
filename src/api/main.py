#!/usr/bin/env python
# -*- coding: utf8 -*-

from fastapi import FastAPI

from api.routers import users

app = FastAPI()


app.include_router( users.router )


# End of Script