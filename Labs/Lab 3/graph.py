
class graph:

    def __init__(self, graph_dict: dict) -> None:
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

    def add_edge(self, edge: tuple):
        vertex1, vertex2, weight = tuple(edge)
        for x, y in [(vertex1, vertex2), (vertex2, vertex1)]:
            if x in self._graph_dict:
                self._graph_dict[x].add((y, weight))
            else:
                self._graph_dict[x] = {(y, weight)}

    def remove_edge(self, edge: tuple):
        vertex1, vertex2 = tuple(edge)
        for x, y in [(vertex1, vertex2), (vertex2, vertex1)]:
            if x in self._graph_dict:
                for connection in self._graph_dict[x]:
                    _vertex, _weight = connection
                    if _vertex == y:
                        self._graph_dict[x].remove(connection)
                        break

    def neighbors(self, vertex: str):
        return self._graph_dict[vertex]
        
        
g = {
    "a": {("b", 6)},
    "b": {("a", 6)}
}

Graph = graph(g)

Graph.add_vertex("c")
Graph.add_vertex("d")
Graph.add_vertex("e")
Graph.add_vertex("d")
Graph.add_edge(("a", "c", 3))
Graph.add_edge(("a", "d", 5))
Graph.add_edge(("c", "d", 1))
Graph.add_edge(("d", "e", 3))
# print(Graph.neighbors("a"))
# Graph.remove_edge(("c", "a"))
Graph.remove_vertex("c")
print(Graph.neighbors("a"))
