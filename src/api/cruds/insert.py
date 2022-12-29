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


class Insert():
	def __init__( self ):
		ins = Connector()
		self.conn = ins.Connector()
	#--- EoF ---

	def execute( self, name, email, pw ):
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

	def main( self, argc, argv ):
		self.execute(
			"nohira",
			"test2@mail",
			"nohira"
		)
		return 0
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
#--- Insert ---


# Entry Point

if __name__ == "__main__":
	ins = Insert()
	sys.exit( ins.main( len( sys.argv ), sys.argv ) )
#-- if



# End of Script