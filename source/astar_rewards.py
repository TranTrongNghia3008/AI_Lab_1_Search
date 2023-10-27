import heapq
import math

def heuristic_with_reward(current_point, end, reward):
    distance_current_to_reward = abs(current_point[0] - reward[0]) + abs(current_point[1] - reward[1])
    distance_reward_to_end = abs(reward[0] - end[0]) + abs(reward[1] - end[1])
    print(reward[2])
    return 3 * (distance_current_to_reward + distance_reward_to_end) + 2 * reward[2]

def findStart(maze, rows, cols):
    print(rows)
    print(cols)
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 'S':
                return i, j, 0

def findEnd(maze, rows, cols):
    for i in range(rows):
        if maze[i][0] == ' ':
            return i, 0, 0
        if maze[i][-1] == ' ':
            return i, cols - 1, 0

    for j in range(cols):
        if maze[0][j] == ' ':
            return 0, j, 0
        if maze[-1][j] == ' ':
            return rows - 1, j, 0  

def heuristic_manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

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

def find_path_astar_with_rewards(maze, points):
    rows, cols = len(maze), len(maze[0])
    start = findStart(maze, rows, cols)
    end = findEnd(maze, rows, cols)
    current_point = start
    
    flag = [-1] * (len(points))
    
    visit = []
    path = []
    tt = 0
    
   
    rewards = points
    
    while (len(rewards) > 0):     
        next_point = end
        h_min = heuristic_with_reward(current_point, end, end)
        print("--------")
        print(h_min)
        for reward in rewards:
            # if (reward != current_point):
                h_with_reward = heuristic_with_reward(current_point, end, reward)
                print(h_with_reward)
                if (h_with_reward < h_min):
                    h_min = h_with_reward
                    next_point = reward
        
        vi, p, x = find_path_astar(maze, current_point, next_point)
        # for i in range(len(points) - 1):
        #     if (points[i] == current_point):
        #         flag[i] = tt
        #         tt += 1
        if (x != -1):
            visit.extend(vi)
            path.extend(p)
            
            if (next_point == end):
                return visit, path, len(path) - 1
        
            current_point = next_point
            
        # elif (len(rewards) == 0):
        #     path.remove(path[len(path) - 1])
            
        
        if next_point in rewards:
            rewards.remove(next_point)
        
    vi, p, x = find_path_astar(maze, current_point, end)
    if (x == -1 ):
        print("No path found.")
        return visit, [], -1
    visit.extend(vi)
    path.extend(p)
    return visit, path, len(path) - 1
                
        