##################################################################
#
# Imports
#

from coventreiya.phonotactics.onsets.ver_1_5_7 import ver_1_5_7 as __onset_mat
from coventreiya.phonotactics.nucleus.ver_1_5_7 import ver_1_5_7 as __nucleus_mat
from coventreiya.phonotactics.codas.ver_1_5_7 import ver_1_5_7 as __coda_mat

from coventreiya.morphology.syllable.closed import Closed, register
##################################################################
#
# Morphology  -  Closed Syllables - according to Morphology 1.3.5
#

class ver_1_3_5(Closed):
    def __init__(self, onset_=None, nucleus_=None, coda_=None):
        onset_mat = __onset_mat()
        nucleus_mat = __nucleus_mat()
        coda_mat = __coda_mat()
        super().__init__(onset_, nucleus_, coda_,
                         onset_mat,nucleus_mat,coda_mat,
                         1,3,5,None)

    pass

# The function signiture of these two no longer make any sense do to
#   the Ctor parameter list above...

def gen_ver_1_3_5(**kw):
    return ver_1_3_5(onset_=kw["onset_"], nucleus_=kw["nucleus_"], 
                     coda_=kw["coda_"])

clos_ = register( ver_1_3_5(), gen_ver_1_3_5 )
