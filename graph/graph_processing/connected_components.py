import collections
import graph.graph_representation.graphs_api as graphs_api


class ConnectedComponent:

    def __init__(self, graph: graphs_api.Graph, s: int):
        v = graph.number_of_vertices()

        self.S = s
        self.marked = [False] * v
        self.id = [-1] * v
        self.count = 0
        for i in range(0, v):
            if not self.marked[v]:
                self.dfs(graph, s)
                self.count += 1

    def dfs(self, graph, v):
        self.marked[v] = True
        self.id[v] = self.count
        for w in graph.adjacent(v):
            if not self.marked[w]:
                self.dfs(graph, w)

    def count(self):
        return self.count()

    def id(self, v):
        return self.id[v]