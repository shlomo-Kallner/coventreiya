

__name__ = 'onsets'
__version__ = '1.5.1'
__package__ = 'phonotactics'

# imports

#some import machinery checking and manipulations...
import sys
import os
from os import path
__mod_path = path.dirname(__file__)
if __mod_path not in sys.path:
    sys.path.append(__mod_path)
    

import utils
from utils.fsm import fsm_state, fsm_transversal
from utils import lists
from utils import gen
import phonology
from phonology import consonants

# generator functions

########################################################
#
#
#   Generating the Onsets
#
#

class Onsets:
    def __init__(self, major=0, minor=0, patch=0):
        self.__version = tuple(major,minor,patch)
    
    def version(self):
        return self.__version

    def finite_state_machine(self):
        return NotImplemented

    def min_length(self):
        return NotImplemented

    def max_length(self):
        return NotImplemented

    def categories(self):
        return NotImplemented

    def replacment_map(self):
        return NotImplemented

    def num_categories(self):
        return len(self.categories())

    def all_allowable_sets_(self):
        fsm_ = self.finite_state_machine()
        t = gen.gen_list( self.max_length() ,
                          [ x for x in range(0,self.num_categories()) ] ,
                          self.min_length() )
        results = list()
        for i in t:
            if fsm_transversal( i, fsm_ ):
                results.append(i)
        return results

    def actuals_per_set(self, set_):
        repl_map = self.replacment_map()
        return gen.gen_replace_str1( set_, repl_map )

    def actuals_per_set_to_file(self, set_, path, encoding_='utf-8'):
        repl_map = self.replacment_map()
        return gen.gen_replace_str_to_file( set_, repl_map, path, encoding_ )

    def all_actuals(self):
        t = self.all_allowable_sets_()
        repl_map = self.replacment_map()
        return gen.gen_actual(t, repl_map)

    def all_actuals_to_file(self, path, encoding_='utf-8'):
        t = self.all_allowable_sets_()
        repl_map = self.replacment_map()
        return gen.gen_actual_file(t, repl_map, path, encoding_)


class ver_1_5_1( Onsets ):
    def __init__(self):
        super().__init__(1,5,1)
    
    def finite_state_machine(self):
        fsm_ = [ fsm_state(str(x),False) for x in range(0,10) ]
        fsm_[0].remap(False, {0 : fsm_[0],
                              1 : fsm_[0],
                              2 : fsm_[0],
                              3 : fsm_[0],
                              4 : fsm_[0]} )
        fsm_[1].remap(False, {0 : fsm_[2],
                              1 : fsm_[3],
                              2 : fsm_[0],
                              3 : fsm_[0],
                              4 : fsm_[0]} )
        fsm_[2].remap(True,  {0 : fsm_[4],
                              1 : fsm_[6],
                              2 : fsm_[5],
                              3 : fsm_[7],
                              4 : fsm_[9]} )
        fsm_[3].remap(False, {0 : fsm_[2],
                              1 : fsm_[0],
                              2 : fsm_[0],
                              3 : fsm_[0],
                              4 : fsm_[0]} )
        fsm_[4].remap(True,  {0 : fsm_[6],
                              1 : fsm_[6],
                              2 : fsm_[5],
                              3 : fsm_[7],
                              4 : fsm_[9]} )
        fsm_[5].remap(True,  {0 : fsm_[0],
                              1 : fsm_[0],
                              2 : fsm_[0],
                              3 : fsm_[7],
                              4 : fsm_[9]} )
        fsm_[6].remap(False, {0 : fsm_[6],
                              1 : fsm_[6],
                              2 : fsm_[6],
                              3 : fsm_[6],
                              4 : fsm_[6]} )
        fsm_[7].remap(True,  {0 : fsm_[6],
                              1 : fsm_[6],
                              2 : fsm_[6],
                              3 : fsm_[8],
                              4 : fsm_[9]} )
        fsm_[8].remap(True,  {0 : fsm_[6],
                              1 : fsm_[6],
                              2 : fsm_[6],
                              3 : fsm_[6],
                              4 : fsm_[9]} )
        fsm_[9].remap(True,  {0 : fsm_[0],
                              1 : fsm_[0],
                              2 : fsm_[0],
                              3 : fsm_[0],
                              4 : fsm_[0]} )
        return fsm_[1]

    def min_length(self):
        return 1

    def max_length(self):
        return 7

    def categories(self):
        # for parse string "(C2)  C1  (C1) (C3) (S   (S)) ('ʕ̞')"
        # will be using:
        # 0 for C1
        # 1 for C2
        # 2 for C3
        # 3 for S
        # 4 for 'ʕ̞'
        # in the generator.
        cons_ = consonants.ver_1_5_4()
        cat_ = [ list() for x in range(0,5) ]
        # cat_[0] is onset_c1
        cat_[0].extend(cons_.stops_())
        cat_[0].extend(cons_.fricatives_())
        cat_[0].extend(cons_.affricates_())
        cat_[0].extend(cons_.onset_approximant_())
        cat_[0].extend(cons_.trill_())
        cat_[0].extend(cons_.all_ejectives_())
        # cat_[1] is onset_c2
        cat_[1].extend(cons_.fricatives_())
        cat_[1].extend(cons_.affricates_())
        cat_[1].extend(cons_.all_ejectives_())
        # cat_[2] is onset_c3
        cat_[2].extend(cons_.rhotic_approximant_())
        cat_[2].extend(cons_.onset_latteral_approximant_ext_())
        # cat_[3] is onset_c4 or "(S)"
        cat_[3].extend(cons_.semi_vowel_())
        # cat[4] is onset_c5 or 'ʕ̞'
        return cat_

    def replacment_map(self):
        { 1 : c1,
          2 : c2,
          3 : c3,
          4 : s,
          5 : [ "ʕ̞" ] }
        return NotImplemented

    


