from graph2 import Graph

def tree_game(num_of_vertices: int, goal: int, vertices):
    # games = int(input())
    # for _ in range(games):
    #     num_of_vertices, goal = list(map(int, input().split(" ")))
    tree = Graph()
    for vert in vertices:
        u, v = tuple(map(str, vert))
        tree.add_edge_not_oriented(u, v, 1)

    if num_of_vertices == 1 or len(tree.neighbors(str(goal))) == 1:
        print("Ayush")
        return

    if num_of_vertices % 2 == 1:
        print("Ashish")
    else:
        print("Ayush")

tree_game(3, 1, [(2,1),(3,1)])
tree_game(3, 2, [(1,2),(1,3)])

games = int(input())
for _ in range(games):
    num_of_vertices, goal = list(map(int, input().split(" ")))
    edges = []
    for _ in range(num_of_vertices-1):
        u, v = input().split(" ")
        edges.append((u, v))
    tree_game(num_of_vertices, goal, edges)
