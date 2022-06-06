
from queues import deque

positive = deque()
negative = deque()


with open('materials\integers.txt', 'r') as f:
    text = f.read().splitlines()
    for num in text:
        if int(num) >= 0:
            positive.push_right(int(num))
        elif int(num) < 0:
            negative.push_right(int(num))
    while not negative.is_empty():
        print(negative.pop_left())
    while not positive.is_empty():
        print(positive.pop_left())