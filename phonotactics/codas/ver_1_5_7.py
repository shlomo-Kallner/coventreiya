
from codas import Codas
from codas import register
from coventreiya.utils.fsm import fsm_state
from coventreiya.phonology.consonants import ver_1_5_9 as cons_ver

class ver_1_5_7( Codas ):
    def __init__(self):
        min_length = 1
        max_length = 5
        super().__init__(min_length, max_length,1,5,7)

    def finite_state_machine(self):
        """ Generates the full Finite State Machine """
        """ and returns it and the Starting State as a Tuple. """
        # setting up the Finite State Machine for parsing...
        # for parse string "(S)(C2)C1(C1)(C1)"
        # will be using:
        # 1 for C1
        # 2 for C2
        # 3 for S
        # in the generator.
        fsm_ = [ fsm_state(str(x),False) for x in range(0,7) ]
        fsm_[0].remap(False, {1 : fsm[1],
                             2 : fsm[2],
                             3 : fsm[3]} )
        fsm_[1].remap(False, {1 : fsm[6],
                             2 : fsm[2],
                             3 : fsm[3]} )
        fsm_[2].remap(False, {1 : fsm[6],
                             2 : fsm[6],
                             3 : fsm[3]} )
        fsm_[3].remap(True,  {1 : fsm[6],
                             2 : fsm[6],
                             3 : fsm[4]} )
        fsm_[4].remap(True,  {1 : fsm[6],
                             2 : fsm[6],
                             3 : fsm[5]} )
        fsm_[5].remap(True,  {1 : fsm[6],
                             2 : fsm[6],
                             3 : fsm[6]} )
        fsm_[6].remap(False, {1 : fsm[6],
                             2 : fsm[6],
                             3 : fsm[6]} )
        return tuple(fsm_, fsm_[0])

    def categories(self):
        ''' Generate the Categories Lists. '''
        # setting up the Finite State Machine for parsing...
        # for parse string "(S)(C2)C1(C1)(C1)"
        # will be using:
        # 1 for C1
        # 2 for C2
        # 3 for S
        # in the generator.
        cons_ = cons_ver()
        cat_ = [ list() for x in range(0,3) ]
        # cat_[0] is C1
        cat_[0].extend(cons_.stops_())
        cat_[0].extend(cons_.all_fricatives_())
        cat_[0].extend(cons_.coda_approximant_())
        cat_[0].extend(cons_.trill_())
        # cat_[1] is C2
        cat_[1].extend(cons_.rhotic_approximant_())
        cat_[1].extend(cons_.coda_approximant_ext_())
        # cat_[2] is S
        cat_[2].extend(cons_.semi_vowel_())
        return cat_

    def replacment_map(self):
        ''' Generate the Replacement Map. '''
        cat_ = self.categories()
        return { 0 : cat_[0],
                 1 : cat_[1],
                 2 : cat_[2] }

def gen_ver_1_5_7():
    return ver_1_5_7()

cod_ = register( ver_1_5_7(), gen_ver_1_5_7 )

