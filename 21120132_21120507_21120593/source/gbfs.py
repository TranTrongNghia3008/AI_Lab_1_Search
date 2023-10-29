import heapq
from utils import *

class GBFS:
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
    
    def is_valid_move(self, node):
        return 0 <= node[0] < self.rows and 0 <= node[1] < self.cols and self.matrix[node[0]][node[1]] != 'x' and (not self.visited[node[0]][node[1]])


    
    def gbfs(self, heuristic): 
        p_queue = [(self.heuristic(heuristic, self.start), self.start)] 
        parents = [[(-1,-1)] * self.cols for _ in range(self.rows)]
        self.visited[self.start[0]][self.start[1]] = True

        while p_queue:
            _, current = heapq.heappop(p_queue)
            self.visit.append(current)

            if current == self.end:
                self.path = [(current)]
                while current != self.start:
                    current = parents[current[0]][current[1]]
                    self.path.append(current)
                self.path.reverse()
                return True
            
            distances = [(-1, 0), (0, 1), (1, 0), (0, -1)]

            for d in distances :
                next = (current[0] + d[0], current[1] + d[1])

                if self.is_valid_move(next):
                    h = self.heuristic(heuristic, next)
                    heapq.heappush(p_queue, (h, next))
                    self.visit.append(next)
                    self.visited[current[0]][current[1]] = True
                    parents[next[0]][next[1]] = current

        return False
        
    
    
def find_path_gbfs_manhattan(matrix):
    alg = GBFS(matrix)

    if alg.gbfs("manhattan"):
        return alg.visit, alg.path, len(alg.path)
    
    print("No path found.")
    return alg.visit,[],-1

def find_path_gbfs_euclidean(matrix):
    alg = GBFS(matrix)

    if alg.gbfs("euclidean"):
        return alg.visit, alg.path, len(alg.path)
    
    print("No path found.")
    return alg.visit,[],-1

def find_path_gbfs_manhattan_euclidean(matrix):
    alg = GBFS(matrix)

    if alg.gbfs("manhattan_euclidean"):
        return alg.visit, alg.path, len(alg.path)
    
    print("No path found.")
    return alg.visit,[],-1

