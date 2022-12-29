#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import hashlib

from api.db.conn import Connector


class Insert():
	def __init__( self ):
		ins = Connector()
		self.conn = ins.Connector()
	#--- EoF ---

	def execute( self ):
		cur = self.conn.cursor()
		sql = self.insert_sql()
		cur.execute(
			sql,
			(
				"nohira",
				"parcels-dollar.0p@icloud.com",
				hashlib.md5( "nohira".encode() ).hexdigest(),
			)
		)
		self.conn.commit()
	#--- EoF ---

	def main( self, argc, argv ):
		self.execute()
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