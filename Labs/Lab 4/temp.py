from queue import PriorityQueue

a = PriorityQueue()
b = PriorityQueue()

a.put((0, 'c'))
a.put((4, 'b'))

a.put((1, 'a'))

b.put('c', 1)
b.put('b', 4)
b.put('a', 0)

c = a.get()[1]

print(c)
print(a.get())
print(a.get())