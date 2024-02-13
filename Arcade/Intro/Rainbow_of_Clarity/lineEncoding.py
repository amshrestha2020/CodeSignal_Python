def solution(s):
    result = []
    i = 0

    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            i += 1
            count += 1
        if count > 1:
            result.append(str(count) + s[i])
        else:
            result.append(s[i])
        i += 1

    return ''.join(result)

