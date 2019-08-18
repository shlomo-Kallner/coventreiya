#  abc.py
#  
#  Copyright 2017 shlomo <shlomo.kallner@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

__package__ = "affix"
if __name__ != "__main__":
	__name__ = "coventreiya.morphology.affix.abc"

##################################################################
#
# Imports
#

from enum import Enum

from coventreiya.utils.ver import Versioned as __Versioned

from coventreiya.utils.lists import is_item_list
from coventreiya.utils.lists import is_same

from coventreiya.utils.phone import get_phonetic_symbol

from abc import ABCMeta, abstractmethod

from io import StringIO

##################################################################
#
# Morphology  -  Affix - ABC
#

class abc(__Versioned, metaclass=ABCMeta):
    def __init__(self, name="", value=None, has_cons=False, has_vowel=False, is_syl=False, 
                 has_neg=False, has_def=False, has_alt=False, has_null=True, 
                 #is_def=False, is_alt=False,
                 major=0, minor=0, patch=0, version=None):
        super().__init__(major, minor, patch, version)
        self.__name = str(name)
        if isinstance(value, int) or isinstance(value, Enum):
            self.__value = value
        else:
            raise TypeError()
        self.__has_consonant = bool(has_cons)
        self.__has_vowel = bool(has_vowel)
        self.__is_syllable = bool(is_syl)
        self.__has_negative = bool(has_neg)
        self.__has_default = bool(has_def)
        self.__has_alternative = bool(has_alt)
        self.__has_null = bool(has_null)
        #self.__is_default = bool(is_def)
        #self.__is_alternative = bool(is_alt)
    
    def name(self):
		return self.__name
		
	def value(self):
		return self.__value

    def has_negative(self):
        return self.__has_negative
        
    def has_null(self):
		return self.__has_null
	
	def gen_null(self):
		tmp = list()
		tmp.append("")
		return tmp

    def has_default(self):
        return self.__has_default

    #def is_default(self):
    #    """ Returns if this Realization is the default or not. """
    #    return self.__is_default

    #@abstractmethod
    #def get_default(self):
    #    """ Returns the default Realization of a given affix? """
    #    pass

    #def default(self):
    #    if self.has_default() and self.is_default():
    #        return self.get_default()
    #    else:
    #        return None

    def has_alternative(self):
        """
            Does a given Realization of an Affix have an Alternative Variant?
            Applies on a per Realization basis.
        """
        return self.__has_alternative

    #def is_alternative(self):
    #    """ Returns if this Realization is the alternative or not. """
    #    return self.__is_alternative

    #@abstractmethod
    #def get_alternative(self):
    #    """
    #        Returns the Alternative Realization if it exists,
    #         if it does not, return None.
    #        Applies on a Realization to Realization basis.
    #    """
    #    pass

    #def alternative(self):
    #    if self.has_alternative():
    #        return self.get_alternative()
    #    else:
    #        return None

    def has_consonant(self):
        return self.__has_consonant

    @abstractmethod
    def get_consonant(self):
        """
           Returns the Consonant as a List of a String.
           If Affix does not have a Consonant, returns an empty list.
        """
        pass

    def consonant(self):
        if self.has_consonant():
            return self.get_consonant()
        else:
            return list()

    def has_vowel(self):
        return self.__has_vowel

    @abstractmethod
    def get_vowel(self):
        """
           Returns the Vowel[s] as a List of Strings.
           If Affix does not have Vowel[s], returns an empty list.
        """
        pass

    def vowel(self):
        if self.has_vowel():
            return self.get_vowel()
        else:
            return list()

    def affix(self):
        """ Returns a given Affix Realization as a list of strings. """
        tmp = list()
        if self.has_consonant():
            tmp.extend(self.consonant())
        if self.has_vowel():
            tmp.extend(self.vowel())
        return tmp

    def is_syllable(self):
        return self.__is_syllable

    @abstractmethod
    def get_syllable(self):
        """ Returns a given Affix Realization as a Syllable. """
        pass

    def syllable(self):
        if self.is_syllable():
            return self.get_syllable()
        else:
            return None
            
    def str(self, strip=True, debug=True):
        cons_ = list()
        vols_ = list()
        if strip:
            if self.has_consonant():
                cTmp = self.consonant()
                for i in cTmp:
                    cons_.append(get_phonetic_symbol(i))
            if self.has_vowel():
                vTmp = self.vowel()
                for i in vTmp:
                    vols_.append(get_phonetic_symbol(i))
        else:
            cons_.extend(self.consonant())
            vols_.extend(self.vowel())
        if debug:
            str_ = "{0} , {1} : {2} , [ [{3}], [{4}] ]"
            return str_.format("coventreiya.morphology.affix.abc", 
                               self.name(), self.value(), cons_, vols_)
        else:
            strm = StringIO()
            if len(cons_) > 0:
                strm.write(list_str2Str(cons_))
            if len(vols_) > 0:
                strm.write(list_str2Str(vols_))
            return strm.getvalue()
            
    def __str__(self):
        return self.str(strip=True, debug=False)

    def __eq__(self, other):
        if isinstance(other,abc):
            return (self.has_negative() == other.has_negative()) \
                   and (self.name() == other.name())\
                   and (self.value() == other.value())\
                   and (self.has_null() == other.has_null())\
                   and (self.has_default() == other.has_default())\
                   and (self.has_alternative() == other.has_alternative())\
                   and (self.has_consonant() == other.has_consonant())\
                   and (self.has_vowel() == other.has_vowel())\
                   and (self.is_syllable() == other.is_syllable())\
                   # up to this point - comparing regardless of sub-class..
                   and (self.__class__ is other.__class__)\
                   and (self.version() == other.version())\
                   and ( is_same(self.consonant(), other.consonant()) )\
                   and ( is_same(self.vowel(), other.vowel()) )
        else:
            return NotImplemented
            
    def __comparitor_check(self, other):
        return isinstance(other,abc) \
        and (self.__class__ is other.__class__) \
        and (self.version() == other.version()) \
        and (self.name() == other.name()) \
        and (self.has_negative() == other.has_negative()) \
        and (self.has_null() == other.has_null()) \
        and (self.has_default() == other.has_default()) \
        and (self.has_alternative() == other.has_alternative()) \
        and (self.has_consonant() == other.has_consonant()) \
        and (self.has_vowel() == other.has_vowel()) \
        and (self.is_syllable() == other.is_syllable())

    def __ne__(self, other):
        if isinstance(other,abc):
            return not self == other
        else:
            return NotImplemented
            
    def __lt__(self, other):
        if self.__comparitor_check(other):
            return int(self.value()) < int(other.value())
        else:
            return NotImplemented
			
	def __gt__(self, other):
		if self.__comparitor_check(other):
			 return int(self.value()) > int(other.value())
        else:
			return NotImplemented
			
	def __le__(self, other):
        if self.__comparitor_check(other):
			 return int(self.value()) <= int(other.value())
        else:
			return NotImplemented
			
	def __ge__(self, other):
		if self.__comparitor_check(other):
			 return int(self.value()) >= int(other.value())
        else:
			return NotImplemented

    ########################################################################
    #
    # a few Internal Utility methods...
    # are these no longer needed since the modification of Open Syllables?
    #
    ########################################################################
    

    def match_or_null(self, mat, inp_):
        """
           If *mat* matches *inp_*, return *inp_*.
           ElseIf *inp_* is a list containing only an empty string,
           return *inp_*.
           Else return a list containing only an empty string.
        """
        if mat.is_allowable_input(inp_) \
           or (is_item_list(inp_) and len(inp_)==1 and inp_[0] == ""):
            return inp_
        else:
            tmp = list()
            tmp.append("")
            return tmp

    def match_or_raise(self, mat, inp_, err_=""):
        """
           If *mat* matches *inp_*, return *inp_*.
           Else raise a ValueError with *err_* as it's explanation string.
        """
        if mat.is_allowable_input(inp_):
            return inp_
        else:
            raise ValueError(err_)
        

