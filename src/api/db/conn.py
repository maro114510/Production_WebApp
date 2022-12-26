#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import psycopg2


class Main():
	def __init__( self ):
		self.conn = psycopg2.connect(
			"postgresql://{user}:{password}@{host}:{port}/{database}".format(
				user="postgres",
				password="passw0rd",
				# ローカルホストにつなぐのはアウト
				host="postgres",
				port="5432",
				database="hogedb"
			)
		)
		cur = self.conn.cursor()
		cur.execute(
			"""
			SET search_path = hogeschema;
			"""
		)
	#--- EoF ---
	
	def execute( self ):
		cur = self.conn.cursor()
		sql = self.create_table()
		cur.execute(
			sql
		)
		self.conn.commit()
		# result = cur.fetchone() 
		print("OK")
	#--- EoF ---
	
	def main( self, argc, argv ):
		self.execute()
		return 0
	#--- EoF ---

	def create_table( self ):
		sql = """
CREATE TABLE morimori (
  daruma VARCHAR(10),
  saitou VARCHAR(10),
  konishi VARCHAR(10),
  PRIMARY KEY (daruma)
);
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