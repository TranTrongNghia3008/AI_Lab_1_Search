from collections import deque

class BFS:
    def __init__(self):
        pass
        

    def find_start(self, grid):
        n_rows = len(grid)
        n_cols = len(grid[0])
        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == 'S':
                    return i, j


    def find_end(self, grid):
        n_rows = len(grid)
        n_cols = len(grid[0])
        
        for i in range(n_rows):
            if grid[i][0] == ' ':
                return i, 0
            if grid[i][-1] == ' ':
                return i, n_cols - 1

        for j in range(n_cols):
            if grid[0][j] == ' ':
                return 0, j
            if grid[-1][j] == ' ':
                return n_rows - 1, j     
            
            
    def read_input_file(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()

        arrPoint = []
        nPoint = int(lines[0])
        for i in range(nPoint):
            values = list(map(lambda x : int(x), lines[i + 1].split()))
            arrPoint.append(values)

        nRow = len(lines) - nPoint - 1
        nCol = len(lines[-1])
        if lines[-1][-1] == ' ':
            nCol -= 1

        maze = []
        for i in range(nPoint + 1, len(lines)):
            maze.append(list(lines[i].rstrip('\n')))

        return arrPoint, maze

    
    def is_valid_move(self, x, y, visited, n_n_rows, n_n_cols, grid):
        return 0 <= x < n_n_rows and 0 <= y < n_n_cols and not visited[x][y] and grid[x][y] != 'x'
    
    
    def is_at_goal(self, current_coordination, end):
        if (end is not None):
            return current_coordination[0] == end[0] and current_coordination[1] == end[1]
        else:
            return False
                
    
    def bfs(self, grid, start, end):
        n_n_rows, n_n_cols = len(grid), len(grid[0])
        
        visited = [[False] * n_n_cols for _ in range(n_n_rows)]
        visit = []
        queue = deque()
        parent = {}  # Store the parent of each visited cell

        # Directions for moving: East, South, West, North
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        queue.append(start)
        visited[start[0]][start[1]] = True
        visit.append((start[0], start[1]))
        
        while queue:
            current_row, current_col = queue.popleft()
            if (current_row, current_col) == end:
                path = []  # Initialize the path
                while (current_row, current_col) != start:
                    path.append((current_row, current_col))
                    current_row, current_col = parent[(current_row, current_col)]
                path.append(start)
                path.reverse()
                return path, visit
            
            for dr, dc in directions:
                new_row, new_col = current_row + dr, current_col + dc
                
                if 0 <= new_row < n_n_rows and 0 <= new_col < n_n_cols and not visited[new_row][new_col] and grid[new_row][new_col] in (' ', 'S', '+'):
                    queue.append((new_row, new_col))
                    visited[new_row][new_col] = True
                    visit.append((new_row, new_col))
                    parent[(new_row, new_col)] = (current_row, current_col)

        return []  # No path found
    

    def export_path(self, path, filename):
        with open(filename, "w") as file:
            file.write(f"{len(path)}\n")
            for tile in path:
                file.write(f"{tile[0]} {tile[1]}\n")
        
def find_path_bfs(grid):
    alg = BFS()

    start, end = alg.find_start(grid), alg.find_end(grid)

    path, visit = alg.bfs(grid, start, end)

    return visit, path, len(path)