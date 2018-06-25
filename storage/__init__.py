#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  __init__.py
#  
#  Copyright 2018 Tomáš Votava <info@tomasvotava.eu>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

"""
Storage defines a way to store and access data on the server.

Data directory structure:
data
	/project_id
		/subdirectory						(bucket)
			/table_id.{version_time}.csv	(data)
			/table_id.meta 					(metadata)
	/users
		/user_id.data						(userdata)
Prefered usage:
from storage.storage import Storage
"""

if __name__ == '__main__':
	print("This package is not meant to be run directly.")
	import sys
	sys.exit(0)

__all__ = ["storage"]
