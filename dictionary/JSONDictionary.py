#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  JSONDictionary.py
#  
#  Copyright 2017 shlomo <shlomo.kallner@gmail.com>
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

__package__ = 'dictionary'

##################################################################
#
# Imports
#

import zipfile
import json

from io import StringIO

from icu import UnicodeString as Ustr

from coventreiya.utils.lists import is_item_list
from coventreiya.utils.lists import list_str2Str
from coventreiya.utils.ver import ver

from coventreiya.morphology.word_stem.abc import cmp_root, abc as wordStem_abc

from coventreiya.dictionary import Dictionary



################################################################################
#
#
#   The JSON based Dictionary class.
#
#

class JSONDictionary(Dictionary):
	def __init__(self, filename="", create_=True, Language="",
	             Version=None, Part="", NextPart="", PrevPart=""):
		self.__cache = dict()
		super().__init__(filename, create_, Language, Version, Part, 
			             Version, Part, NextPart, PrevPart)
		
	__doc__ = """
	          """
	          
	#def __loadInteralFile(self, filename):
	#	if filename not in self.__cache:
	#		try:
	#			ztmp = self.file.getinfo(filename)
	#			fTmp = self.file.open(ztmp)
	#			bTmp = self.decompress(fTmp.read())
	#			xTmp = json.loads(bTmp)
	#			# I no longer see why I wanted to keep around the 
	#			#  binary pre-parsed data once parsed, so .. 
	#			# replaced it with None for now..
	#			# was " [ None, xTmp, True ] "
	#			self.__cache[filename] = xTmp
	#			return xTmp
	#		except:
	#			raise
	#	else:
	#		raise FileExistsError()
			
	def getInternalFileExt(self):
		return "json"
			
	def parseFile(self, data):
		xTmp = json.loads(bTmp)
		#self.__cache[filename] = xTmp
		return xTmp
		
	def flush(self):
		"""This method should *flush* all internal cache structures 
		   to disk.
		"""
		# write some other stuff to disk...
		## write the new 
		# now write the cache[files] to disk..
		for i in self.__cache:
			t1 = self.__cache[i]
			fn_ = None
			if isinstance(i,str):
				fn_ = i.encode("utf-8") 
			elif isinstance(i bytes):
				fn_ = i
			else:
				raise ValueError()
			self.file.writestr(fn_, self.compress(json.dumps(t1)))


#
#
#
##################################################################

##################################################################
#
# Tests Main
#

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
