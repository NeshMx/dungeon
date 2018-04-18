import re

class Node:
    def __init__(self, id, reachable, adj):
        self.id = id
        self.reachable = reachable
        self.adj = adj


class Layer:
    def __init__(self, maze):
        self.maze = maze


class Maze:

    @classmethod
    def load_maze(cls, fname):
        with open(fname) as inf:
            lines = (line.rstrip("\r\n") for line in inf)
            # maze = [list(line) for line in lines]
            count = 0
            for line in list(lines):
                try:
                    if re.match('^[-+]?[0-9]+$', line[0]):
                        
                        print('Passed')
                        
                except:
                    pass
                

    def __init__(self, maze):
        self.maze = maze

    def __str__(self):
        return "\n".join(''.join(line) for line in self.maze)


def main():
    maze = Maze.load_maze("input.txt")
    # print(maze)


if __name__ == "__main__":
    main()
