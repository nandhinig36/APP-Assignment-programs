def set_zeroes(matrix):
    rows = {i for i,row in enumerate(matrix) if 0 in row}
    cols = {j for j in range(len(matrix[0])) if any(matrix[i][j] == 0 for i in range(len(matrix)))}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in rows or j in cols: matrix[i][j] = 0
    return matrix

if __name__ == "__main__":
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    print(set_zeroes(matrix))
