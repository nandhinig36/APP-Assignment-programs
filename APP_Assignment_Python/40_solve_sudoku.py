def solve_sudoku(board):
    def valid(r,c,value):
        if any(board[r][j] == value for j in range(9)): return False
        if any(board[i][c] == value for i in range(9)): return False
        br, bc = 3*(r//3), 3*(c//3)
        return all(board[i][j] != value for i in range(br,br+3) for j in range(bc,bc+3))
    def backtrack():
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    for value in "123456789":
                        if valid(r,c,value):
                            board[r][c] = value
                            if backtrack(): return True
                            board[r][c] = "."
                    return False
        return True
    
    original = [row[:] for row in board]
    for r in range(9):
        for c in range(9):
            value = board[r][c]
            if value != ".":
                board[r][c] = "."
                if not valid(r,c,value): return False
                board[r][c] = value
    if backtrack(): return True
    board[:] = original
    return False

if __name__ == "__main__":
    board = [list(row) for row in [
        "53..7....","6..195...",".98....6.","8...6...3",
        "4..8.3..1","7...2...6",".6....28.","...419..5","....8..79"]]
    if solve_sudoku(board):
        for row in board: print(" ".join(row))
    else: print("Invalid or unsolvable Sudoku board")
