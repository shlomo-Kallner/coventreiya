
from vowels import Vowels
from vowels import register
from vowels.Vowels import Height, Backness, Rounding, Nasality

class ver_1_5_9( Vowels ):
    """ Also Known As the Actually Used Vowels of Coventreiya.
    """
    def __init__(self):
        super().__init__(1,5,9)

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
        """ A mapping of the Phonemes used to
            Height, Backness, Rounding, Nasality for use with get_phone().
            Only the Actual Phones *used* (A.K.A => the current phonemes)!
              And for this version it means => NO NASALS!
        """
        tmp = {}
        # The Non-Nasals: 
        # Height - close - [Height][Backness][Rounding][Nasality] = "[]"
        tmp[tuple(0,0,0,0)] = "[i]"
        tmp[tuple(0,4,1,0)] = "[u]"
        # Height - near close - [Height][Backness][Rounding][Nasality] = "[]"
        tmp[tuple(1,1,0,0)] = "[ɪ]"
        tmp[tuple(1,3,1,0)] = "[ʊ]"
        # Height - close mid - [Height][Backness][Rounding][Nasality] = "[]"
        tmp[tuple(2,0,0,0)] = "[e]"
        # Height - mid - [Height][Backness][Rounding][Nasality] = "[]"
        tmp[tuple(3,2,0,0)] = "[ə]"
        tmp[tuple(3,4,1,0)] = "[o̞]"
        # Height - open mid - [Height][Backness][Rounding][Nasality] = "[]"
        tmp[tuple(4,0,0,0)] = "[ɛ]"
        tmp[tuple(4,0,1,0)] = "[œ]"
        tmp[tuple(4,4,1,0)] = "[ɔ]"
        # Height - near open - [Height][Backness][Rounding][Nasality] = "[]"
        tmp[tuple(5,0,0,0)] = "[æ]"
        # Height - open - [Height][Backness][Rounding][Nasality] = "[]"
        tmp[tuple(6,2,0,0)] = "[ä]"
        return tmp

    def phonemes(self):
        """ Returns a (list) of (str) containing *ALL* legit phonemes.
            Note: all must be present in the phoneme matcher dictionary."""
        tmp = [ "[i]", "[u]", "[ɪ]", "[ʊ]", "[e]", "[ə]", "[o̞]",
                "[ɛ]", "[œ]", "[ɔ]", "[æ]", "[ä]"]
        return tmp

    def phoneme_matcher(self):
        """ Returns a (dict) of (str) whose keys are phonemes
            and whose item are lists of it's key's actualization phones.
            (actualization phones => A.K.A "ALLOPHONES"!)
        """
        tmp = {}
        for i in self.phonemes():
            tmp[i] = [ i ]
        tmp[ "[i]" ].append( "[ĩ]" )
        tmp[ "[u]" ].extend( [ "[ʉ]", "[ũ]", "[ʉ̃]" ] )
        tmp[ "[ɪ]" ].append( "[ɪ̃]" )
        tmp[ "[ʊ]" ].append( "[ʊ̃]" )
        tmp[ "[e]" ].extend( [ "[ẽ]", "[e̞]", "[ẽ̞]" ] )
        tmp[ "[o̞]" ].append("[õ̞]"  )
        tmp[ "[ɛ]" ].append( "[ɛ̃]" )
        tmp[ "[œ]" ].append( "[œ̃]" )
        tmp[ "[ɔ]" ].append( "[ɔ̃]" )
        tmp[ "[æ]" ].append( "[æ̃]" )
        tmp[ "[ä]" ].extend( [ "[a]", "[ɑ]" , "[ɒ]" ] )
        tmp[ "[ä]" ].extend( [ "[ä̃]", "[ã]", "[ɑ̃]", "[ɒ̃]" ] )
        tmp[ "[ə]" ].append( "[ə̃]" )
        return tmp

    def exact_phones(self):
        """ Returns a (list) of (str) containing *ALL* legit exact phones.
            Note: all must be present in the phoneme matcher dictionary
            AND in the exact Phone Matcher.
            Note: includes all ALLOPHONES!
        """
        tmp = list()
        m = self.phoneme_matcher()
        for i in m.keys():
            for j in m[i]:
                if j not in tmp:
                    tmp.append(j)
        return tmp

    def exact_phone_matcher(self):
        """ Returns a (dict) of (str) whose keys are exact phones
            and whose items are the associated phonemes.
        """
        tmp = {}
        for i in self.phonemes():
            tmp[i] = i
        m = self.phoneme_matcher()
        for i in m.keys():
            for j in m[i]:
                if j not in tmp.keys():
                    tmp[ j ] = i

    
                 

def gen_ver_1_5_9():
    return ver_1_5_9()

vowel_ = register( ver_1_5_9(), gen_ver_1_5_9 )
        
