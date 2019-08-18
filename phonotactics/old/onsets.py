

__name__ = 'onsets'
__version__ = '1.5.1'
__package__ = 'phonotactics'

# imports

#some import machinery checking and manipulations...
import sys
import os
from os import path
if '__file__' in dir():
    __mod_path = path.dirname(__file__)
    if __mod_path not in sys.path:
        sys.path.append(__mod_path)
    __pack_path = path.dirname(__mod_path)
    if __pack_path not in sys.path:
        sys.path.append(__pack_path)
    

from coventreiya.utils.ver import ver
from coventreiya.utils.ver import gen_ver
from coventreiya.utils.ver import Version_Registry
from coventreiya.utils.fsm import fsm_state, fsm_transversal
from coventreiya.utils import lists
from coventreiya.utils import gen
from coventreiya.phonology import consonants
from coventreiya.phonotactics.abc import abc



# generator functions

########################################################
#
#
#   Generating the Onsets
#
#

class Onsets:
    def __init__(self, ver_major=0, ver_minor=0, ver_patch=0,
                 min_length=0, max_length=0, version=None):
        self.__version = gen_ver(ver_major,ver_minor,ver_patch,version)
        self.__length = tuple([min_length,max_length])
        tmp = self.__finite_state_machine()
        self.__fsm = tmp[0]
        self.__fsm_start = tmp[1]
        self.__cat = self.__categories()
        self.__repl_map = self.__replacment_map()
    
    def version(self):
        return self.__version

    def min_length(self):
        return self.__length[0]

    def max_length(self):
        return self.__length[1]

    def finite_state_machine(self):
        ''' Returns the Finite State Machine's Start State '''
        return self.__fsm_start

    def categories(self):
        return self.__cat

    def replacment_map(self):
        return self.__repl_map

    def __finite_state_machine(self):
        """ Generates the full Finite State Machine """
        """ and returns it and the Starting State as a Tuple. """
        raise NotImplementedError

    def __categories(self):
        ''' Generate the Categories Lists. '''
        raise NotImplementedError

    def __replacment_map(self):
        ''' Generate the Replacement Map. '''
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

    def is_allowable_onset( self, onset_ ):
        """ checking that (onset_) is a list of """
        """ consonants that form a valid onset """
        tmp = self.all_allowable_sets_()
        repl_map = self.replacment_map()
        sets_ = list()
        for i in tmp:
            if len(i) == len(onset_):
                sets_.append(i)
        allowing_sets = 0
        for i in sets_:
            boll1 = True
            for j in range(0,len(onset_)):
                if onset_[j] not in repl_map[i[j]]:
                    boll1 = False
            if boll1:
                allowing_sets += 1
        return allowing_sets != 0


class ver_1_5_1( Onsets ):
    def __init__(self):
        min_length = 1
        max_length = 7
        super().__init__(1,5,1,min_length,max_length)
    
    def __finite_state_machine(self):
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
        return tuple(fsm_,fsm_[1])

    def __categories(self):
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
        cat_[0].extend(cons_.all_ejectives_())
        cat_[0].extend(cons_.onset_approximant_())
        cat_[0].extend(cons_.glottal_stop_())
        cat_[0].extend(cons_.trill_())
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
        cat_[4].extend(cons_.pharyngeal_approximant_())
        return cat_

    def __replacment_map(self):
        cat_ = self.categories()
        return { 0 : cat_[0],
                 1 : cat_[1],
                 2 : cat_[2],
                 3 : cat_[3],
                 4 : cat_[4] }


