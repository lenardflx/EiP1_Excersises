from time import sleep
from jguvc_eip import basic_io as bio, image_objects as iobj

FILL_COL = {" ": (255, 255, 255), "E": (255, 0, 0), "A": (0, 0, 255),
    "B": (80, 200, 250), "C": (220, 100, 100), "P": (100, 200, 140), ".": (0, 0, 0)}

def read_map(filename):
    return [list(line.strip()) for line in open(filename)]

def get_start(field):
    return next((x, y) for y, row in enumerate(field) for x, cell in enumerate(row) if cell == "E")

def print_map(field, size=20, curr_pos=None):
    stack = [iobj.HorizontalStack([iobj.Rectangle(size, size, FILL_COL[c]) for c in row]) for row in field]
    model = iobj.VerticalStack(stack)
    if curr_pos:
        circ = iobj.Translate(iobj.Circle(10, fill_color=FILL_COL["P"]), curr_pos[0]*size+5, curr_pos[1]*size+5)
        model = iobj.Overlay([model, circ])
    bio.draw_object(model, 50, 50)

def find_way(field, path):
    x, y = path[-1]

    if field[y][x] == " ":
        field[y][x] = "B"

    print_map(field, curr_pos=(x, y))
    sleep(0.15)

    for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
        nx, ny = x + dx, y + dy
        if field[ny][nx] == "A":
            return path + [(nx, ny)]
        if field[ny][nx] == " " and (new_path := find_way(field, path+[(nx,ny)])):
            return new_path

if __name__ == "__main__":
    bio.start()
    maze = read_map("maze_big.txt")  # read_map("maze_small.txt")
    route = find_way(maze, [get_start(maze)])

    bio.print_message("Found route: " + " → ".join(map(str, route)))
    for x, y in route[1:-1]:
        maze[y][x] = "C"

    print_map(maze)
    bio.wait_close()