#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys

from conn import Connector


class Main():
	def __init__( self ):
		ins = Connector()
		self.conn = ins.Connector()
	#--- EoF ---
	
	def execute( self ):
		cur = self.conn.cursor()
		sql = self.show()
		cur.execute( sql )
		result = cur.fetchone() 
		print( result )
	#--- EoF ---

	def show( self ):
		sql = """
			select * from m_manage;
		"""
		return sql
	#--- EoF ---

	def main( self, argc, argv ):
		self.execute()
		return 0
	#--- EoF ---
#--- Main ---


# Entry Point

if __name__ == "__main__":
	ins = Main()
	sys.exit( ins.main( len( sys.argv ), sys.argv ) )
#-- if



# End of Script