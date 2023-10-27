import heapq

def heuristic(node, end):
    return abs(node[0] - end[0]) + abs(node[1] - end[1])

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

def find_path_gbfs(grid):
    rows, cols = len(grid), len(grid[0])
    start_x, start_y = findStart(grid, rows, cols)
    end_x, end_y = findEnd(grid, rows, cols)
    
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    visit = []

    # Priority queue (min heap) to select the node with the lowest heuristic value
    priority_queue = [(heuristic((start_x, start_y), (end_x, end_y)), (start_x, start_y))]  # (heuristic, (x, y))
    
    parents = {(start_x, start_y): None}

    while priority_queue:
        _, (current_x, current_y) = heapq.heappop(priority_queue)
        visit.append((current_x, current_y))

        if current_x == end_x and current_y == end_y:
            path = [(current_x, current_y)]
            while (current_x, current_y) != (start_x, start_y):
                current_x, current_y = parents[(current_x, current_y)]
                path.append((current_x, current_y))
            path.reverse()
            return visit, path, len(path) - 1

        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = current_x + dx, current_y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != 'x' and not visited[nx][ny]:
                heapq.heappush(priority_queue, (heuristic((nx, ny), (end_x, end_y)), (nx, ny)))
                visited[nx][ny] = True
                parents[(nx, ny)] = (current_x, current_y)

    print("No path found.")
    return visit, [], -1