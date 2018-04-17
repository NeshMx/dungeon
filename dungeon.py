# Input: L R C (i.e. 3 4 5)
# Ouput: Escaped in 11 minute(s)

def load_file():
    file_name = input('Introduce la ruta del archivo de entradas: ')
    with open(file_name) as fp:
        params = fp.read().split(" ")
    levels = params[0]
    rows = params[1]
    columns = params[2]

    print(levels)
    print(rows)
    print(columns)

def draw_dungeon(parameter_list):
    pass

def move(parameter_list):
    pass

def main():
    load_file()

if __name__ == '__main__':
    main()