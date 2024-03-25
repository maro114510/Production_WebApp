#!/usr/bin/env python
# -*- coding: utf8 -*-

from api.db.conn import Connector
import sys
from pathlib import Path
from psycopg2.extras import RealDictCursor

sys.path.append(
    str(
        Path(
            __file__
        ).resolve().parent.parent.parent
    )
)


class UserPlaylists():
    def __init__(self):
        ins = Connector()
        self.conn = ins.Connector()
    # --- EoF ---

    def get_all_user_playlists_full_info(self):
        cur = self.conn.cursor(cursor_factory=RealDictCursor)
        sql = self.select_all_sql()
        try:
            cur.execute(sql)
            results = cur.fetchall()
            self.conn.commit()
            print("SELECT OK")
            return results
        except Exception as e:
            self.conn.rollback()
            raise e
        # -- except
    # --- EoF ---

    def get_user_playlists_byUid(self, uid):
        cur = self.conn.cursor(cursor_factory=RealDictCursor)
        sql = self.select_by_uid_sql()
        try:
            cur.execute(
                sql,
                (
                    uid,
                )
            )
            results = cur.fetchall()
            self.conn.commit()
            print("SELECT OK")
            return results
        except Exception as e:
            self.conn.rollback()
            raise e
        # -- except
    # --- EoF ---

    def get_one_user_playlists_d_info(self, uid):
        cur = self.conn.cursor(cursor_factory=RealDictCursor)
        sql = self.select_d_by_uid_sql()
        try:
            cur.execute(
                sql,
                (
                    uid,
                )
            )
            results = cur.fetchall()
            self.conn.commit()
            print("SELECT OK")
            return results
        except Exception as e:
            self.conn.rollback()
            raise e
        # -- except
    # --- EoF ---

    def user_playlists_insert(self, uid, p_org_id):
        cur = self.conn.cursor()
        sql = self.insert_sql()
        try:
            cur.execute(
                sql,
                (
                    uid,
                    p_org_id,
                    uid,
                    p_org_id,
                )
            )
            self.conn.commit()

            if cur.rowcount != 0:
                print("INSERT OK")
                return 0
            # -- if
            else:
                print("DUPRICATED")
                return 1
            # -- else
        except Exception as e:
            self.conn.rollback()
            raise e
        # -- except
    # --- EoF ---

    def delete_user_playlist(self, uid, p_org_id):
        cur = self.conn.cursor()
        sql = self.delete_sql()
        try:
            cur.execute(
                sql,
                (
                    uid,
                    p_org_id,
                )
            )
            self.conn.commit()
            print("DELETE OK")
        except Exception as e:
            self.conn.rollback()
            raise e
        # -- except
        return 0
    # --- EoF ---

    def update_user_playlist(self, uid, p_org_id):
        cur = self.conn.cursor()
        sql = self.update_sql()
        try:
            cur.execute(
                sql,
                (
                    uid,
                    p_org_id,
                )
            )
            self.conn.commit()
            if cur.rowcount != 0:
                print("UPDATE OK")
                return 0
            # -- if
            else:
                return 1
        except Exception as e:
            self.conn.rollback()
            raise e
        # -- except
    # --- EoF ---

    def execute(self):
        print("OK")
    # --- EoF ---

    def main(self, argc, argv):
        self.execute()
        return 0
    # --- EoF ---

    def insert_sql(self):
        sql = """
		INSERT INTO t_user_playlists (
			uid,
			p_org_id
		)
		SELECT
			%s,
			%s
			WHERE NOT EXISTS (
				SELECT 1 FROM t_user_playlists
				WHERE
					uid = %s
				AND
					p_org_id = %s
			)
		;
		"""
        return sql
    # --- EoF ---

    def select_all_sql(self):
        sql = """
		SELECT
			*
		FROM
			t_user_playlists;
		"""
        return sql
    # --- EoF ---

    def select_by_uid_sql(self):
        sql = """
			SELECT
				*
			FROM
				t_user_playlists
			WHERE
				uid = %s
			AND
				flag = True
			;
		"""
        return sql
    # --- EoF ---

    def select_d_by_uid_sql(self):
        sql = """
			SELECT
				*
			FROM
				t_user_playlists
			WHERE
				uid = %s
			AND
				flag = false
			;
		"""
        return sql
    # --- EoF ---

    def delete_sql(self):
        sql = """
		UPDATE
			t_user_playlists
		SET
			flag = false,
			modified_at = CURRENT_TIMESTAMP
		WHERE
			uid = %s
		AND
			p_org_id = %s
		;
		"""
        return sql
    # --- EoF ---

    def update_sql(self):
        sql = """
		UPDATE
			t_user_playlists
		SET
			flag = true,
			modified_at = CURRENT_TIMESTAMP
		WHERE
			uid = %s
		AND
			p_org_id = %s
		;
		"""
        return sql
    # --- EoF ---
# --- UserPlaylists ---


# Entry Point

if __name__ == "__main__":
    ins = UserPlaylists()
    sys.exit(ins.main(len(sys.argv), sys.argv))
# -- if


# End of Script
