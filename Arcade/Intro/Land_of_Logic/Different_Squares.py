def solution(matrix):
    unique_squares = set()
    rows, cols = len(matrix), len(matrix[0])
    
    for i in range(rows - 1):
        for j in range(cols - 1):
            square = (matrix[i][j], matrix[i][j + 1], matrix[i + 1][j], matrix[i + 1][j + 1])
            unique_squares.add(square)
    
    return len(unique_squares)
