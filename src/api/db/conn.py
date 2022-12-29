#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import sys
# import asyncio
# import asyncpg
import psycopg2
from dotenv import load_dotenv


class Connector():
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
		sql = self.show()
		cur.execute( sql )
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

	def show( self ):
		sql = """
			select * from m_manage;
		"""
		return sql
	#--- EoF ---

	def Connector( self ):
		return self.conn
	#--- EoF ---
#--- Connector ---


# Entry Point

if __name__ == "__main__":
	ins = Connector()
	sys.exit( ins.main( len( sys.argv ), sys.argv ) )
#-- if



# End of Script