def solution(time):
    try:
        hours, minutes = map(int, time.split(':'))
        return 0 <= hours < 24 and 0 <= minutes < 60
    except ValueError:
        return False

