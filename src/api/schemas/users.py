#!/usr/bin/env python
# -*- coding: utf8 -*-

from pydantic import BaseModel

class UserBase(BaseModel):
	user_name:str
	user_email:str
	user_pw:str

class UserCreate(UserBase):
	pass

class UserCreateResponse(UserCreate):
	user_id:int

class Users(UserCreate):
	user_id:int
	class Config:
		orm_mode = True
		allow_population_by_field_name = True

# End of Script