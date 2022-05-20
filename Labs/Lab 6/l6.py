from ast import Str
from copy import deepcopy
from re import M
from turtle import distance
from wsgiref import headers
from graph2 import Graph
import math
import pandas as pd
import numpy as np
from tabulate import tabulate

INF = math.inf

def pretty_print_matrix(matrix):
    print(pd.DataFrame(matrix))



def floydWarshall(graph: Graph, v1: str, v2: str):
    dist = graph.generate_DataFrame()

    vertices = graph.unique_vertices()

    for k in vertices:
        for i in vertices:
            for j in vertices:
                dist.at[i, j] = min(dist.at[i, j], dist.at[i, k] + dist.at[k, j])
    return dist


matrix = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0,   1],
         [INF, INF, INF, 0]
         ]
''' Output:
      0      5      8      9
    INF      0      3      4
    INF    INF      0      1
    INF    INF    INF      0
'''

graph = Graph()
graph.from_matrix(matrix)
dist = floydWarshall(graph, "0", "1")
pretty_print_matrix(dist)
pass


def min_distance(dist, unchecked):
    min_index = dist.where(unchecked).idxmin()

    return min_index

def dijkstra(graph: Graph, source: str, destination: str = None): 
    # convert to labeled adjacency matrix
    df = graph.generate_DataFrame()

    
    vertices = sorted(graph.unique_vertices())
    size = graph.size()

    # array with shortest distations to points
    dist = pd.Series([math.inf] * size, index = vertices)
    dist[source] = 0
    prev = pd.Series([None] * size, index = vertices)
    # keep track of already found shortest distations
    unchecked = pd.Series([True] * size, index = vertices)

    # repeat for every unchecked minimum current distance vertex
    for _ in range(size):
        x = min_distance(dist, unchecked)

        unchecked[x] = False

        for y in vertices:
            if unchecked[y] and dist[y] > dist[x] + df.at[x, y]:
                dist[y] = dist[x] + df.at[x, y]
                prev[y] = x

    if destination == None:
        return dist
    else:
        # build path from source to destination via prev[]
        path = list()
        u = destination
        if prev[u] != None or u == source:
            while u != None:
                path.insert(0, u)
                u = prev[u]

        return (path, dist[destination])

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
    
'''
Vertex   Distance from Source
0                0
1                4
2                12
3                19
4                21
5                11
6                9
7                8
8                14
'''

# graph = Graph()
# graph.from_matrix(matrix)

# result = dijkstra(graph, 'a', 'c')
# path = result[0]

# dist = 0
# for i, v in enumerate(path[:-1]):
#     dist += graph.get_dist(v, path[i+1])


# print(result)

def bellmanFord(graph: Graph, source: str, destination: str = None):
    # convert to labeled adjacency matrix
    df = graph.generate_DataFrame()

    vertices = sorted(graph.unique_vertices())
    size = graph.size()

    # array for mimimal distances from source to other vertices
    dist = pd.Series([math.inf] * size, index = vertices)
    dist[source] = 0


    for _ in range(size-1):
        for u in vertices:
            for v in graph.neighbors(u).keys():
                if dist[u] != math.inf and dist[u] + df.at[u, v] < dist[v]:
                    dist[v] = dist[u] + df.at[u, v]

    # check for negative cycles (if there is one, found distance will be incorrect)
    for u in vertices:
        for v in graph.neighbors(u).keys():
            if dist[u] != math.inf and dist[u] + df.at[u, v] < dist[v]:
                print("Graph contains negative weight cycle")
                return

    if destination == None:
        return dist
    return dist[destination]

# graph = Graph()
# graph.add_edge_oriented("0", "1", -1)
# graph.add_edge_oriented("0", "2", 4)
# graph.add_edge_oriented("1", "2", 3)
# graph.add_edge_oriented("1", "3", 2)
# graph.add_edge_oriented("1", "4", 2)
# graph.add_edge_oriented("3", "2", 5)
# graph.add_edge_oriented("3", "1", 1)
# graph.add_edge_oriented("4", "3", -3)

''' OUTPUT
Vertex   Distance from Source
0                0
1                -1
2                2
3                -2
4                1
'''

# print(tabulate(bellmanFord(graph, '0').to_frame().transpose(), headers = 'keys', tablefmt='psql'))

