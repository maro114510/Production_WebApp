#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys

import streamlit as st


class MainPage():
	def __init__( self ):
		st.set_page_config(
			page_title="Youtube Diff Checker",
			page_icon="./img/youtube_profile_image.png",
			layout="wide",
			menu_items={
				"Get help": None,
				"Report a Bug": None,
				"About": None
			}
		)
	#--- EoF ---

	def execute( self ):
		st.title( "morimori" )
	#--- EoF ---

	def main( self, argc, argv ):
		self.execute()
		return 0
	#--- EoF ---
#--- MainPage ---


# Entry Point

if __name__ == "__main__":
	ins = MainPage()
	sys.exit( ins.main( len( sys.argv ), sys.argv ) )
#-- if



# End of Script