def solution(matrix):
    total_sum = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                # Mark all rooms below a haunted room
                for k in range(i + 1, len(matrix)):
                    matrix[k][j] = 0
            else:
                total_sum += matrix[i][j]

    return total_sum


