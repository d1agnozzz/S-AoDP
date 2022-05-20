from queues import deque

brackets = deque()

with open("unbalanced.py", 'r') as f:
    for line in f:
        for char in line:
            if char == '[':
                brackets.pushleft(char)
            elif char == ']':
                brackets.pushright(char)
    while not brackets.is_empty() and brackets.peekleft() == '[' and brackets.peekright() == ']':
        brackets.popleft()
        brackets.popright()
    print( brackets.is_empty())