def solution(a, b):
    # Count the number of differences between the arrays
    diff_count = sum(1 for ai, bi in zip(a, b) if ai != bi)

    # Check if there are zero differences or two differences with elements in reverse order
    return diff_count == 0 or (diff_count == 2 and sorted(a) == sorted(b))

    

