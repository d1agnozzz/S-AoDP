from queues import deque

brackets = deque()

with open("unbalanced.py", 'r') as f:
    for line in f:
        for char in line:
            if char == '[':
                brackets.push_left(char)
            elif char == ']':
                brackets.push_right(char)
    while not brackets.is_empty() and brackets.peek_left() == '[' and brackets.peek_right() == ']':
        brackets.pop_left()
        brackets.pop_right()
    print( brackets.is_empty())