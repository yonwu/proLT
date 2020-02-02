class Digraph:
    def __init__(self, vertices=None, edges=None):

        # assign edge values to a set variable, to avoid iterable error, have to check whether input is empty
        self.set_edges = set(x for x in edges) if edges else set()
        # union theory to collect set of unique vertex from edges and vertices input
        self.set_vertices = ((set(x[0] for x in edges) | set(x[1] for x in edges)) if edges else set()) | (
            set(vertices) if vertices else set())

    def vertices(self):
        return list(self.set_vertices)

    def edges(self):
        return list(self.set_edges)

    # use .add() and .update() functions in set to add edges and vertices
    def add_edge(self, source, dest):
        self.set_edges.add((source, dest))
        self.set_vertices.update([source, dest])

    # use .remove and .difference_update() in set to remove vertices and related edges
    def remove_vertices(self, vertex):
        self.set_vertices.remove(vertex)
        tmp_edges = self.edges()
        self.set_edges.difference_update(x for x in tmp_edges if vertex in x)

    # the idea is to find the transitive relation nodes for each vertex, and then use intersection theory in set
    # to check whether the graph is transitive or not transitive
    def is_transitive(self):
        vertex_value = []
        for key in self.vertices():
            values = set()
            for x in self.edges():
                if key in x:
                    values.update(x)
            vertex_value.append(values)
        tmp = vertex_value[1]
        for x in vertex_value:
            tmp = tmp & x
        if len(tmp) != 0:
            return True
        else:
            return False


# add a print result function to make the test part easier to read
def print_result(digraph):
    print(digraph.edges())
    print(digraph.vertices())


if __name__ == "__main__":
    print("Test of the class behavior, start..\n")
    print("The default for graph should be no edges and no vertices")
    d = Digraph()
    print_result(d)
    print("\n")
    print("It should be possible to instantiate a digraph giving the edges and the vertices (by name).")
    d1 = Digraph(edges=[(1, 2), (1, 3), (2, 3), (3, 5)], vertices=[1, 2, 3, 4])
    print_result(d1)
    print("\n")
    print("All vertices used by any edge are added automatically, and the parameter vertices only needs to mention "
          "additional (isolated) vertices")
    d2 = Digraph(edges=[(1, 2), (1, 3), (2, 3), (3, 3)], vertices=[4])
    print_result(d2)
    print("\n")
    print("A smaller graph that only have an isolated nodes.")
    d4 = Digraph(vertices=[1, 2, 3, 4])
    print_result(d4)
    print("\n")
    print("A smaller graph that doesn’t have an isolated node.")
    d3 = Digraph(edges=[(1, 2), (1, 3), (2, 3), (3, 3)])
    print_result(d3)
    print("\n")
    print("Test of adding edges.")
    d5 = Digraph(edges=[(1, 2), (1, 3), (2, 3), (3, 3)], vertices=[1, 2, 3, 4])
    print("Before adding edges:")
    print_result(d5)
    d5.add_edge(1, 5)
    print("After adding edges (1, 5):")
    print_result(d5)
    print("\n")
    print("Test of removing vertex.")
    d6 = Digraph(edges=[(1, 2), (1, 3), (2, 3), (3, 3)], vertices=[1, 2, 3, 4])
    print("Before removing vertex:")
    print_result(d6)
    d6.remove_vertices(3)
    print("After removing vertex 3:")
    print_result(d6)
    print("Test of transitive.")
    d7 = Digraph(edges=[(1, 2), (1, 3), (2, 3), (3, 3), (4, 5)], vertices=[1, 2, 3, 4, 5])
    print("A graph that is not transitive:")
    print_result(d7)
    print(d7.is_transitive())
    d8 = Digraph(edges=[(1, 2), (1, 3), (2, 3), (3, 3), (3, 4)], vertices=[1, 2, 3, 4])
    print("A graph that is transitive:")
    print_result(d8)
    print(d8.is_transitive())
