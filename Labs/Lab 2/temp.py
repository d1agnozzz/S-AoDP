

size = 8
board = [ [0]*size for i in range(size)]
results_count = 0
def show_board():
    for i in range(size):
        print(board[i])

def tryQueen(a, b):#проверка, нет ли установленных ферзей по вертикали и по диагоналям.
    for i in range(a):
        if(board[i][b]):
            return False
    step = 1
    while step<=a and b - step >= 0 :
        if board[a-step][b-step]:
            return False
        step += 1
    step = 1
    while step <= a and b + step < size :
        if(board[a-step][b+step]):
            return False
        step+=1
    return True

def setQueen(a):
    global results_count
    if a == size:
        print(f"Results #{results_count}")
        results_count += 1
        show_board()
        pass
    for i in range(size):
        if tryQueen(a,i):#Проверяем, если поставить в board[a][i] ферзя, то он будет единственным в строке/столбце/диагоналях
            board[a][i]=1
            setQueen(a+1)
            board[a][i] = 0
    pass

setQueen(0)
