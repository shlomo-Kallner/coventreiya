#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
#
#  ver_1_3_5.py
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
__name__ = "coventreiya.morphology.word_stem.ver_1_3_5"

##################################################################
#
# Imports
#

from coventreiya.morphology.word_stem.abc import abc as Stem_abc
from coventreiya.morphology.word_stem.abc import org_infixes

from coventreiya.morphology.affix.abc import set_abc as affix_set
from coventreiya.morphology.affix.infix import Infix as Infix_abc
from coventreiya.morphology.affix.infix import Consonant as Cons_infix_abc
from coventreiya.morphology.affix.infix import Vowel as Vol_infix_abc

from coventreiya.morphology.affix.infix import ver_1_3_5 as infix_ver
from infix_ver import gen_Consonant_Infixes, gen_Base_Vowel_Infixes 
from infix_ver import gen_Verb_Vowel_Infixes, gen_Noun_Vowel_Infixes
from infix_ver import system1, system2, Lexical_Category

from coventreiya.phonotactics.onsets.ver_1_5_7 import ver_1_5_7 as Onset_match
from coventreiya.phonotactics.nucleus.ver_1_5_7 import ver_1_5_7 as Nucleus_match
from coventreiya.phonotactics.codas.ver_1_5_7 import ver_1_5_7 as Coda_match

from coventreiya.utils.lists import is_item_list

from coventreiya.morphology.syllable.closed.ver_1_3_5 import ver_1_3_5 as Closed_Syl
from coventreiya.morphology.syllable.open.ver_1_3_5 import ver_1_3_5 as Open_Syl

from coventreiya.morphology.roots.ver_1_3_5 import ver_1_3_5 as root_t

##################################################################
#
#  Some Utility Functions...
#
#

def check_if_infix_in_sets( sets_, infix_ ):
		bol = False
		if isinstance(sets_ ,affix_set) or is_item_list(sets_):
			if len(sets_) > 0:
				for i in sets_:
					if infix_ in i:
						bol = True
		return bol
		
def check_2_multisets( set1_, set2_, infix_ ):
	bol1 = check_if_infix_in_sets( set1_, infix_ )
	bol2 = check_if_infix_in_sets( set2_, infix_ )
	return bol1 or bol2
		
def check_2_sets( set1_, set2_, infix_ ):
	return infix_ in set1_ or infix_ in set2_
	
def cmp_infixes(sDict, oDict, infixSet):
	"""returns -1 for lesser than, 0 for equal and 1 for greater than"""
	bol = 0
	for i in infixSet:
		if i.name() in sDict and i.name() in oDict:
			s_ = int(sDict[i.name()].value)
			o_ = int(oDict[i.name()].value)
			if s_ < o_:
				bol = -1
			elif s_ > o_:
				bol = 1
			if bol != 0:
				break
		else:
			raise ValueError()
	return bol
		
	

##################################################################
#
# Morphology  -  Word_Stems - version 1.3.5
#
#

