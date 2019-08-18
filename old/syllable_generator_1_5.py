
from __future__ import unicode_literals
from enum import Enum, IntEnum, unique
import json



# Phonology

stop = [ "m", "n", "ŋ" , "b", "d", "ɡ" , "p", "t", "k", "q" ]
glottal_stop = [ "ʔ" ]


affricate = [ "d͡z", "d͡ʒ" , "t͡s", "t͡ʃ" ]


sibilant_fricative = [ "z", "ʒ" , "s", "ʃ" , "ɬ" , "ɮ" ]
non_sibilant_fricative = [ "f", "v", "θ", "ð", "x", "χ", 
                           "ħ", "ʕ", "h" ]
rhotic_fricative = [ "ɣ", "ʁ", "ɹ̠" ]

def gen_fric_():
    """ 18 consonants """
    fric_ = list(sibilant_fricative)
    fric_.extend(non_sibilant_fricative)
    fric_.extend(rhotic_fricative)
    return fric_


semi_vowel = [ "w", "ʋ", "ð̞", "j" ]
rhotic_approximant = [ "ɰ", "ɹ̠" ]
onset_approximant_ext = [ "l" , "ʍ" , "ʕ̞" ]
coda_approximant_ext = [ "ɫ" ]

def gen_onset_appr_():
    on_appr_ = list(semi_vowel)
    on_appr_.extend(rhotic_approximant)
    on_appr_.extend(onset_approximant_ext)
    return on_appr_

def gen_coda_appr_():
    co_appr_ = list(semi_vowel)
    co_appr_.extend(coda_approximant_ext)
    return co_appr_


trill = [ "r", "ʀ" ]


ejective = [ "pʼ" , "ť" , "kʼ" , "qʼ" , "tsʼ" , "t͡ʃʼ" ,
             "fʼ" , "θʼ" , "sʼ" , "ʃʼ" , "x’" , "χ’" ]

# Affricate - Fricative matching dictionaries

affr_fric_match = { "d͡z": "z", "d͡ʒ": "ʒ", "t͡s": "s", "t͡ʃ": "ʃ" }
stop_affr_match = { "d͡z": "d", "d͡ʒ": "d", "t͡s": "t", "t͡ʃ": "t" }



# Phonotactics
#
#   The new (Version 1.5) Onset Phonotactics are:
#   
#   ( { Fricative ,  Affricate ,  Ejective } ) >>
#   { Stop , Fricative , Affricate , Ejective , Trill ,
#     Onset_Approximant , Glottal_stop } >>
#   ( { Stop , Fricative , Affricate , Ejective , Trill ,
#     Onset_Approximant , Glottal_stop } ) >>
#   ( { Rhotic_Approximant , "l" } ) >>
#   ( Semi_Vowel ( >> Semi_Vowel ) ) >>
#   ( "ʕ̞" )
#
#   or:  "(C2)C1(C1)(C3)(S(S))('ʕ̞')"  where:
#
#   C2 = { Fricative ,  Affricate ,  Ejective };
#   C1 = { Stop , Fricative , Affricate , Ejective , Trill ,
#          Onset_Approximant , Glottal_stop };
#   C3 = { Rhotic_Approximant , "l" };
#   S  = Semi_Vowel ;
#
#   The Options would therefore be:
#
#   Actual_Onset_Pattern  | (C2) | C1  | (C1) | (C3) | (S  | (S)) |('ʕ̞') |
#-------------------------|------|-----|------|------|-----|------|-------|
#             1           |      |  Y  |      |      |     |      |       |
#             2           |      |  Y  |  Y   |      |     |      |       |
#             3           |  Y   |  Y  |      |      |     |      |       |
#             4           |      |  Y  |      |  Y   |     |      |       |
#             5           |      |  Y  |      |      |  Y  |      |       |
#             6           |      |  Y  |      |      |  Y  |  Y   |       |
#             7           |      |  Y  |      |      |     |      |   Y   |
#-------------------------|------|-----|------|------|-----|------|-------|
#             8           |  Y   |  Y  |  Y   |      |     |      |       |
#             9           |  Y   |  Y  |      |  Y   |     |      |       |
#            10           |  Y   |  Y  |      |      |  Y  |      |       |
#            11           |  Y   |  Y  |      |      |  Y  |  Y   |       |
#            12           |  Y   |  Y  |      |      |     |      |   Y   |
#-------------------------|------|-----|------|------|-----|------|-------|  
#            13           |      |  Y  |  Y   |  Y   |     |      |       |
#            14           |      |  Y  |  Y   |      |  Y  |      |       |
#            15           |      |  Y  |  Y   |      |  Y  |  Y   |       |
#            16           |      |  Y  |  Y   |      |     |      |   Y   |
#-------------------------|------|-----|------|------|-----|------|-------|  
#            17           |  Y   |  Y  |      |  Y   |  Y  |      |       |
#                         |      |  Y  |      |  Y   |  Y  |      |       |
#            18           |      |  Y  |      |  Y   |  Y  |  Y   |       |
#            19           |      |  Y  |      |  Y   |     |      |   Y   |
#-------------------------|------|-----|------|------|-----|------|-------|  
#            20           |      |  Y  |      |      |  Y  |      |   Y   |
#            21           |      |  Y  |      |      |  Y  |  Y   |   Y   |
#-------------------------|------|-----|------|------|-----|------|-------|
#                         |      |     |      |      |     |      |       |
#   Actual_Onset_Pattern  | (C2) | C1  | (C1) | (C3) | (S  | (S)) |('ʕ̞') |
#-------------------------|------|-----|------|------|-----|------|-------|
#            22           |      |  Y  |  Y   |  Y   |     |      |       |
#            23           |  Y   |  Y  |  Y   |  Y   |     |      |       |
#            24           |      |  Y  |  Y   |  Y   |  Y  |      |       |
#            25           |      |  Y  |  Y   |  Y   |  Y  |  Y   |       |
#            26           |      |  Y  |  Y   |  Y   |     |      |   Y   |
#-------------------------|------|-----|------|------|-----|------|-------|
#            27           |  Y   |  Y  |  Y   |  Y   |  Y  |      |       |
#            28           |  Y   |  Y  |  Y   |  Y   |  Y  |  Y   |       |
#            29           |  Y   |  Y  |  Y   |  Y   |     |      |   Y   |
#-------------------------|------|-----|------|------|-----|------|-------|
#            30           |  Y   |  Y  |  Y   |  Y   |  Y  |      |   Y   |
#            31           |  Y   |  Y  |  Y   |  Y   |  Y  |  Y   |   Y   |
#                         |      |  Y  |      |      |     |      |       |
#
#
#
#
#
#
#

