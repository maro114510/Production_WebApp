#!/usr/bin/env python
# -*- coding: utf8 -*-

from typing import Optional

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    user_name: Optional[str] = Field(None, example="user")
    user_email: Optional[str] = Field(None, example="user@gmail.com")
    user_pw: str
# -- class


class UserCreate(UserBase):
    pass
# -- class


class UserCreateResponse(UserCreate):
    user_id: int
# -- class


class Users(UserCreate):
    user_id: int

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
# -- class

# End of Script