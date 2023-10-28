from collections import deque
from utils import *

class BFS:
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

    # def is_at_goal(self, current_coordination, end):
        # return current_coordination == end if end else False
    def bfs(self):
        queue = deque()
        parent = {}

        queue.append(self.start)
        self.visited[self.start[0]][self.start[1]] = True
        self.visit.append((self.start[0], self.start[1]))

        while queue:
            current_row, current_col = queue.popleft()
            if ((current_row, current_col) == self.end):
                while (current_row, current_col) != self.start:
                    self.path.append((current_row, current_col))
                    current_row, current_col = parent[(current_row, current_col)]
                self.path.append(self.start)
                self.path.reverse()
                return True

            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                new_row, new_col = current_row + dr, current_col + dc
                if self.is_valid_move(new_row, new_col):
                    queue.append((new_row,new_col))
                    self.visited[new_row][new_col] = True
                    self.visit.append((new_row,new_col))
                    parent[(new_row,new_col)] = (current_row,current_col)

        return False

def find_path_bfs(grid):
    alg = BFS(grid)

    if alg.bfs():
        return alg.visit, alg.path, len(alg.path)
    
    print("No path found.")
    return alg.visit,[],-1