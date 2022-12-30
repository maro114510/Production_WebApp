#!/usr/bin/env python
# -*- coding: utf8 -*-

import streamlit as st
import pandas as pd

from libs.lib import Lib


class Playlist():
	def __init__( self ):
		self.lib_ins = Lib()
	#--- EoF ---

	def playlist_info_page( self, url ):
		try:
			r = self.lib_ins.get_row_data( url )
		except Exception as e:
			st.error( e )
		# -- except

		st.markdown( "### {}".format( r.get( "playlistname" ) ) )
		data = pd.DataFrame( r.get( "music_id_list" ) )
		st.table( data )
		return 0
	#--- EoF ---
#--- Playlist ---



# End of Script