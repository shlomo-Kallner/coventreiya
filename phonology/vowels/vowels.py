
__name__ = "vowels"
# __version__ = "1.5.4"


##################################################################
#
# Imports
#

from enum import Enum

from coventreiya.utils.ver import ver
from coventreiya.utils.ver import gen_ver
from coventreiya.utils.ver import Version_Registry

from coventreiya.phonology.abc import abc

from abc import ABCMeta, abstractmethod

##################################################################
#
# Phonology  -  Vowels
#

class Vowels(abc):
    def __init__(self, major=0, minor=0, patch=0, version=None):
        #self.__actual_phones_matrix = self.__actual_phones()
        super().__init__(major, minor, patch, version)

    @abstractmethod
    def phonemes(self):
        """ Returns a (list) of (str) containing *ALL* legit phonemes.
            Note: all must be present in the phoneme matcher dictionary."""
        pass

    @abstractmethod
    def exact_phones(self):
        """ Returns a (list) of (str) containing *ALL* legit exact phones.
            Note: all must be present in the phoneme matcher dictionary.
            AND in the exact Phone Matcher.
            Note: includes all ALLOPHONES!
        """
        pass

    @abstractmethod
    def exact_phone_matcher(self):
        """ Returns a (dict) of (str) whose keys are exact phones
            and whose items are the associated phonemes.
        """
        pass

    @abstractmethod
    def phoneme_matcher(self):
        """ Returns a (dict) of (str) whose keys are phonemes
            and whose item are lists of it's key's actualization phones.
            (actualization phones => A.K.A "ALLOPHONES"!)
        """
        pass

    @abstractmethod
    def actual_phones(self):
        """ A mapping of the Phonemes used to
            Height, Backness, Rounding, Nasality for use with get_phone().
        """
        pass

    @abstractmethod
    def get_phone(self, height=0, back=0, rounding=0, nasality=0):
		""" Get a (exact) Vowel based on it's phonetic value/name. """
        pass

    #def actual_phones(self):
    #    return self.__actual_phones_matrix

    class Height(int, Enum):
        Min_ = 0
        Close_ = 0
        Near_Close_ = 1
        Close_Mid_ = 2
        Mid_ = 3
        Open_Mid_ = 4
        Near_Open_ = 5
        Open_ = 6
        Max_ = 6

    class Backness(int, Enum):
        Min_ = 0
        Front_ = 0
        Near_Front_ = 1
        Central_ = 2
        Near_Back_ = 3
        Back_ = 4
        Max_ = 4

    class Rounding(int, Enum):
        Min_ = 0
        Unrounded_ = 0
        Rounded_ = 1
        Max_ = 1

    class Nasality(int, Enum):
        Min_ = 0
        Non_Nasal_ = 0
        Nasal_ = 1
        Max_ = 1

    
###################################################################################
#
#   Version Information Control & UnExported [but Versioned] Object Instantiation
#

__versions = Version_Registry(Vowels())

def register( version, functor ):
    if isinstance( version, Vowels ):
        return __versions.register( version, functor )
    else:
        raise TypeError()

def get_version(major=0, minor=0, patch=0, version=None):
    return __versions.get( major, minor, patch, version )

def gen_version( major=0, minor=0, patch=0, version=None ):
    return __versions.gen( major, minor, patch, version )

def get_all_versions():
    return list(__versions)
        
###################################################################################
#
#    Getting/Setting the default/current version...
#    

def get_current():
    return __versions.current()

def get_current_version():
    return __versions.current().version()

def reset_current_version( major=0, minor=0, patch=0, version=None ):
    v = gen_ver(major, minor, patch, version)
    return __versions.current(v)


###################################################################################
#
#    The original default version -- used for the (now obsolete and removed) 
#        "default" gen_*_ functions and the pre-generated lists...
#    
#    Note: the *COMPATABILITY_ONLY* default gen_*_ functions will self-update to
#        accomidate resets (they call into *THE_CURRENT_VERSION_OBJECT*!!)
#        the PRE-GENERATED LISTS will not be updated at all..
#    Note: Using version 1.5.4 as it will be the last version supporting outright
#        the gen_*_ functions below..
#    Note: VERSION 2_0: the *OLD* gen_*_ functions no longer self-update as they are
#        now directly linked to version 1.5.4 only.
#
# from ver_1_5_4 import *
#__versions.current(gen_ver(1,5,4))


