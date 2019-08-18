
from __future__ import unicode_literals
import os
from os import path



##################################################################
#
#          lists and collections utility functions:
#
#

def is_item_list( item ):
    return ( isinstance(item, list) or \
             isinstance(item, tuple) )

        

def is_item_in_sub_lists( list_, item ):
    if (not is_item_list(list_) ) and \
        (not is_item_list(item) ):
            raise TypeError()
    else:
        bol = False
        for i in list_:
            bol2 = False
            if is_item_list(i):
                if len(i) == len(item):
                   blst = list()
                   bol2 = True
                   for j in range(0, len(i)):
                       blst.append( i[j] == item[j] )
                   for j in range(0, len(i)):
                       if blst[j] == False:
                          bol2 = False
            if bol2 == True:
                   bol = bol2
        return bol
                   
def is_item_in_list( list_, item ):
    if not is_item_list(list_):
            raise TypeError()
    elif not is_item_list(item):
            return item in list_
    else:
            return is_item_in_sub_lists(list_, item)

#
#
################################################################

################################################################
#
#   Input Utility Fuctions:
#

class pair:
    def __init__(self, first, second):
        self.__first = first
        self.__second = second

    @property
    def first(self):
        return self.__first

    @property
    def second(self):
        return self.__second

    def __del__(self):
        self.__first = None
        self.__second = None

class Query_matcher(dict):
    def __init__(self, mapping, match_op=lambda x: x, *alt_mappings ):
        self.__alt_mapping = alt_mappings
        self.__func = match_op if match_op.__getattr__('__call__') is not None else lambda x: x
        super().__init__(mapping)
    pass

def Query_for_value(inp, repl_map={}, ):
    if isinstance(inp,str) and isinstance(repl_map,dict):
        res = None
        bol = True
        while bol:
            s = input(inp)
            if s in repl_map:
                bol = False
                res = repl_map[s]
        return res
    else:
        raise TypeError()

#
#
################################################################


################################################################
#
#   String/Collection Generator Fuctions:
#

def gen_str( n, chars ):
    """ generate all possible n length strings of chars """
    """  - uses recursion -  """
    if is_item_list(chars) and isinstance(n,int):
        res = list()
        if n == 1:
            for i in chars:
                t = list()
                t.append(i)
                res.append(t)
        elif n > 1:
            t1 = gen_str( n-1, chars )
            for i in chars:
                for j in t1:
                    t = list()
                    t.append(i)
                    t.extend(j)
                    res.append(t)
        return res
    else:
        raise TypeError()

def gen_str1( n , chars ):
    """ generate all possible n length strings of chars """
    """  - does  not use recursion -  """
    if is_item_list(chars) and isinstance(n,int):
        res = list()
        for i in range(0, n):
            if i == 0:
                for j in chars:
                    t = list()
                    t.append(j)
                    res.append(t)
            else:
                tmp = list()
                for j in chars:
                    for k in res:
                        t = list()
                        t.extend(k)
                        t.append(j)
                        tmp.append(t)
                res = tmp
        return res
    else:
        raise TypeError()

def gen_list( max_chars, pos_chars, min_chars = 1 ):
    result = list()
    if not is_item_list(pos_chars) or not isinstance(max_chars,int) \
                   or not isinstance(min_chars,int):
        raise TypeError()
    elif min_chars > 0 and max_chars > min_chars:
        for i in range(min_chars, max_chars + 1):
            tmp = gen_str1(i, pos_chars)
            result.extend(tmp)
        return result
    else:
        raise ValueError()

def gen_replace_str( n , inp, repl ):
    """ generate all possible replacement strings of inp using repl """
    """  - uses recursion -  """
    if is_item_list(inp) and isinstance(n,int) \
       and isinstance(repl,dict):
        res = list()
        chars = repl[ inp[ n ] ]
        if n == 0:
            for i in chars:
                t = list()
                t.append(i)
                res.append(t)
        elif n > 0:
            t1 = gen_replace_str( n - 1, inp, repl )
            for i in chars:
                for j in t1:
                    t = list()
                    t.append(i)
                    t.extend(j)
                    res.append(t)
        return res
    else:
        raise TypeError()
            


def gen_replace_str1( inp, repl ):
    """ generate all possible replacement strings of inp using repl """
    """  - does not use recursion -  """
    if is_item_list(inp) and isinstance(repl,dict):
        res = list()
        for i in range(0, len(inp) ):
            chars = repl[ inp[ i ] ]
            if i == 0:
                for j in chars:
                    t = list()
                    t.append(j)
                    res.append(t)
            else:
                tmp = list()
                for j in chars:
                    for k in res:
                        t = list()
                        t.extend(k)
                        t.append(j)
                        tmp.append(t)
                res = tmp
        return res
    else:
        raise TypeError()