class ver_1_5_5( Onsets ):
    def __init__(self):
        min_length = 1
        max_length = 7
        super().__init__(1,5,5,min_length,max_length)
    
    def __finite_state_machine(self):
        # for parse string:
        # "(C3) >> (C2) >> C1 >> (C4) >> (C5 >> (C5)) >> (C6)"
        # will be using:
        # 0 for C1
        # 1 for C2
        # 2 for C3
        # 3 for C4
        # 4 for C5
        # 5 for C6
        # in the generator.
        fsm_ = [ fsm_state(str(x),False) for x in range(0,10) ]
        fsm_[0].remap(False, {0 : fsm_[0],
                              1 : fsm_[0],
                              2 : fsm_[0],
                              3 : fsm_[0],
                              4 : fsm_[0],
                              5 : fsm_[0]} )
        fsm_[1].remap(False, {0 : fsm_[4],
                              1 : fsm_[2],
                              2 : fsm_[3],
                              3 : fsm_[0],
                              4 : fsm_[0],
                              5 : fsm_[0]} )
        fsm_[2].remap(False, {0 : fsm_[4],
                              1 : fsm_[0],
                              2 : fsm_[0],
                              3 : fsm_[0],
                              4 : fsm_[0],
                              5 : fsm_[0]} )
        fsm_[3].remap(False, {0 : fsm_[4],
                              1 : fsm_[2],
                              2 : fsm_[0],
                              3 : fsm_[0],
                              4 : fsm_[0],
                              5 : fsm_[0]} )
        fsm_[4].remap(True,  {0 : fsm_[6],
                              1 : fsm_[6],
                              2 : fsm_[6],
                              3 : fsm_[5],
                              4 : fsm_[7],
                              5 : fsm_[9]} )
        fsm_[5].remap(True,  {0 : fsm_[6],
                              1 : fsm_[6],
                              2 : fsm_[6],
                              3 : fsm_[6],
                              4 : fsm_[7],
                              5 : fsm_[9]} )
        fsm_[6].remap(False, {0 : fsm_[6],
                              1 : fsm_[6],
                              2 : fsm_[6],
                              3 : fsm_[6],
                              4 : fsm_[6],
                              5 : fsm_[6]} )
        fsm_[7].remap(True,  {0 : fsm_[6],
                              1 : fsm_[6],
                              2 : fsm_[6],
                              3 : fsm_[6],
                              4 : fsm_[8],
                              5 : fsm_[9]} )
        fsm_[8].remap(True,  {0 : fsm_[6],
                              1 : fsm_[6],
                              2 : fsm_[6],
                              3 : fsm_[6],
                              4 : fsm_[6],
                              5 : fsm_[9]} )
        fsm_[9].remap(True,  {0 : fsm_[0],
                              1 : fsm_[0],
                              2 : fsm_[0],
                              3 : fsm_[0],
                              4 : fsm_[0],
                              5 : fsm_[0]} )
        return tuple(fsm_,fsm_[1])

    def __categories(self):
        # for parse string:
        # "(C3) >> (C2) >> C1 >> (C4) >> (C5 >> (C5)) >> (C6)"
        # will be using:
        # 0 for C1
        # 1 for C2
        # 2 for C3
        # 3 for C4
        # 4 for C5
        # 5 for C6
        # in the generator.
        cons_ = consonants.ver_1_5_5()
        cat_ = [ list() for x in range(0,6) ]
        # cat_[0] is onset_c1
        cat_[0].extend(cons_.stops_())
        cat_[0].extend(cons_.fricatives_())
        cat_[0].extend(cons_.all_ejectives_())
        cat_[0].extend(cons_.onset_approximant_())
        cat_[0].extend(cons_.glottal_stop_())
        cat_[0].extend(cons_.trill_())
        # cat_[1] is onset_c2
        cat_[1].extend(cons_.stops_())
        cat_[1].extend(cons_.fricatives_())
        cat_[1].extend(cons_.all_ejectives_())
        cat_[1].extend(cons_.onset_approximant_())
        cat_[1].extend(cons_.trill_())
        # cat_[2] is onset_c3
        cat_[2].extend(cons_.fricatives_())
        cat_[2].extend(cons_.all_ejectives_())
        # cat_[3] is onset_c4
        cat_[3].extend(cons_.rhotic_approximant_())
        cat_[3].extend(cons_.onset_latteral_approximant_ext_())
        # cat_[4] is onset_c5 
        cat_[4].extend(cons_.semi_vowel_())
        # cat_[5] is onset_c6
        cat_[5].extend(cons_.pharyngeal_approximant_())
        return cat_

    def __replacment_map(self):
        cat_ = self.categories()
        return { 0 : cat_[0],
                 1 : cat_[1],
                 2 : cat_[2],
                 3 : cat_[3],
                 4 : cat_[4],
                 5 : cat_[5] }



__current_version_used = ver_1_5_1()

def reset_current_version( version=None , major=None, minor=None, patch=None ):
    if isinstance( version, Onsets ):
        __current_version_used = version
    elif isinstance(major,int)and isinstance(minor,int)and isinstance(patch,int):
        if major == 1 and minor == 5 :
            if patch == 1:
                __current_version_used = ver_1_5_1()
            elif patch == 5:
                __current_version_used = ver_1_5_5()
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
    return __current_version_used.all_allowable_sets_()

def gen_c1():
    c1_ = list()
    c1_.extend(__current_version_used.categories()[0])
    return c1_

def gen_c2():
    c2_ = list()
    c2_.extend(__current_version_used.categories()[1])
    return c2_

def gen_c3():
    c3_ = list()
    c3_.extend(__current_version_used.categories()[2])
    return c3_

def gen_c4():
    c4_ = list()
    c4_.extend(__current_version_used.categories()[3])
    return c4_

def gen_c5():
    c5_ = list()
    c5_.extend(__current_version_used.categories()[4])
    return c5_

def gen_actual_():
    """ WARNING!!! this fuction uses A LOT of memory """
    """  and may crash python!!!"""
    return __current_version_used.all_actuals()

def gen_actual1_():
    """ WARNING!!! this fuction uses A LOT of memory """
    """  and may crash python!!!"""
    return __current_version_used.all_actuals()

def gen_actual_file_(path, encoding_='utf-8'):
    return __current_version_used.all_actuals_to_file(path, encoding_)

# gen_actual_file(list_, repl_map, path, encoding_='utf-8')
def gen_actual_file1_(path, encoding_='utf-8'):
    return __current_version_used.all_actuals_to_file(path, encoding_)

