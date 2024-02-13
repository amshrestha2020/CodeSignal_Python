def solution(cell1, cell2):
    # Extract row and column numbers from cell coordinates
    row1, col1 = ord(cell1[0]) - ord('A') + 1, int(cell1[1])
    row2, col2 = ord(cell2[0]) - ord('A') + 1, int(cell2[1])
    
    # Check if the sum of row and column indices is even or odd
    return (row1 + col1) % 2 == (row2 + col2) % 2