def gen_actual(list_, repl_map):
    """ WARNING!!! this fuction may use A LOT of memory """
    """  and may crash python!!!"""
    if is_item_list(list_) and isinstance(repl_map,dict):
        results = list()
        for i in list_:
            j = gen_replace_str1( i, repl_map )
            results.extend(j)
        return results
    else:
        raise TypeError()

def gen_actual_file(list_, repl_map, path, encoding_='utf-8'):
    if is_item_list(list_) and isinstance(repl_map,dict) \
       and isinstance(path, str) and isinstance(encoding_,str):
        results = 0
        f = open(path, "w", encoding=encoding_)
        for i in list_:
            t1 = gen_replace_str1( i, repl_map )
            for j in t1:
                print(j, file=f)
                results += 1
        return results
    else:
        raise TypeError()





#
#
################################################################



################################################################
#
#
# the finite state machine type and utility function:


class fsm_state:
    def __init__(self, name, value, mapping = {}):
        self.__value = value
        self.__mapping = mapping
        self.__name = name

    def name(self):
        return self.__name

    def value(self):
        return self.__value

    def remap(self, value, mapping):
        self.__mapping = mapping
        self.__value = value

    def map_transversal( self, key ):
        return self.__mapping[key]


def fsm_transversal( inputs, start_state ):
    fsm = start_state
    for i in inputs:
        fsm = fsm.map_transversal(i)
    return fsm.value()

#
#
##################################################################



##################################################################
#
#
# Phonology

stop = [ "m", "n", "ŋ" , "b", "d", "ɡ" , "p", "t", "k", "q" ]
glottal_stop = [ "ʔ" ]


affricate = [ "d͡z", "d͡ʒ" , "t͡s", "t͡ʃ" ]


sibilant_fricative = [ "z", "ʒ" , "s", "ʃ" , "ɬ" , "ɮ" ]
non_sibilant_fricative = [ "f", "v", "θ", "ð", "x", "χ", 
                           "ħ", "ʕ", "h" ]
rhotic_fricative = [ "ɣ", "ʁ", "ɹ̠" ]

def gen_fric_():
    """ 18 consonants """
    fric_ = list()
    fric_.extend(sibilant_fricative)
    fric_.extend(non_sibilant_fricative)
    fric_.extend(rhotic_fricative)
    return fric_


semi_vowel = [ "w", "ʋ", "ð̞", "j" ]
rhotic_approximant = [ "ɰ", "ɹ̠" ]
onset_approximant_ext = [ "l" , "ʍ" , "ʕ̞" ]
coda_approximant_ext = [ "ɫ" ]

def gen_onset_appr_():
    on_appr_ = list()
    on_appr_.extend(semi_vowel)
    on_appr_.extend(rhotic_approximant)
    on_appr_.extend(onset_approximant_ext)
    return on_appr_

def gen_coda_appr_():
    co_appr_ = list()
    co_appr_.extend(semi_vowel)
    co_appr_.extend(coda_approximant_ext)
    return co_appr_


trill = [ "r", "ʀ" ]


ejective = [ "pʼ" , "ť" , "kʼ" , "qʼ" , "tsʼ" , "t͡ʃʼ" ,
             "fʼ" , "θʼ" , "sʼ" , "ʃʼ" , "x’" , "χ’" ]

# Affricate - Fricative matching dictionaries

affr_fric_match = { "d͡z": "z", "d͡ʒ": "ʒ", "t͡s": "s", "t͡ʃ": "ʃ" }
stop_affr_match = { "d͡z": "d", "d͡ʒ": "d", "t͡s": "t", "t͡ʃ": "t" }



