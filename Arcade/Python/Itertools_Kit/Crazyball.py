from itertools import combinations

def solution(players, k):
    return sorted([sorted(lineup) for lineup in combinations(players, k)])
