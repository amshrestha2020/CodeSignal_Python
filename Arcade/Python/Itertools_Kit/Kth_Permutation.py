from itertools import permutations, islice

def solution(numbers, k):
    return next(islice(permutations(numbers), k-1, None))
