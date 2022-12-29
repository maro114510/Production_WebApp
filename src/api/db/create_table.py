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
		print( "OK" )
	#--- EoF ---

	def main( self, argc, argv ):
		self.execute()
		return 0
	#--- EoF ---

	def create_sql():
		sql = """
		"""
		return 0
	#--- EoF ---
#--- CreateTable ---


# Entry Point

if __name__ == "__main__":
	ins = CreateTable()
	sys.exit( ins.main( len( sys.argv ), sys.argv ) )
#-- if



# End of Script