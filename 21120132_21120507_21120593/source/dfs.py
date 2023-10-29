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