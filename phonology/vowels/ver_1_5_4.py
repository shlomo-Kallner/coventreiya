
from vowels import Vowels
from vowels import register
from vowels.Vowels import Height, Backness, Rounding, Nasality

class ver_1_5_4( Vowels ):
    def __init__(self):
        super().__init__(1,5,4)

    ##############################################################################
    #
    #
    #  this section is the overloading methods...
    #
    #
    ##############################################################################
    
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
        """ """ 
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

    def phonemes(self):
        """ Returns a (list) of (str) containing *ALL* legit phonemes.
            Note: all must be present in the phoneme matcher dictionary."""
        tmp = [ "[ɪ]", "[e]", "[i]", "[u]", "[o̞]",
                "[ɔ]", "[ɒ]", "[ɑ]", "[ä]", "[a]",
                "[æ]", "[œ]", "[ɛ]", "[e̞]", "[ø]",
                "[y]", "[ʉ]", "[ʊ]", "[ɐ]", "[ʏ]",
                "[ɜ]", "[ẽ]", "[ĩ]", "[ũ]", "[õ̞]",
                "[ɔ̃]", "[ɒ̃]", "[ɑ̃]", "[ä̃]", "[ã]",
                "[æ̃]", "[œ̃]", "[ɛ̃]", "[ẽ̞]", "[ø̃]",
                "[ỹ]", "[ʉ̃]", "[ʊ̃]", "[ɐ̃]", "[ʏ̃]",
                "[ɜ̃ ]", "[ə]", "[ə̃]", "[ɪ̃]" ]
        return tmp

    def phoneme_matcher(self):
        """ Returns a (dict) of (str) whose keys are phonemes
            and whose item are lists of it's key's actualization phones. """
        tmp = {}
        for i in self.phonemes():
            tmp[i] = i
        return tmp

    def exact_phones(self):
        """ Returns a (list) of (str) containing *ALL* legit exact phones.
            Note: all must be present in the phoneme matcher dictionary."""
        return self.phonemes()

    def exact_phone_matcher(self):
        return self.phoneme_matcher()
    
    ##############################################################################
    #
    #
    #  below are the rest of the compatability methods....
    #
    #
    ##############################################################################
    
    def negative_sign_(self):
        return [ "ə" ] 
    
    def positive_sign_(self):
        return [ "ə̃" ]
    
    def index_separator_(self):
        return [ "ɪ̃" ]
    
    def sign_symbols_(self):
        signs_ = list()
        signs_.extend(self.negative_sign_())
        signs_.extend(self.positive_sign_())
        return signs_

    def zero_(self):
        return [ "ɪ" ]

    def non_zero_(self):
        return [ "e" , "i" , "u" , "o̞" , "ɔ" , "ɒ" ,
                 "ɑ" , "ä" , "a" , "æ" , "œ" , "ɛ" ,
                 "e̞" , "ø" , "y" , "ʉ" , "ʊ" , "ɐ" ,
                 "ʏ" , "ɜ" , "ẽ" , "ĩ" , "ũ" , "õ̞" ,
                 "ɔ̃" , "ɒ̃" , "ɑ̃" , "ä̃" , "ã" , "æ̃" ,
                 "œ̃" , "ɛ̃" , "ẽ̞" , "ø̃" , "ỹ" , "ʉ̃" ,
                 "ʊ̃" , "ɐ̃" , "ʏ̃" , "ɜ̃ " ]

    def all_digits_(self):
        digits = list()
        digits.extend(self.zero_())
        digits.extend(self.non_zero_())
        return digits

    def is_numeral( self, v ):
        return v in self.all_digits_()
    
    def is_sign_symbol( self, v ):
        return v in self.sign_symbols_()

    def is_negative_sign( self, v ):
        return v in self.negative_sign_()

    def is_positive_sign( self, v ):
        return v in self.positive_sign_()

    def is_index_separator( self, v ):
        return v in self.index_separator_()

    def max_digit_value(self):
        # includes the zeroth digit
        return len(self.all_digits_())
    
    def parse_digit( self, v ):
        if self.is_numeral(v):
            i = 0
            for j in self.all_digits_():
                if v != j:
                    i = i + 1
                else:
                    break
            return i
        else:
            raise ValueError()

    def parse_int_string( self, list_ ):
        # stringed numerals are little endian!
        tmp = 0
        signed = False
        for i in reversed(list_):
            if is_numeral(i):
                t1 = tmp * self.max_digit_value()
                t2 = self.parse_digit( i )
                tmp = t1 + t2
            elif is_sign_symbol( i ):
                if is_negative_sign( i ) and not signed :
                    signed = True
                elif is_positive_sign( i ) and signed :
                    signed = False
            else:
                raise ValueError()
        if signed :
            tmp = -tmp
        return tmp

##################################################################################
#
#
#      Version Control Registry...
#
#

def gen_ver_1_5_4():
    return ver_1_5_4()

__old = vowel_ = register( ver_1_5_4(), gen_ver_1_5_4 )

##################################################################################
#
#    The OLD *DEPRECEATED* "default" gen_*_ functions ...
#       Some of these should move to phonotactics ...        
#
#

def gen_negative_sign_():
    return __old.negative_sign_()

def gen_positive_sign_():
    return __old.positive_sign_()

def gen_index_separator_():
    return __old.index_separator_()

def gen_sign_symbols_():
    return __old.sign_symbols_()

def gen_zero_():
    return __old.zero_()

def gen_non_zero_():
    return __old.non_zero_()

def gen_all_digits_():
    return __old.all_digits_()

def is_numeral( v ):
    return __old.is_numeral( v )

def is_sign_symbol( v ):
    return __old.is_sign_symbol( v )

def is_negative_sign( v ):
    return __old.is_negative_sign( v )

def is_positive_sign( v ):
    return __old.is_positive_sign( v )

def is_index_separator( v ):
    return __old.is_index_separator( v )

def get_single_digit_value( v ):
    return __old.parse_digit( v )

def get_num_single_digit_values():
    return __old.max_digit_value()

def parse_string_int_value( list_ ):
    return __old.parse_int_string( list_ )
            
##################################################################################
#
#
#    The OLD *DEPRECEATED* "default" pre-generated lists...
#

negative_sign = gen_negative_sign_()
positive_sign = gen_positive_sign_()
index_separator = gen_index_separator_()
sign_symbols = gen_sign_symbols_()
zero = gen_zero_()
non_zero = gen_non_zero_()


