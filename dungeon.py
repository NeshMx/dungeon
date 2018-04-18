import re


class Node:
    def __init__(self, id, value, adj):
        self.id = id
        self.start = True if value == 'S' else False
        self.end = True if value == 'E' else False
        self.reachable = True if value == '.' else False
        self.adj = adj


class Layer:
    def __init__(self, maze):
        self.maze = maze


class Maze:

    def __init__(self, maze=[]):
        self.maze = maze

    def __str__(self):
        return "\n".join(''.join(line) for line in self.maze)

    @classmethod
    def load_maze(cls, fname):
        maze_arrays = []
        with open(fname) as inf:
            lines = (line.rstrip("\r\n") for line in inf)
            start_maze = False
            id = 1
            for line in list(lines):
                try:
                    if re.match('^[-+]?[0-9]+$', line[0]):
                        tmp_maze = Maze()
                        id = 0
                        start_maze = True
                        continue
                    if start_maze:
                        for ch in line:
                            tmp_node = Node(id+=1, ch, )
                except:
                    pass


def main():
    maze = Maze.load_maze("input.txt")
    # print(maze)


if __name__ == "__main__":
    main()
