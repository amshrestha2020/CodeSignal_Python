def solution(athletes):
    return [athlete for pair in zip(athletes[1::2], athletes[::2]) for athlete in pair]
