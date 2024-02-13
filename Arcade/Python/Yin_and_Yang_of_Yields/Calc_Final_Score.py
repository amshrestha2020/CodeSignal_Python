def solution(scores, n):
    gen = iter(a**2 for a in sorted(scores)[-n:])

    res = 0
    try:
        for _ in range(n):
            res += next(gen)
    except StopIteration:
        res //= 5

    return res
