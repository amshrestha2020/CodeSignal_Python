def solution(n):
    return [[0] * x for x in functools.reduce(lambda acc, _: acc + [acc[-1] + acc[-2]], range(2, n), [0, 1])]
