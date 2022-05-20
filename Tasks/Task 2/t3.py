import numpy as np

def get_diagonals(matrix):
    diagonals = list()

    rows = len(matrix)
    cols = len(matrix[0])

    # fill diagonals from first to right main
    for i in range(cols):
        col = i
        row = 0
        diagonal = list()
        while col >= 0 and row < rows:
            diagonal.append(matrix[row][col])
            col -= 1
            row += 1
        diagonals.append(diagonal)

    # fill diagonals from right main + 1 to last
    for i in range(1, rows):
        col = cols - 1
        row = i
        diagonal = list()
        while cols >= 0 and row < rows:
            diagonal.append(matrix[row][col])
            col -= 1
            row += 1
        diagonals.append(diagonal)
    
    return diagonals

def build_matrix_from_diagonals(diagonals, rows, cols):

    matrix = list()
    before_main = diagonals[:(len(diagonals)+1)//2]
    after_main = diagonals[(len(diagonals)+1)//2:]

    for row in range(rows):
        matrix_row = list()

        # fill N-th row with N-th number from every before main diagonal
        for diag in before_main:
            if len(diag) < row + 1:
                continue
            matrix_row.append(diag[row])

        # fill N-th row with [row - 1 -> 0] element from [0 -> row - 1] diagonal
        if row != 0:
            diag = 0
            ind = row - 1
            for i in range(row):
                matrix_row.append(after_main[diag][ind])
                diag += 1
                ind -= 1
        matrix.append(matrix_row)
    return np.matrix(matrix)

    
           


def sort_diagonals(matrix):
    diagonals = get_diagonals(matrix)

    diagonals = list(map(sorted, diagonals))

    return build_matrix_from_diagonals(diagonals, len(matrix), len(matrix[0]))

m = np.random.randint(0, 10, size=(5, 5))

print(m)
print()
print(sort_diagonals(m))
