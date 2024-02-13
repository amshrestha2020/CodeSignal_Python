def solution(number):
    def fractions():
        n, d = 1, 1
        
        while True:
            yield [n, d]
            n, d = d, 2 * (n - n % d) + d - n
            # n, d = d, 2 * (n // d) * d + d - n

    gen = fractions()
    res = 0
    while next(gen) != number:
        res += 1
    return res
