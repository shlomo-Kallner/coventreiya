
from nucleus import Nucleus
from nucleus import register
from coventreiya.utils.fsm import fsm_state
from coventreiya.phonology.vowels import Vowels
from coventreiya.phonology.vowels.ver_1_5_9 import ver_1_5_9 as vols_ver
from coventreiya.phonology.vowels import Height, Backness, Rounding, Nasality



#

class ver_1_5_7( Nucleus ):
    __doc__ = "The THEORETICAL version 1.5.7 Maximum using phonology 1.5.9!!!. "
    def __init__(self, vols_=vols_ver):
        min_length = 1
        max_length = 4
        if issubclass(vols_, Vowels):
            self.__vols_ = vols_()
        else:
            raise TypeError()
        super().__init__(min_length, max_length, 1,5,7)

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
        ## getting the "Sign Symbols"..
        tmp0 = self.__vols_.get_phone(Height.Mid_, Backness.Central_,
                             Rounding.Unrounded_, Nasality.Non_Nasal_)
        tmp01 = list(self.__vols_.phoneme_matcher()[tmp0])
        cat_[0].extend(tmp01)
        ## getting the "Index Separator"...
        tmp1 = self.__vols_.get_phone(Height.Near_Close_, Backness.Near_Front_,
                             Rounding.Unrounded_, Nasality.Non_Nasal_)
        tmp11 = list(self.__vols_.phoneme_matcher()[tmp1])
        tmp11.remove(tmp1)
        cat_[0].extend(tmp11)
        # cat_[1] is V1
        cat_[1].extend(self.__vols_.exact_phones())
        ## removing the "Index Separator" and the "Sign Symbols" from V1..
        for i in cat_[0]:
            cat_[1].remove(i)
        return cat_

    def replacment_map(self):
        ''' Generate the Replacement Map. '''
        cat_ = self.categories()
        return { 0 : cat_[0],
                 1 : cat_[1] }

    

def gen_ver_1_5_7():
    return ver_1_5_7()

nuc_ = register( ver_1_5_7(), gen_ver_1_5_7 )


