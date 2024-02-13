def solution(n):
    return [[0] * (i + 1) for i in range(n)] + [[0] * (i + 1) for i in range(n - 2, -1, -1)]
