#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import re


def generate_playlist_id(url):
	"""_summary_

	Args:
		url (str): playlist url

	Returns:
		str: playlist original id
	"""
	pattern = "(.*)list=(.*)"
	u = re.search(pattern,url)
	playlist_id = u.group(2)
	return playlist_id
# --- EoF ---


# End of Script