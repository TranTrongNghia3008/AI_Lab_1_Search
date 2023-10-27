import heapq
import math
from astar import findEnd, findStart

def euclidean(node, end):
    return ((node[0] - end[0]) ** 2 + (node[1] - end[1]) ** 2) ** 0.5

def find_path_astar_euclidean(maze):
    rows, cols = len(maze), len(maze[0])

    start_x, start_y = findStart(maze, rows, cols)
    end_x, end_y = findEnd(maze, rows, cols)
    
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
                    h = euclidean((nx, ny), (end_x, end_y))
                    f = tentative_g + h
                    heapq.heappush(p_queue, (f, (nx, ny,current_x,current_y)))

    print("No path found.")
    return visit, [], -1
    