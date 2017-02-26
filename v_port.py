from functools import total_ordering
from collections import namedtuple
PORT_ITEM = ['dir', 'name', 'type',  'length', 'start', 'end', 'comment']
V_PORT = namedtuple('V_PORT', PORT_ITEM)

@total_ordering
class v_port:
    def __init__(self, p_drect = 'input', name = "", p_type = 'reg',  length = 1, start = 0, comment = ""):
        self.port = V_PORT(p_drect, name, p_type, length, start, start + length -1 , comment)

    def __eq__(self,other):
        return self.port == other.port

    def __lt__(self,other):
        return self.port < other.port



