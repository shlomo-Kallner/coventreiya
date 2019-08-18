

__name__ = 'codas'
#__version = '1.5.1"
#__package__ = 'phonotactics'


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
from coventreiya.utils.fsm import fsm_state, fsm_transversal
from coventreiya.utils import lists
from coventreiya.utils import gen
from coventreiya.phonology import consonants
from coventreiya.phonotactics.abc import abc


########################################################
#
#
#   Generating the Codas
#
#

class Codas(abc):
    def __init__(self, major=0, minor=0, patch=0,
                 min_length=0, max_length=0, version=None):
        super().__init__(self, major, minor, patch,
                         min_length, max_length, version)
        pass
    
    
    
################################################################################
#
# Version Information Control & UnExported [but Versioned] Object Instantiation
#
#

__versions = Version_Registry( Codas() )

def register( version, functor ):
    if isinstance( version, Codas ):
        return __versions.register( version, functor )
    else:
        raise TypeError()

def get_version(major=0, minor=0, patch=0, version=None):
    return __versions.get( major, minor, patch, version )

def gen_version( major=0, minor=0, patch=0, version=None ):
    return __versions.gen( major, minor, patch, version )

###################################################################################
#
#    The default version -- used for the default gen_*_ functions ...
#        and the pre-generated lists...
#    Note: the *COMPATABILITY_ONLY* default gen_*_ functions will self-updated to
#        accomidate resets (they call into *THE_CURRENT_VERSION_OBJECT*!!)
#        the PRE-GENERATED LISTS will not be updated at all..
#

def get_current():
    return __versions.current()

def get_current_version():
    return __versions.current().version()

def reset_current_version( major=0, minor=0, patch=0, version=None ):
    v = gen_ver(major, minor, patch, version)
    return __versions.current(v)

import ver_1_5_1
__versions.current(gen_ver(1,5,1))
    
########################################################
#
#
#     The Backwards Compatability Functions
#
#

def gen_():
    # setting up the Finite State Machine for parsing...
    # for parse string "(S)(C2)C1(C1)(C1)"
    # will be using:
    # 1 for C1
    # 2 for C2
    # 3 for S
    # in the generator.
    fsm = [ fsm_state(str(x),False) for x in range(0,7) ]
    fsm[0].remap(False, {1 : fsm[1],
                         2 : fsm[2],
                         3 : fsm[3]} )
    fsm[1].remap(False, {1 : fsm[6],
                         2 : fsm[2],
                         3 : fsm[3]} )
    fsm[2].remap(False, {1 : fsm[6],
                         2 : fsm[6],
                         3 : fsm[3]} )
    fsm[3].remap(True,  {1 : fsm[6],
                         2 : fsm[6],
                         3 : fsm[4]} )
    fsm[4].remap(True,  {1 : fsm[6],
                         2 : fsm[6],
                         3 : fsm[5]} )
    fsm[5].remap(True,  {1 : fsm[6],
                         2 : fsm[6],
                         3 : fsm[6]} )
    fsm[6].remap(False, {1 : fsm[6],
                         2 : fsm[6],
                         3 : fsm[6]} )
    t = gen.gen_list( 5 , [1,2,3] , 1 )
    results = list()
    for i in t:
        if fsm_transversal( i, fsm[0] ):
            results.append(i)
    return results

########################################################
#
#           Actual Codas Generation Functions
#
#

def gen_c1():
    """ __ consonants """
    c1_ = list()
    c1_.extend(stop)
    c1_.extend(gen_fric_())
    c1_.extend(affricate)
    c1_.extend(gen_coda_appr_())
    c1_.extend(trill)
    return c1_

def gen_c2():
    c2_ = list()
    c2_.extend(rhotic_approximant)
    c2_.extend(coda_approximant_ext)
    return c2_


def gen_actual_():
    """ WARNING!!! this fuction may use A LOT of memory """
    """  and may crash python!!!"""
    results = list()
    c1 = gen_c1()
    c2 = gen_c2()
    s = semi_vowel
    t = gen_codas()
    # for parse string "(S)(C2)C1(C1)"
    # will be using:
    # 1 for C1
    # 2 for C2
    # 3 for S
    # in the generator.
    repl_map = { 1 : c1,
                 2 : c2,
                 3 : s }
    for i in t:
        j = gen_replace_str1( i, repl_map )
        results.extend(j)
    return results

# gen_actual(t, repl_map)
def gen_actual1_():
    """ WARNING!!! this fuction may use A LOT of memory """
    """  and may crash python!!!"""
    c1 = gen_coda_c1()
    c2 = gen_coda_c2()
    t = gen_codas()
    # for parse string "(S)(C2)C1(C1)"
    # will be using:
    # 1 for C1
    # 2 for C2
    # 3 for S
    # in the generator.
    repl_map = { 1 : c1,
                 2 : c2,
                 3 : semi_vowel }
    return gen_actual(t, repl_map)


def gen_actual_file_(path, encoding_='utf-8'):
    results = 0
    f = open(path, "w", encoding=encoding_)
    c1 = gen_coda_c1()
    c2 = gen_coda_c2()
    t = gen_codas()
    # for parse string "(S)(C2)C1(C1)"
    # will be using:
    # 1 for C1
    # 2 for C2
    # 3 for S
    # in the generator.
    repl_map = { 1 : c1,
                 2 : c2,
                 3 : semi_vowel }
    for i in t:
        t1 = gen_replace_str1( i, repl_map )
        for j in t1:
            print(j, file=f)
            results += 1
    return results

# gen_actual_file(list_, repl_map, path, encoding_='utf-8')
def gen_actual_file1_(path, encoding_='utf-8'):
    c1 = gen_coda_c1()
    c2 = gen_coda_c2()
    t = gen_codas()
    # for parse string "(S)(C2)C1(C1)"
    # will be using:
    # 1 for C1
    # 2 for C2
    # 3 for S
    # in the generator.
    repl_map = { 1 : c1,
                 2 : c2,
                 3 : semi_vowel }
    return gen_actual_file(t, repl_map, path, encoding_)

