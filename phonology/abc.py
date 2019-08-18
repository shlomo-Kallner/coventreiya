

__name__ = 'coventreiya.phonology.abc'

####################################################################
#
#
#
#     The Imports
#
#

from coventreiya.utils.ver import Versioned

import re as __re
from io import StringIO as __stringIO
from abc import ABCMeta, abstractmethod

####################################################################
#
#
#
#     The Abstract Base Class for all Phonological sub-Classes
#
#

class abc(Versioned, metaclass=ABCMeta):
    
    def __init__(self, major=0, minor=0, patch=0, version=None):
        super().__init__(major, minor, patch, version)
        #self.__phonemes_dict = self.__phoneme_matcher()
        #self.__phonemes_list = self.__phonemes()
        #self.__exact_phones_list = self.__exact_phones()
        #self.__exact_phones_dict = self.__exact_phone_matcher()

    @abstractmethod
    def phoneme_matcher(self):
        """ Returns a (dict) of (str) whose keys are phonemes
            and whose item are lists of it's key's actualization phones.
            (actualization phones => A.K.A "ALLOPHONES"!)
        """
        return self.__phonemes_dict

    @abstractmethod
    def exact_phone_matcher(self):
        """ Returns a (dict) of (str) whose keys are exact phones
            and whose items are the associated phonemes.
        """
        return self.__exact_phones_dict

    @abstractmethod
    def phonemes(self):
        """ Returns a (list) of (str) containing *ALL* legit phonemes.
            Note: all must be present in the phoneme matcher dictionary."""
        return self.__phonemes_list

    @abstractmethod
    def exact_phones(self):
        """ Returns a (list) of (str) containing *ALL* legit exact phones.
            Note: all must be present in the phoneme matcher dictionary.
            AND in the exact Phone Matcher.
            Note: includes all ALLOPHONES!
        """
        return self.__exact_phones_list

    def is_phoneme(self, str_):
        """ The input must be a String, Raises a TypeError Exception otherwise.
            Returns True if input matches the realization of a phoneme.
            Else Returns False.
        """
        if isinstance(str_, str):
            return str_ in self.phonemes()
        else:
            raise TypeError()

    def is_exact_phone(self, str_):
        """ The input must be a String, Raises a TypeError Exception otherwise.
            Returns True if input matches the realization of an exact sound.
            Else Returns False. 
        """
        if isinstance(str_, str):
            return str_ in self.exact_phones()
        else:
            raise TypeError()

    

####################################################################
#
#
#
#     Some Abstract Phonological Utility functions and their data...
#      - this is just a better place to stash them for now...
#        their imports ( re and io ) are above...
#

__phoneme = __re.compile(r"/(\S{1,3}?)/") 
__exact_phone = __re.compile(r"\[(\S{1,3}?)\]") 

# Note: the numbers in the re parsers above ("1,3") are for individual IPA symbols
#       being represented, not for full-out IPA Character Stream/String parsing.
    
def is_str_phoneme(str_):
    """ Checks the input str_ if it has the marking of phonemes ("/").
        If it has the marking of an exact phone ("[" and "]") it will return false.
        The input must be a String, Raises a TypeError Exception otherwise.
        Returns True if input is written as the realization of a phoneme.
        Returns False if input is written as an exact sound.
        Raises a ValueError Exception if not of the above two options...
    """
    if isinstance(str_, str):
        #phoneme = re.compile(r"(/)(\S{1,3}?)(/)").fullmatch(str_)
        #exact_phone = re.compile(r"(\[)(\S{1,3}?)(\])").fullmatch(str_)
        phoneme = __phoneme.fullmatch(str_)
        exact_phone = __exact_phone.fullmatch(str_)
        # assumption: str_ is a "phone" from one of the "gen" functions of the derived types
        #             of the ABC above.
        # (I know they don't have "gen" in their names... look at the compatability functions....
        if phoneme:  # "/" in str_ and str_.count("/") == 2:
            return True
        elif exact_phone: # "[" in str_ and "]" is str_:
            return False
        else:
            raise ValueError()
    else:
        raise TypeError()

def get_phonetic_symbol(str_):
    """ Extracts the phonetic symbols of the Individual Symbol inputted
        --- one Symbol (excepting Symbol modifiers and for Africates)
        per str_ input to this function
        --- without the slashes or the brackets. """
    if isinstance(str_, str):
        if __phoneme.fullmatch(str_):
            return __phoneme.sub(r"\1", str_)
        elif __exact_phone.fullmatch(str_):
            return __exact_phone.sub(r"\1", str_)
        else:
            raise ValueError()
    else:
        raise TypeError()

def to_phoneme(str_, upto=3):
    """
       Takes a bare IPA letter-set and surrounds it with the Phoneme marking.
       If *upto* is left to default, at 3, the result will be compatible with
       the stripping func above and will issue a ValueError for any length
       longer than it. Set to 0 to disregard string length.
    """
    if isinstance(str_, str) and isinstance(upto, int):
        if upto > 0 and len(str_) > upto:
            raise ValueError()
        strm = __stringIO("/")
        strm.write(str_)
        strm.write("/")
        return strm.getvalue()
    else:
        raise TypeError()

def to_exact_phone(str_, upto=3):
    """
       Takes a bare IPA letter-set and surrounds it with Exact Phone marking.
       If *upto* is left to default, at 3, the result will be compatible with
       the stripping func above and will issue a ValueError for any length
       longer than it. Set to 0 to disregard string length.
    """
    if isinstance(str_, str) and isinstance(upto, int):
        if upto > 0 and len(str_) > upto:
            raise ValueError()
        strm = __stringIO("[")
        strm.write(str_)
        strm.write("]")
        return strm.getvalue()
    else:
        raise TypeError()
    
        
            
        
    
