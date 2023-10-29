import heapq
import random


# def findStart(matrix, rows, cols):
#     for i in range(rows):
#         for j in range(cols):
#             if matrix[i][j] == 'S':
#                 return i, j, 0

# def findEnd(matrix, rows, cols):
#     for i in range(rows):
#         if matrix[i][0] == ' ':
#             return i, 0, 0
#         if matrix[i][-1] == ' ':
#             return i, cols - 1, 0

#     for j in range(cols):
#         if matrix[0][j] == ' ':
#             return 0, j, 0
#         if matrix[-1][j] == ' ':
#             return rows - 1, j, 0  

# def heuristic_manhattan_distance(point1, point2):
#     return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

# def find_shortest_path(matrix, points):
#     rows, cols = len(matrix), len(matrix[0])
#     start = findStart(matrix, rows, cols)
#     end = findEnd(matrix, rows, cols)
#     shortest_distance = float('inf')
#     shortest_permutation = []
    
#     n = 100000
#     for _ in range(n):  # Số lần lặp ngẫu nhiên (thay đổi theo nhu cầu)
#         random.shuffle(points)  # Tạo hoán vị ngẫu nhiên
#         total_distance = 0
#         current_point = start

#         for point in points:
#             total_distance += heuristic_manhattan_distance(current_point, point)
#             current_point = point

#         total_distance += heuristic_manhattan_distance(current_point, end)

#         if total_distance < shortest_distance:
#             shortest_distance = total_distance
            
#             shortest_permutation = [start]
#             shortest_permutation.extend(points)
#             shortest_permutation.append(end)
            
#     print(shortest_permutation)
#     return shortest_permutation

# def find_path_astar(matrix, start, end):
#     rows, cols = len(matrix), len(matrix[0])
#     print(start)
#     start_x, start_y, _ = start
#     end_x, end_y, _ = end
    
#     visited = [[False for _ in range(cols)] for _ in range(rows)]
#     visit = []

#     # Priority queue (min heap) to select the node with the lowest f(x) value
#     priority_queue = [(0, (start_x, start_y))]  # (f(x), (x, y))
    
#     # Dictionary to store the cost to reach a node
#     g_values = {(start_x, start_y): 0}
    
#     parents = {(start_x, start_y): None}

#     while priority_queue:
#         _, (current_x, current_y) = heapq.heappop(priority_queue)
#         visit.append((current_x, current_y))

#         if current_x == end_x and current_y == end_y:
#             path = [(current_x, current_y)]
#             while (current_x, current_y) != (start_x, start_y):
#                 current_x, current_y = parents[(current_x, current_y)]
#                 path.append((current_x, current_y))
#             path.reverse()
#             return visit, path, len(path) - 1

#         for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
#             nx, ny = current_x + dx, current_y + dy
#             if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] != 'x' and not visited[nx][ny]:
#                 tentative_g = g_values[(current_x, current_y)] + 1
#                 if (nx, ny) not in g_values or tentative_g < g_values[(nx, ny)]:
#                     g_values[(nx, ny)] = tentative_g
#                     h = heuristic_manhattan_distance((nx, ny), (end_x, end_y))
#                     f = tentative_g + h
#                     heapq.heappush(priority_queue, (f, (nx, ny)))
#                     visited[nx][ny] = True
#                     parents[(nx, ny)] = (current_x, current_y)

#     print("No path found.")
#     return visit, [], -1

# def find_path_astar(matrix, start, end):
#     rows, cols = len(matrix), len(matrix[0])

#     start_x, start_y, _ = start
#     end_x, end_y, _ = end
    
#     visited = [[False for _ in range(cols)] for _ in range(rows)]
#     visit = []

#     p_queue = [(0, (start_x, start_y,start_x,start_y))]  
    
#     g_values = [[float('inf')] * cols for _ in range(rows)]
#     parents = [[(-1,-1)] * cols for _ in range(rows)]


#     g_values[start_x][start_y] = 0
#     while p_queue:
#         _, (current_x, current_y,parentx,parenty) = heapq.heappop(p_queue)
#         if visited[current_x][current_y] == True :
#             continue
#         visit.append((current_x, current_y))
#         parents[current_x][current_y] = (parentx,parenty)
#         visited[current_x][current_y] = True

#         if current_x == end_x and current_y == end_y:
#             path = [(current_x, current_y)]
#             while (current_x, current_y) != (start_x, start_y):
#                 current_x, current_y = parents[current_x][current_y]
#                 path.append((current_x, current_y))
#             path.reverse()
#             return visit, path, len(path) - 1

#         for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
#             nx, ny = current_x + dx, current_y + dy
#             if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] != 'x' and not visited[nx][ny]:
#                 tentative_g = g_values[current_x][current_y] + 1
#                 if  tentative_g < g_values[nx][ny]:
#                     g_values[nx][ny] = tentative_g
#                     h = heuristic_manhattan_distance((nx, ny), (end_x, end_y))
#                     f = tentative_g + h
#                     heapq.heappush(p_queue, (f, (nx, ny,current_x,current_y)))

#     print("No path found.")
#     return visit, [], -1

