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


class Musics():
    def __init__(self):
        ins = Connector()
        self.conn = ins.Connector()
    # --- EoF ---

    def get_all_musics_full_info(self):
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

    def get_one_music_info(self, m_org_id):
        cur = self.conn.cursor(cursor_factory=RealDictCursor)
        sql = self.select_one_sql()
        try:
            cur.execute(
                sql,
                (
                    m_org_id,
                )
            )
            result = cur.fetchone()
            self.conn.commit()
            print("SELECT OK")
            return result
        except Exception as e:
            self.conn.rollback()
            raise e
        # -- except
    # --- EoF ---

    def musics_insert(self, musics):
        cur = self.conn.cursor()
        sql = self.insert_one_sql()
        try:
            cur.executemany(
                sql,
                musics,
            )
            self.conn.commit()

            if cur.rowcount != len(musics):
                print("INSERT OK")
            # -- if
            else:
                print("SOME OF DUPLICATED")
            # -- else
        except Exception as e:
            self.conn.rollback()
            raise e
        # -- except
    # --- EoF ---

    def music_insert_one(self, music_name, m_org_id):
        cur = self.conn.cursor()
        sql = self.insert_one_sql()
        try:
            cur.execute(
                sql,
                (
                    music_name,
                    m_org_id,
                    m_org_id,
                )
            )
            self.conn.commit()

            if cur.rowcount != 0:
                print("INSERT OK")
            # -- if
            else:
                print("DUPLICATED")
            # -- else
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

    def insert_one_sql(self):
        sql = """
		INSERT INTO t_musics (
			music_name,
			m_org_id
		)
		SELECT
			%s,
			%s
			WHERE NOT EXISTS (
				SELECT 1 FROM t_musics WHERE m_org_id = %s
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
			t_musics;
		"""
        return sql
    # --- EoF ---

    def select_one_sql(self):
        sql = """
		SELECT
			*
		FROM
			t_musics
		WHERE
			m_org_id = %s;
		"""
        return sql
    # --- EoF ---
# --- Musics ---


# Entry Point

if __name__ == "__main__":
    ins = Musics()
    sys.exit(ins.main(len(sys.argv), sys.argv))
# -- if


# End of Script
