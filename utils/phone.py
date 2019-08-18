

####################################################################
#
#
#
#     The Imports
#
#

import re as __re
from io import StringIO as __stringIO


####################################################################
#
#
#
#     Some Abstract Phonological Utility functions and their data...
#      - this is just a better place to stash them for now...
#        their imports ( re and io ) are above...
#

def __get_phoneme():
    return __re.compile(r"/(\S{1,3}?)/")

__phoneme = __get_phoneme()

def __get_exact_phone():
    return __re.compile(r"\[(\S{1,3}?)\]")

__exact_phone = __get_exact_phone()

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
    
