

##################################################################
#
# Imports
#

from enum import Enum as __enum

from coventreiya.morphology.affix.infix import Consonant as __Cons_affix_abc
from coventreiya.morphology.affix.infix import Vowel as __Vol_affix_abc

from coventreiya.morphology.affix.abc import set_abc as __affix_set

from coventreiya.phonotactics.onsets.ver_1_5_7 import ver_1_5_7 as __onset_match
from coventreiya.phonotactics.nucleus.ver_1_5_7 import ver_1_5_7 as __nucleus_match
from coventreiya.phonotactics.codas.ver_1_5_7 import ver_1_5_7 as __coda_match

##################################################################
#
# Coventreiya Morphology  -  Affix - Consonant Infixxes' Base Class
#

class Consonants(__Cons_affix_abc):
	def __init__(self, cons_=None, is_onset=False, 
	             has_neg=False, has_def=True, has_alt=False, has_null=True):
					 if bool(is_onset):
						 match_ = __onset_match()
					 else:
						 match_ = __coda_match()
					 super().__init__(cons_, match_, is_onset, 
					                  has_neg, has_def, has_alt, has_null,
					                  1, 3, 5, None)
	pass
	
#def gen_Consonants_lambda( is_onset=False, has_neg=False, has_def=True, 
#                           has_alt=False, has_null=True ):
#	return lambda str_: Consonants( str_, is_onset, has_neg, has_def,
#					                has_alt, has_null)

##################################################################
#
# Coventreiya Morphology  -  Affix - Consonant Infixxes' Actual Classes
#

class Animacy(int, __enum):
	#min_ = 0
	Inanimate_Object_ = 0
	Inanimate_Energy_ = 1
	# special categories of the possibly Inanimate 
	Spatial_Location = 2
	Temporal_Location = 3 # aka an Event
	Concept_ = 4
	# the Full Categories of the Animate
	Viroid_ = 5
	Protists_ = 6
	Microbes_ = 7
	Fungi_ = 8
	Plant_ = 9
	Animalistic_ = 10
	#max_ = 10
	
def gen_Animacy():
	is_onset=False
	has_neg=False 
	has_def=True 
	has_alt=False 
	has_null=False
	func_ = lambda str_: Consonants( str_, is_onset, has_neg, has_def,
					                 has_alt, has_null)
	set_ = __affix_set( Consonants, "Animacy", has_neg, has_def, 
	                    func_( [ "[θ]" ] ), Animacy.Inanimate_Object_,
	                    None, 1,3,5, None)
	set_[Animacy.Inanimate_Energy_] = func_( [ "[ɡ]" ] )
	set_[Animacy.Spatial_Location] = func_( [ "[ɫ]" ] )
	set_[Animacy.Temporal_Location] = func_( [ "[t]" ] )
	set_[Animacy.Concept_] = func_( [ "[d]" ] )
	set_[Animacy.Viroid_] = func_( [ "[ʃ]" ] )
	set_[Animacy.Protists_] = func_( [ "[ɹ̠]" ] )
	set_[Animacy.Microbes_] = func_( [ "[k]" ] )
	set_[Animacy.Fungi_] = func_( [ "[f]" ] )
	set_[Animacy.Plant_] = func_( [ "[p]" ] )
    set_[Animacy.Animalistic_] = func_( [ "[x]" ] )
    return set_

class Sentience(int, __enum):
	#min_ = 0
	NotSentient_ = 0
	Sentient_ = 1
	Supernatural_ = 2
	Deity_ = 3
	#max_ = 3
	
def gen_Sentience():
	is_onset=False
	has_neg=False 
	has_def=True 
	has_alt=True 
	has_null=True
	func_ = lambda str_, has_alt_=has_alt: Consonants( str_, is_onset, 
	                                                   has_neg, has_def,
					                                   has_alt_, 
					                                   has_null)
	set_ = __affix_set( Consonants, "Sentience", has_neg, has_def, 
	                    func_( [ "" ] , False ), Sentience.NotSentient_,
	                    None, 1,3,5, None)
	set_.add(Sentience.Sentient_, func_([ "[w]" ]), func_([ "[j]" ]) )
	set_.add(Sentience.Supernatural_, func_([ "[v]" ]), func_([ "[ʕ]" ]) )
	set_.add(Sentience.Deity_, func_([ "[ʔ]" ]), func_([ "[l]" ]) )
	return set_
	
class Lexical_Category(int, __enum):
	#min_ = 0
	NotApplicable_ = 0
	Noun_ = 1
	Verb_ = 2
	Adjective_ = 3
	Adverb_ = 4
	Number_ = 5
	#max_ = 5
	
def gen_Lexical_Category():
	is_onset=False
	has_neg=False 
	has_def=True 
	has_alt=False 
	has_null=True
	func_ = lambda str_: Consonants( str_, is_onset, has_neg, has_def,
					                 has_alt, has_null)
	set_ = __affix_set( Consonants, "Lexical_Category", has_neg, has_def, 
	                    func_( [ "" ] ), Lexical_Category.NotApplicable_,
	                    None, 1,3,5, None)
	set_[Lexical_Category.Noun_] = func_( [ "[n]" ] )
	set_[Lexical_Category.Adjective_] = func_( [ "[ŋ]" ] )
	set_[Lexical_Category.Verb_] = func_( [ "[v]" ] )
	set_[Lexical_Category.Adverb_] = func_( [ "[ʒ]" ] )
	set_[Lexical_Category.Number_] = func_( [ "[s]" ] )
	return set_
	
