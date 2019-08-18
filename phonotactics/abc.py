__name__ = 'ABC'
#__version = '1.5.1'
#__package__ = 'phonotactics'


# imports

#some import machinery checking and manipulations...
#import sys
#import os
#from os import path
#if '__file__' in dir():
#    __mod_path = path.dirname(__file__)
#    if __mod_path not in sys.path:
#        sys.path.append(__mod_path)
#    __pack_path = path.dirname(__mod_path)
#    if __pack_path not in sys.path:
#        sys.path.append(__pack_path)
    


from coventreiya.utils.ver import Versioned
from coventreiya.utils.fsm import fsm_state, fsm_transversal
from coventreiya.utils import gen, lists

from coventreiya.utils.matcher import fsm_Matcher

from abc import ABCMeta, abstractmethod

####################################################################
#
#
#
#     The Abstract Base Class for all Phonotactical sub-Classes
#
#

class abc(fsm_Matcher):
	def __init__(self, min_length=0, max_length=0, 
                 major=0, minor=0, patch=0, version=None):
		super().__init__(min_length, max_length, str,
                 major, minor, patch, version)
    
    pass

class old_abc(Versioned, metaclass=ABCMeta)):
    def __init__(self, min_length=0, max_length=0, 
                 major=0, minor=0, patch=0, version=None):
        super().__init__(major, minor, patch, version)
        self.__length = tuple([min_length,max_length])
        tmp = self.finite_state_machine()
        self.__fsm = tmp[0]
        self.__fsm_start = tmp[1]
        #self.__cat = self.categories()
        #self.__repl_map = self.replacment_map()
    
    def fsm_start(self):
        ''' Returns the Finite State Machine's Start State '''
        return self.__fsm_start 

    def min_length(self):
        return self.__length[0] 

    def max_length(self):
        return self.__length[1] 

    #def categories(self):
    #    return self.__cat 

    #def replacment_map(self):
    #    return self.__repl_map 

    def num_categories(self):
        return len(self.categories())

    @abstractmethod
    def finite_state_machine(self):
        """ Generates the full Finite State Machine """
        """ and returns it and the Starting State as a Tuple. """
        pass

    @abstractmethod
    def categories(self):
        ''' Generate the Categories Lists. '''
        pass

    @abstractmethod
    def replacment_map(self):
        ''' Generate the Replacement Map. '''
        pass

    def all_allowable_sets_(self):
        fsm_ = self.fsm_start()
        t = gen.gen_list( self.max_length() ,
                          [ x for x in range(0,self.num_categories()) ] ,
                          self.min_length() )
        results = list()
        for i in t:
            if fsm_transversal( i, fsm_ ):
                results.append(i)
        return results

    def actuals_per_set(self, set_):
		"""WARNING! this method takes up a Huge amount of memory!"""
        repl_map = self.replacment_map()
        return gen.gen_replace_str1( set_, repl_map )

    def actuals_per_set_to_file(self, set_, path, encoding_='utf-8'):
        repl_map = self.replacment_map()
        return gen.gen_replace_str_to_file( set_, repl_map, path, encoding_ )

    def all_actuals(self):
        """WARNING! this method takes up a Huge amount of memory!"""
        t = self.all_allowable_sets_()
        repl_map = self.replacment_map()
        return gen.gen_actual(t, repl_map)

    def all_actuals_to_file(self, path, encoding_='utf-8'):
        t = self.all_allowable_sets_()
        repl_map = self.replacment_map()
        return gen.gen_actual_file(t, repl_map, path, encoding_)

    def is_allowable_input(self, inp_):
        """ Checks whether the input (assumed to be a Container)
            conforms to the specs of an "input stream"
            ===> a list/tuple of strings (of at least one string).
            Also checks input stream length.
            Returns True if acceptable, False if not.
        """
        if lists.is_item_list(inp_):
            if self.__length[0] <= len(inp_) <= self.__length[1]:
                bol = True
                for i in inp_:
                    if not isinstance(i,str):
                        bol = False
                return bol
            else:
                return False
        else:
            return False

    def is_allowable_set( self, inp_ ):
        """ 
           Checks whether (inp_) is a list of 
           Phonemes that form a valid input.
           Returns True if acceptable, False if not.
        """
        if not self.is_allowable_input(inp_):
            return False
        tmp = self.all_allowable_sets_()
        repl_map = self.replacment_map()
        sets_ = list()
        for i in tmp:
            if len(i) == len(inp_):
                sets_.append(i)
        allowing_sets = 0
        for i in sets_:
            boll1 = True
            for j in range(0,len(inp_)):
                if inp_[j] not in repl_map[i[j]]:
                    boll1 = False
            if boll1:
                allowing_sets += 1
        return allowing_sets != 0

    



