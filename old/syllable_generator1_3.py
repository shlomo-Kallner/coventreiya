
from __future__ import unicode_literals
from enum import Enum, IntEnum, unique
import json



null = None

# Phonology

nasal_stop = [ "m", "n", "ɲ", "ŋ" ]
voiced_stop = [ "b", "d", "ɟ", "ɡ" ]
unvoiced_stop = [ "p", "t", "c", "k", "q", "ʔ" ]

voiced_sibilant_affricate = [ "d͡z", "d͡ʒ" ]
unvoiced_sibilant_affricate = [ "t͡s", "t͡ʃ" ]
unvoiced_non_sibilant_affricate = [ "p̪͡f", "k͡x", ]

voiced_sibilant_fricative = [ "z", "ʒ" ] 
unvoiced_sibilant_fricative = [ "s", "ʃ" ]
voiced_non_sibilant_fricative = [ "β", "v", "ð", "ʝ", "ɣ", "ʁ", "ʕ" ]
unvoiced_non_sibilant_fricative = [ "ɸ", "f", "θ", "ç", "x", "χ", "ħ", "h" ]

affr_fric_match = { "d͡z": "z", "d͡ʒ": "ʒ", "t͡s": "s", "t͡ʃ": "ʃ", "p̪͡f": "f", "k͡x": "x" }
stop_affr_match = { "d͡z": "d", "d͡ʒ": "d", "t͡s": "t", "t͡ʃ": "t", "p̪͡f": "p", "k͡x": "k" }

voiced_approximant = [ "w", "β̞", "ʋ", "ð̞", "ɹ", "ɹ̠", "ɻ", "j", "ɰ", "ʁ̞", "ʕ̞", "ɥ" ]
unvoiced_approximant = [ "ʍ" ]

voiced_tap = [ "ɾ", "ɢ̆" ]
                    
voiced_trill = [ "r", "ʀ" ]
unvoiced_trill = [ "ʀ̥" ]

voiced_lateral_approximant = [ "l", "ʎ", "ɫ" ]

unvoiced_ejective_stop = [ "pʼ", "ť", "kʼ" ]
unvoiced_ejective_affricate = [ "tsʼ", "t͡ʃʼ" ]

# in all 65 (counted) consonants!

# Phonotactics
def gen_stops():
    """ 14 consonants , not including the ejective stops """
    stop_ = list(nasal_stop)
    stop_.extend(voiced_stop)
    stop_.extend(unvoiced_stop)
    return stop_

def gen_affr_():
    """ 6 consonants , not including the ejective affricates """
    affr_ = list(voiced_sibilant_affricate)
    affr_.extend(unvoiced_sibilant_affricate)
    affr_.extend(unvoiced_non_sibilant_affricate)
    return affr_

def gen_fric_():
    """ 19 consonants """
    fric_ = list(voiced_sibilant_fricative)
    fric_.extend(unvoiced_sibilant_fricative)
    fric_.extend(voiced_non_sibilant_fricative)
    fric_.extend(unvoiced_non_sibilant_fricative)
    return fric_

def gen_appr_():
    """ 16 consonants """
    appr_ = list(voiced_approximant)
    appr_.extend(unvoiced_approximant)
    appr_.extend(voiced_lateral_approximant)
    return appr_

def gen_trill():
    """ 3 consonants """
    trll_ = list(voiced_trill)
    trll_.extend(unvoiced_trill)
    return trll_

def gen_ejec_():
    """ 5 consonants """
    ejec_ = list(unvoiced_ejective_stop)
    ejec_.extend(unvoiced_ejective_affricate)
    return ejec_

def gen_onset_c1():
    """ 65 consonants """
    c1_ = list(gen_stops())
    c1_.extend(gen_affr_())
    c1_.extend(gen_fric_())
    c1_.extend(gen_appr_())
    c1_.extend(voiced_tap)
    c1_.extend(gen_trill())
    c1_.extend(gen_ejec_())
    return c1_

def gen_onset_c2():
    """ 30 consonants """
    c2_ = list(gen_fric_())
    c2_.extend(gen_affr_())
    c2_.extend(gen_ejec_())
    return c2_

def gen_onset_c3_c4():
    """ 21 consonants """
    c_ = list(gen_appr_())
    c_.extend(voiced_tap)
    c_.extend(gen_trill())
    return c_

def get_max_num_onsets():
    """The absolute maximum number of onsets."""
    """ based on the numbers above, should equal to 932945... """
    c1 = len(gen_onset_c1())
    c2 = len(gen_onset_c2())
    c3 = len(gen_onset_c3_c4())
    c4 = len(gen_onset_c3_c4())
    temp = c1
    temp = temp + ( c1 * c2 )
    temp = temp + ( c1 * c3 )
    temp = temp + ( c1 * c2 * c3 )
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
