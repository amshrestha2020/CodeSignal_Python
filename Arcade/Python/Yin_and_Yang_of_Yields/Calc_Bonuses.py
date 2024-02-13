def solution(bonuses, n):
    it = (b for b in bonuses)
    res = 0

    try:
        for _ in range(n):
            res += next(it)
    except StopIteration:
        res = 0

    return res
