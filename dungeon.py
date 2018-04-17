# Input: L R C (i.e. 3 4 5)
# Ouput: Escaped in 11 minute(s)


class Maze:
    @classmethod
    def load_file(self, fname):
        with open(fname) as fp:
            # params = fp.read().split(" ")
            lines = (line.rstrip("\r\n") for line in fp)
            maze = [list(line) for line in lines]
        return self(maze)

        # levels = params[0]
        # rows = params[1]
        # columns = params[2]

    def __init__(self, maze):
        self.maze = maze

    def __str__(self):
        return '\n'.join(''.join(line) for line in self.maze)

    def move(self, parameter_list):
        pass


def main():
    # file_name = input('Introduce la ruta del archivo de entradas: ')
    maze = Maze().load_file("input.txt")
    print(maze)
    # show_dungeon()


if __name__ == '__main__':
    main()
