def solution(st):
    # Check if the string is already a palindrome
    if st == st[::-1]:
        return st

    # Find the longest suffix that is a palindrome
    for i in range(len(st)):
        if st[i:] == st[i:][::-1]:
            # Append the remainder of the string in reverse
            return st + st[:i][::-1]


