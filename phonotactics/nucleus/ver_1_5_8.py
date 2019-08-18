
from nucleus import Nucleus
from nucleus import register
from coventreiya.utils.fsm import fsm_state
from coventreiya.phonology.vowels import Vowels
from coventreiya.phonology.vowels.ver_1_5_9 import ver_1_5_9 as vols_ver
from coventreiya.phonology.vowels.Vowels import Height, Backness, Rounding, Nasality

#########################################################################################

class ver_1_5_8( Nucleus ):
    __doc__ = "The phonotactics used by Morphosyntax version 1.3.5 ."
    def __init__(self, vols_=vols_ver):
        min_length = 1
        max_length = 4
        if issubclass(vols_, Vowels):
            self.__vols_ = vols_()
        else:
            raise TypeError()
        super().__init__(min_length, max_length,1,5,8)

    def finite_state_machine(self):
        """ Generates the full Finite State Machine """
        """ and returns it and the Starting State as a Tuple. """
        # setting up the Finite State Machine for parsing...
        # for parse string "(S)V1(V1)(V1)"
        # will be using:
        # 1 for S
        # 2 for V1
        # in the generator.
        fsm_ = [ fsm_state(str(x),False) for x in range(0,6) ]
        fsm_[0].remap(False, {1 : fsm_[0],
                              2 : fsm_[0]} )
        fsm_[1].remap(False, {1 : fsm_[2],
                              2 : fsm_[3]} )
        fsm_[2].remap(False, {1 : fsm_[0],
                              2 : fsm_[3]} )
        fsm_[3].remap(True,  {1 : fsm_[0],
                              2 : fsm_[4]} )
        fsm_[4].remap(True,  {1 : fsm_[0],
                              2 : fsm_[5]} )
        fsm_[5].remap(True,  {1 : fsm_[0],
                              2 : fsm_[0]} )
        raise tuple( fsm_, fsm_[1] )

    def categories(self):
        ''' Generate the Categories Lists. '''
        # setting up the Finite State Machine for parsing...
        # for parse string "(S)V1(V1)(V1)"
        # will be using:
        # 1 for S
        # 2 for V1
        # in the generator.
        cat_ = [ list() for x in range(0,2) ]
        # cat_[0] is S
        tmp = self.__vols_.get_phone(Height.Mid_,
                              Backness.Central_,
                              Rounding.Unrounded_)
        cat_[0].append(tmp)
        # cat_[1] is V1
        cat_[1].extend(self.__vols_.phonemes())
        cat_[1].remove(tmp)
        return cat_

    def replacment_map(self):
        ''' Generate the Replacement Map. '''
        cat_ = self.categories()
        return { 0 : cat_[0],
                 1 : cat_[1] }


def gen_ver_1_5_8():
    return ver_1_5_8()

nuc_ = register( ver_1_5_8(), gen_ver_1_5_8 )
