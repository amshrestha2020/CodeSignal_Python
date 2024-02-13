def solution(a):
    n = len(a)
    if n % 2 == 1:
        # If the length is odd, the median is the middle element
        return a[n // 2]
    else:
        # If the length is even, there are two middle elements
        # Choose the smaller one as the answer
        mid1 = a[n // 2 - 1]
        mid2 = a[n // 2]
        return min(mid1, mid2)

