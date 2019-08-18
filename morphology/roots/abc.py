#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  abc.py
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

if __name__ != '__main__':
	__name__ = "abc"

##################################################################
#
# Imports
#

from abc import ABCMeta, abstractmethod
from coventreiya.utils.lists import is_item_list, is_list_of_lists

##################################################################
#
# Morphology  - Roots - Abstract Base Class
#

class root_abc(metaclass=ABCMeta):
	"""
		   Basically, 
		   a] A root has to be a Sequence.
		   b] A root can be a Sequence of non-null strings,
		   c] Or, each item must be a Sequence of non-null strings.
	"""
	def __init__(self, root_=None, length_=0, 
	             min_length=0, max_length=0):
		if isinstance(min_length, int):
			self.__min_length = min_length
		else:
			raise TypeError()
		if isinstance(max_length, int):
			self.__max_length = max_length
		else:
			raise TypeError()
		if isinstance(length_, int):
			if length_ > 0:
				if min_length <= length_ <= max_length:
					self.__length = length_
				else:
					raise ValueError()
			else:
				raise ValueError()
		else:
			raise TypeError()
		if is_item_list(root_):
			if is_list_of_lists(root_) and len(root_) == self.__length:
				bol = True
				mat_ = self.matcher()
				for i in range(0, self.__length):
					if not mat_.is_allowable_set(root_[i]):
						bol = False
				if not bol:
					raise ValueError()
				else:
					self.__root = root_
			elif length_ == 1:
				if self.matcher().is_allowable_set(root_):
					self.__root = root_
					self.__length = 1
				else:
					raise ValueError()
			else:
				raise ValueError()
		else:
			raise TypeError()
		
		
	def __getitem__(self, key):
		if isinstance(key, int):
			if self.__length == 1 and key == 0:
				return self.__root
			elif 0 <= key <= self.__length:
				return self.__root[key]
			else:
				raise KeyError()
		else:
			raise TypeError()
			
	def min_length(self):
		return self.__min_length
		
	def max_length(self):
		return self.__max_length
		
	def __len__(self):
		return self.__length
		
	@abstractmethod
	def matcher(self):
		pass
		
	
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
