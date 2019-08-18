import


def check_list_end( res, tmp ):
    if isinstance(res. list) and \
       ( isinstance(tmp, tuple) or isinstance(tmp. list) ):
        if tmp[0] == True and \
           tmp[1] == True and \
           tmp[2] == True and \
           tmp[3] == True and \
           tmp[4] == True and \
           tmp[5] == True and \
           tmp[6] == True and \
           is_item_in_list(res, tmp):
            return True
        else:
            return False
    else:
        raise TypeError()



req = 1
opt = 2
drg = 3
dgs = 4

def find_drg( arr ):
    i = 0
    for j in range(0, len(arr):
        if arr[j] == drg:
            i = j
    return i
                

syn = [ opt, req , opt, opt, drg, dgs, opt ]
#idxes   0    1    2    3    4    5     6
#      "(C2)  C1  (C1) (C3) (S   (S)) ('ʕ̞')"

syn1 = [ opt, opt, opt, drg, dgs, opt ]
#idxs     0    1    2    3    4    5


def is_item_list( item ):
    return ( isinstance(list_, list) or \
             isinstance(list_, tuple) )

        

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



def gen_str( num_chars, iter_ ):
    str_ = list()
    if num_chars > 1 \
       and ( isinstance(iter_,tuple) \
             or isinstance(iter_,list) ):
                   for i in range(0,num_chars):
                       str_.append(next(iter_[i]))
    elif num_chars == 1 and iter_.__dict__['__next__'] is not None:
            str_.append(next(iter_))
    else:
            raise ValueError("num_char must be 1 or greater!")
    return str_



def gen_list_of_lists_of_chars( num, pos_chars ):
    result = list()
    if not is_item_list(pos_chars) or not isinstance(num,int):
      raise TypeError()
    elif num <= 0 :
      raise ValueError()
    elif num == 1:
        tmp = None
        for i in pos_chars:
            tmp = list()
            tmp.append(i)
            result.append(tmp)
    else:
        # total number of strings to generate is equal to
        # the number of possible chars per position to the power of
        # the length of string to generate.
        tmp = None
        iter_ = iter(pos_chars)
        for i in pos_chars:
            for j in range(0, num):
                tmp = list()
            j = None
            try:
                j = next(iter_)
            except StopIteration as n__:
                   iter_ = iter(pos_chars)
                   j = next(iter_)
            tmp.append(j)
            result.append(tmp)
        for 
                   
        


def gen_list1( max_chars, pos_chars, min_chars = 1 ):
    result = list()
    if ( not isinstance(pos_chars, list) \
         or not isinstance(pos_chars, tuple) ) \
        and ( not isinstance(max_chars,int) \
              not isinstance(min_chars,int) ):
        raise TypeError()
    elif min_chars > 0 and max_chars > min_chars:
        # for 
        for i in range(min_chars, max_chars + 1):
            tmp = None
            if i == 1 :
                for j in pos_chars:
                   tmp = list()
                   tmp.append(j)
                   if not is_item_in_list(result, tmp):
                      result.append(tmp)
            elif i > 1 :
                tmp = list()
                # tmp is the cur str being gen-ed
                # i is the current number of chars to gen per str
                # the number of posibilities is
                #   total possible chars to the power of the number to gen.
                for j in pos_chars:
                   for k in range(min_chars, i):
                     tmp.append(j)
                for j in tmp:
                    
                     tmp.append(k)
                     for m in pos_chars:
                       tmp.append
                     
                     
                         
                       
                   
                   
                   
                    







        
