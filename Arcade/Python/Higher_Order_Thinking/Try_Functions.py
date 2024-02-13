def solution(x, functions):
    return [ eval(f)(x) for f in functions ]
