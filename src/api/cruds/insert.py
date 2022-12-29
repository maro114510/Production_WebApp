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
import hashlib

from api.db.conn import Connector


class Insert():
	def __init__( self ):
		ins = Connector()
		self.conn = ins.Connector()
	#--- EoF ---

	def execute( self, name, email, pw ):
		cur = self.conn.cursor()
		sql = self.insert_sql()
		cur.execute(
			sql,
			(
				name,
				email,
				hashlib.md5( pw.encode() ).hexdigest(),
			)
		)
		self.conn.commit()
		print( "INSERT OK" )
	#--- EoF ---

	def main( self, argc, argv ):
		self.execute(
			"nakata",
			"test2@mail",
			"nakata"
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