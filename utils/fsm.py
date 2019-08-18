
#__modname__ = ["fsm"]

from lists import is_item_list

#__all__ = [ 'fsm_state', 'fsm_transversal' ]

################################################################
#
#
# the finite state machine type and utility function:


class fsm_state:
    def __init__(self, name, value, mapping = {}):
        self.__value = value
        self.__mapping = mapping
        self.__name = name

    def name(self):
        return self.__name

    def value(self):
        return self.__value

    def remap(self, value, mapping):
        self.__mapping = mapping
        self.__value = value

    def map_transversal(self, key):
        return self.__mapping[key]


def fsm_transversal(inputs, start_state):
    if isinstance(start_state, fsm_state) and is_item_list(inputs):
        fsm_ = start_state
        for i in inputs:
            fsm_ = fsm_.map_transversal(i)
        return fsm_.value()
    else:
        raise TypeError()

#
#
##################################################################
