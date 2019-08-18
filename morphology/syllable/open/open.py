##################################################################
#
# Imports
#

from coventreiya.utils.ver import ver
from coventreiya.utils.ver import gen_ver
from coventreiya.utils.ver import Version_Registry

from coventreiya.phonotactics.onsets import Onsets as __Onsets_abc
from coventreiya.phonotactics.nucleus import Nucleus as __Nucleus_abc

from coventreiya.morphology.syllable import Syllable

##################################################################
#
# Morphology  -  Open Syllables
#

class Open(Syllable):
    def __init__(self, onset_=None, nucleus_=None, has_null_vowel=False,
                 onset_mat=None, nucleus_mat=None,
                 major=0, minor=0, patch=0, version=None):
        super().__init__(has_onset=True, has_nucleus=True, has_coda=False,
                       major=0, minor=0, patch=0, version=None)
        if issubclass(onset_mat, __Onsets_abc):
            self.__onset_mat = onset_mat()
        else:
            raise TypeError()
        if issubclass(nucleus_mat, __Nucleus_abc):
            self.__nucleus_mat = nucleus_mat()
        else:
            raise TypeError()
        self.__has_null_vowel = bool(has_null_vowel)
        if self.__onset_mat.is_allowable_input(onset_):
            # by the way, this means that *onset_* is a list of strings..
            self.__onset = onset_
        else:
            raise ValueError("*onset_* must be a list of strings!")
        if self.__nucleus_mat.is_allowable_input(nucleus_):
            # and the same with *nucleus_*...
            self.__nucleus = nucleus_
        elif self.__has_null_vowel:
            # special case for Affixes...
            #  in which if the nucleus is invalid - set null.
            tmp = list()
            tmp.append("")
            self.__nucleus = tmp
        else:
            raise ValueError("*nucleus_* must be a list of strings!")

    def get_onset(self):
        return self.__onset
        
    def get_onset_matcher(self):
        return self.__onset_mat
        
    def get_nucleus(self):
        return self.__nucleus

    def get_nucleus_matcher(self):
        return self.__nucleus_mat

    def has_null_vowel(self):
        if isinstance(self.__nucleus, list) \
           and len(self.__nucleus) == 1 \
           and self.__nucleus[0] == "" \
           and self.__has_null_vowel:
            return True
        else:
            return False

    def get_coda(self):
        ''' Open Syllables do not have Codas so,
            return an empty list.'''
        return list()

    def get_coda_matcher(self):
        ''' Open Syllables do not have Codas so,
            return None.'''
        return None

    
###################################################################################
#
#   Version Information Control & UnExported [but Versioned] Object Instantiation
#

__versions = Version_Registry(Open())

def register( version, functor ):
    if isinstance( version, Open ):
        return __versions.register( version, functor )
    else:
        raise TypeError()

def get_version(major=0, minor=0, patch=0, version=None):
    return __versions.get( major, minor, patch, version )

def gen_version( major=0, minor=0, patch=0, version=None, **kw ):
    return __versions.gen( major, minor, patch, version, kw )

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

