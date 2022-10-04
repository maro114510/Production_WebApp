#!/usr/bin/env python
# -*- coding: utf8 -*-

import json
import sys
from urllib import response
import pytest
from httpx import AsyncClient
from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
import starlette.status

from api.db import get_db
from api.models.db_test_model import Base
from api.schemas.users import UserCreate
from api.main import app

ASYNC_DB_URL = "sqlite+aiosqlite:///:memory:"

@event.listens_for(Engine,"connect")
def my_my_connect(dbapi_connection, connection_record):
	cursor = dbapi_connection.cursor()
	cursor.execute("PRAGMA foreign_keys=ON")
	cursor.close()
#--- EoF ---

@pytest.fixture
async def async_client() -> AsyncClient:
	async_engine = create_async_engine(
		ASYNC_DB_URL,
		echo=True
	)

	async_session = sessionmaker(
		autocommit=False,
		autoflush=False,
		bind=async_engine,
		class_=AsyncSession
	)

	async with async_engine.begin() as conn:
		await conn.run_sync(Base.metadata.drop_all)
		await conn.run_sync(Base.metadata.create_all)
	#-- with

	async def get_test_db():
		async with async_session() as session:
			yield session
		#-- with
	#--- EoF ---

	app.dependency_overrides[get_db] = get_test_db

	async with AsyncClient(app=app,base_url="http://test",) as client:
		yield client
	#-- with
#--- EoF ---

@pytest.mark.asyncio
async def test_create_user(async_client):
	response = await async_client.post(
		"/users/",
		json = {
			"user_name":"nohira",
			"user_email":"nohira@gmail.com",
			"user_pw":"nohira"
		}
	)
	assert response.status_code == starlette.status.HTTP_200_OK
	response_obj = response.json()
	assert response_obj["user_id"] == 1

	response = await async_client.get("/users/")
	assert response.status_code == starlette.status.HTTP_200_OK
	response_obj = response.json()
	assert len(response_obj) == 1
	assert response_obj[0]["user_name"] == "nohira"
	assert response_obj[0]["user_email"] == "nohira@gmail.com"

	return 0
#--- EoF ---

@pytest.mark.asyncio
async def test_create_playlist(async_client):
	params = {
		'url': 'https://youtube.com/playlist?list=PLSFrP_aW8LfyEIahQGnpdvDtPUKKWxi-H',
	}
	response = await async_client.post(
		"/playlists/",
		params=params,
	)
	assert response.status_code == starlette.status.HTTP_200_OK
	response_obj = response.json()
	assert response_obj["playlist_id"] == 1

	response = await async_client.get("/playlists/")
	assert response.status_code == starlette.status.HTTP_200_OK
	response_obj = response.json()
	assert len(response_obj) == 1
	assert response_obj[0]["playlist_name"] == "勉強のお供に123"
	assert response_obj[0]["playlist_original_id"] == "PLSFrP_aW8LfyEIahQGnpdvDtPUKKWxi-H"

	return 0
#--- EoF ---

@pytest.mark.asyncio
async def test_create_music(async_client):
	json_data = {
		'music_name': 'stringer',
		'music_original_id': 'stringer',
	}
	response = await async_client.post(
		"/musics/",
		json=json_data,
	)
	assert response.status_code == starlette.status.HTTP_200_OK
	response_obj = response.json()
	assert response_obj["music_id"] == 1

	response = await async_client.get("/musics/")
	assert response.status_code == starlette.status.HTTP_200_OK
	response_obj = response.json()
	assert len(response_obj) == 1
	assert response_obj[0]["music_name"] == "stringer"
	assert response_obj[0]["music_original_id"] == "stringer"

	return 0
#--- EoF ---


@pytest.mark.asyncio
async def test_error(async_client):
	response = await async_client.post(
		"/users/",
		json = {
			"user_name":"nohira",
			"user_email":"nohira@gmail.com",
			"user_pw":"nohira"
		}
	)
	assert response.status_code == starlette.status.HTTP_200_OK
	response = await async_client.post(
		"/users/",
		json = {
			"user_name":"nohira",
			"user_email":"nohira@gmail.com",
			"user_pw":"nohira"
		}
	)
	assert response.status_code == starlette.status.HTTP_404_NOT_FOUND

	return 0
#--- EoF ---



# End of Script