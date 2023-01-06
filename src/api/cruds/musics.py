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


<< << << < HEAD


async def get_musics(db_session: AsyncSession):
    """_summary_

    Args:
            db_session (AsyncSession): AsyncSession

    Returns:
            list: Music schema list
    """
    result: Result = await (
        db_session.execute(
            select(
                model.Music.music_id,
                model.Music.music_name,
                model.Music.music_original_id,
            )
        )
    )
    return result.all()
# --- EoF ---


async def get_music_by_id(db_session: AsyncSession, music_id: int):
    """_summary_

    Args:
            db_session (AsyncSession): AsyncSession
            music_id (int): music serial numver

    Returns:
            schema: Music schema
    """
    result: Result = await (
        db_session.execute(
            select(
                model.Music.music_id,
                model.Music.music_name,
                model.Music.music_original_id,
            ).filter(
                model.Music.music_id == music_id
            )
        )
    )

    return result.first()
# --- EoF ---


async def get_music_by_name(db_session: AsyncSession, music_name: str):
    """_summary_

    Args:
            db_session (AsyncSession): AsyncSession
            music_name (str): music original name

    Returns:
            schema: Music schema
    """
    result: Result = await (
        db_session.execute(
            select(
                model.Music.music_id,
                model.Music.music_name,
                model.Music.music_original_id,
            ).filter(
                model.Music.music_name == music_name
            )
        )
    )
    return result.first()
# --- EoF ---


async def get_music_by_original_id(db_session: AsyncSession, music_original_id: str):
    """_summary_

    Args:
            db_session (AsyncSession): AsyncSession
            music_original_id (str): music original id

    Returns:
            schema: Music schema
    """
    result: Result = await (
        db_session.execute(
            select(
                model.Music.music_id,
                model.Music.music_name,
                model.Music.music_original_id,
            ).filter(
                model.Music.music_original_id == music_original_id
            )
        )
    )

    return result.first()
# --- EoF ---


async def create_music(
    db: AsyncSession, music_create: schema.MusicCreate
):
    """_summary_

    Args:
            db (AsyncSession): AsyncSession
            music_create (schema.MusicCreate): schema

    Returns:
            schema: Music schema
    """
    music = model.Music(
        music_name=music_create.music_name,
        music_original_id=music_create.music_original_id
    )
    db.add(music)
    await db.commit()
    await db.refresh(music)
    return music
# --- EoF ---


async def create_musics(
    db: AsyncSession, music_list: list
):
    """_summary_

    Args:
            db (AsyncSession): AsyncSession
            music_list (list): MusicCreate schemas list

    Returns:
            list: created music list
    """
    box = []

    for i in music_list:
        id = i.get("video_id")
        r = await (db.execute(select(
            model.Music.music_id,
        ).filter(
            model.Music.music_original_id == id
        )))
        r = r.first()
        if r is None:
            box.append(i)
        # -- if
    # -- for

    if box:
        musics = [
            model.Music(
                music_name=d["video_name"],
                music_original_id=d["video_id"]) for d in box]
        db.add_all(musics)
        await db.commit()
    # -- if
    return box
# --- EoF ---


async def update_music(
    db: AsyncSession, music: schema.MusicCreate, original: model.Music
):
    """_summary_

    Args:
            db (AsyncSession): AsyncSession
            music (schema.MusicCreate): schema
            original (model.Music): scheam

    Returns:
            schema: MusicCreate schema
    """
    result = await db.execute(
        select(
            model.Music
        ).filter(
            model.Music.music_original_id == original.music_original_id
        )
    )
    buf = result.first()
    buf[0].music_name = music.music_name
    db.add(buf[0])
    await db.commit()
    await db.refresh(buf[0])
    return buf[0]
# --- EoF ---


async def delete_music(
    db_session: AsyncSession, original: model.Music
):
    """_summary_

    Args:
            db_session (AsyncSession): AsyncSession
            original (model.Music): scheama
    """
    sql = "DELETE FROM musics WHERE music_id = %s ;" % original.music_id
    await db_session.execute(sql)
    await db_session.commit()
# --- EoF ---
== == == =


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
>>>>>> > develop


# End of Script
