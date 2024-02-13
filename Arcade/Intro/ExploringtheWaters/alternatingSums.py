def solution(a):
    team_1_weight = sum(a[i] for i in range(0, len(a), 2))
    team_2_weight = sum(a[i] for i in range(1, len(a), 2))
    return [team_1_weight, team_2_weight]

