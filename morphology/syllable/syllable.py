##################################################################
#
# Imports
#

from coventreiya.utils.ver import Versioned

from coventreiya.utils.lists import is_item_list
from coventreiya.utils.lists import list_str2Str

from coventreiya.utils.phone import get_phonetic_symbol

from io import StringIO

from abc import ABCMeta, abstractmethod

##################################################################
#
# Morphology  -  Syllables
#

class Syllable(Versioned, metaclass=ABCMeta):
    def __init__(self, has_onset=False, has_nucleus=False, has_coda=False,
                 major=0, minor=0, patch=0, version=None):
        super().__init__(major, minor, patch, version)
        self.__has_onset = bool(has_onset)
        self.__has_nucleus = bool(has_nucleus)
        self.__has_coda = bool(has_coda)
        
    def has_onset(self):
        return self.__has_onset

    def has_nucleus(self):
        return self.__has_nucleus

    def has_coda(self):
        return self.__has_coda

    @abstractmethod
    def get_onset(self):
        pass
        
    def onset(self):
        if self.__has_onset:
            return self.get_onset()
        else:
            return list()

    @abstractmethod
    def get_onset_matcher(self):
        pass
        
    def onset_matcher(self):
        if self.__has_onset:
            return self.get_onset_matcher()
        else:
            return None

    @abstractmethod
    def get_nucleus(self):
        pass

    def nucleus(self):
        if self.__has_nucleus:
            return self.get_nucleus()
        else:
            return list()

    @abstractmethod
    def get_nucleus_matcher(self):
        pass

    def nucleus_matcher(self):
        if self.__has_nucleus:
            return self.get_nucleus_matcher()
        else:
            return None

    @abstractmethod
    def get_coda(self):
        pass

    def coda(self):
        if self.__has_coda:
            return self.get_coda()
        else:
            return list()

    @abstractmethod
    def get_coda_matcher(self):
        pass

    def coda_matcher(self):
        if self.__has_coda:
            return self.get_coda_matcher()
        else:
            return None

    def syllable(self):
        """
           Return the whole Syllable as a single list.
           Does not do any Phonetic/Phonemic Marking stripping.
        """
        tmp = list()
        if self.__has_onset:
            tmp.extend(self.get_onset())
        if self.__has_nucleus:
            tmp.extend(self.get_nucleus())
        if self.__has_coda:
			tmp.extend(self.get_coda())
        return tmp

    def str(self, strip=True):
        """
           Return whole Syllable as a single string.
           if *strip* is True (the default), removes all phonetic
           /phonemic markings (a.k.a. the '/'-es and '[',']'-es).
           else does not.
        """
        if strip:
			strm = StringIO()
			for i in self.syllable():
				strm.write(get_phonetic_symbol(i))
			return strm.getvalue()
        else:
			return list_str2Str(self.syllable())
        

    def __str__(self):
		return self.str(True)
		
	

    

