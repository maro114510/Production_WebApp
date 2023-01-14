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


class Playlists():
	def __init__( self ):
		ins = Connector()
		self.conn = ins.Connector()
	#--- EoF ---

	def get_all_playlists_full_info( self ):
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

	def get_one_playlist_info( self, p_org_id ):
		cur = self.conn.cursor( cursor_factory=RealDictCursor )
		sql = self.select_one_sql()
		try:
			cur.execute(
				sql,
				(
					p_org_id,
				)
			)
			result = cur.fetchone()
			self.conn.commit()
			print( "SELECT OK" )
			return result
		except Exception as e:
			self.conn.rollback()
			raise e
		#-- except
	#--- EoF ---

	def get_by_name_playlist_info( self, playlist_name ):
		cur = self.conn.cursor( cursor_factory=RealDictCursor )
		sql = self.select_by_name_sql()
		try:
			cur.execute(
				sql,
				(
					playlist_name,
				)
			)
			result = cur.fetchone()
			self.conn.commit()
			print( "SELECT OK" )
			return result
		except Exception as e:
			self.conn.rollback()
			raise e
		#-- except
	#--- EoF ---

	def insert_playlist( self, p_name, p_org_id ):
		cur = self.conn.cursor()
		sql = self.insert_sql()
		try:
			cur.execute(
				sql,
				(
					p_name,
					p_org_id,
					p_org_id,
				)
			)
			self.conn.commit()
			if cur.rowcount != 0:
				print( "INSERT OK" )
			#-- if
			else:
				print( "DIPRICATED" )
			#-- else
		except Exception as e:
			self.conn.rollback()
			raise e
		#-- except
	#--- EoF ---

	def execute( self ):
		print( "OK" )
	#--- EoF ---

	def main( self, argc, argv ):
		self.execute()
		return 0
	#--- EoF ---

	def insert_sql( self ):
		sql = """
		INSERT INTO t_playlists (
			playlist_name,
			p_org_id
		)
		SELECT
			%s,
			%s
			WHERE NOT EXISTS (
				SELECT 1 FROM t_playlists WHERE p_org_id = %s
			)
		;
		"""
		return sql
	#--- EoF ---

	def select_all_sql( self ):
		sql = """
		SELECT
			*
		FROM
			t_playlists;
		"""
		return sql
	#--- EoF ---

	def select_one_sql( self ):
		sql = """
		SELECT
			*
		FROM
			t_playlists
		WHERE
			p_org_id = %s;
		"""
		return sql
	#--- EoF ---

	def select_by_name_sql( self ):
		sql = """
		SELECT DISTINCT
			*
		FROM
			t_playlists
		WHERE
			playlist_name = %s;
		"""
		return sql
	#--- EoF ---
#--- Playlists ---


# Entry Point

if __name__ == "__main__":
	ins = Playlists()
	sys.exit( ins.main( len( sys.argv ), sys.argv ) )
#-- if



# End of Script