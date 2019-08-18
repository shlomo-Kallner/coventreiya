__name__ = "lists"


import functools
from io import StringIO

##################################################################
#
#          lists and collections utility functions:
#

def is_item_list( item ):
    return ( isinstance(item, list) or isinstance(item, tuple) )

def list_str2Str( list_ ):
	if is_item_list(list_):
		strm = StringIO()
		for i in list_:
			if isinstance(i,str):
				strm.write(i)
			elif is_item_list(i):
				strm.write(list_str2Str(i))
			else:
				raise ValueError()
		return strm.getvalue()
	else:
		raise ValueError()
		
def are_list_items( list_, cls_ ):
	if is_item_list( list_ ):
		bol = True
		for i in list_:
			if not isinstance(i, cls_):
				bol = False
		return bol
	else:
		return False
		
def not_empty_list_items_are( list_, cls_ ):
	if is_item_list( list_ ) and len(list_) > 0:
		return are_list_items( list_, cls_ )
	else:
		return False

def is_sequence( item ):
	if hasattr(item, "__len__"):
		if hasattr(item, "__getitem__"):
			if hasattr(item, "__iter__"):
				if hasattr(item, "__contains__"):
					return True
	return False
	
def is_mapping( item ):
	if is_sequence(item):
		if hasattr(item, "keys"):
			return True
	return False
             
def is_list_of_lists( list_ ):
	if is_item_list( list_ ):
		bol = True
		for i in list_:
			if not is_item_list(i):
				bol = False
		return bol
	else:
		raise TypeError()

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


def cmp_len( list1_, list2_ ):
    if is_item_list(list1_) and is_item_list(list2_):
        if len(list1_) > len(list2_):
            return 1
        elif len(list1_) < len(list2_):
            return -1
        else:
            return 0
    else:
        raise TypeError()

comp_len = functools.cmp_to_key(cmp_len)

def is_same( list1_, list2 ):
    if is_item_list(list1_) and is_item_list(list2_):
        if cmp_len(list1_, list2) == 0:
            bol = True
            for i in range(0, len(list1_)):
                if is_item_list(list1_[i]) and is_item_list(list2_[i]):
                    if not is_same( list1_[i], list2_[i] ):
                        bol = False
                elif isinstance(list2_[i], list1_[i].__class__):
                    if list1_[i] != list2_[i]:
                        bol = False
            return bol
        else:
            return False
    else:
        raise TypeError()
#
#
################################################################
