#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import sys
import asyncio
import asyncpg
import psycopg2
from dotenv import load_dotenv


class Main():
	def __init__( self ):
		load_dotenv()

		self.conn = psycopg2.connect(
			"postgresql://{user}:{password}@{host}:{port}/{database}".format(
				user=os.environ[ "POSTGRES_USER" ],
				password=os.environ[ "POSTGRES_PASSWORD" ],
				# ローカルホストにつなぐのはアウト
				host="postgres",
				port="5432",
				database="maindb"
			)
		)

		cur = self.conn.cursor()
		cur.execute(
			"""
			SET search_path = schema1;
			"""
		)
	#--- EoF ---
	
	def execute( self ):
		cur = self.conn.cursor()
		sql = self.create_table()
		cur.execute(
			sql
		)
		# self.conn.commit()
		result = cur.fetchone() 
		print( result )
	#--- EoF ---
	
	def main( self, argc, argv ):
		self.execute()
		return 0
	#--- EoF ---

	def create_table( self ):
		sql = """
			select * from m_manage;
		"""
		return sql
	#--- EoF ---
#--- Main ---


# Entry Point

if __name__ == "__main__":
	ins = Main()
	sys.exit( ins.main( len( sys.argv ), sys.argv ) )
#-- if



# End of Script