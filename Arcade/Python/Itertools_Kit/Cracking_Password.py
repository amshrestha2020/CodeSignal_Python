from itertools import permutations, product, combinations_with_replacement

def solution(digits, k, d):
    def createNumber(digs):
        return "".join(map(str, digs))

    return [i for i in sorted([createNumber(i) for i in set(list(product(createNumber(digits), repeat = k)) ) ]) if ((int(i) % d == 0) or int(i.lstrip("0")) % d == 0)  ]