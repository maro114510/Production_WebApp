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
from api.cruds.playlist_musics import PlaylistMusics
from api.libs.plalylist_url_handling import Format


class Cron():
	def __init__( self ):
		ins = Connector()
		self.f_ins = Format()
		self.pm_ins = PlaylistMusics()
		self.conn = ins.Connector()
	#--- EoF ---

	def execute( self ):
		d = self.checklist()
		self.checklists = [ i.get( "p_org_id" ) for i in d ]
		api_list = self.api_data( self.checklists )
		db_list = self.db_data( self.checklists )
		new, dele = self.diff_check( api_list, db_list )

		print( "OK" )
	#--- EoF ---

	def renew( self, new ):
		for n in range( self.check_count ):
			musics = [
				[
					i[ "music_name" ],
					i[ "m_org_id" ],
					i[ "m_org_id" ]
				]
				for i in new[ n ]
			]
			pm_bulk = [
				[
					self.checklists[ n ],
					i[ "m_org_id" ],
					self.checklists[ n ],
					i[ "m_org_id" ],
				]
				for i in new[ n ]
			]
			try:
				self.musics_insert( musics )
				self.playlist_musics_insert( pm_bulk )
			except Exception as e:
				print( "%s" % ( [e.args, ] ), file=sys.stderr )
			#-- except
		#-- for
	#--- EoF ---

	def del_deal( self, dele ):
		return 0
	#--- EoF ---

	def api_data( self, checklist ):
		box = []
		for i in checklist:
			d = self.f_ins.get_plane_data_by_id( i )
			data = [
				{
					"music_name": i[ "video_name" ],
					"m_org_id": i[ "video_id" ],
				}
				for i in d
			]
			box.append( data )
		#-- for
		return box
	#--- EoF ---

	def db_data( self, checklist ):
		box = []
		for i in checklist:
			d = self.playlist_musics( i )
			d = [ i.get( "m_org_id" ) for i in d ]
			box.append( d )
		#-- if
		return box
	#--- EoF ---

	def diff_check( self, api_list, db_list ):
		new_list = []
		del_list = []
		for j in range( self.check_count ):
			tmp_api = [ i.get( "m_org_id" ) for i in api_list[ j ] ]
			nb = []
			deb = []
			for i in api_list[ j ]:
				if i.get( "m_org_id" ) not in db_list:
					nb.append( i )
				#-- if
			#-- for
			for i in db_list[ j ]:
				if i not in tmp_api:
					deb.append( i )
				#-- if
			#-- for
			new_list.append( nb )
			del_list.append( deb )
		#-- for
		return new_list, del_list
	#--- EoF ---

	def checklist( self ):
		cur = self.conn.cursor( cursor_factory=RealDictCursor )
		sql = self.select_list_sql()
		try:
			cur.execute( sql )
			results = cur.fetchall()
			self.conn.commit()
			self.check_count = len( results )
			return results
		except Exception as e:
			self.conn.rollback()
			raise e
		#-- except
	#--- EoF ---

	def playlist_musics( self, p_org_id ):
		cur = self.conn.cursor( cursor_factory=RealDictCursor )
		sql = self.select_list_by_pid_sql()
		try:
			cur.execute(
				sql,
				(
					p_org_id,
				)
			)
			results = cur.fetchall()
			self.conn.commit()
			return results
		except Exception as e:
			self.conn.rollback()
			raise e
		#-- except
	#--- EoF ---

	def musics_insert( self, musics ):
		cur = self.conn.cursor()
		sql = self.insert_one_sql()
		try:
			cur.executemany(
				sql,
				musics,
			)
			self.conn.commit()

			if cur.rowcount != len( musics ):
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

	def playlist_musics_insert( self, pm_list ):
		cur = self.conn.cursor()
		sql = self.insert_pm_sql()
		try:
			cur.executemany(
				sql,
				pm_list,
			)
			self.conn.commit()
			if cur.rowcount != len( pm_list ):
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


	def main( self, argc, argv ):
		self.execute()
		return 0
	#--- EoF ---

	def select_list_sql( self ):
		sql = """
		SELECT DISTINCT
			p_org_id
		FROM
			t_user_playlists
		WHERE
			flag = true
		;
		"""
		return sql
	#--- EoF ---

	def select_list_by_pid_sql( self ):
		sql = """
		SELECT
			m_org_id
		FROM
			t_playlist_musics
		WHERE
			p_org_id = %s
		;
		"""
		return sql
	#--- EoF ---

	def insert_one_sql( self ):
		sql = """
		INSERT INTO t_musics (
			music_name,
			m_org_id
		)
		SELECT
			%s,
			%s
			WHERE NOT EXISTS (
				SELECT 1 FROM t_musics WHERE m_org_id = %s
			)
		;
		"""
		return sql
	#--- EoF ---

	def insert_pm_sql( self ):
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
#--- Cron ---


# Entry Point

if __name__ == "__main__":
	ins = Cron()
	sys.exit( ins.main( len( sys.argv ), sys.argv ) )
#-- if



# End of Script