def solution(cell):
    x, y = ord(cell[0]) - ord('a') + 1, int(cell[1])
    possible_moves = [
        (x + 2, y + 1), (x + 2, y - 1),
        (x - 2, y + 1), (x - 2, y - 1),
        (x + 1, y + 2), (x - 1, y + 2),
        (x + 1, y - 2), (x - 1, y - 2)
    ]

    valid_moves = sum(1 for move in possible_moves if 1 <= move[0] <= 8 and 1 <= move[1] <= 8)
    return valid_moves

