#!/usr/bin/env python
# -*- coding: utf8 -*-

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def hello():
    return {"message": "hello world!"}
# --- EoF ---


# End of Script
