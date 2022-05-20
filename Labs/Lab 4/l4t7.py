
from queues import deque

positive = deque()
negative = deque()


with open('materials\integers.txt', 'r') as f:
    text = f.read().splitlines()
    for num in text:
        if int(num) >= 0:
            positive.pushright(int(num))
        elif int(num) < 0:
            negative.pushright(int(num))
    while not negative.is_empty():
        print(negative.popleft())
    while not positive.is_empty():
        print(positive.popleft())