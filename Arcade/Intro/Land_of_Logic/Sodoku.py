def is_valid_row(grid, row):
    # Check if the row contains all digits from 1 to 9
    return set(grid[row]) == set(range(1, 10))

def is_valid_column(grid, col):
    # Check if the column contains all digits from 1 to 9
    return set(row[col] for row in grid) == set(range(1, 10))

def is_valid_subgrid(grid, start_row, start_col):
    # Check if the 3x3 subgrid contains all digits from 1 to 9
    subgrid = [grid[i][j] for i in range(start_row, start_row + 3) for j in range(start_col, start_col + 3)]
    return set(subgrid) == set(range(1, 10))
    
    
def solution(grid):
    # Check each row, column, and subgrid for validity
    for i in range(9):
        if not is_valid_row(grid, i) or not is_valid_column(grid, i):
            return False

    # Check each 3x3 subgrid for validity
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not is_valid_subgrid(grid, i, j):
                return False

    return True

