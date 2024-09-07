def modifiedMatrix(matrix):
    result = matrix
    result_len = len(result)
    for i in range(result_len):
        row = result[i]
        row_len = len(row)
        for j in range(row_len):
            if row[j] == -1:
                max_val = -1
                for k in range(result_len):
                    if result[k][j] > max_val:
                        max_val = result[k][j]
                row[j] = max_val

    return result


matrix = [
    [3, -1],
    [5, 2],
]


print(modifiedMatrix(matrix))