def gen_onset_c1():
    """ __ consonants """
    c1_ = list(stop)
    c1_.extend(gen_fric_())
    c1_.extend(affricate)
    c1_.extend(gen_onset_appr_())
    c1_.extend(trill)
    c1_.extend(ejective)
    return c1_

def gen_onset_c2():
    """ __ consonants """
    c2_ = list(gen_fric_())
    c2_.extend(affricate)
    c2_.extend(ejective)
    return c2_

def gen_onset_c3():
    """ __ consonants """
    c3_ = list(rhotic_approximant)
    c3_.extend(onset_approximant_ext)
    return c3_

def get_max_num_onsets():
    """The absolute maximum number of onsets."""
    """ based on the numbers above, should equal to __ ... """
    # "(C2)C1(C1)(C3)(S(S))('ʕ̞')"
    c1 = len(gen_onset_c1())
    c2 = len(gen_onset_c2())
    c3 = len(gen_onset_c3_c4())
    s1 = len(semi_vowel)
    s2 = 2
    temp = c1                                     # C1
    temp = temp + ( c1 * c2 )                     # C2 >> C1
    temp = temp + ( c1 * c3 )                     # C1 >> C3
    temp = temp + ( c1 * c1 )                     # C1 >> C1
    temp = temp + ( c1 * c1 * c3 )
    temp = temp + ( c1 * c2 * c3 )
    temp = temp + ( c1 * c1 * c2 * c3 )
    temp = temp + ( c1 * c1 * c2 * c3 * s1 )
    temp = temp + ( c1 * c1 * c2 * c3 * s1 * s1 )
    temp = temp + ( c1 * c1 * c2 * c3 * s1 * s1 )
    
    
    
    temp = temp + ( c1 * c3 * c4 )
    temp = temp + ( c1 * c2 * c3 * c4 )
    return temp

def gen_all_Onsets():
    """ Onsets are (C2)C1(C3(C4)). """
    """  C1 = A Fricative, an Affricate, an Ejective, a Stop, an Approximant, a Tap or a Trill; """
    """  C2 = A Fricative, an Affricate  or an Ejective; """
    """  C3 = An Approximant, a Tap or a Trill; """
    """  C4 = An Approximant, a Tap or a Trill that isn`t C3; """
    all_onsets_ = list()
    
    c1 = gen_onset_c1()
    c2 = gen_onset_c2()
    c3 = gen_onset_c3_c4()
    c4 = gen_onset_c3_c4()

    # first gen all C1 possibilities
    for i0 in range(0, len(c1)):
        all_onsets_.append(tuple(c1[i0]))

    # now gen all C2C1 possibilities
    for i1 in range(0, len(c1)):
        for i2 in range(0, len(c2)):
            t1 = tuple( c2[i2], c1[i1] )
            if t1 not in all_onsets_:
                all_onsets_.append(t1)

    # now gen all C1C3 possibilities
    for i1 in range(0, len(c1)):
        for i3 in range(0, len(c3)):
            t2 = tuple( c1[i1], c3[i3] )
            if t2 not in all_onsets_:
                all_onsets_.append(t2)
    
    # now gen all C1C3C4 possibilities
    for i1 in range(0, len(c1)):
        for i3 in range(0, len(c3)):
            for i4 in range(0, len(c4)):
                t3 = tuple( c1[i1], c3[i3], c4[i4] )
                if t3 not in all_onsets_:
                    all_onsets_.append(t3)
    
    # now gen all C2C1C3 possibilities
    for i1 in range(0, len(c1)):
        for i2 in range(0, len(c2)):
            for i3 in range(0, len(c3)):
                t4 = tuple( c2[i2], c1[i1], c3[i3] )
                if t4 not in all_onsets_:
                    all_onsets_.append(t4)
                    
    # now gen all C2C1C3C4 possibilities
    for i1 in range(0, len(c1)):
        for i2 in range(0, len(c2)):
            for i3 in range(0, len(c3)):
                for i4 in range(0, len(c4)):
                    t5 = tuple( c2[i2], c1[i1], c3[i3], c4[i4] )
                    if t5 not in all_onsets_:
                       all_onsets_.append(t5)
    return all_onsets_

def gen_nucleus():
    """ Nucleuses are (V(V(V))). """
    """  """
    pass
    


def open_syllable ( onset, nucleus ):
    if onset is None or isinstance(onset,vowel):
        raise ValueError
    yield onset
    yield nucleus

def closed_syllable ( onset, nucleus, coda ):
    if onset is None or isinstance(onset,vowel)\
       or coda is None or isinstance(coda,vowel):
        raise ValueError
    yield from onset
    yield from nucleus
    yield from coda

# Root or Word Stem generation ...

def word_stem( variant, root, crypto ):
    stem = None
    var_list = []
    var_list_no_crypto = []
    if variant == 1:
        stem = None
    pass
