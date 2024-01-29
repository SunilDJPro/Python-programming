def is_valid(board, row, col, num):
    # Check if the number is already present in the row
    for i in range(9):
        if board[row][i] == num:
            return False
    
    # Check if the number is already present in the column
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # Check if the number is already present in the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    
    return True

def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True  # Puzzle solved successfully
    else:
        row, col = empty_cell

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0  # Backtrack
    return False

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

# Sample Sudoku puzzle (0 represents empty cells)
board = [
    [2, 0, 0, 9, 0, 6, 0, 0, 0],
    [0, 0, 0, 3, 0, 0, 9, 7, 8],
    [0, 8, 0, 0, 5, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 1],
    [7, 0, 0, 8, 0, 3, 0, 0, 0],
    [0, 0, 1, 6, 2, 7, 0, 0, 0],
    [6, 1, 9, 0, 3, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 8, 0, 3],
    [0, 3, 0, 0, 0, 4, 0, 0, 5]
]

if solve_sudoku(board):
    print("Sudoku puzzle solved successfully:")
    for row in board:
        print(row)
else:
    print("No solution exists for the given Sudoku puzzle.")
