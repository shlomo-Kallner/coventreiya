##################################################################
#
# Imports
#

from coventreiya.morphology.affix.abc import abc as affix_abc
from coventreiya.phonotactics.onsets import Onsets as Onsets_match
from coventreiya.phonotactics.nucleus import Nucleus as Nucleus_match
from coventreiya.phonotactics.codas import Codas as Codas_match

from coventreiya.utils.matcher import Matcher

##################################################################
#
# Morphology  -  Affix - Infixxes
#

class Infix(affix_abc):
	def __init__( self, name="", value=None, has_cons=False, has_vowel=False, 
	              has_neg=False, has_def=True, has_alt=False, 
	              has_null=True, major=0, minor=0, patch=0, 
	              version=None):
		super().__init__(name,value,has_cons,has_vowel,False,
                         has_neg,has_def,has_alt,has_null,
                         major, minor, patch, version)
                         
    def get_syllable(self):
        """
           Returns a given Affix Realization as a Syllable or None.
           Actually copies and returns the internal data (*self.__matcher*).
        """
        return None
    pass
                   

class Consonant(Infix):
    def __init__(self, name="", value=None, cons_=None, matcher_cls=None, is_onset=False,
                 has_neg=False, has_def=True, has_alt=False, has_null=True,
                 major=0, minor=0, patch=0, version=None):
		has_cons = True
		has_vowel = False
        super().__init__( name, value, has_cons, has_vowel, has_neg, 
                          has_def, has_alt, has_null, 
                          major, minor, patch, version )
        if (bool(is_onset) and issubclass(matcher_cls, Onsets_match))\
           or (not bool(is_onset) and issubclass(matcher_cls, Codas_match)):
            self.__matcher = type(matcher_cls).__new__()
            self.__is_onset = bool(is_onset)
        else:
            raise TypeError()
        self.__has_null = bool(has_null)
        if self.__matcher.is_allowable_set(cons_):
            self.__cons_ = cons_
        elif bool(has_def) and bool(has_null):
			tmp = list()
			tmp.append("")
			self.__cons_ = tmp
        else:
            raise ValueError
            
    def is_onset(self):
		return self.__is_onset

    def get_consonant(self):
        """
           Returns the Consonant as a List of a String.
           If Affix does not have a Consonant, returns an empty list.
        """
        return self.__cons_

    def get_vowel(self):
        """
           Returns the Vowel[s] as a List of Strings.
           If Affix does not have Vowel[s], returns an empty list.
        """
        return list()

class Cons_infix_matcher(Matcher):
	def __init__(self, min_length=0, max_length=0,
	             major=0, minor=0, patch=0, version=None):
		super().__init__(min_length=0, max_length=0, Consonant,
                 major=0, minor=0, patch=0, version=None)
                 
    pass
		
       

class Vowel(Infix):
    def __init__(self, name="", value=None, vowel_=None, matcher_cls=None,
                 has_neg=False, has_def=True, has_alt=False, has_null=True,
                 major=0, minor=0, patch=0, version=None):
        has_cons = False
		has_vowel = True
        super().__init__( name, value, has_cons, has_vowel,
                          has_neg, has_def, has_alt, has_null, 
                          major, minor, patch, version )
        if issubclass(matcher_cls, Nucleus_match):
            self.__matcher = type(matcher_cls).__new__()
        else:
            raise TypeError()
        if self.__matcher.is_allowable_set(vowel_):
            self.__vowel_ = vowel_
        elif bool(has_def) and bool(has_null):
			tmp = list()
			tmp.append("")
			self.__vowel_ = tmp
        else:
            raise ValueError()

    def get_vowel(self):
        """
           Returns the Vowel[s] as a List of Strings.
           If Affix does not have Vowel[s], returns an empty list.
        """
        return self.__vowel_

    def get_consonant(self):
        """
           Returns the Consonant as a List of a String.
           If Affix does not have a Consonant, returns an empty list.
        """
        return list()

class Vols_infix_matcher(Matcher):
	def __init__(self, min_length=0, max_length=0,
	             major=0, minor=0, patch=0, version=None):
		super().__init__(min_length=0, max_length=0, Vowel,
                 major=0, minor=0, patch=0, version=None)
                 
    pass



    