##################################################################
#
#   Phonotactics:
#
#   The new (Version 1.5) Onset Phonotactics are:
#   
#   ( { Fricative ,  Affricate ,  Ejective } ) >>
#   { Stop , Fricative , Affricate , Ejective , Trill ,
#     Onset_Approximant , Glottal_stop } >>
#   ( { Stop , Fricative , Affricate , Ejective , Trill ,
#     Onset_Approximant , Glottal_stop } ) >>
#   ( { Rhotic_Approximant , "l" } ) >>
#   ( Semi_Vowel ( >> Semi_Vowel ) ) >>
#   ( "ʕ̞" )
#
#   or:  "(C2)C1(C1)(C3)(S(S))('ʕ̞')"  where:
#
#   C2 = { Fricative ,  Affricate ,  Ejective };
#   C1 = { Stop , Fricative , Affricate , Ejective , Trill ,
#          Onset_Approximant , Glottal_stop };
#   C3 = { Rhotic_Approximant , "l" };
#   S  = Semi_Vowel ;
#
#   or in the onset generator:
#   1 for C1
#   2 for C2
#   3 for C3
#   4 for S
#   5 for 'ʕ̞'
#
#
#   The new (Version 1.5) Coda Phonotactics are:
#
#   Coda = ( Semi-Vowel ) >> ( { Rhotic_approximant , “[ɫ]” } )
#        >> { Stop , Fricative ,  Affricate , Coda_Approximant , Trill }
#        >> ( { Stop , Fricative ,  Affricate , Coda_Approximant , Trill } )
#        >> ( { Stop , Fricative ,  Affricate , Coda_Approximant , Trill } ) ;
#
#   or: "(S)(C2)C1(C1)(C1)"  where:
#
#   C1 = { Stop , Fricative ,  Affricate , Coda_Approximant , Trill } ;
#   C2 = { Rhotic_approximant , “[ɫ]” } ;
#   S  = Semi-Vowel ;
#
#   or in the coda generator:
#   1 for C1
#   2 for C2
#   3 for S
#
#
#


########################################################
#
#
#   Generating the Onsets
#
#

def gen_onsets():
    # setting up the Finite State Machine for parsing...
    # for parse string "(C2)  C1  (C1) (C3) (S   (S)) ('ʕ̞')"
    # will be using:
    # 1 for C1
    # 2 for C2
    # 3 for C3
    # 4 for S
    # 5 for 'ʕ̞'
    # in the generator.
    fsm = [ fsm_state(str(x),False) for x in range(0,10) ]
    fsm[0].remap(False, {1 : fsm[0],
                         2 : fsm[0],
                         3 : fsm[0],
                         4 : fsm[0],
                         5 : fsm[0]} )
    fsm[1].remap(False, {1 : fsm[2],
                         2 : fsm[3],
                         3 : fsm[0],
                         4 : fsm[0],
                         5 : fsm[0]} )
    fsm[2].remap(True,  {1 : fsm[4],
                         2 : fsm[6],
                         3 : fsm[5],
                         4 : fsm[7],
                         5 : fsm[9]} )
    fsm[3].remap(False, {1 : fsm[2],
                         2 : fsm[0],
                         3 : fsm[0],
                         4 : fsm[0],
                         5 : fsm[0]} )
    fsm[4].remap(True,  {1 : fsm[6],
                         2 : fsm[6],
                         3 : fsm[5],
                         4 : fsm[7],
                         5 : fsm[9]} )
    fsm[5].remap(True,  {1 : fsm[0],
                         2 : fsm[0],
                         3 : fsm[0],
                         4 : fsm[7],
                         5 : fsm[9]} )
    fsm[6].remap(False, {1 : fsm[6],
                         2 : fsm[6],
                         3 : fsm[6],
                         4 : fsm[6],
                         5 : fsm[6]} )
    fsm[7].remap(True,  {1 : fsm[6],
                         2 : fsm[6],
                         3 : fsm[6],
                         4 : fsm[8],
                         5 : fsm[9]} )
    fsm[8].remap(True,  {1 : fsm[6],
                         2 : fsm[6],
                         3 : fsm[6],
                         4 : fsm[6],
                         5 : fsm[9]} )
    fsm[9].remap(True,  {1 : fsm[0],
                         2 : fsm[0],
                         3 : fsm[0],
                         4 : fsm[0],
                         5 : fsm[0]} )
    #      "(C2)  C1  (C1) (C3) (S   (S)) ('ʕ̞')"
    # in the generator:
    # 1 for C1
    # 2 for C2
    # 3 for C3
    # 4 for S
    # 5 for 'ʕ̞'
    t = gen_list( 7 , [1,2,3,4,5] , 1 )
    results = list()
    for i in t:
        if fsm_transversal( i, fsm[1] ):
            results.append(i)
    return results

########################################################
#
#           Actual Onsets Generation Functions
#
#

def gen_onset_c1():
    """ __ consonants """
    c1_ = list()
    c1_.extend(stop)
    c1_.extend(gen_fric_())
    c1_.extend(affricate)
    c1_.extend(gen_onset_appr_())
    c1_.extend(trill)
    c1_.extend(ejective)
    return c1_

