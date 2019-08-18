#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  matcher.py
#  
#  Copyright 2017 DELL <DELL@DELL-PC>
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

__package__ = "utils"
if __name__ != '__main__':
        __name__ = "coventreiya.utils.matcher"

##################################################################
#
# Imports
#

    

# coventreiya.utils.
from ver import Versioned
from fsm import fsm_state, fsm_transversal
from gen import gen_list, gen_replace_str1
from gen import gen_replace_str_to_file 
from gen import gen_actual
from gen import gen_actual_file
from lists import is_item_list

from abc import ABCMeta, abstractmethod

####################################################################
#
#
#
#     The Abstract Base Class for all Matcher sub-Classes
#
#
class Matcher(Versioned, metaclass=ABCMeta):
        def __init__(self, min_length=0, max_length=0, sub_cls=str,
                     major=0, minor=0, patch=0, version=None):
                super().__init__(major, minor, patch, version)
                self.__length = tuple([min_length,max_length])
                #self.__cat = self.__categories() 
                #self.__repl_map = self.__replacment_map()  
                self.__sub_cls = sub_cls

        def min_length(self):
                return self.__length[0]

        def max_length(self):
                return self.__length[1]

        #def categories(self):
        #        return self.__categories() #self.__cat

        #def replacment_map(self):
        #        return self.__replacment_map()  #self.__repl_map

        def num_categories(self):
                return len(self.categories())

        @abstractmethod
        def categories(self):
                ''' Generate the Categories Lists. '''
                pass

        @abstractmethod
        def replacment_map(self):
                ''' Generate the Replacement Map. '''
                pass

        @abstractmethod
        def matcher_func(self, inp_):
                """
                The Function that DOES the Matching based
		on some Input (*inp_*) and some Match Data Object
		contained in the Sub-Class Implementing this method.
		Returns True or False.
		"""
                pass

        def all_allowable_sets_(self):
                tmp = gen_list( self.max_length() ,
                                [ x for x in range(0,self.num_categories()) ] ,
                                self.min_length() )
                results = list()
                for i in tmp:
                        if self.matcher_func( i ):
                                results.append(i)
                return results

        def actuals_per_set(self, set_):
                """WARNING! this method takes up a Huge amount of memory!"""
                repl_map = self.replacment_map()
                return gen_replace_str1( set_, repl_map )

        def actuals_per_set_to_file(self, set_, path, encoding_='utf-8'):
                repl_map = self.replacment_map()
                return gen_replace_str_to_file( set_, repl_map, path, encoding_ )

        def all_actuals(self):
                """WARNING! this method takes up a Huge amount of memory!"""
                t = self.all_allowable_sets_()
                repl_map = self.replacment_map()
                return gen_actual(t, repl_map)

        def all_actuals_to_file(self, path, encoding_='utf-8'):
                t = self.all_allowable_sets_()
                repl_map = self.replacment_map()
                return gen_actual_file(t, repl_map, path, encoding_)

        def is_allowable_input(self, inp_):
                """ Checks whether the input (assumed to be a Container)
                    conforms to the specs of an "input stream"
                    ===> a list/tuple of "strings" (of at least one "string").
                    Also checks input stream length.
                    Returns True if acceptable, False if not.
                """
                if is_item_list(inp_):
                        if self.__length[0] <= len(inp_) <= self.__length[1]:
                                bol = True
                                for i in inp_:
                                        if not isinstance(i,self.__sub_cls):
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


class fsm_Matcher(Matcher):
        def __init__(self, min_length=0, max_length=0, sub_cls=str,
                     major=0, minor=0, patch=0, version=None):
                super().__init__( min_length, max_length, sub_cls,
                                  major, minor, patch, version)
                tmp = self.finite_state_machine()
                self.__fsm = tmp[0]
                self.__fsm_start = tmp[1]

        @abstractmethod
        def finite_state_machine(self):
                """ Generates the full Finite State Machine """
                """ and returns it and the Starting State as a Tuple. """
                pass

        def fsm_start(self):
                ''' Returns the Finite State Machine's Start State '''
                return self.__fsm_start

        #def __matcher(self):
        #	return self.finite_state_machine()

        def matcher_func(self, inp_):
                """
		The Function that DOES the Matching based
		on some Input (*inp_*) and some Match Data Object...
		"""
                return fsm_transversal(inp_, self.__fsm_start)

        pass 
    


##################################################################
#
# Tests Main
#

class tester(Matcher):
        def __init__(self, min_length=1, max_length=4):
                super().__init__( min_length, max_length, str,
                                  1, 1, 1, None)

        def categories(self):
                ''' Generate the Categories Lists. '''
                cat_ = list()
                for i in ['a','b','c','d','e','f','g','h']:
                        tmp = list()
                        for j in range(0,10):
                                tmp.append( "{},{}".format(i,j) )
                        cat_.append( tmp )
                return cat_

        def replacment_map(self):
                ''' Generate the Replacement Map. '''
                cat_ = self.categories()
                repl_map = {}
                for i in range(0,len(cat_)):
                        repl_map[i] = cat_[i]
                return repl_map

        def matcher_func(self, inp_):
                """
		The Function that DOES the Matching based
		on some Input (*inp_*) and some Match Data Object
		contained in the Sub-Class Implementing this method.
		Returns True or False.
		"""
                bol = True
                tmp = list()
                for i in inp_:
                        if i not in tmp:
                                tmp.append(i)
                        else:
                                bol = False
                return bol

        pass

def main(args):
        test_ = tester()
        for i in test_.all_allowable_sets_():
                print(i)
        for i in test_.all_actuals():
                print(i)
        input("press Enter to Continue.")
        return 0

if __name__ == '__main__':
        import sys
        m1_ = main(sys.argv)
        sys.exit(m1_)