class ver_1_3_5_matcher:
	
	__lengths = range(1, 6+1, 1) # includes all integers from 1 to 6 
	                             # including 1 and 6!
	
	def __init__(self, length=0):
		if isinstance(length,int) and (length in __lengths):
			self.__length = int(length)
		else:
			raise ValueError()
		self.__cons_infixes = gen_Consonant_Infixes()
		self.__base_vol_infixes = gen_Base_Vowel_Infixes()
		self.__verb_vol_infixes = gen_Verb_Vowel_Infixes()
		self.__noun_vol_infixes = gen_Noun_Vowel_Infixes()
		self.__vols_per_Stem = { 1 : [1,2],
		                         2 : [2,4],
		                         3 : [3,6],
		                         4 : [4,6],
		                         5 : [5,6],
		                         6 : [6,6] }
		self.__cons_per_Stem = { 1 : [1,1],
		                         2 : [1,3],
		                         3 : [2,3],
		                         4 : [2,3],
		                         5 : [2,3],
		                         6 : [2,3] }
		self.__has_verb_vol_infixes = { self.__cons_infixes[0].enum_.Verb_ : True,
		                                self.__cons_infixes[0].enum_.Adverb_: True,
		                                # a set of verb related Number_ Compounds...
		                                # ...
		                                # the Noun "Types"..
		                                self.__cons_infixes[0].enum_.Noun_: False,
		                                self.__cons_infixes[0].enum_.Adjective_ : False,
		                                self.__cons_infixes[0].enum_.Gerund_ : False,
		                                # a set of noun related Number_ Compounds...
		                                # ... 
		                              }
		self.__verb_vol_matcher = { 1 : { 1 : self.__base_vol_infixes },
		                            2 : { 1 : [ self.__verb_vol_infixes[3],
		                                        self.__verb_vol_infixes[2] ],
		                                  2 : self.__base_vol_infixes },
		                            3 : { 1 : [ self.__verb_vol_infixes[3],
		                                        self.__verb_vol_infixes[2] ],
		                                  2 : [ self.__verb_vol_infixes[1],
		                                        self.__verb_vol_infixes[0] ],
		                                  3 : self.__base_vol_infixes },
		                            4 : { 1 : [ self.__verb_vol_infixes[3],
		                                        self.__verb_vol_infixes[2] ],
		                                  2 : [ self.__verb_vol_infixes[1],
		                                        self.__verb_vol_infixes[0] ],
		                                  3 : [ self.__base_vol_infixes[1], ],
		                                  4 : [ self.__base_vol_infixes[0], ] },
		                            5 : { 1 : [ self.__verb_vol_infixes[3], ],
		                                  2 : [ self.__verb_vol_infixes[2], ],
		                                  3 : [ self.__verb_vol_infixes[1],
		                                        self.__verb_vol_infixes[0] ],
		                                  4 : [ self.__base_vol_infixes[1], ],
		                                  5 : [ self.__base_vol_infixes[0], ] },
		                            6 : { 1 : [ self.__verb_vol_infixes[3], ],
		                                  2 : [ self.__verb_vol_infixes[2], ],
		                                  3 : [ self.__verb_vol_infixes[0], ],
		                                  4 : [ self.__verb_vol_infixes[1], ],
		                                  5 : [ self.__base_vol_infixes[1], ],
		                                  6 : [ self.__base_vol_infixes[0], ] } }
		self.__noun_vol_matcher = { 1 : { 1 : self.__base_vol_infixes },
		                            2 : { 1 : [ self.__noun_vol_infixes[3], 
		                                        self.__noun_vol_infixes[2] ],
		                                  2 : self.__base_vol_infixes },
		                            3 : { 1 : [ self.__noun_vol_infixes[3], 
		                                        self.__noun_vol_infixes[2] ],
		                                  2 : [ self.__noun_vol_infixes[1], 
		                                        self.__noun_vol_infixes[0] ],
		                                  3 : self.__base_vol_infixes },
		                            4 : { 1 : [ self.__noun_vol_infixes[3], 
		                                        self.__noun_vol_infixes[2] ],
		                                  2 : [ self.__noun_vol_infixes[1], 
		                                        self.__noun_vol_infixes[0] ],
		                                  3 : [ self.__base_vol_infixes[1], ],
		                                  4 : [ self.__base_vol_infixes[0], ] },
		                            5 : { 1 : [ self.__noun_vol_infixes[3], ],
		                                  2 : [ self.__noun_vol_infixes[2], ],
		                                  3 : [ self.__noun_vol_infixes[1], 
		                                        self.__noun_vol_infixes[0] ],
		                                  4 : [ self.__base_vol_infixes[1], ],
		                                  5 : [ self.__base_vol_infixes[0], ] },
		                            6 : { 1 : [ self.__noun_vol_infixes[3], ],
		                                  2 : [ self.__noun_vol_infixes[2], ],
		                                  3 : [ self.__noun_vol_infixes[0], ],
		                                  4 : [ self.__noun_vol_infixes[1], ],
		                                  5 : [ self.__base_vol_infixes[1], ],
		                                  6 : [ self.__base_vol_infixes[0], ] } }
		self.__cons_matcher = { 1 : { 1 : [ self.__cons_infixes[0], ] },
		                        2 : { 1 : [ self.__cons_infixes[1], ],
		                              2 : [ self.__cons_infixes[0], 
		                                    self.__cons_infixes[2], ] },
		                        3 : { 1 : [ self.__cons_infixes[1], ],
		                              2 : [ self.__cons_infixes[2], ],
		                              3 : [ self.__cons_infixes[0], ] },
		                        4 : { 1 : [ self.__cons_infixes[1], ],
		                              2 : [ self.__cons_infixes[2], ],
		                              3 : None,
		                              4 : [ self.__cons_infixes[0], ] },
		                        5 : { 1 : [ self.__cons_infixes[1], ],
		                              2 : [ self.__cons_infixes[2], ],
		                              3 : None,
		                              4 : None,
		                              5 : [ self.__cons_infixes[0], ] },
		                        6 : { 1 : [ self.__cons_infixes[1], ],
		                              2 : [ self.__cons_infixes[2], ],
		                              3 : None,
		                              4 : None,
		                              5 : None,
		                              6 : [ self.__cons_infixes[0], ] } }
		
	def length(self):
		"""Return the Length in Syllables."""
		return self.__length
		
	def all_lengths(self):
		return __lengths
		
	def has_verb_vol_infixes(self, infix_):
		return self.__has_verb_vol_infixes[ infix_ ]
		
	def vol_matcher(self, syllable_, infix_, hasVerbInfixes_):
		tmp = None
		if hasVerbInfixes_:
			tmp = list( self.__verb_vol_matcher[ self.__length ][ syllable_ ] )
		else:
			tmp = list( self.__noun_vol_matcher[ self.__length ][ syllable_ ] )
		return check_if_infix_in_sets(tmp, infix_)
		
	def has_vol_alternative(self, infix_, hasVerbInfixes_):
		tmp_set = None
		for i in self.__base_vol_infixes:
			if infix_ in i:
				tmp_set = i
				break
		if tmp_set is None:
			if hasVerbInfixes_:
				for i in self.__verb_vol_infixes:
					if infix_ in i:
						tmp_set = i
						break
			else:
				for i in self.__noun_vol_infixes:
					if infix_ in i:
						tmp_set = i
						break
		if not tmp_set is None:
			return tmp_set.has_alternative(infix_)
		else:
			return False
		
	def get_vol_alternative(self, infix_, hasVerbInfixes_):
		tmp_set = None
		for i in self.__base_vol_infixes:
			if infix_ in i:
				tmp_set = i
				break
		if tmp_set is None:
			if hasVerbInfixes_:
				for i in self.__verb_vol_infixes:
					if infix_ in i:
						tmp_set = i
						break
			else:
				for i in self.__noun_vol_infixes:
					if infix_ in i:
						tmp_set = i
						break
		if not tmp_set is None:
			if tmp_set.has_alternative(infix_):
				return tmp_set.get_alternative(infix_)
		return None
		
	def cons_matcher(self, syllable_, infix_):
		tmp = self.__cons_matcher[ self.__length ][ syllable_ ] 
		if tmp is not None:
			return check_if_infix_in_sets( list( tmp ), infix_ )
		else:
			return False
			
	def has_cons_alternative(self, infix_):
		tmp_set = None
		for i in self.__cons_infixes:
			if infix_ in i:
				tmp_set = i
				break
		if not tmp_set is None:
			return tmp_set.has_alternative(infix_)
		else:
			return False
			
	def get_cons_alternative(self, infix_):
		tmp_set = None
		for i in self.__cons_infixes:
			if infix_ in i:
				tmp_set = i
				break
		if not tmp_set is None:
			if tmp_set.has_alternative(infix_):
				return tmp_set.get_alternative(infix_)
		return None
		
	def num_Vols(self):
		return self.__vols_per_Stem[ self.__length ]
		
	def num_Cons(self):
		return self.__cons_per_Stem[ self.__length ]
		
	def num_vol_cats(self):
		return lambda cat_: [0,1]
		
	def num_cons_cats(self):
		return lambda cat_: [0,1] if cat_ != "Lexical_Category" else [1,1]
	
	def vol_cat_checker(self, hasVerbInfixes_, infix_ ):
		if check_if_infix_in_sets( self.__base_vol_infixes, infix_ ) :
			return True
		elif hasVerbInfixes_ and check_if_infix_in_sets( self.__verb_vol_infixes, infix_ ) :
			return True
		elif not hasVerbInfixes_ and check_if_infix_in_sets( self.__noun_vol_infixes, infix_ ) :
			return True
		else:
			return False
			
	def cmp_cons_infixes(self, sDict, oDict):
		"""returns -1 for lesser than, 0 for equal and 1 for greater than"""
		if len(sDict) < len(oDict):
			return -1
		elif len(sDict) > len(oDict):
			return 1
		return cmp_infixes(sDict, oDict, self.__cons_infixes)
	
	def cmp_vols_infixes(self, sDict, oDict, hasVerbInfixes_):
		"""returns -1 for lesser than, 0 for equal and 1 for greater than"""
		if len(sDict) < len(oDict):
			return -1
		elif len(sDict) > len(oDict):
			return 1
		bol = cmp_infixes(sDict, oDict, self.__base_vol_infixes)
		if bol == 0:
			if hasVerbInfixes_:
				bol = cmp_infixes(sDict, oDict, self.__verb_vol_infixes)
			else:
				bol = cmp_infixes(sDict, oDict, self.__noun_vol_infixes)
		return bol

