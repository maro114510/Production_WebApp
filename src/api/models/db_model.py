#!/usr/bin/env python
# -*- coding: utf8 -*-

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

import hashlib

Base = declarative_base()

class UserPlaylist(Base):
	"""ユーザープレイリストテーブル"""
	__tablename__ = "user_playlists"
	id = Column(Integer,primary_key=True)
	user_name = Column(ForeignKey("users.user_name"))
	playlist_original_id = Column(ForeignKey("playlists.playlist_original_id"),index=True)

	user = relationship("User",back_populates="playlists")
	playlist = relationship("Playlist",back_populates="users")
#-- class

class NormalPlaylistMusic(Base):
	"""一般のプレイリスト音楽テーブル"""
	__tablename__ = "n_playlist_music"
	id = Column(Integer,primary_key=True)
	playlist_original_id = Column(ForeignKey("playlists.playlist_original_id"),index=True)
	music_original_id = Column(ForeignKey("musics.music_original_id"),index=True)
	date = Column(String(30))

	n_playlist = relationship("Playlist",back_populates="n_musics")
	n_music = relationship('Music',back_populates="n_playlists")
#-- class

class DeletedPlaylistMusic(Base):
	"""削除されたプレイリスト音楽テーブル"""
	__tablename__ = "d_playlist_music"
	id = Column(Integer,primary_key=True)
	playlist_original_id = Column(ForeignKey("playlists.playlist_original_id"),index=True)
	music_original_id = Column(ForeignKey("musics.music_original_id"),index=True)
	date = Column(String(30))

	d_music = relationship('Music',back_populates="d_playlists")
	d_playlist = relationship("Playlist",back_populates="d_musics")
#-- class

class User(Base):
	"""ユーザーテーブル"""
	__tablename__ = 'users'
	user_id = Column(Integer, primary_key = True,index=True)
	user_name = Column(String(64),nullable=False,unique=True)
	user_email = Column(String(128),nullable=False,unique=True)
	user_pw = Column(String(256),nullable=False)

	def __init__(self,user_name,user_email,user_pw):
		self.user_name = user_name
		self.user_email = user_email
		self.user_pw = hashlib.md5(user_pw.encode()).hexdigest()

	playlists = relationship("UserPlaylist",back_populates="user")
#-- class

class Playlist(Base):
	"""プレイリストテーブル"""
	__tablename__ = 'playlists'
	playlist_id  = Column(Integer,primary_key=True,index=True)
	playlist_name = Column(String(126))
	playlist_original_id = Column(String(126),index=True,unique=True)

	users = relationship("UserPlaylist",back_populates="playlist")

	n_musics = relationship("NormalPlaylistMusic",back_populates="n_playlist")
	d_musics = relationship("DeletedPlaylistMusic",back_populates="d_playlist")

	notify = relationship('PlaylistNotify',back_populates="playlister")
#-- class

class Music(Base):
	"""音楽テーブル"""
	__tablename__ = 'musics'
	music_id  = Column(Integer,primary_key=True,index=True)
	music_name = Column(String(126))
	music_original_id = Column(String(126),index=True,unique=True)

	n_playlists = relationship("NormalPlaylistMusic",back_populates="n_music")
	d_playlists = relationship("DeletedPlaylistMusic",back_populates="d_music")
#-- class

class PlaylistNotify(Base):
	"""通知可否テーブル"""
	__tablename__ = "playlistnotify"
	# id = Column(Integer,primary_key=True)
	playlist_original_id = Column(ForeignKey('playlists.playlist_original_id'),primary_key=True,index=True)
	notify = Column(Boolean())

	playlister = relationship("Playlist",back_populates="notify")
#-- class


# End of Script