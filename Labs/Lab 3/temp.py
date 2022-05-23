from queue import PriorityQueue


candidates = PriorityQueue()

candidates.put((39, "a"))
candidates.put((0, "b"))
candidates.put((11, "c"))

print(candidates.empty())
print(candidates.get())
print(candidates.get())
print(candidates.get())
print(candidates.empty())
