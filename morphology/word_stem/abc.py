#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
#
#  abc.py
#  
#  Copyright 2017 Shlomo <Shlomo@Shlomo-Laptop>
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

__package__ = "word_stem"
__name__ = "coventreiya.morphology.word_stem.abc"

##################################################################
#
# Imports
#

from coventreiya.utils.ver import Versioned

from coventreiya.utils.lists import is_same
from coventreiya.utils.lists import is_item_list
from coventreiya.utils.lists import list_str2Str

from coventreiya.morphology.affix.infix import Infix as Infix_abc
from coventreiya.morphology.affix.infix import Consonant as Cons_infix_abc
from coventreiya.morphology.affix.infix import Vowel as Vol_infix_abc

from coventreiya.morphology.roots.abc import root_abc

from coventreiya.utils.phone import get_phonetic_symbol

from io import StringIO

from abc import ABCMeta, abstractmethod

from icu import UnicodeString as Ustr

##################################################################
#
# Some Static Utility Functions:
#

def org_infixes( infixes_ ):
		tmp = dict()
		for i in infixes_:
			s = i.name()
			if s in tmp.keys():
				tmp[s].append(i)
			else:
				tmp[s] = list() 
				tmp[s].append(i)
		return tmp
		
def cmp_root(root1, root2):
	""" Compare two roots 'alphabetically'. """
	if isinstance(root1, root_abc) and isinstance(root2, root_abc):
		r1 = min( len(root1), len(root2) )
		str1_ = None
		str2_ = None 
		bol = 0
		for i in range(0, r1):
			str1_ = Ustr(list_str2Str(root1[i]))
			str2_ = Ustr(list_str2Str(root2[i]))
			if str1_ < str2_:
				bol = -1
				break
			elif str1_ > str2_:
				bol = 1
				break
			else:
				continue
		return bol
	else:
		raise TypeError()
		
def extract_Infixes(infixxes_, infix_cls=None):
	tmp = list()
	if issubclass(infix_cls, Infix_abc):
		for i in infixxes_:
			if issubclass(i, infix_cls):
				tmp.append(i)
	return tmp
	
	

##################################################################
#
# Morphology  -  Word_Stems - ABC
#
# Basically, I need a class with which to describe programmatically
#  how to 
#  a] take a *root* and validate it.
#  b] take a set of *infixxes* and validate them.
#  c] assemble the *root* and *infixxes* into a valid word stem.
#  and do all the above in a commonly programmable manner/API... 
#  d] and *should* do it's full data manipulation workset in it's Ctor
#  including calling *all* of the data manipulating methods on the
#  inputted data set.
#

class abc(Versioned, metaclass=ABCMeta):
    def __init__(self, root_=None, con_infixxes_=None, 
                 vol_infixxes_=None, length=0,
                 major=0, minor=0, patch=0, version=None):
        super().__init__(major, minor, patch, version)
        if isinstance(root_ , root_abc):
			self.__root = root_
		else:
			raise TypeError()
        if not isinstance(length, int) or length != len(root_):
				raise ValueError()
		if self.infix_checker(con_infixxes_,vol_infixxes_):
			self.__con_infixxes = con_infixxes_
			self.__vol_infixxes = vol_infixxes_
			self.__data = self.assemble()			
		else:
			raise ValueError()
        
    def root(self):
		return self.__root
	
	def con_infixxes(self):
		return self.__con_infixxes
		
	def vol_infixxes(self):
		return self.__vol_infixxes
		
	def syllables(self):
		return self.__data
		
	def str(self, strip=True):
		strm = StringIO()
		for i in self.__data:
			strm.write(i.str(strip))
			strm.write(".") # sepparate syllables with "."
		# but that creates a trailling "." ..
		str_ = strm.getvalue().rstrip(".")
		return str_
		
	def __str__(self):
		return self.str(True)
		
	@abstractmethod
	def all_lengths(self):
		""" Returns A Range Object that contains all valid lengths. """
		pass
		
	@abstractmethod
    def length(self):
		pass
		
	def __len__(self):
		return self.length()
		
	@abstractmethod
	def cmp_infixes(self, other, sCons, sVols, oCons, oVols):
		pass
		
	def __cmp(self, other):
		"""
		   Compares first the root alphabetically, then the infixes
		   arbitrarily. Used to compare by length as well.
		   Returns -1 for lesser than, 
		            0 for equal 
		        and 1 for greater than.
		"""
		if isinstance(other,abc):
			#if self.length() < other.length():
			#	return -1
			#elif self.length() > other.length():
			#	return 1
			bol = cmp_root( self.root(), other.root() )
			if bol == 0:
				sCons = self.con_infixxes()
				oCons = other.con_infixxes()
				sVols = self.vol_infixxes()
				oVols = other.vol_infixxes()
				bol = self.cmp_infixes(other, sCons, sVols, oCons, oVols)
			return bol
		else:
			raise TypeError()
	
	def __lt__(self, other):
		if isinstance(other,abc):
			return self.__cmp(other) == -1
		else:
			raise NotImplemented
	
	def __gt__(self, other):
		if isinstance(other,abc):
			return self.__cmp(other) == 1
		else:
			raise NotImplemented
	
	def __eq__(self, other):
		if isinstance(other,abc):
			return self.__cmp(other) == 0
		else:
			raise NotImplemented
	
	def __ne__(self, other):
		if isinstance(other,abc):
			return self.__cmp(other) != 0
		else:
			raise NotImplemented
	
	def __le__(self, other):
		if isinstance(other,abc):
			return self.__cmp(other) != 1
		else:
			raise NotImplemented
	
	def __ge__(self, other):
		if isinstance(other,abc):
			return self.__cmp(other) != -1
		else:
			raise NotImplemented
	
	def get_root_checker(self):
		"""
		   Just returns a Phonotactical matcher 
		   to check if each Root_member is valid...
		"""
		return self.__root.matcher()
	
	@abstractmethod
    def check_infixes( self, con_infixxes_, vol_infixxes_ ):
		pass
	
	def infix_checker( self, con_infixxes_, vol_infixxes_ ):
		if is_item_list( con_infixxes_ ) and is_item_list( vol_infixxes_ ):
			bol = True
			for i in con_infixxes_:
				if not isinstance(i, Cons_infix_abc):
					bol = False
			if bol:
				for i in vol_infixxes_:
					if not isinstance(i, Vol_infix_abc):
						bol = False
			if bol:
				return self.check_infixes( con_infixxes_, vol_infixxes_ )
			else:
				return False
		else:
			return False
	
	@abstractmethod
    def assemble(self):
		pass
	
	########################################################################
    #
    # a few Internal Utility methods...
    # these are no longer needed since ...
    #
    ########################################################################
    
    @staticmethod
	def total_int_from_dict(dict_):
		x = 0
		if isinstance(dict_, dict):
			for i in dict_.keys():
				if isinstance(dict_[i], int):
					x += dict_[i]
		return x
			
	@staticmethod
	def is_list_str( set_ ):
		if is_item_list(set_):
			bol = True
			for i in set_:
				if not isinstance(i, str) and i != "":
					bol = False
			return bol
		else:
			return False
		
	@staticmethod
	def is_list_set( set_ ):
		if is_item_list(set_):
			bol = True
			for i in set_:
				if not is_list_str(i) or len(i) <= 0:
					bol = False	
			return bol
		else:
			return False
			

##################################################################
#
# Tests Main
#

def test():
	return 0

def main(args):
    return test()

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
