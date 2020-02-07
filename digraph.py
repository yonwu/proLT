from itertools import combinations


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
    def remove_vertex(self, vertex):
        self.set_vertices.remove(vertex)
        tmp_edges = self.edges()
        self.set_edges.difference_update(x for x in tmp_edges if vertex in x)

    def is_transitive(self):
        for i in range(0, len(self.edges())):
            for j in range(0, len(self.edges())):
                if self.edges()[i][1] == self.edges()[j][0]:
                    if (self.edges()[i][0], self.edges()[j][1]) in self.edges():
                        continue
                    else:
                        return False
        return True


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
    d6.remove_vertex(3)
    print("After removing vertex 3:")
    print_result(d6)
    print("Test of transitive.")
    d7 = Digraph(edges=[(2, 3), (1, 3), (1, 2), (2, 4), (1, 5)], vertices=[1, 2, 3, 4, 5])
    print("A graph that is transitive:")
    print_result(d7)
    print(d7.is_transitive())
    d8 = Digraph(edges=[(1, 2), (2, 3), (3, 3), (3, 4)], vertices=[1, 2, 3, 4])
    print("A graph that is not transitive:")
    print_result(d8)
    print(d8.is_transitive())
    print("------------------")
    d9 = Digraph(edges=[(1, 2), (2, 1), (1, 1), (2, 2)])
    print(d9.is_transitive())
    d10 = Digraph(edges=[(2, 3), (1, 3), (1, 2), (2, 4), (1, 5), (1, 4)], vertices=[1, 2, 3, 4, 5])
    print("A graph that is transitive:")
    print_result(d10)
    print(d10.is_transitive())
