def solution(year):
    # Calculate the century by dividing the year by 100
    # and rounding up to the nearest whole number
    century = (year - 1) // 100 + 1
    return century

