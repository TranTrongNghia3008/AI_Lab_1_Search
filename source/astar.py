# 

import heapq
from utils import *

class ASTAR:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.start = Utils.find_start(matrix=matrix, rows=self.rows, cols=self.cols)
        self.end = Utils.find_end(matrix=matrix, rows=self.rows, cols=self.cols)
        self.visited = [[False]*self.cols for _ in range(self.rows)]
        self.visit = []
        self.path = []
        
    def heuristic(self, heuristic, node):
        if heuristic == "manhattan":
            return Utils.heuristic_manhattan(node, self.end)
        if heuristic == "euclidean": 
            return Utils.heuristic_euclidean(node, self.end)
        if heuristic == "manhattan_euclidean": 
            return Utils.heuristic_manhattan_euclidean(node, self.end)
        print("Can not find heuristic!")
        return 0
        
    def astar(self, heurictic):        
        p_queue = [(0, (self.start[0], self.start[1],self.start[0],self.start[1]))]  
        
        g_values = [[float('inf')] * self.cols for _ in range(self.rows)]
        parents = [[(-1,-1)] * self.cols for _ in range(self.rows)]


        g_values[self.start[0]][self.start[1]] = 0
        while p_queue:
            _, (current_x, current_y,parentx,parenty) = heapq.heappop(p_queue)
            if self.visited[current_x][current_y] == True :
                continue
            self.visit.append((current_x, current_y))
            parents[current_x][current_y] = (parentx,parenty)
            self.visited[current_x][current_y] = True

            if current_x == self.end[0] and current_y == self.end[1]:
                self.path = [(current_x, current_y)]
                while (current_x, current_y) != (self.start[0], self.start[1]):
                    current_x, current_y = parents[current_x][current_y]
                    self.path.append((current_x, current_y))
                self.path.reverse()
                return True

            for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nx, ny = current_x + dx, current_y + dy
                if 0 <= nx < self.rows and 0 <= ny < self.cols and self.matrix[nx][ny] != 'x' and not self.visited[nx][ny]:
                    tentative_g = g_values[current_x][current_y] + 1
                    if  tentative_g < g_values[nx][ny]:
                        g_values[nx][ny] = tentative_g
                        h = self.heuristic(heurictic, (nx, ny))
                        f = tentative_g + h
                        heapq.heappush(p_queue, (f, (nx, ny,current_x,current_y)))

        return False
    
def find_path_astar_manhattan(matrix):
    alg = ASTAR(matrix)

    if alg.astar("manhattan"):
        return alg.visit, alg.path, len(alg.path)
    
    print("No path found.")
    return alg.visit,[],-1

def find_path_astar_euclidean(matrix):
    alg = ASTAR(matrix)

    if alg.astar("euclidean"):
        return alg.visit, alg.path, len(alg.path)
    
    print("No path found.")
    return alg.visit,[],-1

def find_path_astar_manhattan_euclidean(matrix):
    alg = ASTAR(matrix)

    if alg.astar("manhattan_euclidean"):
        return alg.visit, alg.path, len(alg.path)
    
    print("No path found.")
    return alg.visit,[],-1