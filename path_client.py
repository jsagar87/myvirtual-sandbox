import sys
import graph.graph_processing.path as path
from graph.graph_representation.graphs_api import Graph

if __name__ == "__main__":
    inp = []
    for line in sys.stdin:
        inp.append(line)
    g = Graph(inp=inp)
    # All the paths from source 0
    paths = path.PathsBFS(g, 0)

    for v in range(0, g.number_of_vertices()):
        """ For every vertex in graph_representation 
            Print all vertices connected to s
        """
        if paths.has_path_to(v):
            print("Path to %r" % v)
            print(paths.path_to(v))
        else:
            print("No Path to %r" % v)
