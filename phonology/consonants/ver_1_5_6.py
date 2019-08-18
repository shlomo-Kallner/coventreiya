
from consonants import Consonants
from consonants import register
from consonants.Consonants import ArticulationManner1st 
from consonants.Consonants import ArticulationManner2nd 
from consonants.Consonants import ArticulationManner3rd
from consonants.Consonants import ArticulationType
from consonants.Consonants import ArticulationPlace
from consonants.Consonants import Voicing


class ver_1_5_6( Consonants ):
    def __init__(self):
        super().__init__(1,5,6)
    
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
    
    def sibilant_fricatives_(self):
        return [ "[z]", "[ʒ]" , "[s]", "[ʃ]" , "[ɬ]" , "[ɮ]" ]
    
    def non_sibilant_fricatives_(self):
        return [ "[f]", "[v]", "[θ]", "[ð]", "[x]", "[χ]", "[ħ]", "[ʕ]", "[h]" ]
    
    def rhotic_fricatives_(self):
        return [ "[ɣ]", "[ʁ]" ]
    
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
        tmp = list()
        tmp.extend(self.onset_latteral_approximant_ext_())
        tmp.append( "[ʍ]" )
        return tmp
    
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
    
    def ejectives_stops_(self):
        return [ "[pʼ]" , "[ť]" , "[kʼ]" , "[qʼ]" ]

    def ejectives_fricatives_(self):
        return [ "[fʼ]" , "[θʼ]" , "[sʼ]" , "[ʃʼ]" , "[x’]" , "[χ’]" ]
    
    def all_ejectives_(self):
        ejec_ = list()
        ejec_.extend(self.ejectives_stops_())
        ejec_.extend(self.ejectives_fricatives_())
        return ejec_

    def exact_phones(self):
        """ Returns a (list) of (str) containing *ALL* legit exact phones.
            Note: all must be present in the phoneme matcher dictionary."""
        tmp = list()
        tmp.extend(self.all_stops_())
        tmp.extend(self.fricatives_())
        tmp.extend(self.semi_vowel_())
        tmp.extend(self.rhotic_approximant_())
        tmp.extend(self.onset_approximant_ext_())
        tmp.extend(self.pharyngeal_approximant_())
        tmp.extend(self.coda_approximant_ext_())
        tmp.extend(self.trill_())
        tmp.extend(self.all_ejectives_())
        return tmp

    def phonemes(self):
        """ Returns a (list) of (str) containing *ALL* legit phonemes.
            Note: all must be present in the phoneme matcher dictionary."""
        return self.exact_phones()

    def phoneme_matcher(self):
        """ Returns a (dict) of (str) whose keys are phonemes
            and whose item are lists of it's key's actualization phones. """
        tmp = {}
        for i in self.phonemes():
            tmp[i] = i
        return tmp

    def exact_phone_matcher(self):
        """ Returns a (dict) of (str) whose keys are exact phones
            and whose items are the associated phonemes.
        """
        return self.phoneme_matcher()

def gen_ver_1_5_6():
    return ver_1_5_6()

cons = register( ver_1_5_6(), gen_ver_1_5_6 )
    

