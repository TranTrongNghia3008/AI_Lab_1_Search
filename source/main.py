import os
from dfs import find_path_dfs
from bfs import find_path_bfs
from ucs import find_path_ucs
from gbfs import find_path_gbfs
from astar import find_path_astar
from algo2 import find_path_algo2
from astar_random import find_path_astar_random
from astar_rewards import find_path_astar_with_rewards
from astar_euclidean import find_path_astar_euclidean
from astar_manhattan_euclidean import find_path_astar_manhattan_euclidean
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

# algoName = ['dfs', 'bfs', 'ucs', 'gbfs', 'astar_heuristic_1']
# algoName = ['astar_manhattan_euclidean']
# for algo in algoName:
#     for i in range(5):
#         file_path = getPath('input', 'level_1', f'input{i + 1}.txt')

#         arrPoint, grid = read_input_file(file_path)
#         visit = []
#         path = []
#         resLength = 0

#         if algo == 'dfs':
#             visit, path, resLength = find_path_dfs(grid)
#         elif algo == 'bfs':
#             visit, path, resLength = find_path_bfs(grid)
#         elif algo == 'ucs':
#             visit, path, resLength = find_path_ucs(grid)
#         elif algo == 'gbfs':
#             visit, path, resLength = find_path_gbfs(grid)
#         elif algo == 'astar_heuristic_1':
#             visit, path, resLength = find_path_astar(grid)
#         elif algo == 'astar_manhattan_euclidean':
#             visit, path, resLength = find_path_astar_euclidean(grid)
#         else:
#             visit, path, resLength = find_path_astar_manhattan_euclidean(grid)

#         write_draw_file('level_1', f'input{i + 1}', f'{algo}.txt', path, visit)
#         write_ouput_file('level_1', f'input{i + 1}', f'{algo}.txt', resLength)
#         print(f"Done output input{i + 1} for {algo}!")
#         convert_result_to_video(f'../input/level_1/input{i + 1}.txt', f'../draw/level_1/input{i + 1}/{algo}.txt', f'../output/level_1/input{i + 1}/{algo}.gif', 5)

for i in range(3):
    file_path = getPath('input', 'level_2', f'input{i + 1}.txt')

    arrPoint, grid = read_input_file(file_path)

    visit, path, resLength = find_path_astar_with_rewards(grid, arrPoint)
    visit = []

    write_draw_file('level_2', f'input{i + 1}', 'astart_l2.txt', path, visit)
    write_ouput_file('level_2', f'input{i + 1}', 'astart_l2.txt', resLength)
    print(f"Done output input{i + 1} for astart_l2!")

    convert_result_to_video(f'../input/level_2/input{i + 1}.txt', f'../draw/level_2/input{i + 1}/astart_l2.txt', f'../output/level_2/input{i + 1}/astart_l2.gif', 3)