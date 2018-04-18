class Layer:
    def __init__(self, maze):
        self.maze = maze


class Maze:

    @classmethod
    def get_layers(self, ):
        

    @classmethod
    def load_maze(cls, fname):
        with open(fname) as inf:
            lines = (line.rstrip("\r\n") for line in inf)
            maze = [list(line) for line in lines]
        return cls(maze)

    def __init__(self, maze):
        self.maze = maze

    def __str__(self):
        return "\n".join(''.join(line) for line in self.maze)


def main():
    maze = Maze.load_maze("input.txt")
    print(maze)


if __name__ == "__main__":
    main()
