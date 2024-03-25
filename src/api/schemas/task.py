#!/usr/bin/env python
# -*- coding: utf8 -*-

from typing import Optional

from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: Optional[str] = Field(None, example="クリーニングを取りに行く")
# --- TaskBase ---


class TaskCreate(TaskBase):
    pass
# --- TaskBase ---


class TaskCreateResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True
    # --- Config ---
# --- TaskCreateResponse ---


class Task(TaskBase):
    id: int
    done: bool = Field(False, description="完了フラグ")

    class Config:
        orm_mode = True
    # --- Config ---
# --- Task ---


# End of Script
