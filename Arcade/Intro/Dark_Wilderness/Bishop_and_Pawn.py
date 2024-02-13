def solution(bishop, pawn):
    # Extract row and column indices for both bishop and pawn
    b_row, b_col = ord(bishop[0]) - ord('a') + 1, int(bishop[1])
    p_row, p_col = ord(pawn[0]) - ord('a') + 1, int(pawn[1])

    # Check if the absolute difference in row and column indices is the same
    return abs(b_row - p_row) == abs(b_col - p_col)

