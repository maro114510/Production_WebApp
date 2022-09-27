#!/usr/bin/env python
# -*- coding: utf8 -*-

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, ForeignKey
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp
from sqlalchemy.sql.expression import text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

import hashlib

Base = declarative_base()


class UserPlaylist(Base):
	"""ユーザープレイリストテーブル"""
	__tablename__ = "user_playlists"
	# __abstract__ = True
	id = Column(Integer, primary_key=True)
	user_name = Column(
		ForeignKey(
			"users.user_name",
			ondelete="CASCADE"
		)
	)
	playlist_original_id = Column(
		ForeignKey(
			"playlists.playlist_original_id",
			ondelete="CASCADE"
		)
	)
	created_at=Column(
		Timestamp,
		server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')
	)

	user = relationship("User", back_populates="playlists")
	playlist = relationship("Playlist", back_populates="users")

	def __repr__(self) -> str:
		return "<UserPlaylist %r>" % self.id
# -- class


class NormalPlaylistMusic(Base):
	"""一般のプレイリスト音楽テーブル"""
	__tablename__ = "n_playlist_music"
	# __abstract__ = True
	id = Column(Integer, primary_key=True)
	playlist_original_id = Column(
		ForeignKey(
			"playlists.playlist_original_id",
			ondelete="CASCADE"
		)
	)
	music_original_id = Column(
		ForeignKey(
			"musics.music_original_id",
			ondelete="CASCADE"
		)
	)
	created_at=Column(
		Timestamp,
		server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')
	)

	n_playlist = relationship("Playlist", back_populates="n_musics")
	n_music = relationship('Music', back_populates="n_playlists")

	def __repr__(self) -> str:
		return "<NormalPlaylistMusic %r>" % self.id
# -- class


class DeletedPlaylistMusic(Base):
	"""削除されたプレイリスト音楽テーブル"""
	__tablename__ = "d_playlist_music"
	# __abstract__ = True
	id = Column(Integer, primary_key=True)
	playlist_original_id = Column(
		ForeignKey(
			"playlists.playlist_original_id",
			ondelete="CASCADE"
		)

	)
	music_original_id = Column(
		ForeignKey(
			"musics.music_original_id",
			ondelete="CASCADE"
		)
	)
	created_at=Column(
		Timestamp,
		server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')
	)

	d_music = relationship('Music', back_populates="d_playlists")
	d_playlist = relationship("Playlist", back_populates="d_musics")
	def __repr__(self) -> str:
		return "<DeletedPlaylistMusic %r>" % self.id
# -- class


class User(Base):
	"""ユーザーテーブル"""
	__tablename__ = 'users'
	# __abstract__ = True
	user_id = Column(Integer, primary_key=True, index=True)
	user_name = Column(String(64), nullable=False, unique=True)
	user_email = Column(String(128), nullable=False, unique=True)
	user_pw = Column(String(256), nullable=False)

	def __init__(self, user_name, user_email, user_pw):
		self.user_name = user_name
		self.user_email = user_email
		self.user_pw = hashlib.md5(user_pw.encode()).hexdigest()

	playlists = relationship(
		"UserPlaylist",
		back_populates="user",
		cascade="all, delete"
	)

	def __repr__(self) -> str:
		return "<User %r>" % self.user_id
# -- class


class Playlist(Base):
	"""プレイリストテーブル"""
	__tablename__ = 'playlists'
	# __abstract__ = True
	playlist_id = Column(Integer, primary_key=True, index=True)
	playlist_name = Column(String(126))
	playlist_original_id = Column(String(126), index=True, unique=True)

	users = relationship(
		"UserPlaylist",
		back_populates="playlist",
		cascade="all, delete"
	)
	n_musics = relationship(
		"NormalPlaylistMusic",
		back_populates="n_playlist",
		cascade="all, delete"
	)
	d_musics = relationship(
		"DeletedPlaylistMusic",
		back_populates="d_playlist",
		cascade="all, delete"
	)
	notify = relationship(
		'PlaylistNotify',
		back_populates="playlister",
		cascade="all, delete"
	)

	def __repr__(self) -> str:
		return "<Playlist %r>" % self.playlist_id
# -- class


class Music(Base):
	"""音楽テーブル"""
	__tablename__ = 'musics'
	# __abstract__ = True
	music_id = Column(Integer, primary_key=True, index=True)
	music_name = Column(String(126))
	music_original_id = Column(String(126), index=True, unique=True)

	n_playlists = relationship(
		"NormalPlaylistMusic", 
		back_populates="n_music",
		cascade="all, delete"
	)
	d_playlists = relationship(
		"DeletedPlaylistMusic",
		back_populates="d_music",
		cascade="all, delete"
	)

	def __repr__(self) -> str:
		return "<Music %r>" % self.music_id
# -- class


class PlaylistNotify(Base):
	"""通知可否テーブル"""
	__tablename__ = "playlistnotify"
	# __abstract__ = True
	# id = Column(Integer,primary_key=True)
	playlist_original_id = Column(
		ForeignKey('playlists.playlist_original_id'),
		primary_key=True,
		index=True
	)
	notify = Column(Boolean())

	playlister = relationship("Playlist", back_populates="notify")
# -- class


# End of Script
