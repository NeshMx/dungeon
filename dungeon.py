import re
import graph


class Node:
    def __init__(self, id, value, adj):
        self.id = id
        self.start = True if value == 'S' else False
        self.end = True if value == 'E' else False
        self.reachable = True if value == '.' else False
        self.adj = adj


class Maze:

    def __init__(self, maze=[]):
        self.maze = maze
        self.maze_graph = graph.Graph()

    def __str__(self):
        for m in self.maze:
            for line in m:
                print(line)

        # return "\n".join(''.join(line) for line in self.maze)
        return ''

    def matrix_2_graph(self):
        for i, layer in enumerate(self.maze):
            for j, row in enumerate(layer):
                for k, ch in enumerate(row):
                    id = str(i) + str(j) + str(k)
                    neighbor_right = str(i) + str(j) + str(k + 1)
                    neighbor_left = str(i) + str(j) + str(k - 1)
                    neighbor_down = str(i) + str(j + 1) + str(k)
                    neighbor_up = str(i) + str(j - 1) + str(k)
                    neighbor_forward = str(i + 1) + str(j) + str(k)
                    neighbor_backward = str(i - 1) + str(j) + str(k)

                    if not '#' == ch:
                        self.maze_graph.add_vertex(id, ch)
                        self.maze_graph.add_edge([id, neighbor_right])
                        self.maze_graph.add_edge([id, neighbor_left])
                        self.maze_graph.add_edge([id, neighbor_down])
                        self.maze_graph.add_edge([id, neighbor_up])
                        self.maze_graph.add_edge([id, neighbor_forward])
                        self.maze_graph.add_edge([id, neighbor_backward])

        # print(self.maze_graph)
        """ print('Vertex: ')
        print(self.maze_graph.vertices())
        print('Edges: ')
        print(self.maze_graph.edges()) """
        print('Solución : ')
        print(self.maze_graph.find_all_paths('000', '024'))
        ddddvar = input('input dummy')

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

            # print(all_mazes)
            for maze in all_mazes:
                maze.matrix_2_graph()
                # print(maze)


def main():
    maze = Maze.load_maze("input.txt")
    # print(maze)


if __name__ == "__main__":
    main()
