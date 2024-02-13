def solution(participants):
    return sorted([i for i, count in enumerate(participants) if count < i])
