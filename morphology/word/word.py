#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  word.py
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

__package__ = 'word'

################################################################################
#
#
#   Imports
#
#

from abc import ABCMeta, abstractmethod

from io import StringIO

from icu import UnicodeString as Ustr

from coventreiya.utils.lists import is_item_list
from coventreiya.utils.lists import list_str2Str
from coventreiya.utils.lists import not_empty_list_items_are

from coventreiya.utils.phone import get_phonetic_symbol

from coventreiya.utils.ver import ver

from coventreiya.morphology.word_stem.abc import cmp_root, abc as wordStem_abc
from coventreiya.morphology.affix.prefix import Prefix as prefix_abc
from coventreiya.morphology.affix.suffix import Suffix as suffix_abc


################################################################################
#
#
#   The Word ABC class.
#
#

class Word(metaclass=ABCMeta):
	def __init__(self, wordStem_, prefixes_=list(), suffixes_=list()):
		if isinstance(wordStem_ , wordStem_abc):
			self.__wordStem = wordStem_
		else:
			raise TypeError()
		if not_empty_list_items_are(prefixes_,prefix_abc):
			self.__prefixes = prefixes_
		else:
			raise TypeError()
		if not_empty_list_items_are(suffixes_,suffix_abc):
			self.__suffixes = suffixes_
		else:
			raise TypeError()
		
	def wordStem(self):
		return self.__wordStem
		
	def prefixes(self):
		return self.__prefixes
		
	def suffixes(self):
		return self.__suffixes
		
	def str(self, strip=True):
		strm = StringIO()
		if len(self.__prefixes) > 0:
			for i in self.__prefixes:
				strm.write(i.str(strip,debug=False))
				strm.write(".")
		strm.write(self.__wordStem.str(strip))
		if len(self.__suffixes) > 0:
			for i in self.__suffixes:
				strm.write(i.str(strip,debug=False))
				strm.write(".")
		# but that creates a trailling "." ..
		str_ = strm.getvalue().rstrip(".")
		return str_
		
	def __str__(self):
		return self.str(True)
		
	def __len__(self):
		p_ = len(self.__prefixes)
		s_ = len(self.__suffixes)
		w_ = len(self.__wordStem)
		return p_ + w_ + s_
		
		

################################################################################
#
# Main/Testing suite...
#
#

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
