def compose(functions):
    return functools.reduce(lambda f, g: lambda x: f(g(x)), functions)

def solution(functions, x):
    return compose(map(eval, functions))(x)
