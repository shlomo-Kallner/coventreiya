
__name__ = ["phonology"]
__version__ = "1.5.4"

##################################################################
#
#
# Phonology  -  Consonants

def gen_nasal_stops_():
    return [ "m", "n", "ŋ" ]

nasal_stop = gen_nasal_stops_()

def gen_non_nasal_stops_():
    return [ "b", "d", "ɡ" , "p", "t", "k", "q" ]

non_nasal_stop = gen_non_nasal_stops_()

def gen_glottal_stop_():
    return [ "ʔ" ]

glottal_stop = gen_glottal_stop_()

def gen_stops_():
    stop_ = list()
    stop_.extend(nasal_stop)
    stop_.extend(non_nasal_stop)
    return stop_

stop = gen_stops_()

def gen_all_stops_():
    all_stops_ = list()
    all_stops_.extend(stop)
    all_stops_.extend(glottal_stop)
    return all_stops_

all_stops = gen_all_stops_()

def gen_affricates_():
    return [ "d͡z", "d͡ʒ" , "t͡s", "t͡ʃ" ]

affricate = gen_affricates_()

def sibilant_fricatives_():
    return [ "z", "ʒ" , "s", "ʃ" , "ɬ" , "ɮ" ]

sibilant_fricative = sibilant_fricatives_()

def non_sibilant_fricatives_():
    return [ "f", "v", "θ", "ð", "x", "χ", "ħ", "ʕ", "h" ]
    
non_sibilant_fricative = non_sibilant_fricatives_()

def gen_rhotic_fricatives_():
    return [ "ɣ", "ʁ", "ɹ̠" ]

rhotic_fricative = gen_rhotic_fricatives_()

def gen_fric_():
    """ 18 consonants """
    fric_ = list()
    fric_.extend(sibilant_fricative)
    fric_.extend(non_sibilant_fricative)
    fric_.extend(rhotic_fricative)
    return fric_

fricative = gen_fric_()

def gen_semi_vowel_():
    return [ "w", "ʋ", "ð̞", "j" ]

semi_vowel = gen_semi_vowel_()
rhotic_approximant = [ "ɰ", "ɹ̠" ]

onset_approximant_ext = [ "l" , "ʍ" , "ʕ̞" ]

def gen_onset_appr_():
    on_appr_ = list()
    on_appr_.extend(semi_vowel)
    on_appr_.extend(rhotic_approximant)
    on_appr_.extend(onset_approximant_ext)
    return on_appr_

onset_approximant = gen_onset_appr_()

coda_approximant_ext = [ "ɫ" ]

def gen_coda_appr_():
    co_appr_ = list()
    co_appr_.extend(semi_vowel)
    co_appr_.extend(coda_approximant_ext)
    return co_appr_

coda_approximant = gen_coda_appr_()

def gen_trill_():
    return [ "r", "ʀ" ]

trill = gen_trill_()

def gen_ejectives_():
    return [ "pʼ" , "ť" , "kʼ" , "qʼ" , "tsʼ" , "t͡ʃʼ" ,
             "fʼ" , "θʼ" , "sʼ" , "ʃʼ" , "x’" , "χ’" ]

ejective = gen_ejectives_()

def gen_pharyngeal_approximant_():
    return [ "ʕ̞" ]

pharyngeal_approximant = gen_pharyngeal_approximant_()

# Affricate - Fricative matching dictionaries
#             Remember Affricates are made up of
#             a Stop followed by a Fricative.

def gen_affr_fric_match_():
    return { "d͡z": "z", "d͡ʒ": "ʒ", "t͡s": "s", "t͡ʃ": "ʃ" }

affr_fric_match = gen_affr_fric_match_()

def gen_stop_affr_match_():
    return { "d͡z": "d", "d͡ʒ": "d", "t͡s": "t", "t͡ʃ": "t" }

stop_affr_match = gen_stop_affr_match_()

