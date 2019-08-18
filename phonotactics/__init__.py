
#__path__ = ['I:\\my_stuff\\temp_media\\work\\ProtectorsOfSpaceAndTime\\Coventreiya\\scripts',
#            'I:\\my_stuff\\temp_media\\work\\ProtectorsOfSpaceAndTime\\Coventreiya\\scripts\\utils',
#            'I:\\my_stuff\\temp_media\\work\\ProtectorsOfSpaceAndTime\\Coventreiya\\scripts\\phonotactics'
#            'I:\\my_stuff\\temp_media\\work\\ProtectorsOfSpaceAndTime\\Coventreiya\\scripts\\phonology' ]

#__name__ = 'phonotactics'
__package__ = 'phonotactics'
#__version__ = "1.5.1"
__all__ = [ 'abc', 'onsets', 'nucleus', 'codas' ]

#__doc__ = """
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
############################################################################
#         """
