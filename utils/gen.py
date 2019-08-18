#  gen.py
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



__all__ = ['gen_str', 'gen_str1', 'gen_list', 'gen_replace_str',
           'gen_replace_str1', 'get_n_actuals', 'gen_actual',
           'gen_actual_file' ]

if __name__ != "__main__":
	__name__ = "gen"
from lists import is_item_list, is_list_of_lists

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
        
def is_unique(list_):
	if is_item_list(list_):
		res = True
		dic_ = dict()
		for i in list_:
			if i not in dic_.keys():
				dic_[i] = 1
			else:
				dic_[i] += 1
		for i in dic_.keys():
			if dic_[i] > 1:
				res = False
		return res
	else:
		raise TypeError()
		
def gen_unique(list_):
	if is_item_list(list_):
		res = list()
		for i in list_:
			if is_unique(i):
				res.append(i)
		return res
	else:
		raise TypeError()
				

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

def gen_replace_str_to_file( inp, repl, path, encoding_='utf-8'):
    if is_item_list(inp) and isinstance(repl,dict) \
       and isinstance(path, str) and isinstance(encoding_,str):
        f = open(path, "w", encoding=encoding_)
        tmp = gen_replace_str1( inp, repl )
        for j in tmp:
            print(j, file=f)
        f.close()
        return len(tmp)
    else:
        raise TypeError()

def get_n_actuals(list_, repl_map):
    """ Gets the number of actual strings. """
    results = 0
    if is_item_list(list_) and isinstance(repl_map,dict):
        for item in list_:
            tmp = 0
            if is_item_list(item):
                for i in range(0,len(item)):
                    tmp1 = len(repl_map[item[i]])
                    if i == 0:
                        tmp = tmp1
                    else:
                        tmp *= tmp1
            results += tmp
        return results
    else:
        raise TypeError()

def gen_actual(list_, repl_map):
    """ WARNING!!! this fuction (depending on the list) """
    """ may use A LOT of memory and may crash python!!!"""
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
        f.close()
        return results
    else:
        raise TypeError()


def gen_list_from_lists(*list_):
    if len(list_) > 0:
        for i in list_:
            if not is_item_list(i):
                raise TypeError("Argument must be a list/tuple/vararg of lists!")
        res = list()
        for i in range(0, len(list_)):
            if i == 0:
                for j in list_[0]:
                    t = list()
                    t.append(j)
                    res.append(t)
            else:
                tmp = list()
                for j in list_[i]:
                    for k in res:
                        t = list()
                        t.extend(k)
                        t.append(j)
                        tmp.append(t)
                res = tmp
        return res
    else:
        raise TypeError()
                       
def gen_list_from_lists1(list_):
    if len(list_) > 0:
        for i in list_:
            if not is_item_list(i):
                raise TypeError("Argument must be a list/tuple of lists!")
        res = list()
        for i in range(0, len(list_)):
            if i == 0:
                for j in list_[0]:
                    t = list()
                    t.append(j)
                    res.append(t)
            else:
                tmp = list()
                for j in list_[i]:
                    for k in res:
                        t = list()
                        t.extend(k)
                        t.append(j)
                        tmp.append(t)
                res = tmp
        return res
    else:
        raise TypeError()

def gen_list_from_lists2(*list_):
    if len(list_) > 0:
        for i in list_:
            if not is_item_list(i):
                raise TypeError("Argument must be a list/tuple/vararg of lists!")
        res = list()
        for i in range(0, len(list_)):
            if i == 0:
                for j in list_[0]:
                    t = list()
                    t.append(j)
                    res.append(t)
            else:
                tmp = list()
                for j in list_[i]:
                    for k in res:
                        t = list()
                        t.extend(k)
                        t.append(j)
                        tmp.append(t)
                res = tmp
        return res
    else:
        raise TypeError()
                       
def gen_generic_list_( char_, num_ ):
	return [ char_ + str(x) for x in range(1,num_ +1) ]
    
def gen_list_from_dict( dict_ ):
	tmp = list()
	for i in iter(dict_):
		tmp.append( gen_generic_list_(i, dict_[i]))
	return tmp                       

def print_list(list_):
	if is_item_list(list_):
		for i in list_:
			print(i)
	else:
		raise TypeError()



                       

#
#
################################################################


##################################################################
#
# Tests Main
#

def main(args):
	repl = { 0 : ['a1','a2','a3'],
	         1 : ['b1','b2','b3'],
	         2 : ['c1','c2','c3'],
	         3 : ['d1','d2','d3'],
	         4 : ['e1','e2','e3'],
	         5 : ['f1','f2','f3'] }
    t1 = gen_list(2,[ x for x in [0,1] ], 1)
    t2 = gen_list(4,[ x for x in [0,1,4,5] ],3)
    t3 = gen_str1(6,[ x for x in range(0,6)])
    print("len(t1) = ",len(t1))
    print("len(t2) = ",len(t2))
    print("len(t3) = ",len(t3))
    t1a = gen_unique(t1)
    t2a = gen_unique(t2)
    t3a = gen_unique(t3)
    print("len(t1a) = ",len(t1a))
    print("len(t2a) = ",len(t2a))
    print("len(t3a) = ",len(t3a))
    t1b = gen_actual(t1a, repl)
    t2b = gen_actual(t2a, repl)
    t3b = gen_actual(t3a,repl)
    print("len(t1b) = ",len(t1b))
    print("len(t2b) = ",len(t2b))
    print("len(t3b) = ",len(t3b))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
