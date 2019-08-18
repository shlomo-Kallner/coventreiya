
from consonants import Consonants
from consonants import register
from consonants.Consonants import ArticulationManner1st 
from consonants.Consonants import ArticulationManner2nd 
from consonants.Consonants import ArticulationManner3rd
from consonants.Consonants import ArticulationType
from consonants.Consonants import ArticulationPlace
from consonants.Consonants import Voicing
		

class ver_1_5_4( Consonants ):
    def __init__(self):
        super().__init__(1,5,4)
    
    def nasal_stops_(self):
        return [ "[m]", "[n]", "[ŋ]" ]
    
    def non_nasal_stops_(self):
        return [ "[b]", "[d]", "[ɡ]" , "[p]", "[t]", "[k]", "[q]" ]
    
    def glottal_stop_(self):
        return [ "[ʔ]" ]
    
    def stops_(self):
        stop_ = list()
        stop_.extend(self.nasal_stops_())
        stop_.extend(self.non_nasal_stops_())
        return stop_
    
    def all_stops_(self):
        all_stops_ = list()
        all_stops_.extend(self.stops_())
        all_stops_.extend(self.glottal_stop_())
        return all_stops_
    
    def affricates_(self):
        """ OLD AND *DEPRECEATED* """
        return [ "[d͡z]", "[d͡ʒ]" , "[t͡s]", "[t͡ʃ]" ]
    
    def sibilant_fricatives_(self):
        return [ "[z]", "[ʒ]" , "[s]", "[ʃ]" , "[ɬ]" , "[ɮ]" ]
    
    def non_sibilant_fricatives_(self):
        return [ "[f]", "[v]", "[θ]", "[ð]", "[x]", "[χ]", "[ħ]", "[ʕ]", "[h]" ]
    
    def rhotic_fricatives_(self):
        return [ "[ɣ]", "[ʁ]", "[ɹ̠]" ]
    
    def fricatives_(self):
        fric_ = list()
        fric_.extend(self.sibilant_fricatives_())
        fric_.extend(self.non_sibilant_fricatives_())
        fric_.extend(self.rhotic_fricatives_())
        return fric_
    
    def semi_vowel_(self):
        return [ "[w]", "[ʋ]", "[ð̞]", "[j]" ]
    
    def rhotic_approximant_(self):
        return [ "[ɰ]", "[ɹ̠]" ]
    
    def onset_latteral_approximant_ext_(self):
        return [ "[l]" ]
    
    def onset_approximant_ext_(self):
        return [ "[l]" , "[ʍ]" ]
    
    def pharyngeal_approximant_(self):
        return [ "[ʕ̞]" ]
    
    def onset_approximant_(self):
        on_appr_ = list()
        on_appr_.extend(self.semi_vowel_())
        on_appr_.extend(self.rhotic_approximant_())
        on_appr_.extend(self.onset_approximant_ext_())
        on_appr_.extend(self.pharyngeal_approximant_())
        return on_appr_
    
    def coda_approximant_ext_(self):
        return [ "[ɫ]" ]
    
    def coda_approximant_(self):
        co_appr_ = list()
        co_appr_.extend(self.semi_vowel_())
        co_appr_.extend(self.coda_approximant_ext_())
        return co_appr_
    
    def trill_(self):
        return [ "[r]", "[ʀ]" ]
    
    def ejective_affricates_(self):
        """ OLD AND *DEPRECEATED* """
        return [ "[tsʼ]" , "[t͡ʃʼ]" ]
    
    def ejectives_stops_(self):
        return [ "[pʼ]" , "[ť]" , "[kʼ]" , "[qʼ]" ]

    def ejectives_fricatives_(self):
        return [ "[fʼ]" , "[θʼ]" , "[sʼ]" , "[ʃʼ]" , "[x’]" , "[χ’]" ]
    
    def all_ejectives_(self):
        ejec_ = list()
        ejec_.extend(self.ejectives_stops_())
        ejec_.extend(self.ejective_affricates_())
        ejec_.extend(self.ejectives_fricatives_())
        return ejec_
    
    def phonemes(self):
        """ Returns a (list) of (str) containing *ALL* legit phonemes.
            Note: all must be present in the phoneme matcher dictionary."""
        tmp = list()
        tmp.extend(self.all_stops_())
        tmp.extend(self.affricates_())
        tmp.extend(self.fricatives_())
        tmp.extend(self.semi_vowel_())
        tmp.extend(self.rhotic_approximant_())
        tmp.extend(self.onset_approximant_ext_())
        tmp.extend(self.pharyngeal_approximant_())
        tmp.extend(self.coda_approximant_ext_())
        tmp.extend(self.trill_())
        tmp.extend(self.all_ejectives_())
        return tmp

    def exact_phones(self):
        """ Returns a (list) of (str) containing *ALL* legit exact phones.
            Note: all must be present in the phoneme matcher dictionary."""
        return self.phonemes()

    
    def phoneme_matcher(self):
        """ Returns a (dict) of (str) whose keys are phonemes
            and whose item are lists of it's key's actualization phones. """
        tmp = {}
        for i in self.phonemes():
            tmp[i] = i
        return tmp

    def exact_phone_matcher(self):
        """ """
        return self.phoneme_matcher()

    def affr_fric_match_(self):
        """ OLD AND *DEPRECEATED* """
        return { "[d͡z]": "[z]", "[d͡ʒ]": "[ʒ]", "[t͡s]": "[s]", "[t͡ʃ]": "[ʃ]" }
    
    def stop_affr_match_(self):
        """ OLD AND *DEPRECEATED* """
        return { "[d͡z]": "[d]", "[d͡ʒ]": "[d]", "[t͡s]": "[t]", "[t͡ʃ]": "[t]" }
        
    ##########################################################################
    #
    #
    #    the get_phone() API Methods...
    #
    #
    ##########################################################################
    
    __1stManners = range(0, 6+1)
    __2ndManners = list([0, 1])
    __3rdManners = list([0, 1])
    __artTypes = list([0, 1])
    __artPlaces = list([1, 2, 4, 5, 6, 9, 10, 11, 12, 14])
    __coArtPlaces = list([0, 1])
    __voicings = list([0, 3])
		
    def actual_phones(self):
		""" """ 
        tmp = {}
        # the Stops, Stop_ = 0
        ## Nasal, Voiceless, Voiced, Ejective
        # the Non-Sibilant Affricates, Affricate_ = 1
        ## Voiceless, Voiced
        # the Sibilant Affricates, SibilantAffricate_ = 2
        ## Voiceless, Voiced, Ejective
        # the Non-Sibilant Fricatives, Fricative_ = 3
        ## Voiceless, Voiced
        # the Sibilant Fricatives, SibilantFricative_ = 4
        ## Voiceless, Voiced, Ejective
        # the Approximants, Approximant = 5
        ## Rhotic, Non-Rhotic
        # the Trills, Trill_ = 6
        
        return tmp
	    
    def get_phone( self, ArtMan1_= ArticulationManner1st.Min_, 
	                     ArtMan2_ = ArticulationManner2nd.Min_,
	                     ArtMan3_ = ArticulationManner3rd.Min_,
	                     ArtTyp_ = ArticulationType.Min_,
	                     ArtPlc_ = ArticulationPlace.Min_,
	                     CoArtPlc_ = ArticulationPlace.Min_,
	                     Voice_ = Voicing.Min_ ):
		am1_ = int(ArtMan1_) if int(ArtMan1_) in __1stManners else ValueError()
		am2_ = int(ArtMan2_) if int(ArtMan2_) in __2ndManners else ValueError()
		am3_ = int(ArtMan3_) if int(ArtMan3_) in __3rdManners else ValueError()
		at_ = int(ArtTyp_) if int(ArtTyp_) in __artTypes else ValueError()
		ap_ = int(ArtPlc_) if int(ArtPlc_) in __artPlaces else ValueError()
		cap_ = int(CoArtPlc_) if int(CoArtPlc_) in __coArtPlaces else ValueError()
		v_ = int(Voice_) if int(Voice_) in __voicings else ValueError()
		k = tuple(am1_, am2_, am3_, at_, ap_, cap_, v_)
		t_ = self.actual_phones()
		return t_[k] if k in t_ else ""
		
		
	    


