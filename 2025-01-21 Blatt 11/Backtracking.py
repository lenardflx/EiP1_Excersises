from time import sleep

from jguvc_eip import basic_io as bio, image_objects as iobj

FILL_COLORS = {
    " ": (255, 255, 255),  # walkable
    "E": (255, 0, 0),  # start
    "A": (0, 0, 255),  # end
    "B": (80, 200, 250),  # visited
    "C": (220, 100, 100),  # correct path
    ".": (0, 0, 0)  # wall
}
PIXEL_SIZE = 20


def read_map(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file]


def get_start(field):
    for y, row in enumerate(field):
        for x, char in enumerate(row):
            if char == "E":
                return x, y


def print_map(field, pixel_size=PIXEL_SIZE):
    obj = iobj.VerticalStack([
        iobj.HorizontalStack([
            iobj.Rectangle(pixel_size, pixel_size, FILL_COLORS[char]) for char in row
        ]) for row in field
    ])

    bio.draw_object(obj, 50, 50)


def find_way(field, path):
    x, y = path[-1]

    if field[y][x] == " ":
        field[y][x] = "B"
        sleep(0.1)
        print_map(field)

    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_x, new_y = x + dx, y + dy
        match field[new_y][new_x]:
            case "A":
                return path + [(new_x, new_y)]
            case " ":
                new_path = find_way(field, path + [(new_x, new_y)])
                if new_path:
                    return new_path
            case _:
                continue


if __name__ == "__main__":
    bio.start()
    if input("Type 'b' for big maze, else small maze: ") == "b":
        maze = read_map("maze_big.txt")
    else:
        maze = read_map("maze_small.txt")

    print_map(maze)
    start = get_start(maze)
    route = find_way(maze, [start])

    bio.print_message("Found route: " + " → ".join(map(str, route)))
    for x, y in route[1:-1]:
        maze[y][x] = "C"
    print_map(maze)

    bio.wait_close()
