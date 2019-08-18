

__name__ = ["consonants"]


###################################################################################
#
# Imports
#

from enum import Enum

from coventreiya.utils.ver import ver
from coventreiya.utils.ver import gen_ver
from coventreiya.utils.ver import Version_Registry

from coventreiya.phonology.abc import abc

from abc import ABCMeta, abstractmethod


###################################################################################
#
# Phonology  -  Consonants
#
 
class Consonants(abc):
    def __init__(self, major=0, minor=0, patch=0, version=None):
        super().__init__(major, minor, patch, version)
	    
    @abstractmethod
    def nasal_stops_(self):
        pass 
	    
    @abstractmethod
    def non_nasal_stops_(self):
        pass
	    
    @abstractmethod
    def glottal_stop_(self):
        pass 
	    
    @abstractmethod
    def stops_(self):
        pass 
	    
    @abstractmethod
    def all_stops_(self):
        pass
	    
    @abstractmethod
    def sibilant_fricatives_(self):
        pass
	    
    @abstractmethod
    def non_sibilant_fricatives_(self):
        pass
	    
    @abstractmethod
    def rhotic_fricatives_(self):
        pass 
	    
    @abstractmethod
    def fricatives_(self):
        pass
	    
    @abstractmethod
    def semi_vowel_(self):
        pass
	    
    @abstractmethod
    def rhotic_approximant_(self):
        pass
	    
    @abstractmethod
    def onset_latteral_approximant_ext_(self):
        pass
	    
    @abstractmethod
    def onset_approximant_ext_(self):
        pass 
		
    @abstractmethod
    def pharyngeal_approximant_(self):
        pass 
	    
    @abstractmethod
    def onset_approximant_(self):
        pass
	    
    @abstractmethod
    def coda_approximant_ext_(self):
        pass
	    
    @abstractmethod
    def coda_approximant_(self):
        pass
	    
    @abstractmethod
    def trill_(self):
        pass
	    
    @abstractmethod
    def ejectives_stops_(self):
        pass 
		
    @abstractmethod
    def ejectives_fricatives_(self):
        pass
		    
    @abstractmethod
    def all_ejectives_(self):
        pass
		
    ###################################
    #
    # Some stuff from the ABC that derived types MUST
    #  Overide for Compatiblity with the ABC.
    #
    ###################################
	    
    @abstractmethod
    def phoneme_matcher(self):
        """ Returns a (dict) of (str) whose keys are phonemes
            and whose item are lists of it's key's actualization phones. """
        pass
		
    @abstractmethod
    def phonemes(self):
        """ Returns a (list) of (str) containing *ALL* legit phonemes.
            Note: all must be present in the phoneme matcher dictionary."""
        pass
		
    @abstractmethod
    def exact_phones(self):
        """ Returns a (list) of (str) containing *ALL* legit exact phones.
            Note: all must be present in the phoneme matcher dictionary."""
        pass
		
    @abstractmethod
    def exact_phone_matcher(self):
        """ """
        pass
		
    ##########################################################################
    #
    #
    #    the Enums for a possible future get_phone() API...
    #
    #
    ##########################################################################
		
    class ArticulationManner1st(int, Enum):
        Min_ = 0
        Stop_ = 0
        Affricate_ = 1
        SibilantAffricate_ = 2
        Fricative_ = 3
        SibilantFricative_ = 4
        Approximant = 5
        Trill_ = 6
        Tap_ = 7
        Flap = 8
        Max_ = 8
        
    class ArticulationManner2nd(int, Enum):
        Min_ = 0
        None_ = 0
        Lateral_ = 1
        Max_ = 1
		
    class ArticulationManner3rd(int, Enum):
        Min_ = 0
        None_ = 0
        Nasal_ = 1
        Max_ = 1
		
    class ArticulationType(int, Enum):
        Min_ = 0
        Pulmonic_ = 0
        Ejective_ = 1
        Implosive_ = 2
        Click_ = 3
        Max_ = 3
		
    class ArticulationPlace(int, Enum):
        Min_ = 0
        None_ = 0
        BiLabial_ = 1
        LabioDental_ = 2
        LinguoLabial_ = 3
        Dental_ = 4
        Alveolar_ = 5
        PalatoAlveolar_ = 6
        Retroflex_ = 7
        AlveoloPalatal_ = 8
        Palatal_ = 9
        Velar_ = 10
        Uvular_ = 11
        Pharyngeal_ = 12
        Epiglottal_ = 13
        Glottal_ = 14
        Max_ = 14
		
    class Voicing(int, Enum):
        Min_ = 0
        Voiceless_ = 0
        Breathy_ = 1
        Slack_ = 2
        Modal_ = 3 # the "sweet spot", A.K.A "Voiced"
        Voiced_ = 3 # An Alias of Modal_.
        Stiff_ = 4
        Creaky_ = 5
        Glottal_ = 6
        Max_ = 6
        
    ##########################################################################
    #
    #
    #    the future get_phone() API Methods...
    #
    #
    ##########################################################################
		
    @abstractmethod
	def actual_phones(self):
		pass
		
	@abstractmethod
	def get_phone( self, ArtMan1_=ArticulationManner1st.Min_, 
	               ArtMan2_ = ArticulationManner2nd.Min_,
	               ArtMan3_ = ArticulationManner3rd.Min_,
	               ArtTyp_ = ArticulationType.Min_,
	               ArtPlc_ = ArticulationPlace.Min_,
	               CoArtPlc_ = ArticulationPlace.Min_,
	               Voice_ = Voicing.Min_ ):
		pass
		
		
###################################################################################
#
# Version Information Control & UnExported [but Versioned] Object Instantiation
#

__versions = Version_Registry(Consonants())

def register( version, functor ):
    if isinstance( version, Consonants ):
        return __versions.register( version, functor )
    else:
        raise TypeError()

def get_version(major=0, minor=0, patch=0, version=None):
    return __versions.get( major, minor, patch, version )

def gen_version( major=0, minor=0, patch=0, version=None ):
    return __versions.gen( major, minor, patch, version )

def get_all_versions():
    return list(__versions)
        
###################################################################################
#
#    Getting/Setting the default/current version...
#    

def get_current():
    return __versions.current()

def get_current_version():
    ''' Shortcut function for acquiring the current version's version information. '''
    return __versions.current().version()

def reset_current_version( major=0, minor=0, patch=0, version=None ):
    v = gen_ver(major, minor, patch, version)
    return __versions.current(v)

###################################################################################
#
#    The original default version -- used for the(now obsolete and removed) 
#        "default" gen_*_ functions and the pre-generated lists...
#    Note: the *COMPATABILITY_ONLY* default gen_*_ functions will self-update 
#        to accomidate resets (they call into *THE_CURRENT_VERSION_OBJECT*!!)
#        the PRE-GENERATED LISTS will not be updated at all..
#    Note: VERSION 2_0: the *OLD* gen_*_ functions no longer self-update as 
#        they are now directly linked to version 1.5.4 only.
#    Version 1.5.4 is only being used due to it's still having Affricates!
#    Later versions don't have them.
#
# from ver_1_5_4 import *
#__versions.current( gen_ver(1,5,4) )


