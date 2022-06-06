from queues import stack
A = stack()
B = stack()
C = stack()

n = 6

def move(a, b):
    if a.is_empty() and not b.is_empty():
        a.push_right(b.pop_right())
    elif not a.is_empty() and b.is_empty():
        b.push_right(a.pop_right())
    elif a.peek_right() > b.peek_right():
        a.push_right(b.pop_right())
    else:
        b.push_right(a.pop_right())

for i in range(n, 0, -1):
    A.push_right(i)

start, dest, aux = A, C, B

while not dest.is_empty():
    print(dest.pop_right())



total_num_of_moves = int(pow(2, n)-1)

for i in range(1, total_num_of_moves+1):
    if i%3==1:
        move(start, dest)
    elif i%3==2:
        move(start, aux)
    elif i%3==0:
        move(aux, dest)

if n % 2 == 0:
    temp = dest
    dest = aux
    aux = temp

while not dest.is_empty():
    print(dest.pop_right())