def johnson(graph: Graph, v1: str = None, v2: str = None):
    # copy original graph for modifications
    modified = deepcopy(graph)

    # add extra vertex with edges with 0 weight to all original vertices
    mod_source = '@'
    modified.add_vertex(mod_source)
    vertices = sorted(graph.unique_vertices())
    for v in vertices:
        modified.add_edge_oriented(mod_source, v, 0)

    # calculate bellman-ford table with that extra vertex as a source
    h = bellmanFord(modified, mod_source)

    # remove that extra verex
    modified.remove_vertex(mod_source)

    # update weights with b.-ford table to avoid negative weights
    for u in vertices:
        for v in modified.neighbors(u):
            new_weight = modified.get_dist(u, v) + h[u] - h[v]
            modified.add_edge_oriented(u, v, new_weight)

    # use dejikstra for resulting modified graph 
    if v1 != None:
        return dijkstra(modified, v1, v2)
    else:
        dijkstra_complete = dijkstra(modified, vertices[0])
        for v in vertices[1:]:
            current_dijkstra = dijkstra(modified, v).to_frame()
            current_dijkstra.columns = [v]
            dijkstra_complete = pd.concat([dijkstra_complete, current_dijkstra], axis = 1)
        return dijkstra_complete.transpose()

    
    
# graph = Graph()

# matrix = [[0, -4, INF, 1, -2],
#           [INF, 0, 5, INF, INF],
#           [2, INF, 0, INF, INF],
#           [INF, INF, INF, 0, 3],
#           [INF, INF, INF, INF, 0]]

# ''' OUTPUT
#     0   0   1   1   0
#     3   0   1   4   3
#     2   2   0   3   2
#     inf inf inf 0   5
#     inf inf inf inf 0
# '''

# graph.from_matrix(matrix)

# print(johnson(graph, ))



def levit(graph: Graph, source: str, destination: str = None):
    df = graph.generate_DataFrame()
    vertices = sorted(graph.unique_vertices())
    size = len(vertices)

    dist = pd.Series([math.inf] * size, index = vertices)
    dist[source] = 0

    # checked
    M0 = set()
    # current
    M1 = list()
    M1.append(source)
    # current urgent
    M1u = list()
    # unchecked yet
    M2 = set()
    for v in vertices:
        if v != source:
            M2.add(v)

    while len(M1) != 0:
        u = M1u.pop(0) if len(M1u) != 0 else M1.pop(0)

        for v in graph.neighbors(u):
            if v in M2:
                dist[v] = dist[u] + graph.get_dist(u, v)
                M1.append(v)
                M2.remove(v)
            elif v in M1:
                dist[v] = min(dist[v], dist[u] + graph.get_dist(u, v))
            elif v in M0 and dist[v] > dist[u] + graph.get_dist(u, v):
                dist[v] = dist[u] + graph.get_dist(u, v)
                M1u.append(v)
                M0.remove(v)
        
        M0.add(u)

    return dist

# graph = Graph()

# graph.add_edge_oriented('1', '2', 5)
# graph.add_edge_oriented('1', '3', -6)
# graph.add_edge_oriented('2', '3', 7)
# graph.add_edge_oriented('2', '4', 4)
# graph.add_edge_oriented('3', '2', -2)
# graph.add_edge_oriented('3', '4', 6)

''' OUTPUT
 0 
-8
-6
-4
'''

# print(levit(graph, '1'))


def yen(graph: Graph, source: str, destination: str, paths: int):
    path, distance = dijkstra(graph, source, destination)
    original_path = path.copy()
    # all shortest paths
    A = list()
    A.append(path)
    lengths = list()
    lengths.append(distance)
    # potential shortest path
    B = list()

    for k in range(1, paths):
        for i in range(len(A[-1])-1):
            modified = deepcopy(graph)
            # modified.remove_edge_oriented(original_path[i], original_path[i+1])
            spur_node = A[-1][i]
            root_path = A[-1][:i+1]

            whole_distance = 0
            for ind, v in enumerate(root_path[:-1]):
                whole_distance += modified.get_dist(v, root_path[ind-1])

            for paths in A:
                if root_path == paths[:i+1]:
                    modified.remove_edge_oriented(paths[i], paths[i+1])
            
            for vertex in root_path:
                if vertex != spur_node:
                    modified.remove_vertex(vertex)
                
            spur_path, distance = dijkstra(modified, spur_node, destination)
            if len(spur_path) < 1:
                continue

            total_path = root_path[:-1] + spur_path
            if total_path not in B:
                B.append((total_path, whole_distance + distance))

        if len(B) == 0:
            break
        sorted_B = B
        B.sort(key = lambda x: x[1])
        A.append(sorted_B[0][0])
        lengths.append(sorted_B[0][1])
        B.remove(sorted_B[0])
    return (A, lengths)

graph = Graph()
graph.add_edge_oriented('c', 'd', 3)
graph.add_edge_oriented('c', 'e', 2)
graph.add_edge_oriented('e', 'd', 1)
graph.add_edge_oriented('e', 'f', 2)
graph.add_edge_oriented('e', 'g', 3)
graph.add_edge_oriented('d', 'f', 4)
graph.add_edge_oriented('f', 'g', 2)
graph.add_edge_oriented('f', 'h', 1)
graph.add_edge_oriented('g', 'h', 2)


print(yen(graph, 'c', 'h', 5))

                



    