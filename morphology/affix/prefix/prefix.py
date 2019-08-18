##################################################################
#
# Imports
#

from coventreiya.morphology.affix.abc import abc as __affix_abc
from coventreiya.morphology.syllable.open import Open as __openSyllable

##################################################################
#
# Morphology  -  Affix - Prefixxes
#

class Prefix(__affix_abc):
    def __init__(self, name="", value=None, cons_=None, vowel_=None, matcher_cls=None, 
                 has_def=True, has_alt=False, has_null=True,
                 #def_=None, is_def=False, alt_=None, is_alt=False,
                 major=0, minor=0, patch=0, version=None):
        super().__init__(name,value,True,True,True,True,
                         has_def,has_alt,has_null,
                         #is_def,is_alt,
                         major,minor,patch,version)
        if issubclass(matcher_cls,__openSyllable):
            self.__matcher = type(matcher_cls).__new__(cons_, vowel_, has_def)
        else:
            raise TypeError()
                    
    def get_consonant(self):
        """
           Returns the Consonant as a List of a String.
           If Affix does not have a Consonant, returns an empty list.
        """
        return self.__matcher.onset()

    def get_vowel(self):
        """
           Returns the Vowel[s] as a List of Strings.
           If Affix does not have Vowel[s], returns an empty list.
        """
        return self.__matcher.nucleus()

    def get_syllable(self):
        """
           Returns a given Affix Realization as a Syllable.
           Actually copies and returns the internal data (*self.__matcher*).
        """
        return type(self.__matcher).__new__(self.__matcher.onset(),
                                            self.__matcher.nucleus(), True)

    
