import heapq
class module:
    def __init__(self, name, port = []):
        '''module.name
           module.port: port list of v_port object '''
        self.name = name
        self.port = []
        for i in port :
            heapq.heappush(self.port, i)

    def add_port(self, port_item):
        heapq.heappush(self.port, port_item)


