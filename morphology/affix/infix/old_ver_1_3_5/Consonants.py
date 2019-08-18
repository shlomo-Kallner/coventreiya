

##################################################################
#
# Imports
#

from coventreiya.morphology.affix.infix import Consonant as __Cons_affix_abc

from coventreiya.morphology.affix.abc import set_abc as __affix_set

from coventreiya.phonotactics.onsets.ver_1_5_7 import ver_1_5_7 as __onset_match

from coventreiya.phonotactics.codas.ver_1_5_7 import ver_1_5_7 as __coda_match

##################################################################
#
# Coventreiya Morphology  -  Affix - Consonant Infixxes
#

class Consonants(__Cons_affix_abc):
	def __init__(self, cons_=None, is_onset=False, 
	             has_neg=False, has_def=True, has_alt=False, has_null=True,
                 #def_=None, is_def=False, alt_=None, is_alt=False,
                 major=0, minor=0, patch=0, version=None):
					 if bool(is_onset):
						 match_ = __onset_match()
					 else:
						 match_ = __coda_match()
					 super().__init__(cons_, match_, is_onset, 
					                  has_neg, has_def, has_alt, has_null,
					                  major, minor, patch, version)
	pass
					 
class Animacy(__Cons_affix_abc):
    pass

class Sentience(__Cons_affix_abc):
	pass
	
class Lexical_Category(__Cons_affix_abc):
	pass
	