__current_version_used = ver_1_5_1()

def reset_current_version( version=None , major=None, minor=None, patch=None ):
    if isinstance( version, Consonants ):
        __current_version_used = version
    elif isinstance(major,int)and isinstance(minor,int)and isinstance(patch,int):
        if major == 1 and minor == 5 :
            if patch == 1:
                __current_version_used = ver_1_5_1()
            else:
                raise ValueError()
        else:
            raise ValueError()
    else:
        raise TypeError()
    
def get_current():
    return __current_version_used

def get_current_version():
    return __current_version_used.version()

#################################################################
#
#
#   the old functions for compatibility...
#
#


def gen_():
    # setting up the Finite State Machine for parsing...
    # for parse string "(C2)  C1  (C1) (C3) (S   (S)) ('ʕ̞')"
    # will be using:
    # 1 for C1
    # 2 for C2
    # 3 for C3
    # 4 for S
    # 5 for 'ʕ̞'
    # in the generator.
    fsm_ = [ fsm_state(str(x),False) for x in range(0,10) ]
    fsm_[0].remap(False, {1 : fsm_[0],
                         2 : fsm_[0],
                         3 : fsm_[0],
                         4 : fsm_[0],
                         5 : fsm_[0]} )
    fsm_[1].remap(False, {1 : fsm_[2],
                         2 : fsm_[3],
                         3 : fsm_[0],
                         4 : fsm_[0],
                         5 : fsm_[0]} )
    fsm_[2].remap(True,  {1 : fsm_[4],
                         2 : fsm_[6],
                         3 : fsm_[5],
                         4 : fsm_[7],
                         5 : fsm_[9]} )
    fsm_[3].remap(False, {1 : fsm_[2],
                         2 : fsm_[0],
                         3 : fsm_[0],
                         4 : fsm_[0],
                         5 : fsm_[0]} )
    fsm_[4].remap(True,  {1 : fsm_[6],
                         2 : fsm_[6],
                         3 : fsm_[5],
                         4 : fsm_[7],
                         5 : fsm_[9]} )
    fsm_[5].remap(True,  {1 : fsm_[0],
                         2 : fsm_[0],
                         3 : fsm_[0],
                         4 : fsm_[7],
                         5 : fsm_[9]} )
    fsm_[6].remap(False, {1 : fsm_[6],
                         2 : fsm_[6],
                         3 : fsm_[6],
                         4 : fsm_[6],
                         5 : fsm_[6]} )
    fsm_[7].remap(True,  {1 : fsm_[6],
                         2 : fsm_[6],
                         3 : fsm_[6],
                         4 : fsm_[8],
                         5 : fsm_[9]} )
    fsm_[8].remap(True,  {1 : fsm_[6],
                         2 : fsm_[6],
                         3 : fsm_[6],
                         4 : fsm_[6],
                         5 : fsm_[9]} )
    fsm_[9].remap(True,  {1 : fsm_[0],
                         2 : fsm_[0],
                         3 : fsm_[0],
                         4 : fsm_[0],
                         5 : fsm_[0]} )
    #      "(C2)  C1  (C1) (C3) (S   (S)) ('ʕ̞')"
    # in the generator:
    # 1 for C1
    # 2 for C2
    # 3 for C3
    # 4 for S
    # 5 for 'ʕ̞'
    t = gen.gen_list( 7 , [1,2,3,4,5] , 1 )
    results = list()
    for i in t:
        if fsm_transversal( i, fsm_[1] ):
            results.append(i)
    return results

