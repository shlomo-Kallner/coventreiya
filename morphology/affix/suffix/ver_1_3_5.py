#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
#
#  ver_1_3_5.py
#  
#  Copyright 2017 Shlomo Kallner <shlomo.kallner@gmail.com>
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


##################################################################
#
# Imports
#

from enum import Enum

from coventreiya.morphology.affix.suffix import Suffix as affix_abc
from coventreiya.morphology.affix.abc import set_abc as affix_set

from coventreiya.phonotactics.onsets.ver_1_5_7 import ver_1_5_7 as onset_match

from coventreiya.morphology.syllable.open.ver_1_3_5 import ver_1_3_5 openSyllable

##################################################################
#
# Morphology  -  Affix - Prefixxes
#

class ver_1_3_5(affix_abc):
	def __init__( self, name="", value=None, cons_=None, vowel_=None, 
	              has_alt=False ):
		has_def=True
		has_null=True
		super().__init__(name, value, cons_, vowel_, openSyllable, 
                 has_def, has_alt, has_null,
                 1, 3, 5, None)
    pass
    
class ver_1_3_5_set(affix_set):
	def __init__( self, name="", cons_=None, set_enum=None ):
		if issubclass(set_enum, int) and issubclass(set_enum, Enum):
			self.__enum = set_enum
		else: 
			raise TypeError()
		has_neg=True
		has_def=True
		d = dict({ 0 : [ "" ],
		           # setting the positive values
		           1 : [ "[e]" ],
		           2 : [ "[i]" ],
		           3 : [ "[u]" ],
		           4 : [ "[o̞]" ],
		           5 : [ "[ɔ]" ],
		           6 : [ "[ä]" ],
		           7 : [ "[æ]" ],
		           8 : [ "[œ]" ],
		           # setting the negative values
		           -1 : [ "[əe]" ],
		           -2 : [ "[əi]" ],
		           -3 : [ "[əu]" ],
		           -4 : [ "[əo̞]" ],
		           -5 : [ "[əɔ]" ],
		           -6 : [ "[əä]" ],
		           -7 : [ "[əæ]" ],
		           -8 : [ "[əœ]" ] })
		func_ = lambda str_, val_, has_alt_=False: ver_1_3_5( name, val_, 
		                                                cons_, str_, 
		                                                has_alt_ )
		super().__init__(ver_1_3_5, name, has_neg, has_def,
		                 func_( d[0], set_enum(0), True ), set_enum(0), 
		                 func_( [ "[ɪ]" ], True ), 1, 3, 5, None )
		for i in set_enum:
			if i.value != 0:
				super()[i] = func_( d[i.value], i )
		
	def __setitem__(self, key, value):
		"""
		   Completely disregard *value* 
		   - this method is supposed to hide the super-classes method
		     and prevent the adding of values...
		"""
        return super()[key]
        
    def add(self, index, item=None, alt_item=None):
		"""
		   Completely disregard *item* and *alt_item*
		   - this method is supposed to hide the super-classes method
		     and prevent the adding of values...
		"""
        return super()[index]
        
    pass

	
class all_values(ver_1_3_5_set):
	class enum_(int, Enum):
		Default_ = 0
		FirstPositiveValue_ = 1
		SecondPositiveValue_ = 2
		ThirdPositiveValue_ = 3
		FourthPositiveValue_ = 4
		FifthPositiveValue_ = 5
		SixthPositiveValue_ = 6
		SeventhPositiveValue_ = 7
		EighthPositiveValue_ = 8
		FirstNegativeValue_ = -1
		SecondNegativeValue_ = -2
		ThirdNegativeValue_ = -3
		FourthNegativeValue_ = -4
		FifthNegativeValue_ = -5
		SixthNegativeValue_ = -6
		SeventhNegativeValue_ = -7
		EighthNegativeValue_ = -8
		
	def __init__(self, name="", cons_=None ):
		super().__init__(name, cons_, self.enum_)
		
    pass	

##################################################################
#
# The Non-Comparative Number, Gender, Person, Contuation and 
# Suffixed Aspects and Cases
#

