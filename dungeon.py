import re
import graph


class Maze:

    def __init__(self, maze=[]):
        self.maze = maze
        self.maze_graph = None

    def __str__(self):
        for m in self.maze:
            for line in m:
                print(line)
        return ''

    def matrix_2_graph(self):
        tmp_start_id = ''
        tmp_end_id = ''
        vertex_list = []
        edges_list = []
        for i, layer in enumerate(self.maze):
            for j, row in enumerate(layer):
                for k, ch in enumerate(row):

                    id = str(i) + str(j) + str(k)

                    try:
                        neighbor_right = str(
                            i) + str(j) + str(k + 1) if self.maze[i][j][k + 1] != '#' else 'z'
                    except:
                        neighbor_right = 'z'
                    try:
                        neighbor_left = str(
                            i) + str(j) + str(k - 1) if self.maze[i][j][k - 1] != '#' else 'z'
                    except:
                        neighbor_left = 'z'
                    try:
                        neighbor_down = str(
                            i) + str(j + 1) + str(k) if self.maze[i][j + 1][k] != '#' else 'z'
                    except:
                        neighbor_down = 'z'
                    try:
                        neighbor_up = str(
                            i) + str(j - 1) + str(k) if self.maze[i][j - 1][k] != '#' else 'z'
                    except:
                        neighbor_up = 'z'
                    try:
                        neighbor_forward = str(
                            i + 1) + str(j) + str(k) if self.maze[i + 1][j][k] != '#' else 'z'
                    except:
                        neighbor_forward = 'z'
                    try:
                        neighbor_backward = str(
                            i - 1) + str(j) + str(k) if self.maze[i - 1][j][k] != '#' else 'z'
                    except:
                        neighbor_backward = 'z'

                    if ch != '#' and ch != '' and ch != ' ':
                        if ch == 'S':
                            tmp_start_id = id
                        if ch == 'E':
                            tmp_end_id = id
                        vertex_list.append(id)
                        if '-' not in id and '-' not in neighbor_right and 'z' not in id and 'z' not in neighbor_right:
                            edges_list.append((id, neighbor_right))
                        if '-' not in id and '-' not in neighbor_left and 'z' not in id and 'z' not in neighbor_left:
                            edges_list.append((id, neighbor_left))
                        if '-' not in id and '-' not in neighbor_down and 'z' not in id and 'z' not in neighbor_down:
                            edges_list.append((id, neighbor_down))
                        if '-' not in id and '-' not in neighbor_up and 'z' not in id and 'z' not in neighbor_up:
                            edges_list.append((id, neighbor_up))
                        if '-' not in id and '-' not in neighbor_forward and 'z' not in id and 'z' not in neighbor_forward:
                            edges_list.append((id, neighbor_forward))
                        if '-' not in id and '-' not in neighbor_backward and 'z' not in id and 'z' not in neighbor_backward:
                            edges_list.append((id, neighbor_backward))

        g = {}
        for v in vertex_list:
            g[str(v)] = []
        for e in edges_list:
            (v1, v2) = e
            g[str(v1)].append(str(v2))
            g[str(v2)].append(str(v1))
        self.maze_graph = graph.Graph(g)
        self.solution = self.maze_graph.find_path(tmp_start_id, tmp_end_id)
        try:
            self.solution_time = len(self.solution) - 1
        except:
            self.solution_time = None

    @classmethod
    def load_maze(cls, fname):
        all_mazes = []
        with open(fname) as inf:
            lines = (line.rstrip("\r\n") for line in inf)
            big_maze = []
            tmp_maze = []
            for line in list(lines):
                if len(line) < 1:
                    big_maze.append(tmp_maze)
                    tmp_maze = []
                    continue
                try:
                    if re.match('^[-+]?[0-9]+$', line[0]):
                        all_mazes.append(Maze(big_maze))
                        big_maze = [] if line[0] != '0' else big_maze
                        continue
                except:
                    pass
                tmp_maze.append(list(line))

        counter = 0
        for maze in all_mazes:
            if counter > 0:
                maze.matrix_2_graph()
                if maze.solution_time != None:
                    print('Tiempo para salir del laberinto ' + str(counter) +
                          ' : ' + str(maze.solution_time) + ' segundos.')
                else:
                    print('No fue posible salir del laberinto ' +
                          str(counter) + '...')
            counter += 1


def main():
    Maze.load_maze("input.txt")


if __name__ == "__main__":
    main()