def gen_onset_c2():
    """ __ consonants """
    c2_ = list()
    c2_.extend(gen_fric_())
    c2_.extend(affricate)
    c2_.extend(ejective)
    return c2_

def gen_onset_c3():
    """ __ consonants """
    c3_ = list()
    c3_.extend(rhotic_approximant)
    c3_.extend(onset_approximant_ext)
    return c3_

def gen_actual_onsets():
    """ WARNING!!! this fuction uses A LOT of memory """
    """  and may crash python!!!"""
    results = list()
    c1 = gen_onset_c1()
    c2 = gen_onset_c2()
    c3 = gen_onset_c3()
    t = gen_onsets()
    # in the generator:
    # 1 for C1
    # 2 for C2
    # 3 for C3
    # 4 for S
    # 5 for 'ʕ̞'
    repl_map = { 1 : c1,
                 2 : c2,
                 3 : c3,
                 4 : semi_vowel,
                 5 : [ "ʕ̞" ] }
    for i in t:
        j = gen_replace_str1( i, repl_map )
        results.extend(j)
    return results


def gen_actual_onsets1():
    """ WARNING!!! this fuction uses A LOT of memory """
    """  and may crash python!!!"""
    c1 = gen_onset_c1()
    c2 = gen_onset_c2()
    c3 = gen_onset_c3()
    t = gen_onsets()
    # in the generator:
    # 1 for C1
    # 2 for C2
    # 3 for C3
    # 4 for S
    # 5 for 'ʕ̞'
    repl_map = { 1 : c1,
                 2 : c2,
                 3 : c3,
                 4 : semi_vowel,
                 5 : [ "ʕ̞" ] }
    return gen_actual(t, repl_map)


def gen_actual_onsets_to_file(path, encoding_='utf-8'):
    results = 0
    f = open(path, "w", encoding=encoding_)
    c1 = gen_onset_c1()
    c2 = gen_onset_c2()
    c3 = gen_onset_c3()
    t = gen_onsets()
    # in the generator:
    # 1 for C1
    # 2 for C2
    # 3 for C3
    # 4 for S
    # 5 for 'ʕ̞'
    repl_map = { 1 : c1,
                 2 : c2,
                 3 : c3,
                 4 : semi_vowel,
                 5 : [ "ʕ̞" ] }
    for i in t:
        t1 = gen_replace_str1( i, repl_map )
        for j in t1:
            print(j, file=f)
            results += 1
    return results

# gen_actual_file(list_, repl_map, path, encoding_='utf-8')
def gen_actual_onsets_to_file1(path, encoding_='utf-8'):
    c1 = gen_onset_c1()
    c2 = gen_onset_c2()
    c3 = gen_onset_c3()
    t = gen_onsets()
    # in the generator:
    # 1 for C1
    # 2 for C2
    # 3 for C3
    # 4 for S
    # 5 for 'ʕ̞'
    repl_map = { 1 : c1,
                 2 : c2,
                 3 : c3,
                 4 : semi_vowel,
                 5 : [ "ʕ̞" ] }
    return gen_actual_file(t, repl_map, path, encoding_)

########################################################
#
#
#   Generating the Codas
#
#

def gen_codas():
    # setting up the Finite State Machine for parsing...
    # for parse string "(S)(C2)C1(C1)(C1)"
    # will be using:
    # 1 for C1
    # 2 for C2
    # 3 for S
    # in the generator.
    fsm = [ fsm_state(str(x),False) for x in range(0,7) ]
    fsm[0].remap(False, {1 : fsm[1],
                         2 : fsm[2],
                         3 : fsm[3]} )
    fsm[1].remap(False, {1 : fsm[6],
                         2 : fsm[2],
                         3 : fsm[3]} )
    fsm[2].remap(False, {1 : fsm[6],
                         2 : fsm[6],
                         3 : fsm[3]} )
    fsm[3].remap(True,  {1 : fsm[6],
                         2 : fsm[6],
                         3 : fsm[4]} )
    fsm[4].remap(True,  {1 : fsm[6],
                         2 : fsm[6],
                         3 : fsm[5]} )
    fsm[5].remap(True,  {1 : fsm[6],
                         2 : fsm[6],
                         3 : fsm[6]} )
    fsm[6].remap(False, {1 : fsm[6],
                         2 : fsm[6],
                         3 : fsm[6]} )
    t = gen_list( 5 , [1,2,3] , 1 )
    results = list()
    for i in t:
        if fsm_transversal( i, fsm[0] ):
            results.append(i)
    return results

