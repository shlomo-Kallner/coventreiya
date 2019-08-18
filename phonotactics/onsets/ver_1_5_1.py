

from onsets import Onsets
from onsets import register

from coventreiya.phonology.consonants.ver_1_5_4 import ver_1_5_4
from coventreiya.utils.fsm import fsm_state

class ver_1_5_1( Onsets ):
    def __init__(self):
        min_length = 1
        max_length = 7
        super().__init__(min_length,max_length,1,5,1)
    
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
        return tuple(fsm_,fsm_[1])

    def categories(self):
        # for parse string "(C2)  C1  (C1) (C3) (S   (S)) ('ʕ̞')"
        # will be using:
        # 0 for C1
        # 1 for C2
        # 2 for C3
        # 3 for S
        # 4 for 'ʕ̞'
        # in the generator.
        cons_ = ver_1_5_4()
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

    def replacment_map(self):
        cat_ = self.categories()
        return { 0 : cat_[0],
                 1 : cat_[1],
                 2 : cat_[2],
                 3 : cat_[3],
                 4 : cat_[4] }

def gen_ver_1_5_1():
    return ver_1_5_1()

ons_ = register( ver_1_5_1(), gen_ver_1_5_1 )

##################################################################################
#
#    The OLD *DEPRECEATED* "default" gen_*_ functions ...
#      
#

def gen_():
    return ons_.all_allowable_sets_()

def gen_c1():
    c1_ = list()
    c1_.extend(ons_.categories()[0])
    return c1_

def gen_c2():
    c2_ = list()
    c2_.extend(ons_.categories()[1])
    return c2_

def gen_c3():
    c3_ = list()
    c3_.extend(ons_.categories()[2])
    return c3_

def gen_c4():
    c4_ = list()
    c4_.extend(ons_.categories()[3])
    return c4_

def gen_c5():
    c5_ = list()
    c5_.extend(ons_.categories()[4])
    return c5_

def gen_actual_():
    """ WARNING!!! this fuction uses A LOT of memory """
    """  and may crash python!!!"""
    return ons_.all_actuals()

def gen_actual1_():
    """ WARNING!!! this fuction uses A LOT of memory """
    """  and may crash python!!!"""
    return ons_.all_actuals()

def gen_actual_file_(path, encoding_='utf-8'):
    return ons_.all_actuals_to_file(path, encoding_)

def gen_actual_file1_(path, encoding_='utf-8'):
    return ons_.all_actuals_to_file(path, encoding_)


