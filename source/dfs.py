# def is_valid_move(x, y, visited, rows, cols, grid):
#     return 0 <= x < rows and 0 <= y < cols and not visited[x][y] and grid[x][y] != 'x'

# def dfs(x, y, e_x, e_y, visited, rows, cols, grid, path, visit):
#     if not is_valid_move(x, y, visited, rows, cols, grid):
#         return False

#     visited[x][y] = True
#     path.append((x, y))
#     visit.append((x, y))

#     if x == e_x and y == e_y:
#         return True  

#     for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
#         nx, ny = x + dx, y + dy
#         if dfs(nx, ny, e_x, e_y, visited, rows, cols, grid, path, visit):
#             return True

#     path.pop()
#     return False

# def findStart(grid, rows, cols):
#     for i in range(rows):
#         for j in range(cols):
#             if grid[i][j] == 'S':
#                 return i, j

# def findEnd(grid, rows, cols):
#     for i in range(rows):
#         if grid[i][0] == ' ':
#             return i, 0
#         if grid[i][-1] == ' ':
#             return i, cols - 1

#     for j in range(cols):
#         if grid[0][j] == ' ':
#             return 0, j
#         if grid[-1][j] == ' ':
#             return rows - 1, j        

# def find_path_dfs(grid):
#     rows, cols = len(grid), len(grid[0])
#     start_x, start_y = findStart(grid, rows, cols)
#     end_x, end_y = findEnd(grid, rows, cols)

#     visited = [[False for _ in range(cols)] for _ in range(rows)]
#     visit = []
#     path = []

#     if dfs(start_x, start_y, end_x, end_y, visited, rows, cols, grid, path, visit):
#         return visit, path, len(path)
#     else:
#         print("No path found.")
#         return visit, [], -1

from utils import *

class DFS:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.start = Utils.find_start(matrix=matrix, rows=self.rows, cols=self.cols)
        self.end = Utils.find_end(matrix=matrix, rows=self.rows, cols=self.cols)
        self.visited = [[False]*self.cols for _ in range(self.rows)]
        self.visit = []
        self.path = []

    def is_valid_move(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols and not self.visited[x][y] and self.matrix[x][y] != 'x'

    def dfs(self, x, y):
        if not self.is_valid_move(x, y):
            return False

        self.path.append((x, y))
        self.visit.append((x, y))
        self.visited[x][y] = True

        if (x, y) == self.end:
            return True  

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if self.dfs(x + dx, y + dy):
                return True

        self.path.pop()
        return False

def find_path_dfs(matrix):
    alg = DFS(matrix)

    if alg.dfs(*alg.start):
        return alg.visit, alg.path, len(alg.path)
    
    print("No path found.")
    return alg.visit,[],-1