########################################################
#
#           Actual Codas Generation Functions
#
#

def gen_coda_c1():
    """ __ consonants """
    c1_ = list()
    c1_.extend(stop)
    c1_.extend(gen_fric_())
    c1_.extend(affricate)
    c1_.extend(gen_coda_appr_())
    c1_.extend(trill)
    return c1_

def gen_coda_c2():
    c2_ = list()
    c2_.extend(rhotic_approximant)
    c2_.extend(coda_approximant_ext)
    return c2_


def gen_actual_codas():
    """ WARNING!!! this fuction may use A LOT of memory """
    """  and may crash python!!!"""
    results = list()
    c1 = gen_coda_c1()
    c2 = gen_coda_c2()
    t = gen_codas()
    # for parse string "(S)(C2)C1(C1)"
    # will be using:
    # 1 for C1
    # 2 for C2
    # 3 for S
    # in the generator.
    repl_map = { 1 : c1,
                 2 : c2,
                 3 : semi_vowel }
    for i in t:
        j = gen_replace_str1( i, repl_map )
        results.extend(j)
    return results

# gen_actual(t, repl_map)
def gen_actual_codas1():
    """ WARNING!!! this fuction may use A LOT of memory """
    """  and may crash python!!!"""
    c1 = gen_coda_c1()
    c2 = gen_coda_c2()
    t = gen_codas()
    # for parse string "(S)(C2)C1(C1)"
    # will be using:
    # 1 for C1
    # 2 for C2
    # 3 for S
    # in the generator.
    repl_map = { 1 : c1,
                 2 : c2,
                 3 : semi_vowel }
    return gen_actual(t, repl_map)


def gen_actual_codas_to_file(path, encoding_='utf-8'):
    results = 0
    f = open(path, "w", encoding=encoding_)
    c1 = gen_coda_c1()
    c2 = gen_coda_c2()
    t = gen_codas()
    # for parse string "(S)(C2)C1(C1)"
    # will be using:
    # 1 for C1
    # 2 for C2
    # 3 for S
    # in the generator.
    repl_map = { 1 : c1,
                 2 : c2,
                 3 : semi_vowel }
    for i in t:
        t1 = gen_replace_str1( i, repl_map )
        for j in t1:
            print(j, file=f)
            results += 1
    return results

# gen_actual_file(list_, repl_map, path, encoding_='utf-8')
def gen_actual_codas_to_file1(path, encoding_='utf-8'):
    c1 = gen_coda_c1()
    c2 = gen_coda_c2()
    t = gen_codas()
    # for parse string "(S)(C2)C1(C1)"
    # will be using:
    # 1 for C1
    # 2 for C2
    # 3 for S
    # in the generator.
    repl_map = { 1 : c1,
                 2 : c2,
                 3 : semi_vowel }
    return gen_actual_file(t, repl_map, path, encoding_)


###########################################################
#      
#            Module Main
#
#
def main():
    print("begining module tests...")
    print("Onset parse string: \"(C2) C1 (C1) (C3) (S (S)) (\'ʕ̞\')\"")
    print("components being refered to according to the fallowing table: ")
    print(" 1 for C1 ")
    print(" 2 for C2 ")
    print(" 3 for C3 ")
    print(" 4 for S ")
    print(" 5 for \'ʕ̞\' ")
    print()
    input("press ENTER to continue.")
    print()
    t = gen_onsets()
    print("TThe total number cobination of onset types is: ", len(t) )
    for i in t:
        print(i)
    print()
    input("press ENTER to continue.")
    print()
    s = input("please enter a file name with path for output: ")
    t1 = gen_actual_onsets_to_file(s)
    print("The total number of actual onset options is: ", t1 )
    bol = Query_for_value("Input Y / y to display Onsets or N / n to not: ",
                          {"Y" : True,
                           "y" : True,
                           "N" : False,
                           "n" : False})
    while bol:
        qs1 = input("Input Y / y to display Onsets or N / n to not: ")
        
    print("printing all possible onsets for file ", s, " ...")
    encoding_='utf-8'
    f = open(s,encoding=encoding_)
    bol = True
    while f.readable() and bol:
        s1 = f.readline()
        if len(s1) > 0:
            print(s1)
        else:
            bol = False
    print()
    input("press ENTER to continue.")
    print()
        


if __name__ == "__main__":
    main()
    