class ver_1_3_5(Stem_abc):
	def __init__(self, root_=None, con_infixxes_=None, 
                 vol_infixxes_=None, length=0):
		if isinstance(root_, root_t):
			if len(root_) == length:
				self.__matcher = ver_1_3_5_matcher(length)
				super().__init__( root_, con_infixxes_, vol_infixxes_, 
				                  length, 1,3,5, None )
			else:
				raise ValueError()
		else:
			raise TypeError()
		
	def matcher(self):
		return self.__matcher
		
	def length(self):
		"""Return the Length in Syllables."""
		return self.__matcher.length()
		
	def all_lengths(self):
		return self.__matcher.all_lengths()
		
	def check_infix( self, num_, infixes_, mat_ ):
		""" 
		   *num_* is a 2 length Sequence of ints. 
		   *mat_* is a lambda/function that takes a key(str) 
		   and returns a 2 length Sequence of ints.
		   *infixes_* is a Sequence of infix instances.
		"""
		len_ = len(infixes_)
		# checking if the total number of infixxes 
		#  is in the correct ranges...
		if num_[0] <= len_ <= num_[1]:
			bol = True
			dict_ = org_infixes(infixes_)
			# checking the number of infixes per Category
			#  is in the correct ranges...
			for i in dict_.keys():
				if not ( mat_(i)[0] <= len(dict_[i]) <= mat_(i)[1]):
					bol = False
			return bol
		else:
			return False
		
	def check_infixes(self, con_infixes_, vol_infixes_ ):
		mat_ = self.matcher()
		if self.check_infix( mat_.num_Vols(), vol_infixes_, mat_.num_vol_cats() )\
		and self.check_infix( mat_.num_Cons(), con_infixes_, mat_.num_cons_cats() ):
			vol_ = org_infixes(vol_infixes_)
			cons_ = org_infixes(con_infixes_)
			hasVerbInfixes_ = mat_.has_verb_vol_infixes(cons_["Lexical_Category"])
			bol = True
			for i in vol_.keys():
				# checking the Vowel Infix list by Lexical Category
				#  for "illegal" Infixes.
				if not mat_.vol_cat_checker(hasVerbInfixes_,vol_[i]):
					bol = False 
			return bol
		else:
			return False
		
	def assemble(self):
		""" 
		   Basic assumption: get_root_checker and check_infixes returned True,
		   in other words this a valid word_stem and all that needs to 
		   be done is to assemble it into a list of Syllables and return them. 
		"""
		mat_ = self.matcher()
		tmp = list()
		nuc_mat = Nucleus_match()
		co_mat = Coda_match()
		# copy the root and infix lists so we can delete elements with impunity..
		root_  = list(self.root())
		vol_ = list(self.vol_infixxes())
		cons_ = list(self.con_infixxes())
		# extract the Lexical Category for hasVerbInfixes_ checking..
		cons_d = org_infixes(cons_)
		hasVerbInfixes_ = mat_.has_verb_vol_infixes(cons_d["Lexical_Category"])
		for i in range(0,mat_.length()):
			onset_ = root_[i]
			vSys1 = None
			vSys2 = None
			nuc_vols = list()
			coda_ = None
			syl_ = None
			# checking and extracting the vowel infixes ..
			for j in vol_:
				if mat_.vol_matcher(i+1, j, hasVerbInfixes_):
					if isinstance(j, system1): 
						if vSys1 is None:
							vSys1 = j
						else:
							raise ValueError()
					elif isinstance(j, system2): 
						if vSys2 is None:
							vSys2 = j
						else:
							raise ValueError()
					else:
						raise TypeError()
			if not vSys1 is None:
				vol_.remove(vSys1)
				nuc_vols.extend( vSys1.vowel() )
			if not vSys2 is None:
				vol_.remove(vSys2)
				# need to rewrite using a temporary
				# and some fancy ringmarole to swap 
				#  the Infix with it's Alternate if needed..
				if len(vSys2.vowel()[0]) == 1 and vSys2.vowel()[0] == "" :
					# if vSys1 is None.. we *want* to a vSys2 to *not* be None or Null...
					if mat_.has_vol_alternative(vSys2, hasVerbInfixes_) and vSys1 is None:
						vTmp = mat_.get_vol_alternative(vSys2, hasVerbInfixes_)
						nuc_vols.extend( vTmp.vowel() )
				else:
					nuc_vols.extend( vSys2.vowel() )
			if not nuc_mat.is_allowable_set(nuc_vols):
				raise ValueError("Unallowed set of Nucleus Vowels :" + str(nuc_vols))
			# checking and extracting the Consonant infixes ..
			conTmp = list()
			for j in cons_:
				if mat_.cons_matcher(i+1, j):
					if j.is_onset():
						# need to rewrite using a temporary
						# and some fancy ringmarole to swap 
						#  the Infix with it's Alternate if needed..
						tOns_ = list(onset_)
						tOns_.extend( j.consonant() )
						if self.get_root_checker().is_allowable_set( tOns_ ):
							onset_ = tOns_
						elif mat_.has_cons_alternative( j ):
							tCon = mat_.get_cons_alternative( j )
							tOns1_ = list(onset_)
							tOns1_.extend( tCon.consonant() )
							if self.get_root_checker().is_allowable_set( tOns1_ ):
								onset_ = tOns1_
							else:
								raise ValueError()
						else: 
							raise ValueError()
					else:
						if coda_ is None:
							coda_ = j.consonant()
							if not co_mat.is_allowable_set( coda_ ):
								raise ValueError()
					conTmp.append(j)
			for j in conTmp:
				cons_.remove( j )
			# havin retrieved all elements necessary, let's build!
			if coda_ is not None:
				syl_ = Closed_Syl( onset_, nuc_vols, coda_ )
			else:
				syl_ = Open_Syl( onset_, nuc_vols, False )
			tmp.append( syl_ )
		return tmp
		
	def cmp_infixes(self, other, sCons, sVols, oCons, oVols):
		# basic assumption: being called by self.__X__(other)
		#  and both self as well as other are both valid word stems.
		if not isinstance(other ,ver_1_3_5):
			raise TypeError()
		sMat_ = self.matcher()
		oMat_ = other.matcher()
		if sMat_.__class__ is not oMat_.__class__:
			raise TypeError()
		if len(sCons) != 0 and len(sVols) != 0 and len(oCons) != 0 and len(oVols) != 0:
			if len(sCons) < len(oCons):
				return -1
			elif len(sCons) > len(oCons):
				return 1
			if len(sVols) < len(oVols):
				return -1
			elif len(sVols) > len(oVols):
				return 1
			sVol_ = org_infixes(sVols)
			oVol_ = org_infixes(oVols)
			sCon_ = org_infixes(sCons)
			oCon_ = org_infixes(oCons)
			# cmp_cons_infixes(self, sDict, oDict)
			bol = sMat_.cmp_cons_infixes(sCon_, oCon_)
			if bol == 0:
				hasVerbInfixes1_ = sMat_.has_verb_vol_infixes(sCon_["Lexical_Category"])
				hasVerbInfixes2_ = sMat_.has_verb_vol_infixes(oCon_["Lexical_Category"])
				if hasVerbInfixes1_ == hasVerbInfixes2_:
					# cmp_vols_infixes(self, sDict, oDict, hasVerbInfixes_)
					bol = sMat_.cmp_vols_infixes(sVol_, oVol_, hasVerbInfixes1_)
				else:
					raise ValueError()
			return bol 
		else:
			raise ValueError()

##################################################################
#
# Tests Main
#

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
