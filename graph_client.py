import graph.graph_representation.graphs_api as ga
import sys


if __name__ == "__main__":
    inp = []
    for line in sys.stdin:
        inp.append(line)
    g = ga.Graph(inp=inp)
    # print("%r" % g)
    x = g.number_of_vertices()
    # print(f"number of vertices are {x}")
    for v in range(0, g.number_of_vertices()):
        """ For every vertex in graph_representation """
        for w in g.adjacent(v):
            print(f"{v}  - {w}")
