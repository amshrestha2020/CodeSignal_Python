def solution(a):
    return functools.reduce(lambda x, y: x + [ x[-1] + y ], a, [0])[1:]