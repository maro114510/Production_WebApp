#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
from pathlib import Path

sys.path.append(
	str(
		Path(
			__file__
		).resolve().parent.parent.parent
	)
)

from api.db.conn import Connector


class Users():
	def __init__( self ):
		ins = Connector()
		self.conn = ins.Connector()
	#--- EoF ---

	def user_insert( self, name, email, pw ):
		cur = self.conn.cursor()
		sql = self.insert_sql()
		try:
			cur.execute(
				sql,
				(
					name,
					email,
					pw,
				)
			)
			self.conn.commit()
			print( "INSERT OK" )
		except Exception as e:
			self.conn.rollback()
			raise e
		#-- except
	#--- EoF ---

	def get_all_users_full_info( self ):
		cur = self.conn.cursor()
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

	def execute():
		return 0
	#--- EoF ---

	def main( self, argc, argv ):
		self.execute()
		return 0
	#--- EoF ---

	def select_all_sql( self ):
		sql = """
		SELECT * FROM t_users;
		"""
		return sql
	#--- EoF ---

	def insert_sql( self ):
		sql = """
		INSERT INTO t_users(
			user_name,
			user_email,
			user_pw
		) VALUES (
			%s,
			%s,
			%s
		);
		"""
		return sql
	#--- EoF ---
#--- Users ---


# Entry Point

if __name__ == "__main__":
	ins = Users()
	sys.exit( ins.main( len( sys.argv ), sys.argv ) )
#-- if



# End of Script