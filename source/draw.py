import matplotlib.pyplot as plt
import imageio.v2 as imageio

# Create a list to store each frame
def visualize_maze(matrix, bonus, start, end, route=None, traversal_cells=None , speed = 4):
    """
    Args:
      1. matrix: The matrix read from the input file,
      2. bonus: The array of bonus points,
      3. start, end: The starting and ending points,
      4. route: The route from the starting point to the ending one, defined by an array of (x, y), e.g. route = [(1, 2), (1, 3), (1, 4)]
      5. traversedMatrix: A matrix to mark traversed cells.
    """
    # 1. Define walls and array of direction based on the route
    walls = [(i, j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j] == 'x']
    frames = []

    if route:
        direction = []
        for i in range(1, len(route)):
            if route[i][0] - route[i - 1][0] > 0:
                direction.append('v')  # ^
            elif route[i][0] - route[i - 1][0] < 0:
                direction.append('^')  # v
            elif route[i][1] - route[i - 1][1] > 0:
                direction.append('>')
            else:
                direction.append('<')

        direction.pop(0)

    # 2. Drawing the map
    ax = plt.figure(dpi=100).add_subplot(111)

    for i in ['top', 'bottom', 'right', 'left']:
        ax.spines[i].set_visible(False)

    plt.scatter([i[1] for i in walls], [-i[0] for i in walls],
                marker='X', s=100, color='black')

    plt.scatter([i[1] for i in bonus], [-i[0] for i in bonus],
                marker='P', s=100, color='green')

    plt.scatter(start[1], -start[0], marker='*',
                s=100, color='gold')

    plt.text(end[1], -end[0], 'EXIT', color='red',
                horizontalalignment='center',
                verticalalignment='center')
   
    plt.xticks([])
    plt.yticks([])
    if traversal_cells:
        for i in range(len(traversal_cells) - 2):
            plt.scatter(traversal_cells[i + 1][1], -traversal_cells[i + 1][0],
                        marker='P', s=100, color='blue',edgecolors='none')
            if i % speed == 0 or i ==  len(traversal_cells) - 2:

                plt.savefig('frame.png')
                frames.append(imageio.imread('frame.png'))
            # plt.savefig('frame.png')
            # frames.append(imageio.imread('frame.png'))


    if route:
        for i in range(len(route) - 2):
            if route[i + 1] in traversal_cells:
                # Clear the color of the cell
                plt.scatter(route[i + 1][1], -route[i + 1][0],
                            marker='P', s=100, color='white',edgecolors='none')
            plt.scatter(route[i + 1][1], -route[i + 1][0],
                       marker= direction[i], s=100, color='silver')
            if i % speed == 0 or i ==  len(route) - 2:

                plt.savefig('frame.png')
                frames.append(imageio.imread('frame.png'))

   


    plt.xticks([])
    plt.yticks([])
    plt.savefig('frame.png')
    frames.append(imageio.imread('frame.png'))

    print(f'Starting point (x, y) = {start[0], start[1]}')
    print(f'Ending point (x, y) = {end[0], end[1]}')

    for _, point in enumerate(bonus):
        print(f'Bonus point at position (x, y) = {point[0], point[1]} with point {point[2]}')

    return frames


def read_file(file_name: str = 'maze.txt'):
  f=open(file_name,'r')
  n_bonus_points = int(next(f)[:-1])
  bonus_points = []
  for i in range(n_bonus_points):
    x, y, reward = map(int, next(f)[:-1].split(' '))
    bonus_points.append((x, y, reward))

  text=f.read()
  matrix=[list(i) for i in text.splitlines()]
  f.close()

  return bonus_points, matrix


def read_traversal_and_route(file_name: str = 'traversal_and_route.txt'):
    with open(file_name, 'r') as f:
        n_traversal_cells = int(next(f).strip())
        traversal_cells = []
        for _ in range(n_traversal_cells):
            i, j = map(int, next(f).strip().split())
            traversal_cells.append((i, j))

        m = int(next(f).strip())
        route = []
        for _ in range(m):
            i, j = map(int, next(f).strip().split())
            route.append((i, j))

    return traversal_cells, route

def convert_result_to_video(input_file = "input.txt", trace_file = "output.txt",saved_file="maze.gif",speed = 3):
    bonus_points, matrix = read_file(input_file)
    traversal_cells, route = read_traversal_and_route(trace_file)
    frames=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'S':
                start = (i, j)
            elif matrix[i][j] == ' ':
                if (i == 0) or (i == len(matrix) - 1) or (j == 0) or (j == len(matrix[0]) - 1):
                    end = (i, j)
    frames = visualize_maze(matrix, bonus_points, start, end,route,traversal_cells,speed)
    imageio.mimsave(saved_file, frames, 'GIF', duration=0.001)

# convert_result_to_video('../input/level_1/input1.txt','../draw/level_1/input1/dfs.txt','../output/level_1/input1/dfs.gif',5)