def is_valid_move(x, y, visited, rows, cols, grid):
    return 0 <= x < rows and 0 <= y < cols and not visited[x][y] and grid[x][y] != 'x'

def dfs(x, y, e_x, e_y, visited, rows, cols, grid, path, visit):
    if not is_valid_move(x, y, visited, rows, cols, grid):
        return False

    visited[x][y] = True
    path.append((x, y))
    visit.append((x, y))

    if x == e_x and y == e_y:
        return True  

    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if dfs(nx, ny, e_x, e_y, visited, rows, cols, grid, path, visit):
            return True

    path.pop()
    return False

def findStart(grid, rows, cols):
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'S':
                return i, j

def findEnd(grid, rows, cols):
    for i in range(rows):
        if grid[i][0] == ' ':
            return i, 0
        if grid[i][-1] == ' ':
            return i, cols - 1

    for j in range(cols):
        if grid[0][j] == ' ':
            return 0, j
        if grid[-1][j] == ' ':
            return rows - 1, j        

def find_path_dfs(grid):
    rows, cols = len(grid), len(grid[0])
    start_x, start_y = findStart(grid, rows, cols)
    end_x, end_y = findEnd(grid, rows, cols)

    visited = [[False for _ in range(cols)] for _ in range(rows)]
    visit = []
    path = []

    if dfs(start_x, start_y, end_x, end_y, visited, rows, cols, grid, path, visit):
        return visit, path, len(path)
    else:
        print("No path found.")
        return visit, [], -1