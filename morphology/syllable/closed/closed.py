##################################################################
#
# Imports
#

from coventreiya.utils.ver import ver
from coventreiya.utils.ver import gen_ver
from coventreiya.utils.ver import Version_Registry

from coventreiya.phonotactics.onsets import Onsets as __Onsets_abc
from coventreiya.phonotactics.nucleus import Nucleus as __Nucleus_abc
from coventreiya.phonotactics.codas import Codas as __Codas_abc

from coventreiya.morphology.syllable import Syllable

##################################################################
#
# Morphology  -  Closed Syllables
#

class Closed(Syllable):
    def __init__(self, onset_=None, nucleus_=None, coda_=None,
                 onset_mat=None, nucleus_mat=None, coda_mat=None,
                 major=0, minor=0, patch=0, version=None):
        super().__init__(has_onset=True, has_nucleus=True, has_coda=True,
                       major, minor, patch, version)
        if issubclass(onset_mat, __Onsets_abc):
            self.__onset_mat = onset_mat()
        else:
            raise TypeError()
        if issubclass(nucleus_mat, __Nucleus_abc):
            self.__nucleus_mat = nucleus_mat()
        else:
            raise TypeError()
        if issubclass(coda_mat,__Codas_abc):
            self.__coda_mat = coda_mat()
        else:
            raise TypeError()
        if self.__onset_mat.is_allowable_input(onset_):
            # by the way, this means that *onset_* is a list of strings..
            self.__onset = onset_
        else:
            raise ValueError("*onset_* must be a list of strings!")
        if self.__nucleus_mat.is_allowable_input(nucleus_):
            # and the same with *nucleus_*...
            self.__nucleus = nucleus_
        else:
            raise ValueError("*nucleus_* must be a list of strings!")
        if self.__coda_mat.is_allowable_input(coda_):
            # and with *coda_*!!!
            self.__coda = coda_
        else:
            raise ValueError("*coda_* must be a list of strings!")

    def get_onset(self):
        return self.__onset
        
    def get_onset_matcher(self):
        return self.__onset_mat
        
    def get_nucleus(self):
        return self.__nucleus

    def get_nucleus_matcher(self):
        return self.__nucleus_mat 

    def get_coda(self):
        ''' Closed Syllables *have* Codas. '''
        return self.__coda

    def get_coda_matcher(self):
        return self.__coda_mat

    

###################################################################################
#
#   Version Information Control & UnExported [but Versioned] Object Instantiation
#

__versions = Version_Registry(Closed())

def register( version, functor ):
    if isinstance( version, Closed ):
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

