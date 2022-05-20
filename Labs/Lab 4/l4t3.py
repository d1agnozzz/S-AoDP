from queues import stack
A = stack()
B = stack()
C = stack()

n = 6

def move(a, b):
    if a.is_empty() and not b.is_empty():
        a.pushright(b.popright())
    elif not a.is_empty() and b.is_empty():
        b.pushright(a.popright())
    elif a.peekright() > b.peekright():
        a.pushright(b.popright())
    else:
        b.pushright(a.popright())

for i in range(n, 0, -1):
    A.pushright(i)

start, dest, aux = A, C, B

while not dest.is_empty():
    print(dest.popright())



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
    print(dest.popright())