# def find_path_astar_random(matrix, points):
#     shortest_path = find_shortest_path(matrix, points)
#     n = len(shortest_path)
#     visit = []
#     path = []
#     for i in range(n - 1):
#         vi, p, x = find_path_astar(matrix,shortest_path[i],shortest_path[i+1])
#         if (x == -1):
#             return visit, [], -1
#         visit.extend(vi)
#         path.extend(p)
#     return visit, path, len(path)

import heapq
from utils import *

class AStartReward:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.start = Utils.find_start(matrix=matrix, rows=self.rows, cols=self.cols)
        self.end = Utils.find_end(matrix=matrix, rows=self.rows, cols=self.cols)
        self.visit = []
        self.path = []
        
        
    def find_shortest_path(self, points):
        shortest_distance = float('inf')
        shortest_permutation = []
        
        n = len(points) * 10000
        for _ in range(n):  # Số lần lặp ngẫu nhiên (thay đổi theo nhu cầu)
            random.shuffle(points)  # Tạo hoán vị ngẫu nhiên
            total_distance = 0
            current_point = (self.start[0], self.start[1], 0)

            for point in points:
                total_distance += Utils.heuristic_manhattan((current_point[0], current_point[1]), (point[0], point[1]))
                current_point = point

            total_distance += Utils.heuristic_manhattan((current_point[0], current_point[1]), self.end)

            if total_distance < shortest_distance:
                shortest_distance = total_distance
                
                shortest_permutation = [(self.start[0], self.start[1], 0)]
                shortest_permutation.extend(points)
                shortest_permutation.append((self.end[0], self.end[1], 0))
                
        return shortest_permutation
    
    def astar(self, start, end):

        start_x, start_y, _ = start
        end_x, end_y, _ = end

        p_queue = [(0, (start_x, start_y,start_x,start_y))]  
        
        g_values = [[float('inf')] * self.cols for _ in range(self.rows)]
        parents = [[(-1,-1)] * self.cols for _ in range(self.rows)]
        visited = [[False]*self.cols for _ in range(self.rows)]

        visit = []
        
        g_values[start_x][start_y] = 0
        while p_queue:
            _, (current_x, current_y,parentx,parenty) = heapq.heappop(p_queue)
            if visited[current_x][current_y] == True :
                continue
            visit.append((current_x, current_y))
            parents[current_x][current_y] = (parentx,parenty)
            visited[current_x][current_y] = True

            if current_x == end_x and current_y == end_y:
                path = [(current_x, current_y)]
                while (current_x, current_y) != (start_x, start_y):
                    current_x, current_y = parents[current_x][current_y]
                    path.append((current_x, current_y))
                path.reverse()
                
                return visit, path, len(path) - 1
            for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nx, ny = current_x + dx, current_y + dy
                if 0 <= nx < self.rows and 0 <= ny < self.cols and self.matrix[nx][ny] != 'x' and not visited[nx][ny]:
                    tentative_g = g_values[current_x][current_y] + 1
                    if  tentative_g < g_values[nx][ny]:
                        g_values[nx][ny] = tentative_g
                        h = Utils.heuristic_manhattan((nx, ny), (end_x, end_y))
                        f = tentative_g + h
                        heapq.heappush(p_queue, (f, (nx, ny,current_x,current_y)))

        print("No path found.")
        return False
    def astar_random(self, points):
        shortest_path = self.find_shortest_path(points)
        n = len(shortest_path)
        for i in range(n - 1):
            vi, p, x = self.astar(shortest_path[i],shortest_path[i+1])
            if (x == -1):
                return False
            self.visit.extend(vi)
            self.path.extend(p)
        return True
    
    def astar_rewards(self, points):
        start = (self.start[0], self.start[1], 0)
        end = (self.end[0], self.end[1], 0)
        current_point = start

        rewards = points
        
        while rewards:     
            next_point = end
            h_min = Utils.heuristic_with_reward(current_point, end, end)
            for reward in rewards:
                h_with_reward = Utils.heuristic_with_reward(current_point, end, reward)
                if (h_with_reward < h_min):
                    h_min = h_with_reward
                    next_point = reward
            
            vi, p, x = self.astar(current_point, next_point)

            if (x != -1):
                self.visit.extend(vi)
                self.path.extend(p)
                
                if (next_point == end):
                    return True
            
                current_point = next_point
                
            
            if next_point in rewards:
                rewards.remove(next_point)
            
        vi, p, x = self.astar(current_point, end)
        if (x == -1 ):
            print("No path found.")
            return False
        self.visit.extend(vi)
        self.path.extend(p)
        return True
    
def find_path_astar_rewards(matrix, points):
    alg = AStartReward(matrix)

    if alg.astar_rewards(points):
        return alg.visit, alg.path, len(alg.path)
    
    print("No path found.")
    return alg.visit,[],-1

def find_path_astar_random(matrix, points):
    alg = AStartReward(matrix)

    if alg.astar_random(points):
        return alg.visit, alg.path, len(alg.path)
    
    print("No path found.")
    return alg.visit,[],-1
            
        



            
            
        


