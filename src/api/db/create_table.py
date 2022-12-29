#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
from conn import Connector


class CreateTable():
	def __init__( self ):
		ins = Connector()
		self.conn = ins.Connector()
	#--- EoF ---

	def execute( self ):
		cur = self.conn.cursor()
		sql = self.create_sql()
		cur.execute( sql )
		self.conn.commit()
		print( "OK" )
	#--- EoF ---

	def main( self, argc, argv ):
		self.execute()
		return 0
	#--- EoF ---

	def create_sql( self ):
		sql = """
DROP TABLE IF EXISTS t_users;
CREATE TABLE t_users (
  uid			SERIAL			PRIMARY KEY, -- 通し番号
  user_name		VARCHAR(50)		NOT NULL, -- ユーザー名
  user_email	VARCHAR(100)	NOT NULL , -- Emailアドレス
  user_pw		VARCHAR(100)	NOT NULL,  -- ハッシュ化されたパスワード
  status		INTEGER			DEFAULT 0,  -- ユーザーの状態管理
  created_at	TIMESTAMP		DEFAULT CURRENT_TIMESTAMP,  -- 作成日付時刻
  modified_at	TIMESTAMP		DEFAULT CURRENT_TIMESTAMP, -- 修正日付時刻

  -- UNIQUE
  UNIQUE( user_email, user_pw )
);
GRANT ALL PRIVILEGES ON t_users TO ytber;

DROP TABLE IF EXISTS t_playlists;
CREATE TABLE t_playlists (
  pid			SERIAL			PRIMARY KEY,  -- 通し番号
  playlist_name	VARCHAR(100)	NOT NULL, -- プレイリスト名
  p_org_id		VARCHAR(100)	NOT NULL, -- プレイリストID
  created_at	TIMESTAMP		DEFAULT CURRENT_TIMESTAMP, -- 作成日付時刻
  modified_at	TIMESTAMP		DEFAULT CURRENT_TIMESTAMP, -- 修正日付時刻

  -- UNIQUE
  UNIQUE( p_org_id )
);
GRANT ALL PRIVILEGES ON t_playlists TO ytber;

DROP TABLE IF EXISTS t_musics;
CREATE TABLE t_musics (
  mid			SERIAL			PRIMARY KEY,  -- 通し番号
  music_name	VARCHAR(100)	NOT NULL, -- 動画名
  m_org_id		VARCHAR(100)	NOT NULL, -- 動画ID
  created_at	TIMESTAMP		DEFAULT CURRENT_TIMESTAMP, -- 作成日付時刻
  modified_at	TIMESTAMP		DEFAULT CURRENT_TIMESTAMP, -- 修正日付時刻

  -- UNIQUE
  UNIQUE( m_org_id )
);
GRANT ALL PRIVILEGES ON t_musics TO ytber;


DROP TABLE IF EXISTS t_user_playlists;
CREATE TABLE t_user_playlists (
  id			SERIAL			PRIMARY KEY, -- 通し番号
  uid			INTEGER			NOT NULL, -- ユーザー名
  p_org_id		VARCHAR(100)	NOT NULL,  -- プレイリストID
  flag			BOOLEAN			DEFAULT true, -- ユーザーの持つプレイリストの状態管理
  created_at	TIMESTAMP		DEFAULT CURRENT_TIMESTAMP, -- 作成日付時刻
  modified_at	TIMESTAMP		DEFAULT CURRENT_TIMESTAMP, -- 修正日付時刻

  -- FOREIGN KEY
  CONSTRAINT fk_t_user_playlist__uid FOREIGN KEY (
    uid
  ) REFERENCES t_users( uid ),
  CONSTRAINT fk_t_user_playlist__p_org_id FOREIGN KEY (
    p_org_id
  ) REFERENCES t_playlists( p_org_id )
);
GRANT ALL PRIVILEGES ON t_user_playlists TO ytber;

DROP TABLE IF EXISTS t_playlist_musics;
CREATE TABLE t_playlist_musics (
  id			SERIAL			PRIMARY KEY, -- 通し番号
  p_org_id		VARCHAR(50)		NOT NULL, -- プレイリストID
  m_org_id		VARCHAR(100)	NOT NULL, -- 動画ID
  status		INTEGER			DEFAULT 0, -- プレイリストの状態管理
  created_at	TIMESTAMP		DEFAULT CURRENT_TIMESTAMP, -- 作成日付時刻
  modified_at	TIMESTAMP		DEFAULT CURRENT_TIMESTAMP, -- 修正日付時刻

  -- FOREIGN KEY
  CONSTRAINT fk_t_playlist_music__p_org_id FOREIGN KEY (
    p_org_id
  ) REFERENCES t_playlists( p_org_id ),
  CONSTRAINT fk_t_playlist_music__m_org_id FOREIGN KEY (
    m_org_id
  ) REFERENCES t_musics( m_org_id )
);
GRANT ALL PRIVILEGES ON t_playlist_musics TO ytber;
		"""
		return sql
	#--- EoF ---
#--- CreateTable ---


# Entry Point

if __name__ == "__main__":
	ins = CreateTable()
	sys.exit( 1 )
	sys.exit( ins.main( len( sys.argv ), sys.argv ) )
#-- if



# End of Script