class Number_(ver_1_3_5_set):
	class enum_(int, Enum):
		#Singular_ = 0
		SimpleInclusivePlural_ = 1  # at least 2...
		InclusiveExactlyTwo_ = 2
		InclusiveExactlyThree_ = 3
		InclusiveExactlyFour_ = 4
		InclusiveExactlyFive_ = 5
		InclusiveExactlySix_ = 6
		InclusiveExactlySeven_ = 7
		InclusiveExactlyEight_ = 8
		SimpleExclusivePlural_ = -1  # at least 2...
		ExclusiveExactlyTwo_ = -2
		ExclusiveExactlyThree_ = -3
		ExclusiveExactlyFour_ = -4
		ExclusiveExactlyFive_ = -5
		ExclusiveExactlySix_ = -6
		ExclusiveExactlySeven_ = -7
		ExclusiveExactlyEight_ = -8
		
	def __init__(self):
		super().__init__("Number.Marking", [ "[s]", ] , self.enum_)
		
    pass

class Gender_(ver_1_3_5_set):
	class enum_(int, Enum):
		#Neuter_ = 0
		Male_ = 1
		Female_ = 2
		Intersex_ = 3
		Mitosis_ = 4
		Budding_ = 5
		Sporing_ = 6
		EnzymaticCatalyst_ = 7
		#EighthPositiveValue_ = 8
		#EighthNegativeValue_ = -8
		
	def __init__(self):
		super().__init__("Gender.Marking", [ "[t]", ] , self.enum_)
		
    pass

class Person_(ver_1_3_5_set):
	class enum_(int, Enum):
		#FirstPerson_ = 0
		SecondPerson_ = 1
		ThirdPerson_ = 2
		FourthPerson_ = 3
		#EighthPositiveValue_ = 8
		#EighthNegativeValue_ = -8
		
	def __init__(self):
		super().__init__("Person.Marking", [ "[x]", ] , self.enum_)
		
    pass

class Continuation_(ver_1_3_5_set):
	class enum_(int, Enum):
		#Default_ = 0
		AtLeastOne_ = 1
		#SecondPositiveValue_ = 2
		NumberConnector_ = 3
		#EighthPositiveValue_ = 8
		#EighthNegativeValue_ = -8
		
	def __init__(self):
		super().__init__("Continuation.Marking", [ "[ʔ]", ] , self.enum_)
		
    pass

class Progressive_ImperfectiveAspect_(ver_1_3_5_set):
	class enum_(int, Enum):
		#Default_ = 0
		IsProgressive_ = 1
		#EighthPositiveValue_ = 8
		IsContinuous_ = -1
		#EighthNegativeValue_ = -8
		
	def __init__(self):
		super().__init__("Progressive.ImperfectiveAspect", [ "[ɮ]", ] , self.enum_)
		
    pass

##################################################################
#
# The Comparative Suffixes
#

class Comparatives_(ver_1_3_5_set):
	class enum_(int, Enum):
		Default_ = 0
		Positive_ = 1
		MoreThan_ = 2
		MoreThanPlus1_ = 3
		MoreThanPlus2_ = 4
		MoreThanPlus3_ = 5
		MoreThanPlus4_ = 6
		MoreThanPlus5_ = 7
		PositiveSuperlative_ = 8
		Negative_ = -1
		LessThan_ = -2
		LessThanPlus1_ = -3
		LessThanPlus2_ = -4
		LessThanPlus3_ = -5
		LessThanPlus4_ = -6
		LessThanPlus5_ = -7
		NegativeSuperlative_ = -8
		
	def __init__(self, name="", cons_=None ):
		super().__init__(name, cons_, self.enum_)
		
    pass
		                                                  

class Demonstrative_Case_(Comparatives_):
	"""Distance Demonstative"""
	def __init__(self):
		super().__init__("Demonstrative.Case", [ "[ð]", ] )
		
	pass
	
class Tense_(Comparatives_):
	def __init__(self):
		super().__init__("Tense", [ "[z]", ] )
		
	pass
	
class Honorific_(Comparatives_):
	def __init__(self):
		super().__init__("Honorific", [ "[n]", ] )
		
	pass
	
class Genitive_Case_(Comparatives_):
	"""Possessed Genitive"""
	def __init__(self):
		super().__init__("Genitive.Case", [ "[j]", ] )
		
	pass
	
class Iterative_ImperfectiveAspect_(Comparatives_):
	def __init__(self):
		super().__init__("Iterative.ImperfectiveAspect", [ "[r]", ] )
		
	pass
	
class Habitual_ImperfectiveAspect_(Comparatives_):
	def __init__(self):
		super().__init__("Habitual.ImperfectiveAspect", [ "[ʍ]", ] )
		
	pass
	
class Affiliative_Case_(Comparatives_):
	def __init__(self):
		super().__init__("Affiliative.Case", [ "[v]", ] )
		
	pass

##################################################################
#
# Tests Main
#

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
