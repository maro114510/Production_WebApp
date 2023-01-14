#!/usr/bin/env python
# -*- coding: utf8 -*-

import streamlit as st

from libs.lib import Lib


class User():
	def __init__( self ):
		self.lib_ins = Lib()
	#--- EoF ---

	def user_page( self, un, uid ):
		st.markdown( f"## Welcome, {un}!" )
		st.markdown( "### Your register playlist" )
		try:
			r = self.lib_ins.get_users_playlist( uid )
		except Exception:
			st.warning(
			"""
			Sorry, something is wrong and I can"t display it.
			Please try again in a few hours.
			"""
		)
		#-- except
		st.table( r )

		st.markdown( "### Your registerd diff" )
		d_r = None
		try:
			d_r = self.lib_ins.get_delete_music( uid )
		except Exception:
			st.warning(
			"""
			Sorry, something is wrong and I can not display it.
			Please try again in a few hours.
			"""
		)
		#-- except
		st.dataframe( d_r )

		st.markdown( "### Register new playlist" )
		with st.form( key = "key" ):
			url = st.text_input( "Input playlist url" )
			submit_button = st.form_submit_button( label = "Submit" )
			if submit_button:
				res = self.lib_ins.first_register( uid, url )
				if res == 0:
					st.success("Registration Complete")
				# -- if
				elif res == 1:
					st.error(
						"""
						The playlist you indicated is already registered.
						"""
					)
				#--elif
				else:
					st.error(
						"""
						Registration failed.
						Please check if the URL is correct and the communication environment is correct.
						"""
					)
				#-- else
			#-- if
		#-- with

		st.markdown( "### Exclude playlists from monitoring" )
		with st.form( key = "del" ):
			p_list = st.multiselect(
				label="Select playlists not to be monitored",
				options=r.iloc[:][ "Playlist_Name" ],
			)
			submit_button = st.form_submit_button( label = "Submit" )
			if submit_button:
				btn = self.lib_ins.exclude( uid, p_list )
			#-- if
		#-- with

		st.markdown( "### Restore excluded playlist " )
		with st.form( key = "up" ):
			dd_r = self.lib_ins.get_d_users_playlist( uid )
			try:
				p_list = st.multiselect(
					label="Select playlists restored",
					options=dd_r.iloc[:][ "Playlist_Name" ],
				)
			#-- try
			except Exception as e:
				st.write( "Notiong" )
			#-- except
			submit_button = st.form_submit_button( label = "Submit" )
			if submit_button:
				btn = self.lib_ins.restore( uid, p_list )
			#-- if
		#-- with
	#--- EoF ---
#--- User ---





# End of Script
