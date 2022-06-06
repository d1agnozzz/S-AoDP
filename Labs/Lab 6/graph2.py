import math
from pandas import DataFrame, isna
from copy import copy, deepcopy


class Graph:
    def __init__(self, graph_dict: dict = None) -> None:
        if graph_dict == None:
            graph_dict = dict()
        self._graph_dict = graph_dict

    def add_vertex(self, vertex: str):
        if vertex not in self._graph_dict:
            self._graph_dict[vertex] = dict()

    def remove_vertex(self, vertex: str):
        self._graph_dict.pop(vertex, None)

        for key in self._graph_dict.keys():
            self._graph_dict[key].pop(vertex, None)

            # for connection in val:
            #     _vertex, _weight = connection

            #     if vertex == _vertex:
            #         self._graph_dict[key].remove(connection)
            #         break

    def add_edge_not_oriented(self, v1: str, v2: str, weight: int):
        for u, v in [(v1, v2), (v2, v1)]:
            self._graph_dict[u][v] = weight

    def add_edge_oriented(self, v1: str, v2: str, weight: int):
        if v1 in self._graph_dict:
            self._graph_dict[v1][v2] = weight
        else:
            self._graph_dict[v1] = {v2: weight}

    def remove_edge_not_oriented(self, v1: str, v2: str):
        for u, v in [(v1, v2), (v2, v1)]:
            self._graph_dict[u].pop(v, None)

    def remove_edge_oriented(self, v1: str, v2: str):
        self._graph_dict[v1].pop(v2, None)

    def neighbors(self, vertex: str):
        if vertex in self._graph_dict:
            return self._graph_dict[vertex]
        return dict()

    def get_dist(self, vertex1: str, vertex2: str):
        if vertex1 not in self._graph_dict or vertex2 not in self._graph_dict[vertex1]:
            return math.inf
        else:
            return self._graph_dict[vertex1][vertex2]

    def size(self):
        return len(self.vertices())

    def vertices(self) -> set:
        vertices = set()

        for key, value in self._graph_dict.items():
            vertices.add(key)
            for v, w in value.items():
                vertices.add(v)

        return vertices

    def generate_matrix(self):
        vertices = sorted(list(self.vertices()))

        size = len(vertices)

        matrix = [[0 for i in range(size)] for j in range(size)]  # matrix size*size

        for i, v1 in enumerate(vertices):
            for j, v2 in enumerate(vertices):
                if v1 == v2:
                    matrix[i][j] = 0

                elif self.neighbors(v1) is not None and v2 in self.neighbors(v1):
                    matrix[i][j] = self.get_dist(v1, v2)
                else:
                    matrix[i][j] = math.inf
        return matrix

    def generate_DataFrame(self):
        vertices = sorted(list(self.vertices()))

        df = DataFrame(self._graph_dict)

        for vertex in self.vertices():
            # when there is no connection to or from point, add blank columns and rows
            if vertex not in df.columns:
                df.insert(0, vertex, math.inf)
            if vertex not in df.index:
                df.loc[vertex] = math.inf

            # init self connection to 0 if there is no
            if vertex not in self._graph_dict or vertex not in self._graph_dict[vertex]:
                df.at[vertex, vertex] = 0

        df = df.sort_index(axis=0)
        df = df.sort_index(axis=1)
        df = df.fillna(math.inf)
        df = df.transpose()

        return df

    def from_matrix(self, matrix):
        self._graph_dict.clear()
        # create vertices named with numbers ('1', '2'...)
        for index in range(len(matrix)):
            self.add_vertex(str(index))

        for current_ind, connections in enumerate(matrix):
            current = str(current_ind)
            for index, distance in enumerate(connections):
                if distance != 0 and distance < math.inf:
                    self.add_edge_oriented(current, str(index), distance)

    def from_DataFrame(self, df):
        self._graph_dict.clear()

        for index in df.index:
            self.add_vertex(str(index))

        vertices = self.vertices()

        for u in vertices:
            for v in vertices:
                if df.at[u, v] != 0 and not isna(df.at[u, v]):
                    self.add_edge_oriented(u, v, df.at[u, v])

    def __copy__(self):
        cls = self.__class__
        new_one = cls.__new__(cls)
        new_one.__dict__.update(self.__dict__)
        return new_one

    def __deepcopy__(self, memo):
        cls = self.__class__
        new_one = cls.__new__(cls)
        memo[id(self)] = new_one
        for k, v in self.__dict__.items():
            setattr(new_one, k, deepcopy(v, memo))
        return new_one


if __name__ == "__main__":
    # g = {"a": {"b": 6, "c": 2}, "b": {"a": 6}, "c": {"a": 2}}

    # Graph = Graph(g)

    # Graph.add_vertex("c")
    # Graph.add_vertex("d")
    # Graph.add_vertex("e")
    # Graph.add_vertex("d")
    # Graph.add_edge_not_oriented("a", "c", 3)
    # Graph.add_edge_not_oriented("a", "d", 5)
    # Graph.add_edge_not_oriented("c", "d", 1)
    # Graph.add_edge_not_oriented("d", "e", 3)
    # # print(Graph.neighbors("a"))
    # # Graph.remove_edge(("c", "a"))
    # Graph.remove_vertex("c")
    # print(Graph.neighbors("a"))
    # print(*Graph.generate_matrix(), sep="\n")

    # print(Graph.generate_DataFrame())

    # graph = Graph()
    # INF = math.inf
    # matrix = [
    #     [0, 4, 0, 0, 0, 0, 0, 8, 0],
    #     [4, 0, 8, 0, 0, 0, 0, 11, 0],
    #     [0, 8, 0, 7, 0, 4, 0, 0, 2],
    #     [0, 0, 7, 0, 9, 14, 0, 0, 0],
    #     [0, 0, 0, 9, 0, 10, 0, 0, 0],
    #     [0, 0, 4, 14, 10, 0, 2, 0, 0],
    #     [0, 0, 0, 0, 0, 2, 0, 1, 6],
    #     [8, 11, 0, 0, 0, 0, 1, 0, 7],
    #     [0, 0, 2, 0, 0, 0, 6, 7, 0],
    # ]
    # graph.from_matrix(matrix)
    # print(graph.generate_DataFrame())

    graph = Graph()
    graph.add_edge_oriented("0", "1", 9)
    graph.add_edge_oriented("0", "2", 3)
    graph.add_edge_oriented("1", "2", 6)
    graph.add_edge_oriented("1", "4", 2)
    graph.add_edge_oriented("2", "1", 2)
    graph.add_edge_oriented("2", "3", 1)
    graph.add_edge_oriented("3", "2", 2)
    graph.add_edge_oriented("3", "4", 2)
    df = graph.generate_DataFrame()
    print(df)
    print(df.at["0", "1"])

    pass
