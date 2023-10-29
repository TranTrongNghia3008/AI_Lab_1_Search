import heapq
from utils import *

class UCS:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.start = Utils.find_start(matrix=matrix, rows=self.rows, cols=self.cols)
        self.end = Utils.find_end(matrix=matrix, rows=self.rows, cols=self.cols)
        self.visited = [[False]*self.cols for _ in range(self.rows)]
        self.visit = []
        self.path = []

    def is_valid_move(self, node):
        return 0 <= node[0] < self.rows and 0 <= node[1] < self.cols and self.matrix[node[0]][node[1]] != 'x' and not self.visited[node[0]][node[1]]


    def ucs(self, dist, trace):
        p_queue = [(0, self.start)]
        heapq.heapify(p_queue)

        self.visit.append(self.start)
        dist[self.start[0]][self.start[1]] = 0
        self.visited[self.start[0]][self.start[1]] = True

        while p_queue:
            cost, current = heapq.heappop(p_queue)

            if current == self.end:
                return True

            self.visited[current[0]][current[1]] == True

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dx, dy in directions:
                next = (current[0] + dx, current[1] + dy)
                if self.is_valid_move(next):
                    next_cost = cost + 1
                    self.visit.append(next)
                    heapq.heappush(p_queue, (next_cost, next))
                    self.visited[current[0]][current[1]] = True

                    if dist[next[0]][next[1]] == -1 or dist[next[0]][next[1]] > next_cost:
                        trace[next[0]][next[1]] = current
                        dist[next[0]][next[1]] = next_cost
        
        return False

    def traced(self, trace):
        i = self.end[0]
        j = self.end[1]

        while i != -1 and j != -1:
            self.path.append((i, j))
            (i, j) = trace[i][j]
        
        return self.path.reverse()

def find_path_ucs(matrix):
    alg = UCS(matrix)
    trace = [[(-1, -1)] * alg.cols for _ in range(alg.rows)]
    dist = [[-1] * alg.cols for _ in range(alg.rows)]
    
    if alg.ucs(dist, trace):
        alg.traced(trace)
        return alg.visit, alg.path, len(alg.path)
    
    print("No path found.")
    return alg.visit, [], -1

    