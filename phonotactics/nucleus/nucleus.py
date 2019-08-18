
__name__ = 'nucleus'

########################################################
#
#
#   Imports
#
#

from coventreiya.utils.ver import ver
from coventreiya.utils.ver import gen_ver
from coventreiya.utils.ver import Version_Registry
from coventreiya.phonotactics.abc import abc

########################################################
#
#
#   Codas the ABC for Generating the Nucleus of Syllables...
#
#

class Nucleus(abc):
    def __init__(self, min_length=0, max_length=0, 
                 major=0, minor=0, patch=0, version=None):
        super().__init__(min_length, max_length, 
                         major, minor, patch, version)
        pass
    
    
    
################################################################################
#
# Version Information Control & UnExported [but Versioned] Object Instantiation
#
#

__versions = Version_Registry( Nucleus() )

def register( version, functor ):
    if isinstance( version, Nucleus ):
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

    
