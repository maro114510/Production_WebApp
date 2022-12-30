#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
from pathlib import Path

sys.path.append(
	str(
		Path(
			__file__
		).resolve().parent.parent.parent
	)
)

from api.db.conn import Connector


class Users():
	def __init__( self ):
		ins = Connector()
		self.conn = ins.Connector()
	#--- EoF ---

	def user_insert( self, name, email, pw ):
		cur = self.conn.cursor()
		sql = self.insert_sql()
		try:
			cur.execute(
				sql,
				(
					name,
					email,
					pw,
				)
			)
			self.conn.commit()
			print( "INSERT OK" )
		except Exception as e:
			self.conn.rollback()
			raise e
		#-- except
	#--- EoF ---

	def get_all_users_full_info( self ):
		cur = self.conn.cursor()
		sql = self.select_all_sql()
		try:
			cur.execute( sql )
			results = cur.fetchall()
			self.conn.commit()
			print( "SELECT OK" )
			return results
		except Exception as e:
			self.conn.rollback()
			raise e
		#-- except
	#--- EoF ---

	def update_user_info(
		self,
		user_name,
		user_email,
		user_pw,
		old_user_name,
		old_user_email,
	):
		cur = self.conn.cursor()
		sql = self.update_sql()
		try:
			cur.execute(
				sql,
				(
					user_name,
					user_email,
					user_pw,
					old_user_name,
					old_user_email
				)
			)
			self.conn.commit()
			print( "UPDATE OK" )
		except Exception as e:
			self.conn.rollback()
			raise e
		#-- except
		return 0
	#--- EoF ---

	def get_one_user_info( self, user_name, user_email ):
		cur = self.conn.cursor()
		sql = self.select_one_sql()
		try:
			cur.execute(
				sql,
				(
					user_name,
					user_email,
				)
			)
			results = cur.fetchall()
			self.conn.commit()
			print( "SELECT OK" )
			return results
		except Exception as e:
			self.conn.rollback()
			raise e
		#-- except
	#--- EoF ---

	def delete_user( self, user_name, user_email ):
		cur = self.conn.cursor()
		sql = self.delete_sql()
		try:
			cur.execute(
				sql,
				(
					user_name,
					user_email,
				)
			)
			self.conn.commit()
			print( "DELETE OK" )
		except Exception as e:
			self.conn.rollback()
			raise e
		#-- except
		return 0
	#--- EoF ---

	def execute():
		return 0
	#--- EoF ---

	def main( self, argc, argv ):
		self.execute()
		return 0
	#--- EoF ---

	def select_all_sql( self ):
		sql = """
		SELECT
			*
		FROM
			t_users
		WHERE
			status = 0;
		"""
		return sql
	#--- EoF ---

	def insert_sql( self ):
		sql = """
		INSERT INTO t_users (
			user_name,
			user_email,
			user_pw
		) VALUES (
			%s,
			%s,
			%s
		);
		"""
		return sql
	#--- EoF ---

	def select_one_sql( self ):
		sql = """
		SELECT
			uid,
			user_name,
			user_email,
			user_pw
		FROM
			t_users
		WHERE
			user_name = %s
		AND
			user_email = %s
		AND
			status = 0;
		"""
		return sql
	#--- EoF ---

	def update_sql( self ):
		sql = """
		UPDATE
			t_users
		SET
			user_name = %s,
			user_email = %s,
			user_pw = %s,
			modified_at = CURRENT_TIMESTAMP
		WHERE
			user_name = %s
		AND
			user_email = %s
		AND
			status = 0
		;
		"""
		return sql
	#--- EoF ---

	def delete_sql( self ):
		sql = """
		UPDATE
			t_users
		SET
			status = 1,
			modified_at = CURRENT_TIMESTAMP
		WHERE
			user_name = %s
		AND
			user_email = %s
		;
		"""
		return sql
	#--- EoF ---
#--- Users ---


# Entry Point

if __name__ == "__main__":
	ins = Users()
	sys.exit( ins.main( len( sys.argv ), sys.argv ) )
#-- if



# End of Script