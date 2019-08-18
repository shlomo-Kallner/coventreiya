
from __future__ import unicode_literals
from enum import Enum, IntEnum, unique
import json



null = None

# Phonology

class vowel(Enum):
    pass

class semi_vowel(Enum):
    pass

class consonant(Enum):
    pass

nasal_stop = [ "m", "n", "ɲ", "ŋ" ]
voiced_stop = [ "b", "d", "ɟ", "ɡ" ]
unvoiced_stop = [ "p", "t", "c", "k", "q", "ʔ" ] 
voiced_sibilant_fricative = [ "z", "ʒ" ] 
unvoiced_sibilant_fricative = [ "s", "ʃ" ]
voiced_sibilant_affricate = [ "d͡z", "d͡ʒ" ]
unvoiced_sibilant_affricate = [ "t͡s", "t͡ʃ" ]
unvoiced_non_sibilant_affricate = [ "p̪͡f", "k͡x", ]
voiced_non_sibilant_fricative = [ "β", "v", "ð", "ʝ", "ɣ", "ʁ", "ʕ" ]
unvoiced_non_sibilant_fricative = [ "ɸ", "f", "θ", "ç", "x", "χ", "ħ", "h" ]
voiced_approximant = [ "w", "β̞", "ʋ", "ð̞", "ɹ", "ɹ̠", "ɻ", "j", "ɰ", "ʁ̞", "ʕ̞", "ɥ" ]
unvoiced_approximant = [ "ʍ" ]
voiced_tap = [ "ɾ", "ɢ̆" ]
voiced_trill = [ "r", "ʀ" ]
unvoiced_trill = [ "ʀ̥" ]
voiced_lateral_approximant = [ "l", "ʎ", "ɫ" ]
unvoiced_ejective_stop = [ "pʼ", "ť", "kʼ" ]
unvoiced_ejective_affricate = [ "tsʼ", "t͡ʃʼ" ]


# Phonotactics

Onset = lambda Con1, Con2, Con3, Sem1, Sem2 : pass
Nucleus = lambda Vow1 : pass
Coda = lambda Con1, Con2, Con3 : pass

def gen_Onsets(g2,g3,g3):
    """ Onsets are (C2)C1(C3(C4)). """
    """  C1 = A Fricative, an Affricate, a Stop, an Approximant, a Tap or a Trill; """
    """  C2 = A Fricative, an Affricate  or an Ejective; """
    """  C3 = An Approximant, a Tap or a Trill; """
    """  C4 = An Approximant, a Tap or a Trill that isn`t C3; """
    all_onsets_ = list()
    fric_ = list()
    affr_ = list()
    stop_ = list()
    appr_ = list()
    tap_  = list()
    trll_ = list()
    
    if g2 == True:
        #gen C2
        pass
    # gen C1
        for i2 in range(0, 1+1):
            if i2 == 1:
                #gen C3
                pass
            for i3 in range(0, 1+1):
                if i3 == 1:
                    #gen C4
                    pass
            pass
        pass
    pass

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
