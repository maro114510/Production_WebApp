#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import random
import string


class RandomString():
	def __init__( self ):
		pass
	#--- EoF ---

	def execute( self, num: int ) -> str:
		rand_list = [ random.choice( string.ascii_letters ) for _ in range( num ) ]
		return "".join( rand_list )
	#--- EoF ---

	def main( self, argc, argv ):
		string = self.execute( 10 )
		print( string )
		return 0
	#--- EoF ---
#--- RandomString ---


# Entry Point

if __name__ == "__main__":
	ins = RandomString()
	sys.exit( ins.main( len( sys.argv ), sys.argv ) )
#-- if



# End of Script