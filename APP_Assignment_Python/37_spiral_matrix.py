def spiral_order(matrix):
    result = []
    top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
    while top <= bottom and left <= right:
        result.extend(matrix[top][left:right+1]); top += 1
        for row in range(top, bottom+1): result.append(matrix[row][right])
        right -= 1
        if top <= bottom:
            result.extend(matrix[bottom][left:right+1][::-1]); bottom -= 1
        if left <= right:
            for row in range(bottom, top-1, -1): result.append(matrix[row][left])
            left += 1
    return result

if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(spiral_order(matrix))
