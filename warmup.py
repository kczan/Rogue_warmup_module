def generate_map(max_height, max_width):

    map_list = []
    map_row = []
    for _ in range(max_height):
        map_row.append('#')
        for _ in range(max_width - 2):
            map_row.append('.')
        map_row.append('#')
        map_list.append(map_row)
        map_row = []
    return map_list


def draw_map(map_list):
    import os
    os.system('clear')
    map_width = 30
    print(map_width * '# ')
    for row in map_list:
        print(' '.join(row))
    print(map_width * '# ')


def read_from_keyboard():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def move_character(x_coord, y_coord, char, max_width, max_height):
    import sys
    if char == 'w' and y_coord > 0:
        y_coord -= 1
    elif char == 's' and y_coord < max_height - 1:
        y_coord += 1
    elif char == 'd' and x_coord < max_width - 2:
        x_coord += 1
    elif char == 'a' and x_coord > 1:
        x_coord -= 1
    elif char == ';':
        sys.exit(0)

    return x_coord, y_coord


def place_character_on_map(x_coord, y_coord, map_list):
    map_list[y_coord][x_coord] = '@'
    return map_list


max_width = 30
max_height = 20
x_coord = 5
y_coord = 7
game_map = generate_map(max_height, max_width)
draw_map(game_map)
while True:
    movement = read_from_keyboard()
    x_coord, y_coord = move_character(x_coord, y_coord, movement, max_width, max_height)
    game_map = place_character_on_map(x_coord, y_coord, game_map)
    draw_map(game_map)
    game_map = generate_map(max_height, max_width)
