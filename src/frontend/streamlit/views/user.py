#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import streamlit as st
import requests

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
		except Exception as e:
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
			submit_button = st.form_submit_button( label = "submit" )
			# if submit_button:
			# 	res = register(un, url)
			# 	if res.status_code == 200:
			# 		if len(res.json()) == 0:
			# 			st.info(
			# 				"The playlist with the URL you sent is already registered")
			# 		# -- if
			# 		else:
			# 			st.success("Registration Complete")
			# 		# -- else
			# 	# -- if
			# 	else:
			# 		st.error(
			# 			"""
			# 			Registration failed.
			# 			Please check if the URL is correct and the communication environment is correct.
			# 			"""
			# 		)
			# 	# -- else
			# # -- if
		# -- with
	# --- EoF ---
#--- User ---





# End of Script