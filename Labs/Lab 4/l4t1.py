from queues import deque

with open("books.txt", 'r') as books:
    d1 = deque()
    d2 = deque()
    
    for line in books:
        d1.push_right(line)

    while not d1.is_empty():
        current = d1.pop_right()
        while not d2.is_empty() and d2.peek_right() > current:
            d1.push_left(d2.pop_right())
        d2.push_right(current)
    while not d2.is_empty():
        print(d2.pop_left())