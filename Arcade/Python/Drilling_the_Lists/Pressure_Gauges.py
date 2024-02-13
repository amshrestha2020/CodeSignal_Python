def solution(morning, evening):
    return [[min(pressures) for pressures in zip(morning, evening)], [max(pressures) for pressures in zip(morning, evening)]]
