import os
from dfs import find_path_dfs
from bfs import find_path_bfs
from ucs import find_path_ucs
from gbfs import find_path_gbfs
from astar import find_path_astar_manhattan, find_path_astar_euclidean, find_path_astar_manhattan_euclidean
from algo2 import find_path_algo2
from astar_rewards import find_path_astar_rewards, find_path_astar_random
# from astar_rewards import find_path_astar_with_rewards
# from astar_euclidean import find_path_astar_euclidean
# from astar_manhattan_euclidean import find_path_astar_manhattan_euclidean
from draw import convert_result_to_video


def read_input_file(file_path):
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

def getPath(direct, level, name):
    current_directory = os.path.abspath(os.getcwd())
    parent_directory = os.path.dirname(current_directory)
    file_path = os.path.join(parent_directory, direct, level, name)

    return file_path

def write_draw_file(level, inputName, name, path, visit):
    file_path = os.path.join(getPath('draw', level, inputName), name)

    with open(file_path, 'w') as file:
        file.write(f"{len(visit)}\n")
        for vertex in visit:
            file.write(f"{vertex[0]} {vertex[1]}\n")

        file.write(f"{len(path)}\n")
        for vertex in path:
            file.write(f"{vertex[0]} {vertex[1]}\n")

def write_ouput_file(level, inputName, name, res):
    file_path = os.path.join(getPath('output', level, inputName), name)

    with open(file_path, 'w') as file:
        if res == -1:
            file.write("NO")
        else:
            file.write(str(res))
            
            
def process(algs, level):
    numInp = 3
    if level == "level_1":
        numInp = 5
    for i in range(numInp):
        file_path = getPath('input', level, f'input{i + 1}.txt')
        arrPoint, grid = read_input_file(file_path)
        for alg in algs:
            visit, path, resLength = [], [], 0
            if alg == 'dfs':
                visit, path, resLength = find_path_dfs(grid)
            elif alg == 'bfs':
                visit, path, resLength = find_path_bfs(grid)
            elif alg == 'ucs':
                visit, path, resLength = find_path_ucs(grid)
            elif alg == 'gbfs_heuristic_1':
                visit, path, resLength = find_path_gbfs(grid)
            # elif alg == 'gbfs_heuristic_2':
            #     visit, path, resLength = find_path_gbfs_euclidean(grid)
            # elif alg == 'gbfs_heuristic_3':
            #     visit, path, resLength = find_path_gbfs_manhattan_euclidean(grid)
            elif alg == 'astar_heuristic_1':
                visit, path, resLength = find_path_astar_manhattan(grid)
            elif alg == 'astar_heuristic_2':
                visit, path, resLength = find_path_astar_euclidean(grid)
            elif alg == 'astar_heuristic_3':
                visit, path, resLength = find_path_astar_manhattan_euclidean(grid)
            elif alg == 'astar_heuristic_4':
                visit, path, resLength = find_path_astar_rewards(grid, arrPoint)
            elif alg == 'astar_heuristic_5':
                visit, path, resLength = find_path_astar_random(grid, arrPoint)

            write_draw_file(level, f'input{i + 1}', f'{alg}.txt', path, visit)
            write_ouput_file(level, f'input{i + 1}', f'{alg}.txt', resLength)
            print(f"Done output input{i + 1} for {alg}!")
            convert_result_to_video(f'../input/{level}/input{i + 1}.txt', f'../draw/{level}/input{i + 1}/{alg}.txt', f'../output/{level}/input{i + 1}/{alg}.gif', 5)
    

# algs = ['dfs', 'bfs', 'ucs', 'gbfs_heuristic_1', 'gbfs_heuristic_2', 'gbfs_heuristic_3', 'astar_heuristic_1', 'astar_heuristic_2', 'astar_heuristic_3', 'astar_heuristic_4', 'astar_heuristic_5']
algs = ['astar_heuristic_4']
process(algs, "level_2")
