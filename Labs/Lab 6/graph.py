import math
from pprint import pprint


class Graph:
    def __init__(self, graph_dict: dict = None) -> None:
        if graph_dict == None:
            graph_dict = dict()
        self._graph_dict = graph_dict

    def add_vertex(self, vertex: str):
        if vertex not in self._graph_dict:
            self._graph_dict[vertex] = set()

    def remove_vertex(self, vertex: str):
        self._graph_dict.pop(vertex, None)

        for key, val in self._graph_dict.items():
            for connection in val:
                _vertex, _weight = connection

                if vertex == _vertex:
                    self._graph_dict[key].remove(connection)
                    break

    def add_edge_not_oriented(self, edge: tuple):
        vertex1, vertex2, weight = tuple(edge)

        for x, y in [(vertex1, vertex2), (vertex2, vertex1)]:
            if x in self._graph_dict:
                if y not in [connection[0] for connection in self._graph_dict[x]]:
                    self._graph_dict[x].add((y, weight))
            else:
                self._graph_dict[x] = {(y, weight)}

    def add_edge_oriented(self, edge: tuple):
        vertex1, vertex2, weight = tuple(edge)

        if vertex1 in self._graph_dict:
            if vertex2 not in [connection[0] for connection in self._graph_dict[vertex1]]:
                self._graph_dict[vertex1].add((vertex2, weight))
        else:
            self._graph_dict[vertex1] = {(vertex2, weight)}


    def remove_edge_not_oriented(self, edge: tuple):
        vertex1, vertex2 = tuple(edge)
        for x, y in [(vertex1, vertex2), (vertex2, vertex1)]:
            if x in self._graph_dict:
                for connection in self._graph_dict[x]:
                    _vertex, _weight = connection
                    if _vertex == y:
                        self._graph_dict[x].remove(connection)
                        break

    def remove_edge_oriented(self, edge: tuple):
        vertex1, vertex2 = tuple(edge)
        if vertex1 in self._graph_dict:
            for connection in self._graph_dict[vertex1]:
                _vertex, _weight = connection
                if _vertex == vertex2:
                    self._graph_dict[vertex1].remove(connection)
                    break

    def neighbors(self, vertex: str):
        if vertex in self._graph_dict:
            return self._graph_dict[vertex]
        return None

    def get_dist(self, vertex1: str, vertex2: str):
        if vertex2 not in [connection[0] for connection in self.neighbors(vertex1)]:
            return math.inf
        else:
            pool = self._graph_dict[vertex1]
            for connection in pool:
                _vertex, _weight = connection
                if _vertex == vertex2:
                    return _weight

    def size(self):
        unique_verts = set()

        for key, value in self._graph_dict.items():
            unique_verts.add(key)
            for connection in value:
                _vertex, _weight = connection
                unique_verts.add(_vertex)
        
        size = len(unique_verts)
        return size
                
    def generate_matrix(self):
        unique_verts = set()

        for key, value in self._graph_dict.items():
            unique_verts.add(key)
            for connection in value:
                _vertex, _weight = connection
                unique_verts.add(_vertex)
        
        size = len(unique_verts)

        matrix = [[ 0 for i in range(size)] for j in range(size)]

        i = 0
        for v1 in sorted(unique_verts):
            j = 0
            for v2 in sorted(unique_verts):
                if v1 == v2:
                    matrix[i][j] = 0
                    

                elif self.neighbors(v1) is not None and v2 in [connection[0] for connection in self.neighbors(v1)]:
                    matrix[i][j] = self.get_dist(v1, v2)
                else:
                    matrix[i][j] = math.inf
                j += 1
            i += 1
        return matrix

    def from_matrix(self, matrix):
        self._graph_dict.clear()
        for i in range(len(matrix)):
            self.add_vertex(str(i))

        for current_ind, connections in enumerate(matrix):
            current = str(current_ind)
            for index, distance in enumerate(connections):
                if distance != 0 and distance < math.inf:
                    self.add_edge_oriented((current, str(index), distance))


if __name__ == '__main__':
    g = {"a": {("b", 6), ("c", 2)}, "b": {("a", 6)}, "c": {("a", 2)}}

    # Graph = Graph(g)

    # Graph.add_vertex("c")
    # Graph.add_vertex("d")
    # Graph.add_vertex("e")
    # Graph.add_vertex("d")
    # Graph.add_edge_not_oriented(("a", "c", 3))
    # Graph.add_edge_not_oriented(("a", "d", 5))
    # Graph.add_edge_not_oriented(("c", "d", 1))
    # Graph.add_edge_not_oriented(("d", "e", 3))
    # # print(Graph.neighbors("a"))
    # # Graph.remove_edge(("c", "a"))
    # Graph.remove_vertex("c")
    # print(Graph.neighbors("a"))
    # print(*Graph.generate_matrix(), sep = "\n")

    graph = Graph()
    INF = math.inf
    matrix = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
            [4, 0, 8, 0, 0, 0, 0, 11, 0],
            [0, 8, 0, 7, 0, 4, 0, 0, 2],
            [0, 0, 7, 0, 9, 14, 0, 0, 0],
            [0, 0, 0, 9, 0, 10, 0, 0, 0],
            [0, 0, 4, 14, 10, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 1, 6],
            [8, 11, 0, 0, 0, 0, 1, 0, 7],
            [0, 0, 2, 0, 0, 0, 6, 7, 0]
            ]
    graph.from_matrix(matrix)
    print(*graph.generate_matrix(), sep = "\n")
    pass
