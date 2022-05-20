from queue import PriorityQueue
import numpy as np
import heapq
from typing import final


def check_solvability(tags: list[int]) -> bool:
    check_sum = 0
    for ind1, pivot in enumerate(tags):
        for ind2, element in enumerate(tags[ind1:]):
            if element < pivot and element != 0:
                check_sum += 1
    check_sum += tags.index(0) // 4 + 1

    return check_sum % 2 == 0

n = 4

tags = [12, 5, 8, 7, 4, 11, 2, 13, 6, 1, 0, 10, 9, 15, 14, 3]
unsolvable_tags = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 14, 0]


def moves(position):
    blank = position.index(0)
    i, j = divmod(blank, n)
    offsets = []
    if i > 0: offsets.append(-n)     
    if i < n - 1: offsets.append(n)  
    if j > 0: offsets.append(-1)
    if j < n - 1: offsets.append(1)  
    for offset in offsets:
        swap = blank + offset
        yield tuple(position[swap] if x==blank else position[blank] if x==swap else position[x] for x in range(n*n))

def manhatan(state):
    solved = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)
    dist = 0
    for ind, (real, ideal) in enumerate(zip(state, solved)):
        if real != ideal:
            horizontal = abs(ind%4 - solved.index(real)%4)
            vertical   = abs(ind//4 - solved.index(real)//4)
            dist += horizontal+vertical
    return dist

class Node:
    def __init__(self, position, distance_from_start, node):
        self.position = position
        self.distance_from_start = distance_from_start
        self.previous_node = node

    def __lt__(self, other):
        return self.distance_from_start < other.distance_from_start

    def __str__(self):
        return '\n'.join((n*'{:3}').format(*[i%(n*n) for i in self.position[i:]]) for i in range(0, n*n, n))


SOLVED = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)
start = [1, 2, 3, 4,
         5, 6, 7, 8,
         9, 10, 11, 12,
         13, 14, 0, 15]

start = tags
# start = unsolvable_tags

if check_solvability(start) == 0:
    print('Can\'t solved')
else:
    start = tuple(start)

    current_state = Node(start, 0, None)

    print(current_state)
    print()

    candidates = [(0, current_state)]

    visited = set([current_state])
    came_from = {current_state.position: None}

    while len(candidates) > 0 and current_state.position != SOLVED:
        cost, current_state = heapq.heappop(candidates)
        for k in moves(current_state.position):
            if k not in visited:
                new_candidate = (manhatan(k), Node(k, current_state.distance_from_start + 1, current_state))
                heapq.heappush(candidates, new_candidate)
                came_from[k] = current_state
                visited.add(k)

    path = []
    prev = current_state
    final_step = current_state
    while current_state.position != start:
        current_state = came_from[current_state.position]
        number = current_state.position[prev.position.index(0)]
        path.append(number)
        prev = current_state
    path.reverse()

    print(path)
    print()

    print(Node(SOLVED, 0, None))
    print()
    while(final_step.previous_node is not None):
        print(final_step.previous_node)
        print()
        final_step = final_step.previous_node