def solve_maze(maze):
    n = len(maze)
    if not n or maze[0][0] == 0 or maze[n-1][n-1] == 0: return None
    solution = [[0]*n for _ in range(n)]
    directions = ((1,0),(-1,0),(0,1),(0,-1))
    def backtrack(r,c):
        if not (0 <= r < n and 0 <= c < n) or maze[r][c] == 0 or solution[r][c]:
            return False
        solution[r][c] = 1
        if (r,c) == (n-1,n-1): return True
        for dr,dc in directions:
            if backtrack(r+dr,c+dc): return True
        solution[r][c] = 0
        return False
    return solution if backtrack(0,0) else None

if __name__ == "__main__":
    maze = [[1,0,0,0],[1,1,0,1],[0,1,0,0],[1,1,1,1]]
    result = solve_maze(maze)
    if result:
        print("Solution Path:")
        for row in result: print("".join(map(str,row)))
    else: print("No solution exists")
