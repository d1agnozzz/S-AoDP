from queues import deque

with open("books.txt", 'r') as books:
    d1 = deque()
    d2 = deque()
    
    for line in books:
        d1.pushright(line)

    while not d1.is_empty():
        current = d1.popright()
        while not d2.is_empty() and d2.peekright() > current:
            d1.pushleft(d2.popright())
        d2.pushright(current)
    while not d2.is_empty():
        print(d2.popleft())