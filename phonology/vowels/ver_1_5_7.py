
from vowels import Vowels
from vowels import register
from vowels.Vowels import Height, Backness, Rounding, Nasality

class ver_1_5_7( Vowels ):
    """ Also Known As the Theoretical (Design) Maximum of Vowels
        for Coventreiya.
    """
    def __init__(self):
        super().__init__(1,5,7)

    __height = 7
    __back = 5
    __rounding = 2
    __nasality = 2
    
    def get_phone(self, height=Height.Min_, back=Backness.Min_,
                    rounding=Rounding.Min_, nasality=Nasality.Min_):
        h = int(height) if int(height) in range(0, __height) else raise ValueError()
        b = int(back) if int(back) in range(0, __back) else raise ValueError()
        r = int(rounding) if int(rounding) in range(0, __rounding) else raise ValueError()
        n = int(nasality) if int(nasality) in range(0, __nasality) else raise ValueError()
        t = tuple(h,b,r,n)
        a = self.actual_phones()
        return a[t] if t in a else ""

    def actual_phones(self):
        """ """ #  Vowels..Min_.value to Vowels..Max_.value + 1
        # initializing the first dimension... ( Height )
        tmp = {}
        # The Non-Nasals: 
        # Height - close - [Height][Backness][Rounding][Nasality] = "[]"
        tmp[tuple(0,0,0,0)] = "[i]"
        tmp[tuple(0,0,1,0)] = "[y]"
        tmp[tuple(0,2,1,0)] = "[ʉ]"
        tmp[tuple(0,4,1,0)] = "[u]"
        # Height - near close - [Height][Backness][Rounding][Nasality] = "[]"
        tmp[tuple(1,1,0,0)] = "[ɪ]"
        tmp[tuple(1,1,1,0)] = "[ʏ]"
        tmp[tuple(1,3,1,0)] = "[ʊ]"
        # Height - close mid - [Height][Backness][Rounding][Nasality] = "[]"
        tmp[tuple(2,0,0,0)] = "[e]"
        tmp[tuple(2,0,1,0)] = "[ø]"
        # Height - mid - [Height][Backness][Rounding][Nasality] = "[]"
        tmp[tuple(3,0,0,0)] = "[e̞]"
        tmp[tuple(3,2,0,0)] = "[ə]"
        tmp[tuple(3,4,1,0)] = "[o̞]"
        # Height - open mid - [Height][Backness][Rounding][Nasality] = "[]"
        tmp[tuple(4,0,0,0)] = "[ɛ]"
        tmp[tuple(4,0,1,0)] = "[œ]"
        tmp[tuple(4,2,0,0)] = "[ɜ]"
        tmp[tuple(4,4,1,0)] = "[ɔ]"
        # Height - near open - [Height][Backness][Rounding][Nasality] = "[]"
        tmp[tuple(5,0,0,0)] = "[æ]"
        tmp[tuple(5,2,0,0)] = "[ɐ]"
        # Height - open - [Height][Backness][Rounding][Nasality] = "[]"
        tmp[tuple(6,0,0,0)] = "[a]"
        tmp[tuple(6,2,0,0)] = "[ä]"
        tmp[tuple(6,4,0,0)] = "[ɑ]"
        tmp[tuple(6,4,1,0)] = "[ɒ]"
        # The Nasals: 
        # Height - close - [Height][Backness][Rounding][Nasality] = "[]"
        tmp[tuple(0,0,0,1)] = "[ĩ]"
        tmp[tuple(0,0,1,1)] = "[ỹ]"
        tmp[tuple(0,2,1,1)] = "[ʉ̃]"
        tmp[tuple(0,4,1,1)] = "[ũ]"
        # Height - near close - [Height][Backness][Rounding][Nasality] = "[]"
        tmp[tuple(1,1,0,1)] = "[ɪ̃]"
        tmp[tuple(1,1,1,1)] = "[ʏ̃]"
        tmp[tuple(1,3,1,1)] = "[ʊ̃]"
        # Height - close mid - [Height][Backness][Rounding][Nasality] = "[]"
        tmp[tuple(2,0,0,1)] = "[ẽ]"
        tmp[tuple(2,0,1,1)] = "[ø̃]"
        # Height - mid - [Height][Backness][Rounding][Nasality] = "[]"
        tmp[tuple(3,0,0,1)] = "[ẽ̞]"
        tmp[tuple(3,2,0,1)] = "[ə̃]"
        tmp[tuple(3,4,1,1)] = "[õ̞]"
        # Height - open mid - [Height][Backness][Rounding][Nasality] = "[]"
        tmp[tuple(4,0,0,1)] = "[ɛ̃]"
        tmp[tuple(4,0,1,1)] = "[œ̃]"
        tmp[tuple(4,2,0,1)] = "[ɜ̃ ]"
        tmp[tuple(4,4,1,1)] = "[ɔ̃]"
        # Height - near open - [Height][Backness][Rounding][Nasality] = "[]"
        tmp[tuple(5,0,0,1)] = "[æ̃]"
        tmp[tuple(5,2,0,1)] = "[ɐ̃]"
        # Height - open - [Height][Backness][Rounding][Nasality] = "[]"
        tmp[tuple(6,0,0,1)] = "[ã]"
        tmp[tuple(6,2,0,1)] = "[ä̃]"
        tmp[tuple(6,4,0,1)] = "[ɑ̃]"
        tmp[tuple(6,4,1,1)] = "[ɒ̃]"
        return tmp

    def exact_phones(self):
        """ Returns a (list) of (str) containing *ALL* legit exact phones.
            Note: all must be present in the phoneme matcher dictionary."""
        tmp = [ "[i]", "[y]", "[ʉ]", "[u]", "[ɪ]", "[ʏ]", "[ʊ]", "[e]",
                "[ø]", "[e̞]", "[ə]", "[o̞]", "[ɛ]", "[œ]", "[ɜ]", "[ɔ]",
                "[æ]", "[ɐ]", "[a]", "[ä]", "[ɑ]", "[ɒ]",
                "[ĩ]", "[ỹ]", "[ʉ̃]", "[ũ]", "[ɪ̃]", "[ʏ̃]", "[ʊ̃]", "[ẽ]",
                "[ø̃]", "[ẽ̞]", "[ə̃]", "[õ̞]", "[ɛ̃]", "[œ̃]", "[ɜ̃ ]", "[ɔ̃]",
                "[æ̃]", "[ɐ̃]", "[ã]", "[ä̃]", "[ɑ̃]", "[ɒ̃]" ]
        return tmp

    def phonemes(self):
        """ Returns a (list) of (str) containing *ALL* legit phonemes.
            Note: all must be present in the phoneme matcher dictionary."""
        return self.exact_phones()

    def phoneme_matcher(self):
        """ Returns a (dict) of (str) whose keys are phonemes
            and whose item are lists of it's key's actualization phones. """
        tmp = {}
        for i in self.exact_phones():
            tmp[i] = [ i ]
        return tmp

    def exact_phone_matcher(self):
        """ """
        return self.phoneme_matcher()

    

    


def gen_ver_1_5_7():
    return ver_1_5_7()

vowel_ = register( ver_1_5_7(), gen_ver_1_5_7 )
