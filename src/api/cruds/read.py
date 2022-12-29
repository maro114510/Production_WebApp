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


class Read():
	def __init__( self ):
		ins = Connector()
		self.conn = ins.Connector()
	#--- EoF ---

	def execute( self ):
		try:
			cur = self.conn.cursor()
			sql = self.select_sql()
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

	def main( self, argc, argv ):
		self.execute()
		return 0
	#--- EoF ---

	def select_sql( self ):
		sql = """
		SELECT * FROM t_users;
		"""
		return sql
	#--- EoF ---
#--- Read ---


# Entry Point

if __name__ == "__main__":
	ins = Read()
	sys.exit( ins.main( len( sys.argv ), sys.argv ) )
#-- if



# End of Script