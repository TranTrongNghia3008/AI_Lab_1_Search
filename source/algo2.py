import heapq
MAX_INF = 1000000007

def is_valid_move(x, y, rows, cols, grid):
    return 0 <= x < rows and 0 <= y < cols and grid[x][y] != 'x'

def findStart(grid, rows, cols):
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'S':
                return i, j

def findEnd(grid, rows, cols):
    for i in range(rows):
        if grid[i][0] == ' ':
            return i, 0
        if grid[i][-1] == ' ':
            return i, cols - 1

    for j in range(cols):
        if grid[0][j] == ' ':
            return 0, j
        if grid[-1][j] == ' ':
            return rows - 1, j   

def check_bit(num, i):
    bit_value = (num >> i) & 1
    return bit_value

def set_bit_to_1(num, i):
    num = num | (1 << i)
    return num


def dijkstra(x, y, e_x, e_y, rows, cols, n, nState, grid, points, dist, trace, visit):
    queue = [(0, (x, y, 0))]
    heapq.heapify(queue)

    visited = [[[0 for _ in range(nState)] for _ in range(cols)] for _ in range(rows)]
    dist[x][y][0] = 0
    visit.append((x, y))

    (xEnd, yEnd, stEnd) = (-1, -1, -1)
    res = MAX_INF

    while queue:
        cost, (current_x, current_y, current_st) = heapq.heappop(queue)

        if dist[current_x][current_y][current_st] < cost:
            continue

        if current_x == e_x and current_y == e_y:
            if res > cost:
                res = cost
                (xEnd, yEnd, stEnd) = (current_x, current_y, current_st)
               
        visited[current_x][current_y][current_st] = 1

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_x, next_y = current_x + dx, current_y + dy
            if not is_valid_move(next_x, next_y, rows, cols, grid):
                continue
            
            jj = -1
            for i in range(n):
                if next_x == points[i][0] and next_y == points[i][1]:
                    jj = i
                    break
            
            next_st = 0
            weight = 1
            if jj == -1 or check_bit(current_st, jj) == 1:
                next_st = current_st
            else:
                next_st = set_bit_to_1(current_st, jj)
                weight = 1 + points[jj][2]
            next_cost = cost + weight
                
            if visited[next_x][next_y][next_st] == 1 or dist[next_x][next_y][next_st] < next_cost:
                continue
            
            visit.append((next_x, next_y))
            heapq.heappush(queue, (next_cost, (next_x, next_y, next_st)))
            trace[next_x][next_y][next_st] = (current_x, current_y, current_st)
            dist[next_x][next_y][next_st] = next_cost

    return res, (xEnd, yEnd, stEnd)

def traced(x, y, st, e_x, e_y, e_st, trace, path):
    i = e_x
    j = e_y
    k = e_st

    while i != -1 and j != -1 and k != -1:
        path.append((i, j))
        (i, j, k) = trace[i][j][k]
    
    return path.reverse()

def find_path_algo2(grid, points):
    rows, cols = len(grid), len(grid[0])
    nPoint = len(points)
    maxState = 1 << nPoint

    start_x, start_y = findStart(grid, rows, cols)
    end_x, end_y = findEnd(grid, rows, cols)

    trace = [[[(-1, -1, -1) for _ in range(maxState)] for _ in range(cols)] for _ in range(rows)]
    dist = [[[MAX_INF for _ in range(maxState)] for _ in range(cols)] for _ in range(rows)]
    path = []
    visit = []

    res, (xEnd, yEnd, stEnd) = dijkstra(start_x, start_y, end_x, end_y, rows, cols, nPoint, maxState, grid, points, dist, trace, visit)
    
    if res == MAX_INF:
        return visit, [], -1

    traced(start_x, start_y, 0, xEnd, yEnd, stEnd, trace, path)
    
    return visit, path, res