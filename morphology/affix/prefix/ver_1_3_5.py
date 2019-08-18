#!/usr/bin/env python3
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

from coventreiya.morphology.affix.prefix import Prefix as affix_abc
from coventreiya.morphology.affix.abc import set_abc as affix_set

from coventreiya.phonotactics.onsets.ver_1_5_7 import ver_1_5_7 as onset_match

from coventreiya.morphology.syllable.open.ver_1_3_5 import ver_1_3_5 as openSyllable

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
# The Non-Comparative Prepositions and Prefixed Aspects
#

class Case_Marking_(ver_1_3_5_set):
	class enum_(int, Enum):
		#Default_ = 0
		PassiveSubject_ = 1
		InvoluntaryAgentiveSubject_ = 2
		VoluntaryAgentiveSubject_ = 3
		RecipientSubject_ = 4
		InstrumentalSubject_ = 5 # the subject's Instrument..
		AntiInstrumentalSubject_ = 6 # negated InstrumentalSubject..
		#EighthPositiveValue_ = 8
		PassiveObject_ = -1
		InvoluntaryAgentiveObject_ = -2
		VoluntaryAgentiveObject_ = -3
		RecipientObject_ = -4
		InstrumentalObject_ = -5
		AntiInstrumentalObject_ = -6
		#EighthNegativeValue_ = -8
				
	def __init__(self):
		super().__init__("Case.Marking", [ "[ť]" ], self.enum_)
		
    pass

class Prospective_Aspect_(ver_1_3_5_set):
	class enum_(int, Enum):
		#Default_ = 0
		ToDoInfinitive_ = 1
		ToDoOptative_ = 2
		ToDoSpeculativeIf_ = 3
		SpeculativeThen_ = 4
		ToBeSpeculativeIf_ = 5
		ToBeOptative_ = 6
		ToBeInfinitive_ = 7
		#EighthPositiveValue_ = 8
		NegativeToDoInfinitive_ = -1
		AntiToDoOptative_ = -2
		ToDoSpeculativeIfNot_ = -3
		SpeculativeThenNot_ = -4
		ToBeSpeculativeIfNot_ = -5
		AntiToBeOptative_ = -6
		NegativeToBeInfinitive_ = -7
		#EighthNegativeValue_ = -8
		
	def __init__(self):
		super().__init__("Prospective.Aspect", [ "[l]" ], self.enum_)
		
    pass
    
class Conjunctor_Prepositions_(ver_1_3_5_set):
	class enum_(int, Enum):
		#Default_ = 0
		And_ = 1
		With_ = 2
		InclusiveOr_ = 3
		Also_ = 4
		But_ = 5
		#EighthPositiveValue_ = 8
		AndNot_ = -1
		Without_ = -2
		ExclusiveOr_ = -3
		Neither_ = -4
		ButNot_ = -5
		#EighthNegativeValue_ = -8
		
	def __init__(self):
		super().__init__("Conjunctor.Prepositions", [ "[w]" ], self.enum_)
		
    pass
    
class Spatial_Prepositions_(ver_1_3_5_set):
	class enum_(int, Enum):
		#Default_ = 0
		InsideOf_ = 1
		At_ = 2
		Towards_ = 3
		OnTopOf_ = 4
		Beyond_ = 5 # Behind_ ?
		InTo_ = 6
		#EighthPositiveValue_ = 8
		OutsideOf_ = -1
		Around_ = -2
		AwayFrom_ = -3
		Underneath_ = -4
		UpTo_ = -5
		OutFrom_ = -6
		#EighthNegativeValue_ = -8
		
	def __init__(self):
		super().__init__("Spatial.Prepositions", [ "[m]" ], self.enum_)
		
    pass
    
class Temporal_Prepositions_(ver_1_3_5_set):
	class enum_(int, Enum):
		#Default_ = 0
		WithIn_ = 1
		At_ = 2
		TowardsUntil_ = 3
		On_ = 4
		After_ = 5
		InTo_ = 6
		#EighthPositiveValue_ = 8
		OutsideOf_ = -1
		Around_ = -2
		From_ = -3
		NotOn_ = -4
		Before_ = -5
		OutFrom_ = -6
		#EighthNegativeValue_ = -8
		
	def __init__(self):
		super().__init__("Temporal.Prepositions", [ "[ʃʼ]" ], self.enum_)
		
    pass
    
