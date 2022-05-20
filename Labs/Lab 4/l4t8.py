from queues import stack

s = stack()

with open('materials/text.txt', 'r') as f:
    text = f.read()
    lines = text.splitlines()

    for line in lines:
        s.pushright(line)
    
with open('materials/reversed_text.txt', 'w') as f:
    while not s.is_empty():
        f.write(s.popright())
        f.write("\n")