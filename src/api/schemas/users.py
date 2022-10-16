#!/usr/bin/env python
# -*- coding: utf8 -*-

from typing import Optional

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    """_summary_

    Args:
            BaseModel (class): Inherit pydantic's Basemodel class
    """
    user_name: Optional[str] = Field(None, example="user")
    user_email: Optional[str] = Field(None, example="user@gmail.com")
    user_pw: str
# -- class


class UserCreate(UserBase):
    """_summary_

    Args:
            UserBase (class): Inherits UserBase class
    """
    pass
# -- class


class UserCreateResponse(UserCreate):
    """_summary_

    Args:
            UserCreate (class): Inherits UserCreate class
    """
    user_id: int
# -- class


class Users(UserCreate):
    """_summary_

    Args:
            UserCreate (class): Inherits UserCreate class
    """
    user_id: int

    class Config:
        orm_mode = True
        # allow_population_by_field_name = True
# -- class

# End of Script