def gen_ver_1_5_4():
    return ver_1_5_4()

cons_ = register( ver_1_5_4(), gen_ver_1_5_4 )

##################################################################################
#
#    The OLD *DEPRECEATED* "default" gen_*_ functions ...
#       Some of these should move to phonotactics ...        
#
#

def gen_nasal_stops_():
    return cons_.nasal_stops_() 

def gen_non_nasal_stops_():
    return cons_.non_nasal_stops_()

def gen_glottal_stop_():
    return cons_.glottal_stop_()

def gen_stops_():
    return cons_.stops_()

def gen_all_stops_():
    return cons_.all_stops_()

def gen_affricates_():
    return cons_.affricates_()

def gen_sibilant_fricatives_():
    return cons_.sibilant_fricatives_()

def gen_non_sibilant_fricatives_():
    return cons_.non_sibilant_fricatives_()

def gen_rhotic_fricatives_():
    return cons_.rhotic_fricatives_()

def gen_fricatives_():
    return cons_.fricatives_()

def gen_semi_vowel_():
    return cons_.semi_vowel_()

def gen_rhotic_approximant_():
    return cons_.rhotic_approximant_()

def gen_onset_approximant_ext_():
    return cons_.onset_approximant_ext_()

def gen_pharyngeal_approximant_():
    return cons_.pharyngeal_approximant_()

