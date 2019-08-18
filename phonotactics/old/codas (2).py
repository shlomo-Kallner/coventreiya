

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
    

from coventreiya.utils.fsm import fsm_state, fsm_transversal
from coventreiya.utils import lists
from coventreiya.utils import gen
from coventreiya.phonology import consonants

########################################################
#
#
#   Generating the Codas
#
#

class Codas:
    def __init__(self, major=0, minor=0, patch=0):
        self.__version = tuple([major,minor,patch])
    
    def version(self):
        return self.__version

    def finite_state_machine(self):
        """ Generates the full Finite State Machine """
        """ and returns the Starting State. """
        raise NotImplementedError 

    def min_length(self):
        raise NotImplementedError 

    def max_length(self):
        raise NotImplementedError 

    def categories(self):
        raise NotImplementedError 

    def replacment_map(self):
        raise NotImplementedError 

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
    c1 = gen_coda_c1()
    c2 = gen_coda_c2()
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

