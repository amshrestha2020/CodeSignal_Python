def solution(n):
    def sum_of_digits(num):
        return sum(int(digit) for digit in str(num))

    digit_degree = 0

    while n >= 10:
        n = sum_of_digits(n)
        digit_degree += 1

    return digit_degree

