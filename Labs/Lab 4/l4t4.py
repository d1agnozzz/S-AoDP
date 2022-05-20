from queues import stack

brackets = stack()

with open("materials\\unbalanced_2.py", 'r') as f:
    balanced = True
    for line in f:
        for char in line:
            if char == '(':
                brackets.pushright("(") 
            elif char == ')':
                if not brackets.is_empty():
                    brackets.popright()
                else:
                    balanced = False
                    break 
        if not balanced:
            break
    if balanced and brackets.is_empty():
        print('balanced')
    else:
        print('unbalanced')


