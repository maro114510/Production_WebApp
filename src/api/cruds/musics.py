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


class Musics():
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
#--- Musics ---


# Entry Point

if __name__ == "__main__":
	ins = Musics()
	sys.exit( ins.main( len( sys.argv ), sys.argv ) )
#-- if



# End of Script