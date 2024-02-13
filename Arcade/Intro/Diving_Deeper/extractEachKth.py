def solution(inputArray, k):
    return [elem for i, elem in enumerate(inputArray) if (i + 1) % k != 0]

