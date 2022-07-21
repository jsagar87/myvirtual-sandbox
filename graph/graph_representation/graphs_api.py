# adjacency list repr
class Graph:

    def __init__(self, V=0, inp=None):
        self.V = 0
        self.E = 0
        if V != 0:
            self.V = V
            self.adj = [0]*V
            for i in range(0, V):
                self.adj[i] = list()

        if inp:
            self.V = int(inp[0])
            # self.E = int(inp[1]) # Lets commonly stay dependent on add_edge method
            self.adj = list()
            for _ in range(0, self.V):
                self.adj.append(list())
            for ln in inp[2:]:
                edges = ln.split(" ")
                self.add_edge(int(edges[0]), int(edges[1]))

    def add_edge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.E += 1

    def adjacent(self, v):
        return self.adj[v]

    def number_of_vertices(self) -> int:
        """ Returns number of vertices"""
        return self.V

    def number_of_edges(self) -> int:
        """ Returns number of edges"""
        return self.E

    def __repr__(self):
        return self.adj.__repr__()

# class Glass:
#     def __init__(self, name, timestamp=0):
#         self.__name = name
#         self.__timestamp = timestamp
#
#     def __eq__(self, other):
#         return self.__name == other.__name
#
#
# G1 = Glass("G1")
# G2 = Glass("G1")
# G3 = Glass("G1")
#
# cmp = G1 == G2
#
# print(cmp)
