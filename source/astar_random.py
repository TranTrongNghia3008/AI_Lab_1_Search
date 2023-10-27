import heapq
import random


def findStart(grid, rows, cols):
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'S':
                return i, j, 0

def findEnd(grid, rows, cols):
    for i in range(rows):
        if grid[i][0] == ' ':
            return i, 0, 0
        if grid[i][-1] == ' ':
            return i, cols - 1, 0

    for j in range(cols):
        if grid[0][j] == ' ':
            return 0, j, 0
        if grid[-1][j] == ' ':
            return rows - 1, j, 0  

def heuristic_manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def find_shortest_path(grid, points):
    rows, cols = len(grid), len(grid[0])
    start = findStart(grid, rows, cols)
    end = findEnd(grid, rows, cols)
    shortest_distance = float('inf')
    shortest_permutation = []
    
    n = 100000
    for _ in range(n):  # Số lần lặp ngẫu nhiên (thay đổi theo nhu cầu)
        random.shuffle(points)  # Tạo hoán vị ngẫu nhiên
        total_distance = 0
        current_point = start

        for point in points:
            total_distance += heuristic_manhattan_distance(current_point, point)
            current_point = point

        total_distance += heuristic_manhattan_distance(current_point, end)

        if total_distance < shortest_distance:
            shortest_distance = total_distance
            
            shortest_permutation = [start]
            shortest_permutation.extend(points)
            shortest_permutation.append(end)
            
    print(shortest_permutation)
    return shortest_permutation

# def find_path_astar(grid, start, end):
#     rows, cols = len(grid), len(grid[0])
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
#             if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != 'x' and not visited[nx][ny]:
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

def find_path_astar(maze, start, end):
    rows, cols = len(maze), len(maze[0])

    start_x, start_y, _ = start
    end_x, end_y, _ = end
    
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    visit = []

    p_queue = [(0, (start_x, start_y,start_x,start_y))]  
    
    g_values = [[float('inf')] * cols for _ in range(rows)]
    parents = [[(-1,-1)] * cols for _ in range(rows)]


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
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] != 'x' and not visited[nx][ny]:
                tentative_g = g_values[current_x][current_y] + 1
                if  tentative_g < g_values[nx][ny]:
                    g_values[nx][ny] = tentative_g
                    h = heuristic_manhattan_distance((nx, ny), (end_x, end_y))
                    f = tentative_g + h
                    heapq.heappush(p_queue, (f, (nx, ny,current_x,current_y)))

    print("No path found.")
    return visit, [], -1

def find_path_astar_random(grid, points):
    shortest_path = find_shortest_path(grid, points)
    n = len(shortest_path)
    visit = []
    path = []
    for i in range(n - 1):
        vi, p, x = find_path_astar(grid,shortest_path[i],shortest_path[i+1])
        if (x == -1):
            return visit, [], -1
        visit.extend(vi)
        path.extend(p)
    return visit, path, len(path)
        
        
        


