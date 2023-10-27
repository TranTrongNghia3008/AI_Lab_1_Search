import heapq

def is_valid_move(x, y, rows, cols, grid, closed):
    return 0 <= x < rows and 0 <= y < cols and grid[x][y] != 'x' and ((x, y) not in closed)

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

def ucs(x, y, e_x, e_y, rows, cols, grid, dist, trace, visit):
    queue = [(0, (x, y))]
    heapq.heapify(queue)

    closed = set()
    visit.append((x, y))
    dist[x][y] = 0

    while queue:
        cost, (current_x, current_y) = heapq.heappop(queue)

        if current_x == e_x and current_y == e_y:
            return True

        closed.add((current_x, current_y))

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_x, next_y = current_x + dx, current_y + dy
            if is_valid_move(next_x, next_y, rows, cols, grid, closed):
                next_cost = cost + 1
                visit.append((next_x, next_y))
                heapq.heappush(queue, (next_cost, (next_x, next_y)))

                if dist[next_x][next_y] == -1 or dist[next_x][next_y] > next_cost:
                    trace[next_x][next_y] = (current_x, current_y)
                    dist[next_x][next_y] = next_cost
    
    return False

def traced(x, y, e_x, e_y, trace, path):
    i = e_x
    j = e_y

    while i != -1 and j != -1:
        path.append((i, j))
        (i, j) = trace[i][j]
    
    return path.reverse()

def find_path_ucs(grid):
    rows, cols = len(grid), len(grid[0])

    start_x, start_y = findStart(grid, rows, cols)
    end_x, end_y = findEnd(grid, rows, cols)

    trace = [[(-1, -1)] * cols for _ in range(rows)]
    dist = [[-1] * cols for _ in range(rows)]
    path = []
    visit = []

    checkAns = ucs(start_x, start_y, end_x, end_y, rows, cols, grid, dist, trace, visit)
    
    if checkAns == False:
        return visit, [], -1

    traced(start_x, start_y, end_x, end_y, trace, path)
    
    return visit, path, len(path)