##################################################################
#
# Coventreiya Morphology  -  Affix - Vowel Infixxes' Base Class
#

class Vowels(__Vol_affix_abc):
	def __init__( self, vowel_=None, has_neg=False, has_def=True, 
	              has_alt=False, has_null=True ):
					  matcher = __nucleus_match()
					  super().__init__(vowel_,matcher,has_neg,has_def,
					                   has_alt,has_null,
					                   1, 3, 5, None)
	pass

#def gen_Vowels_lambda( has_neg=False, has_def=True, has_alt=False, 
#                       has_null=True ):
#	return lambda str_: Vowels( str_, has_neg, has_def, has_alt,
#						        has_null )

##################################################################
#
# Coventreiya Morphology  -  Affix - Vowel Infixxes' Actual Classes
#

def gen_system1( catName_="" ):
	has_neg=False
	has_def=True
	has_alt=False
	has_null=True
	func_ = lambda str_: Vowels( str_, has_neg, has_def, has_alt,
						         has_null )
	set_ = __affix_set( Vowels, catName_, has_neg, has_def,
	                    func_( [ "[ä]" ] ), 0, None, 1,3,5,None)
	set_[1] = func_( [ "[e]" ] )
	set_[2] = func_( [ "[ʊ]" ] )
	set_[3] = func_( [ "[ɛ]" ] )
	return set_
	
def gen_system2( catName_="" ):
	has_neg=False
	has_def=True
	has_alt=False
	has_null=True
	func_ = lambda str_: Vowels( str_, has_neg, has_def, has_alt,
						         has_null )
	set_ = __affix_set( Vowels, catName_, has_neg, has_def,
	                    func_( [ "" ] ), 0, [ "[ɪ]" ], 1,3,5,None)
	set_[1] = func_( [ "[i]" ] )
	set_[2] = func_( [ "[u]" ] )
	set_[3] = func_( [ "[o̞]" ] )
	set_[4] = func_( [ "[ɔ]" ] )
	set_[5] = func_( [ "[æ]" ] )
	set_[6] = func_( [ "[œ]" ] )
	return set_

class Modality(int, __enum):
	#min_ = 0
	Indicative_ = 0
	Declarative_ = 1
	Interrogative_ = 2
	Jussive_ = 3
	#NotApplicable_ = 4 # empty slot!!!
	Imperative_ = 5
	#max_ = 5
	
def gen_Modality():
	return gen_system2( "Modality" )
	
class Abstractivity(int, __enum):
	#min_ = 0
	Concrete_ = 0
	Virtual_ = 1
	Abstract_ = 2
	#max_ = 2
	
def gen_Abstractivity():
	return gen_system1( "Abstractivity" )
	


class Verb_Transitivity(int, __enum):
	#min_ = 0
	Intransitive_ = 0
	Transitive_ = 1
	Ditransitive_ = 2
	Tritransitive_ = 3
	#max_ = 3
	
def gen_Verb_Transitivity():
	return gen_system2( "Verb.Transitivity" )
	
class Verb_Finiteness(int, __enum):
	#min_ = 0
	Finite_ = 0
	Participle_ = 1
	Gerund_ = 2
	#max_ = 2
	
def gen_Verb_Finiteness():
	return gen_system1( "Verb.Finiteness" )
	
class Verb_Valency(int, __enum):
	#min_ = 0
	Normative_ = 0
	Reciprocal_ = 1
	#max_ = 1
	
def gen_Verb_Valency():
	return gen_system2( "Verb.Valency" )
	
class Verb_Voice(int, __enum):
	#min_ = 0
	Active_ = 0
	Passive_ = 1
	Reflexive_ = 2
	#max_ = 2
	
def gen_Verb_Voice():
	return gen_system1( "Verb.Voice" )
	


class Noun_Countability(int, __enum):
	#min_ = 0
	NonCountable_ = 0
	Countable_ = 1
	Mass_ = 2
	#max_ = 1
	
def gen_Noun_Countability():
	return gen_system2( "Noun.Countability" )
	
class Noun_Individuality(int, __enum):
	#min_ = 0
	Indivual_ = 0
	Collective_ = 1
	#max_ = 1
	
def gen_Noun_Individuality():
	return gen_system1( "Noun.Individuality" )
	
class Noun_Type(int, __enum):
	#min_ = 0
	Common_ = 0
	Derived_ = 1
	#max_ = 1
	
def gen_Noun_Type():
	return gen_system2( "Noun.Type" )
	
class Noun_Dependency(int, __enum):
	#min_ = 0
	Independent_ = 0
	Dependent_ = 1
	#max_ = 1
	
def gen_Noun_Dependency():
	return gen_system1( "Noun.Dependency" )
