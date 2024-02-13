def solution(n):
    n_str = str(n)
    max_number = max(int(n_str[:i] + n_str[i+1:]) for i in range(len(n_str)))
    return max_number

