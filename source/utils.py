class Utils:
    def find_start(matrix, rows, cols):
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 'S':
                    return i, j
                
    def find_end(matrix, rows, cols):
        for i in range(rows):
            if matrix[i][0] == ' ':
                return i, 0
            if matrix[i][-1] == ' ':
                return i, cols - 1
        for j in range(cols):
            if matrix[0][j] == ' ':
                return 0, j
            if matrix[-1][j] == ' ':
                return rows - 1, j
            
    def heuristic_manhattan(node, end):
        return abs(node[0] - end[0]) + abs(node[1] - end[1])
    
    def heuristic_euclidean(node, end):
        euclidean_dist = ((node[0] - end[0])** 2 + (node[1] - end[1])** 2) ** 0.5
        return euclidean_dist

    def heuristic_manhattan_euclidean(node, end):
        manhattan_dist = abs(node[0] - end[0]) + abs(node[1] - end[1])
        euclidean_dist = ((node[0] - end[0])** 2 + (node[1] - end[1])** 2) ** 0.5
        return (manhattan_dist + euclidean_dist)
    
    def heuristic_with_reward(current_point, end, reward):
        distance_current_to_reward = abs(current_point[0] - reward[0]) + abs(current_point[1] - reward[1])
        distance_reward_to_end = abs(reward[0] - end[0]) + abs(reward[1] - end[1])
        return 3*(distance_current_to_reward + distance_reward_to_end) + 2*reward[2]
            
    # def is_valid_move(x, y, ):
        # return 0 <= x < self.rows and 0 <= y < self.cols and not self.visited[x][y] and self.matrix[x][y] != 'x'