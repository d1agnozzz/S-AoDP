from queues import stack

s = stack()

with open('materials/text.txt', 'r') as f:
    text = f.read()
    lines = text.splitlines()

    for line in lines:
        s.push_right(line)
    
with open('materials/reversed_text.txt', 'w') as f:
    while not s.is_empty():
        f.write(s.pop_right())
        f.write("\n")