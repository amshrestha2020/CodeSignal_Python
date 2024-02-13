def solution(ids, k):
    digitSum = lambda n: sum(int(digit) for digit in str(n))

    sm = 0
    for questionId in ids:
        sm += digitSum(questionId)
    return sm % k == 0
