import random

def create_maze(rows, cols):
    # 1 walls
    # 0 path
    maze = [[1 for i in range(cols)] for i in range(rows)]

    start_row = 1
    start_col = 1
    maze[start_row][start_col] = 3

    def dfs(r, c):
        directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]
        random.shuffle(directions)

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if 0 < nr < rows and 0 < nc < cols:
                if maze[nr][nc] == 1:
                    maze[r + dr//2][c + dc//2] = 0
                    maze[nr][nc] = 0
                    dfs(nr, nc)

    dfs(start_row, start_col)
    return maze



    

    create_maze()