def gen_onset_approximant_():
    return cons_.onset_approximant_()

def gen_coda_approximant_ext_():
    return cons_.coda_approximant_ext_()

def gen_coda_approximant_():
    return cons_.coda_approximant_()

def gen_trill_():
    return cons_.trill_()

def gen_ejectives_():
    return cons_.all_ejectives_()

def gen_affr_fric_match_():
    return cons_.affr_fric_match_()

def gen_stop_affr_match_():
    return cons_.stop_affr_match_()

##################################################################################
#
#
#    The OLD *DEPRECEATED* "default" pre-generated lists...
#    Originally intended as Aliases for compatability...
#

nasal_stop = gen_nasal_stops_()
non_nasal_stop = gen_non_nasal_stops_()
glottal_stop = gen_glottal_stop_()
stop = gen_stops_()
all_stops = gen_all_stops_()
affricate = gen_affricates_()
sibilant_fricative = gen_sibilant_fricatives_()
non_sibilant_fricative = gen_non_sibilant_fricatives_()
rhotic_fricative = gen_rhotic_fricatives_()
gen_fric_ = gen_fricatives_
fricative = gen_fricatives_()
semi_vowel = gen_semi_vowel_()
rhotic_approximant = gen_rhotic_approximant_()
onset_approximant_ext = gen_onset_approximant_ext_()
pharyngeal_approximant = gen_pharyngeal_approximant_()
gen_onset_appr_ = gen_onset_approximant_
onset_approximant = gen_onset_approximant_()
coda_approximant_ext = gen_coda_approximant_ext_()
gen_coda_appr_ = gen_coda_approximant_
coda_approximant = gen_coda_approximant_()
trill = gen_trill_()
ejective = gen_ejectives_()
# Affricate - Fricative matching dictionaries
#             Remember Affricates are made up of
#             a Stop followed by a Fricative.
affr_fric_match = gen_affr_fric_match_()
stop_affr_match = gen_stop_affr_match_()



