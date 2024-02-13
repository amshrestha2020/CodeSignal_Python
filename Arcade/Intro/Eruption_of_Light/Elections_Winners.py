def solution(votes, k):
    greatest = max(votes)
    if k == 0:
        if votes.count(greatest) == 1:
            return 1
        else:
            return 0

    counter = 0
    for i in votes:
        if k + i > greatest:
            counter += 1
    
    return counter