########################################################
#
#           Actual Onsets Generation Functions
#
#

def gen_c1():
    """ __ consonants """
    c1_ = list()
    c1_.extend(stop)
    c1_.extend(gen_fric_())
    c1_.extend(affricate)
    c1_.extend(gen_onset_appr_())
    c1_.extend(trill)
    c1_.extend(ejective)
    return c1_

def gen_c2():
    """ __ consonants """
    c2_ = list()
    c2_.extend(gen_fric_())
    c2_.extend(affricate)
    c2_.extend(ejective)
    return c2_

def gen_c3():
    """ __ consonants """
    c3_ = list()
    c3_.extend(rhotic_approximant)
    c3_.extend(onset_approximant_ext)
    return c3_

def gen_actual_():
    """ WARNING!!! this fuction uses A LOT of memory """
    """  and may crash python!!!"""
    results = list()
    c1 = gen_c1()
    c2 = gen_c2()
    c3 = gen_c3()
    t = gen_()
    s = semi_vowel
    # in the generator:
    # 1 for C1
    # 2 for C2
    # 3 for C3
    # 4 for S
    # 5 for 'ʕ̞'
    repl_map = { 1 : c1,
                 2 : c2,
                 3 : c3,
                 4 : s,
                 5 : [ "ʕ̞" ] }
    for i in t:
        j = gen.gen_replace_str1( i, repl_map )
        results.extend(j)
    return results


def gen_actual1_():
    """ WARNING!!! this fuction uses A LOT of memory """
    """  and may crash python!!!"""
    c1 = gen_c1()
    c2 = gen_c2()
    c3 = gen_c3()
    t = gen_()
    # in the generator:
    # 1 for C1
    # 2 for C2
    # 3 for C3
    # 4 for S
    # 5 for 'ʕ̞'
    repl_map = { 1 : c1,
                 2 : c2,
                 3 : c3,
                 4 : semi_vowel,
                 5 : [ "ʕ̞" ] }
    return gen_actual(t, repl_map)


def gen_actual_file_(path, encoding_='utf-8'):
    results = 0
    f = open(path, "w", encoding=encoding_)
    c1 = gen_c1()
    c2 = gen_c2()
    c3 = gen_c3()
    t = gen_()
    # in the generator:
    # 1 for C1
    # 2 for C2
    # 3 for C3
    # 4 for S
    # 5 for 'ʕ̞'
    repl_map = { 1 : c1,
                 2 : c2,
                 3 : c3,
                 4 : semi_vowel,
                 5 : [ "ʕ̞" ] }
    for i in t:
        t1 = gen.gen_replace_str1( i, repl_map )
        for j in t1:
            print(j, file=f)
            results += 1
    return results

# gen_actual_file(list_, repl_map, path, encoding_='utf-8')
def gen_actual_file1_(path, encoding_='utf-8'):
    c1 = gen_c1()
    c2 = gen_c2()
    c3 = gen_c3()
    t = gen_()
    # in the generator:
    # 1 for C1
    # 2 for C2
    # 3 for C3
    # 4 for S
    # 5 for 'ʕ̞'
    repl_map = { 1 : c1,
                 2 : c2,
                 3 : c3,
                 4 : semi_vowel,
                 5 : [ "ʕ̞" ] }
    return gen.gen_actual_file(t, repl_map, path, encoding_)
