"""
Расставить на стандартной 64-клеточной шахматной доске 8 ферзей так, чтобы ни один из них не находился под боем другого». Подразумевается, что ферзь бьёт все клетки, расположенные по вертикалям, горизонталям и обеим диагоналям
Написать программу,  которая находит хотя бы один способ решения задач.
"""
import copy



found_eight_queens = []




def is_diagonal_vacant(current_found_queens, x, y):
    for position in current_found_queens:
        xf, yf = position
        if (abs(xf-x) - abs(yf-y) == 0):
            return False
    return True

def place_queens_reursively(current_found_queens, queen_counter):
    found_queens_x = [position[0] for position in current_found_queens]
    found_queens_y = [position[1] for position in current_found_queens]

    if queen_counter < 8:

        for y in range(8):
            if y not in found_queens_y:

                for x in range(8):
                    if x not in found_queens_x:
                        
                        if is_diagonal_vacant(current_found_queens, x, y):
                            current_found_queens_copy = current_found_queens.copy()
                            current_found_queens_copy.append((x, y))
                            place_queens_reursively(current_found_queens_copy[:], queen_counter + 1)
    else:
        if len(found_eight_queens) > 0:
            if set(current_found_queens) not in found_eight_queens:
                found_eight_queens.append(set(current_found_queens))
        else:
            found_eight_queens.append(set(current_found_queens))


def count_qeens_for_cords(x, y):
    current_queens = [(x, y)]
    return place_queens_reursively(current_queens, 1)

for i in range(8):
    count_qeens_for_cords(i, 0)

print("Solutions found:" + len(found_eight_queens))

clear_board = [[0 for i in range(8)] for i in range(8)]

def print_board(board):
    for i in range(8):
        print(board[i])

solution_counter = 1
for solution in found_eight_queens:
    board = clear_board.copy()
    for position in solution:
        x, y = position
        board[x][y] = 1
    print()
    print(f'Solution #{solution_counter}')
    print_board(board)
    solution_counter += 1