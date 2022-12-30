#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import random
import requests


class Recommend():
	def __init__( self ):
		self.headers = {
			"accept": "application/json",
		}
		self.params = {
			"p_org_id": "PLSFrP_aW8LfyEIahQGnpdvDtPUKKWxi-H",
		}
	#--- EoF ---

	def execute( self ):
		contents = self.getter()
		content = random.choice( contents )
		m_org_id = content[ "m_org_id" ]
		return "https://youtu.be/" + m_org_id
	#--- EoF ---

	def getter( self ):
		res = requests.get(
			"http://192.168.11.2:8000/playlist_musics/playlist_musics",
			headers=self.headers,
			params=self.params,
		)
		return res
	#--- EoF ---

	def main( self, argc, argv ):
		i = self.execute()
		print( i )
		return 0
	#--- EoF ---
#--- Recommend ---


# Entry Point

if __name__ == "__main__":
	ins = Recommend()
	sys.exit( ins.main( len( sys.argv ), sys.argv ) )
#-- if



# End of Script