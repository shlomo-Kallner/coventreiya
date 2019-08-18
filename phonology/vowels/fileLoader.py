
from vowels import Vowels
from vowels import register

class fileLoader( Vowels ):
    def __init__(self, path):
		self.__path = path
        pass
        
    def path(self):
		return self.__path
        
    @abstractmethod
    def phonemes(self):
        """ Returns a (list) of (str) containing *ALL* legit phonemes.
            Note: all must be present in the phoneme matcher dictionary."""
        pass

    @abstractmethod
    def exact_phones(self):
        """ Returns a (list) of (str) containing *ALL* legit exact phones.
            Note: all must be present in the phoneme matcher dictionary.
            AND in the exact Phone Matcher.
            Note: includes all ALLOPHONES!
        """
        pass

    @abstractmethod
    def exact_phone_matcher(self):
        """ Returns a (dict) of (str) whose keys are exact phones
            and whose items are the associated phonemes.
        """
        pass

    @abstractmethod
    def phoneme_matcher(self):
        """ Returns a (dict) of (str) whose keys are phonemes
            and whose item are lists of it's key's actualization phones.
            (actualization phones => A.K.A "ALLOPHONES"!)
        """
        pass

    @abstractmethod
    def actual_phones(self):
        """ A mapping of the Phonemes used to
            Height, Backness, Rounding, Nasality for use with get_phone().
        """
        pass

    @abstractmethod
    def get_phone(self, height=0, back=0, rounding=0, nasality=0):
		""" Get a (exact) Vowel based on it's phonetic value/name. """
        pass

    

    
