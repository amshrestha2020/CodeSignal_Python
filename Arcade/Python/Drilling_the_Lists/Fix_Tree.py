def solution(tree):
    return [t.strip().center(max(len(t) for t in tree)) for t in tree]
