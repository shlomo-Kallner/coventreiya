##################################################################
#
# Imports
#

from coventreiya.phonotactics.onsets.ver_1_5_7 import ver_1_5_7 as __onset_mat
from coventreiya.phonotactics.nucleus.ver_1_5_7 import ver_1_5_7 as __nucleus_mat

from coventreiya.morphology.syllable.open import Open, register
##################################################################
#
# Morphology  -  Open Syllables - according to Morphology 1.3.5
#

class ver_1_3_5(Open):
    def __init__(self, onset_=None, nucleus_=None, has_null_vowel=False):
        onset_mat = __onset_mat()
        nucleus_mat = __nucleus_mat()
        super().__init__(onset_, nucleus_, has_null_vowel,
                         onset_mat,nucleus_mat,1,3,5,None)

    pass

# The function signiture of these two no longer make any sense do to
#   the Ctor parameter list above...

def gen_ver_1_3_5(**kw):
    return ver_1_3_5(onset_=kw["onset_"], nucleus_=kw["nucleus_"],
                     has_null_vowel=kw["has_null_vowel"])

opn_ = register( ver_1_3_5(), gen_ver_1_3_5 )
