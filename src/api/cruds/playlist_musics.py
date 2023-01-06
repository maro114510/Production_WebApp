#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
from pathlib import Path
from psycopg2.extras import RealDictCursor

sys.path.append(
	str(
		Path(
			__file__
		).resolve().parent.parent.parent
	)
)

from api.db.conn import Connector


class PlaylistMusics():
	def __init__( self ):
		ins = Connector()
		self.conn = ins.Connector()
	#--- EoF ---

	def get_all_playlist_musics_full_info( self ):
		cur = self.conn.cursor( cursor_factory=RealDictCursor )
		sql = self.select_all_sql()
		try:
			cur.execute( sql )
			results = cur.fetchall()
			self.conn.commit()
			print( "SELECT OK" )
			return results
		except Exception as e:
			self.conn.rollback()
			raise e
		#-- except
	#--- EoF ---

	def get_one_playlist_musics_info( self, p_org_id ):
		cur = self.conn.cursor( cursor_factory=RealDictCursor )
		sql = self.select_by_pid_sql()
		try:
			cur.execute(
				sql,
				(
					p_org_id,
				)
			)
			results = cur.fetchall()
			self.conn.commit()
			print( "SELECT OK" )
			return results
		except Exception as e:
			self.conn.rollback()
			raise e
		#-- except
	#--- EoF ---

	def get_del_playlist_musics_info( self, p_org_id ):
		cur = self.conn.cursor( cursor_factory=RealDictCursor )
		sql = self.select_by_pid_d_sql()
		try:
			cur.execute(
				sql,
				(
					p_org_id,
				)
			)
			results = cur.fetchall()
			self.conn.commit()
			print( "SELECT OK" )
			return results
		except Exception as e:
			self.conn.rollback()
			raise e
		#-- except
	#--- EoF ---

	def playlist_musics_insert( self, p_org_id, m_org_id ):
		cur = self.conn.cursor()
		sql = self.insert_sql()
		try:
			cur.execute(
				sql,
				(
					p_org_id,
					m_org_id,
					p_org_id,
					m_org_id,
				)
			)
			self.conn.commit()
			print( "INSERT OK" )
		except Exception as e:
			self.conn.rollback()
			raise e
		#-- except
	#--- EoF ---

	def playlist_musics_bulk_insert( self, bulk ):
		cur = self.conn.cursor()
		sql = self.insert_sql()
		try:
			cur.executemany(
				sql,
				bulk,
			)
			self.conn.commit()

			if cur.rowcount != len( bulk ):
				print( "INSERT OK" )
			#-- if
			else:
				print( "SOME OF DUPLICATED" )
			#-- else
		except Exception as e:
			self.conn.rollback()
			raise e
		#-- except
	#--- EoF ---

	def delete_playlist_musics( self, p_org_id, m_org_id ):
		cur = self.conn.cursor()
		sql = self.delete_sql()
		try:
			cur.execute(
				sql,
				(
					p_org_id,
					m_org_id,
				)
			)
			self.conn.commit()
			print( "DELETE OK" )
		except Exception as e:
			self.conn.rollback()
			raise e
		#-- except
		return 0
	#--- EoF ---

	def execute( self ):
		print( "OK" )
	#--- EoF ---

	def main( self, argc, argv ):
		self.execute()
		return 0
	#--- EoF ---

	def select_all_sql( self ):
		sql = """
		SELECT
			*
		FROM
			t_playlist_musics
		WHERE
			status = 0;
		"""
		return sql
	#--- EoF ---

	def insert_sql( self ):
		sql = """
		INSERT INTO t_playlist_musics (
			p_org_id,
			m_org_id
		)
		SELECT
			%s,
			%s
			WHERE NOT EXISTS (
				SELECT 1 FROM t_playlist_musics
				WHERE
					p_org_id = %s
				AND
					m_org_id = %s
			)
		;
		"""
		return sql
	#--- EoF ---

	def select_by_pid_sql( self ):
		sql = """
			SELECT
				*
			FROM
				t_playlist_musics
			WHERE
				p_org_id = %s
			AND
				status = 0
			;
		"""
		return sql
	#--- EoF ---

	def select_by_pid_d_sql( self ):
		sql = """
			SELECT
				*
			FROM
				t_playlist_musics
			WHERE
				p_org_id = %s
			AND
				status = 1
			;
		"""
		return sql
	#--- EoF ---

	def delete_sql( self ):
		sql = """
		UPDATE
			t_playlist_musics
		SET
			status = 1,
			modified_at = CURRENT_TIMESTAMP
		WHERE
			p_org_id = %s
		AND
			m_org_id = %s
		;
		"""
		return sql
	#--- EoF ---
#--- PlaylistMusics ---


# Entry Point

if __name__ == "__main__":
	ins = PlaylistMusics()
	sys.exit( ins.main( len( sys.argv ), sys.argv ) )
#-- if



# End of Script