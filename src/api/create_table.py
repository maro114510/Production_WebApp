#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
from sqlalchemy import create_engine

from api.models.db_model import Base

DB_URL = "mysql+pymysql://root@db:3306/demo?charset=utf8"
engine = create_engine(DB_URL, echo=True)


def main(argc, argv):
    """_summary_

    Args:
            argc (int): Number of command line arguments
            argv (str): command line argument

    Returns:
            int: return
    """

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    return 0
# --- EoF ---


# Entry Point

if __name__ == "__main__":
    sys.exit(main(len(sys.argv), sys.argv))
# -- if

# End of Script
