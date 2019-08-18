

__name__ = 'onsets'
__version__ = '1.5.1'
__package__ = 'phonotactics'

# imports

#some import machinery checking and manipulations...
#import sys
#import os
#from os import path
#if '__file__' in dir():
#    __mod_path = path.dirname(__file__)
#    if __mod_path not in sys.path:
#        sys.path.append(__mod_path)
#    __pack_path = path.dirname(__mod_path)
#    if __pack_path not in sys.path:
#        sys.path.append(__pack_path)
    

from coventreiya.utils.ver import ver
from coventreiya.utils.ver import gen_ver
from coventreiya.utils.ver import Version_Registry
from coventreiya.phonotactics.abc import abc

########################################################
#
#
#   Generating the Onsets
#
#

class Onsets(abc):
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

__versions = Version_Registry( Onsets() )

def register( version, functor ):
    if isinstance( version, Onsets ):
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
#    The original default version -- used for the(now obsolete and removed) 
#        "default" gen_*_ functions and the pre-generated lists...
#    Note: the *COMPATABILITY_ONLY* default gen_*_ functions will self-update to
#        accomidate resets (they call into *THE_CURRENT_VERSION_OBJECT*!!)
#        the PRE-GENERATED LISTS will not be updated at all..
#    Note: VERSION 2_0: the *OLD* gen_*_ functions no longer self-update as 
#        they are now directly linked to version 1.5.1 only.
#
# from ver_1_5_1 import *
# __versions.current(gen_ver(1,5,1))
    
