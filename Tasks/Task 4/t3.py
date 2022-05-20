def matrix_sort(inp_matrix):
    result = [[]]
    matrix = inp_matrix.copy()

    columns = len(inp_matrix[0])
    current_row = 0

    while len(matrix) > 0:
        if len(result[current_row]) == columns:
            current_row += 1
            result.append([])

        min_row, min_col = 0, 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[min_row][min_col] > matrix[i][j]:
                    min_row, min_col = i, j

        result[current_row].append(matrix[min_row].pop(min_col))

        if len(matrix[min_row]) == 0:
            matrix.pop(min_row)

    return result


def get_left(matrix, out = list()):
    if len(matrix)>0:
        result = out.copy()

        for i in range(len(matrix)-1,-1,-1):
            if (len(matrix[i])>0):
                result.append(matrix[i].pop(0))
        
        return get_top(matrix, result)
    return out



def get_down(matrix, out = list()):
    if len(matrix)>0:
        result = out.copy()

        current_row = matrix.pop()
        while len(current_row) > 0:
            result.append(current_row.pop())
        
        return get_left(matrix, result)
    return out



def get_right(matrix, out = list()):
    if len(matrix)>0:
        result = out.copy()

        for i in range(0, len(matrix)):
            if (len(matrix[i])>0):
                result.append(matrix[i].pop())
        
        return get_down(matrix, result)
    return out



def get_top(matrix, out = list()):
    if len(matrix)>0:
        result = out.copy()

        current_row = matrix.pop(0)
        while len(current_row) > 0:
            result.append(current_row.pop(0))
        
        return get_right(matrix, result)
    return out


m = [[1, 3, 2], [7, 4, 9], [6, 5, 8], [10, 12, 11], [13, 14, 15]]
print(get_top(matrix_sort(m)))
