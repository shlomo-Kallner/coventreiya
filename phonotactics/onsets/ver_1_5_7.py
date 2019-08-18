
from onsets import Onsets
from onsets import register

from coventreiya.phonology.consonants.ver_1_5_9 import ver_1_5_9 as cons_ver
from coventreiya.utils.fsm import fsm_state

class ver_1_5_7( Onsets ):
    def __init__(self):
        min_length = 1
        max_length = 7
        super().__init__(min_length,max_length,1,5,7)
    
    def finite_state_machine(self):
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

    def categories(self):
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
        cons_ = cons_ver()
        cat_ = [ list() for x in range(0,6) ]
        # cat_[0] is onset_c1
        cat_[0].extend(cons_.stops_())
        cat_[0].extend(cons_.all_fricatives_())
        cat_[0].extend(cons_.all_ejectives_())
        cat_[0].extend(cons_.onset_approximant_())
        cat_[0].extend(cons_.glottal_stop_())
        cat_[0].extend(cons_.trill_())
        # cat_[1] is onset_c2
        cat_[1].extend(cons_.stops_())
        cat_[1].extend(cons_.all_fricatives_())
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

    def replacment_map(self):
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
        cat_ = self.categories()
        return { 0 : cat_[0],
                 1 : cat_[1],
                 2 : cat_[2],
                 3 : cat_[3],
                 4 : cat_[4],
                 5 : cat_[5] }

def gen_ver_1_5_7(**kw):
    return ver_1_5_7()

ons_ = register( ver_1_5_7(), gen_ver_1_5_7 )



