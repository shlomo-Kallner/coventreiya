
__name__ = ["utils"]


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
    results = list()
    for i in list_:
        j = gen_replace_str1( i, repl_map )
        results.extend(j)
    return results

def gen_actual_file(list_, repl_map, path, encoding_='utf-8'):
    results = 0
    f = open(path, "w", encoding=encoding_)
    for i in list_:
        t1 = gen_replace_str1( i, repl_map )
        for j in t1:
            print(j, file=f)
            results += 1
    return results




#
#
################################################################