##################################################################
#
# Morphology  -  Affix - Affix Set ABC
#

class set_abc(__Versioned):
    def __init__(self, cls, name="", has_neg=False, has_def=False, 
                 def_=None, def_idx=0, def_alt_=None,
                 major=0, minor=0, patch=0, version=None):
        super().__init__(major, minor, patch, version)
        self.__dict = dict()
        self.__name = str(name)
        self.__has_negative = bool(has_neg)
        self.__has_default = bool(has_def)
        if issubclass(type(cls),abc):
            self.__cls = type(cls)
        else:
            raise TypeError()
        if bool(has_def) and def_ is not None:
            self.add(def_idx, def_, def_alt_)
            self.__def_idx = int(def_idx)
        else:
            self.__def_idx = None
            if self.__has_default:
                self.__has_default = False
            
                
    def name(self):
		return self.__name
		
	def get_class(self):
		return self.__cls

    def has_negative(self):
        return self.__has_negative

    def has_default(self):
        return self.__has_default

    def is_default(self, def_):
        if isinstance(def_, self.__cls):
            if self.has_default():
                t = self.all_alternative(self.__def_idx)
                bol = False
                for i in t:
                    if def_ == i:
                        bol = True
                return bol
            else:
                # if we don't have a default return False always...
                return False
        else:
            raise TypeError()
            

    def default(self):
        #Note: may return None, and will if it were not set...
        if self.has_default:
            return self[self.__def_idx]
        else:
            return None

    def __check_index(self, index, setting=False):
        if issubclass(type(index),int):
            if int(index) < 0 and not self.has_negative():
                return False
            if setting:
                return not int(index) in self.__dict
            else:
                return True
        else:
            raise TypeError()

    def __getitem__(self, index):
        if self.__check_index(index):
			i = int(index)
            return self.__dict[i][0]
        else:
            raise IndexError()

    def __check_item_list(self, lst_):
        if is_item_list(lst_):
            bol = True
            for i in lst_:
                if not isinstance(i,self.__cls):
                    bol = False
            return bol
        else:
            return False

    def add(self, index, item, alt_item=None):
        """
            Raises IndexError if index is of the wrong type
            or if it's already in use.
            Raises TypeError if item is of the wrong type.
            If alt_item is of the wrong type - ignores alt_item.
        """
        if self.__check_index(index,True):
            i = int(index)
            if isinstance(item,self.__cls):
                t = list()
                t.append(item)
                if not alt_item is None and isinstance(alt_item,self.__cls):
                    t.append(alt_item)
                elif self.__check_item_list(alt_item):
                    t.extend(alt_item)
                self.__dict[i] = t
                return item
            elif self.__check_item_list(item):
                t = list(item)
                if not alt_item is None and isinstance(alt_item,self.__cls):
                    t.append(alt_item)
                elif self.__check_item_list(alt_item):
                    t.extend(alt_item)
                self.__dict[i] = t
                return item
            else:
                raise TypeError() 
        else:
            raise IndexError()

    def __setitem__(self, key, value):
        return self.add(key,value,None)

    def has_alternative(self, index):
        # returns if a given Realization has a alternative to itself.
        if self.__check_index(index):
            i = int(index)
            return len(self.__dict[i]) > 1
        else:
            raise IndexError()

    def num_alternative(self, index):
        if self.__check_index(index):
            i = int(index)
            return len(self.__dict[i]) - 1
        else:
            raise IndexError()

    def get_alternative(self, index):
        if self.__check_index(index):
            i = int(index)
            return self.__dict[i][1]
        else:
            raise IndexError()

    def all_alternative(self, index):
        # gets all realization for a given index
        # - including the regular one.
        if self.__check_index(index):
            i = int(index)
            return list(self.__dict[i])
        else:
            raise IndexError()

    def keys(self, sort_=True):
        lst = list(self.__dict.keys())
        if sort_:
            lst.sort()
        return lst

    def __contains__(self, item):
        if isinstance(item, self.__cls):
            bol = False
            for i in self.__dict.values():
                # as i will be a list...
                if item in i:
                    bol = True
            return bol
        elif issubclass(type(item),int):
            return int(item) in self.keys(False)
        else:
            raise TypeError()

    def __iter__(self):
        lst = self.keys()
        for i in lst:
            yield self.__dict[i][0]
        raise StopIteration()
    
    def __len__(self):
		return len(list(self.keys(False)))
        
    def __str__(self):
        str_ = "{0} - {1} , {2} :\n[\n[ {3} ],\n[ {4} ]\n]"
        def_ = "Default: {0}".format(self.default())
        items_ = list()
        item_ = "Index {0} : [ {1} ]\n"
        for i in self.keys():
            items_.append(item_.format(i, self.all_alternative(i)))
        return str_.format("coventreiya.morphology.affix.set_abc", 
                           self.get_class(), self.name(), def_, items_)

        
            
                          


    
