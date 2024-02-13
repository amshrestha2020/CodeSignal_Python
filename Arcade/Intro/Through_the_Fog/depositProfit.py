def solution(deposit, rate, threshold):
    years = math.ceil(math.log(threshold / deposit) / math.log(1 + rate / 100))
    return years

