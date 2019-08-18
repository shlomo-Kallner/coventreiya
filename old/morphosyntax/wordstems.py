



##################################################################
#
#
# Imports

from coventreiya.utils.ver import ver
from coventreiya.utils.ver import gen_ver
from coventreiya.utils.ver import Version_Registry



##################################################################
#
#
# Morphosyntax - Word Stems

class Infixes:
    def __init__(self, major=0, minor=0, patch=0, version=None, pos={}, value=None):
        self.__version = gen_ver(major, minor, patch, version)
        self.__pos = pos
        self.__value = value

    def value(self):
        return self.__value

    def pos(self):
        return self.__pos

class Word_Stem:
    def __init__(self, major=0, minor=0, patch=0, version=None, root=[], infixes=[]):
        self.__version = gen_ver(major, minor, patch, version)
        self.__root = root
        self.__infixes = infixes

    def __len__(self):
        ''' Returns the Word Stem length in Syllables. '''
        return len(self.__root)

    pass



 