class Logical_Identity_Prepositions_(ver_1_3_5_set):
	class enum_(int, Enum):
		#Default_ = 0
		IsPositive_ = 1
		LikeSimilar_ = 2
		As_ = 3
		Pretending_ = 4
		#EighthPositiveValue_ = 8
		IsNegative_ = -1
		NotLikeSimilar_ = -2
		NotAs_ = -3
		NotPretending_ = -4
		#EighthNegativeValue_ = -8
		
	def __init__(self):
		super().__init__("LogicalIdentity.Prepositions", [ "[kʼ]" ], self.enum_)
		
    pass
    
class Logical_Causality_Prepositions_(ver_1_3_5_set):
	class enum_(int, Enum):
		#Default_ = 0
		InOrderForTo_ = 1
		BecauseOf_ = 2
		AboutRegarding_ = 3
		Therefore_ = 4
		#EighthPositiveValue_ = 8
		VersusAgainst_ = -1
		NotBecauseOf_ = -2
		NotAboutRegarding_ = -3
		ThereforeNot_ = -4
		#EighthNegativeValue_ = -8
		
	def __init__(self):
		super().__init__("LogicalCausality.Prepositions", [ "[r]" ], self.enum_)
		
    pass
    
#####################
#
# the fallowing typically have only 
#  one positive and one negative value.
#
#####################

class Inchoative_Cessative_Aspect_(ver_1_3_5_set):
	class enum_(int, Enum):
		Inchoative_ = 1
		Cessative_ = -1
		
	def __init__(self):
		super().__init__("InchoativeCessative.Aspect", [ "[x’]" ], self.enum_)
		
    pass

class Sequensor_Prepositions_(ver_1_3_5_set):
	class enum_(int, Enum):
		Sequential_ = 1
		Parallel_ = -1
		
	def __init__(self):
		super().__init__("Sequensor.Prepositions", [ "[sʼ]" ], self.enum_)
		
    pass	

class Partitive_Case_(ver_1_3_5_set):
	class enum_(int, Enum):
		Set_ = 1
		Entity_ = -1
		
	def __init__(self):
		super().__init__("Partitive.Case", [ "[pʼ]" ], self.enum_)
		
    pass	

class Relativizer_Prepositions_(ver_1_3_5_set):
	class enum_(int, Enum):
		Active_ = 1
		Passive_ = -1		
		
	def __init__(self):
		super().__init__("Relativizer.Prepositions", [ "[d]" ], self.enum_)
		
    pass
    
class Complamentizer_Prepositions_(ver_1_3_5_set):
	class enum_(int, Enum):
		Active_ = 1
		Passive_ = -1	
		
	def __init__(self):
		super().__init__("Complamentizer.Prepositions", [ "[b]" ], self.enum_)
		
    pass

##################################################################
#
# The Comparative Prefixes/Prepositions
#

class Comparatives_(ver_1_3_5_set):
	class enum_(int, Enum):
		#Default_ = 0
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

class Definity_(Comparatives_):
	def __init__(self):
		super().__init__( "Definity", [ "[h]" ] )
		
	pass

class Intensity_Prepositions_(Comparatives_):
	def __init__(self):
		super().__init__( "Intensity.Prepositions", [ "[ɡ]" ] )
		
	pass

class Quantity_Prepositions_(Comparatives_):
	def __init__(self):
		super().__init__( "Quantity.Prepositions", [ "[fʼ]" ] )
		
	pass
	
class Quality_Prepositions_(Comparatives_):
	def __init__(self):
		super().__init__( "Quality.Prepositions", [ "[qʼ]" ] )
		
	pass


#
#
#
##################################################################

##################################################################
#
# Tests Main
#

def test( tg ):
	print("testing ", tg.name(), " ...")
	print("testing *keys()* and the *__getitem__* API...")
	for i in tg.keys():
		print(tg[i].affix())
	print("testing the *__iter__* API...")
	for i in tg:
		print(i.affix())
	print("test complete!")
	return input("press any key and then press ENTER...")

def main(args):
	print("testing *gen_prefix_set_all* ...")
	t1 = all_values( "test_group1", [ "t" ] )
	test( t1 )
	print("testing *gen_prefix_subset_* ...")
	
	class testEnum(ver_1_3_5_set):
		class enum_(int, Enum):
			m1 = -3
			m2 = 5
			m3 = 0
			m4 = -7
		def __init__(self, name="", cons_=None ):
			super().__init__(name, cons_, self.enum_)
		
	t2 = testEnum( "test_group2", [ "m" ] )
	test( t2 )
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
