import collections
import graph.graph_representation.graphs_api as graphs_api


class PathsDFS:
    def __init__(self, graph: graphs_api.Graph, s: int):
        v = graph.number_of_vertices()

        self.S = s
        self.marked = [False] * v
        # for i in range(v):
        #     self.edge_to_v[i] = -1
        self.edge_to_v = [-1] * v
        print("Now we will run DFS to build paths")
        self.dfs(graph, s)

    def has_path_to(self, v: int) -> bool:
        """ Query 1: Has source vertex s has path to vertex v?
        """
        return self.marked[v]

    def path_to(self, v: int) -> collections.deque:
        """ Query 2: If source vertex s has path to v, return the path
            (list of vertex in order). None if no such path.
        """
        if not self.has_path_to(v):
            return None
        path = collections.deque()
        x = v
        while self.edge_to_v[x] != -1:
            path.append(x)
            x = self.edge_to_v[x]
        return path

    def dfs(self, graph, v):
        self.marked[v] = True
        for w in graph.adjacent(v):
            if not self.marked[w]:
                self.dfs(graph, w)
                self.edge_to_v[w] = v


class PathsBFS:
    def __init__(self, graph: graphs_api.Graph, s: int):
        v = graph.number_of_vertices()

        self.S = s
        self.marked = [False] * v
        self.edge_to_v = [-1] * v
        self.dist_to_v = [-1] * v
        print("Now we will run BFS to build paths")
        queue = collections.deque()
        queue.append(s)
        dist = 0
        self.dist_to_v[s] = dist
        self.marked[s] = True
        while len(queue) > 0:
            v = queue.popleft()
            # print(v)
            for w in graph.adjacent(v):
                # print("-- %r" % w)
                dist += 1
                if not self.marked[w]:
                    # print("--- %r" % self.marked[w])
                    self.marked[w] = True
                    self.edge_to_v[w] = v
                    self.dist_to_v[v] = dist
                    queue.append(w)

    def has_path_to(self, v: int) -> bool:
        """ Query 1: Has source vertex s has path to vertex v?
        """
        return self.marked[v]

    def path_to(self, v: int) -> collections.deque:
        """ Query 2: If source vertex s has path to v, return the path
            (list of vertex in order). None if no such path.
        """
        if not self.has_path_to(v):
            return None
        path = collections.deque()
        x = v
        while self.edge_to_v[x] != -1:
            path.append(x)
            x = self.edge_to_v[x]
        return path
