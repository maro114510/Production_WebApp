#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import streamlit as st
import requests
import pandas as pd

from libs.lib import *


def playlist_info_page(url):
    try:
        r = get_row_data(url)
    except Exception as e:
        st.error(e)
    # -- except

    st.markdown("### {}".format(r.get("playlistname")))
    data = pd.DataFrame(r.get("music_id_list"))
    st.table(data)
    return 0
# --- EoF ---


# End of Script
