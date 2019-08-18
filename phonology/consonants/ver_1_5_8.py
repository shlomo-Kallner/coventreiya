
from consonants import Consonants
from consonants import register
from consonants.Consonants import ArticulationManner1st 
from consonants.Consonants import ArticulationManner2nd 
from consonants.Consonants import ArticulationManner3rd
from consonants.Consonants import ArticulationType
from consonants.Consonants import ArticulationPlace
from consonants.Consonants import Voicing

class ver_1_5_8( Consonants ):
    def __init__(self):
        super().__init__(1,5,8)

    def nasal_stops_(self):
        return [ "[m]", "[n]", "[ŋ]" ]
    
    def unvoiced_non_nasal_stops_(self):
        return [ "[p]", "[t]", "[k]", "[q]" ]

    def voiced_non_nasal_stops_(self):
        return [ "[b]", "[d]", "[ɡ]" , "[ɢ]" ]

    def non_nasal_stops_(self):
        tmp = list()
        tmp.extend(self.voiced_non_nasal_stops_())
        tmp.extend(self.unvoiced_non_nasal_stops_())
        return tmp

    def glottal_stop_(self):
        return [ "[ʔ]" ]

    def stops_(self):
        tmp = list()
        tmp.extend(self.nasal_stops_())
        tmp.extend(self.non_nasal_stops_())
        return tmp
    
    def all_stops_(self):
        tmp = list()
        tmp.extend(self.stops_())
        tmp.extend(self.glottal_stop_())
        return tmp

    def unvoiced_sibilant_fricatives_(self):
        return [ "[z]", "[ʒ]" ]

    def unvoiced_lateral_sibilant_fricatives_(self):
        return [ "[ɬ]" ]

    def voiced_sibilant_fricatives_(self):
        return [ "[s]", "[ʃ]" ]
    
    def voiced_lateral_sibilant_fricatives_(self):
        return [ "[ɮ]" ]

    def sibilant_fricatives_(self):
        tmp = list()
        tmp.extend(self.unvoiced_sibilant_fricatives_())
        tmp.extend(self.unvoiced_lateral_sibilant_fricatives_())
        tmp.extend(self.voiced_sibilant_fricatives_())
        tmp.extend(self.voiced_lateral_sibilant_fricatives_())
        return tmp

    def unvoiced_non_sibilant_fricatives_(self):
        return [ "[f]", "[θ]", "[x]", "[χ]", "[ħ]", "[h]" ]

    def voiced_non_sibilant_fricatives_(self):
        return [ "[v]", "[ð]", "[ʕ]" ]

    def non_sibilant_fricatives_(self):
        tmp = list()
        tmp.extend(self.unvoiced_non_sibilant_fricatives_())
        tmp.extend(self.voiced_non_sibilant_fricatives_())
        return tmp

    def rhotic_fricatives_(self):
        return [ "[ɣ]", "[ʁ]" ]

    def fricatives_(self):
        tmp = list()
        tmp.extend(self.sibilant_fricatives_())
        tmp.extend(self.non_sibilant_fricatives_())
        tmp.extend(self.rhotic_fricatives_())
        return tmp

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
        tmp.extend( [ "[ɸ]", "[β]", "[β̞]", "[l̪]", "[ɾ]", "[ɢ̆]" ] )
        return tmp

    def phonemes(self):
        """ Returns a (list) of (str) containing *ALL* legit phonemes.
            Note: all must be present in the phoneme matcher dictionary."""
        tmp = list()
        # the stops
        tmp.extend(self.all_stops_())
        # the fricatives
        tmp.extend(self.fricatives_())
        # the Approximants
        tmp.extend([ "[w]", "[j]", "[ɹ̠]" , "[l]", "[ʍ]" ])
        # the Trills
        tmp.extend(self.trill_())
        # the Ejectives
        tmp.extend(self.all_ejectives_())
        return tmp

    def phoneme_matcher(self):
        """ Returns a (dict) of (str) whose keys are phonemes
            and whose item are lists of it's key's actualization phones. """
        tmp = {}
        for i in self.phonemes():
            tmp[i] = i
        # tmp[  ].append(  ) tmp[  ].extend( [  ] )
        # appending the Approximants to their respective fricatives..
        tmp[ "[f]" ].append( "[ɸ]" )
        tmp[ "[v]" ].extend( [ "[β]", "[β̞]", "[ʋ]" ] )
        tmp[ "[ð]" ].append( "[ð̞]" ) 
        tmp[ "[ɣ]" ].append( "[ɰ]" )
        tmp[ "[ʕ]" ].append( "[ʕ̞]" )
        tmp[ "[l]" ].extend( [ "[l̪]" , "[ɫ]" ] )
        # appending the Flaps/Taps to their respective Trills..
        tmp[ "[r]" ].append( "[ɾ]" )
        tmp[ "[ʀ]" ].append( "[ɢ̆]" )

        # finished populating the dict...
        return tmp

    def exact_phone_matcher(self):
        """ Returns a (dict) of (str) whose keys are exact phones
            and whose items are the associated phonemes.
        """
        tmp = {}
        p = self.phoneme_matcher()
        for i in p.keys():
            for j in p[i]
            tmp[j] = i
        return tmp

def gen_ver_1_5_8():
    return ver_1_5_8()

cons = register( ver_1_5_8(), gen_ver_1_5_8 )
    



