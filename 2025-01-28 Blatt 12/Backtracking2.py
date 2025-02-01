from time import sleep, time
from jguvc_eip import basic_io as bio, image_objects as iobj

FILL_COL = {" ": (255, 255, 255), "E": (255, 0, 0), "A": (0, 0, 255),
            "B": (80, 200, 250), "C": (220, 100, 100), "P": (100, 200, 140), ".": (0, 0, 0)}
PX_SIZE = 10
USE_MEMORY = True

def read_map(filename):
    return [list(line.strip()) for line in open(filename)]

def get_start(field):
    return next((x, y) for y, row in enumerate(field) for x, cell in enumerate(row) if cell == "E")

def print_map(field, pos=None, visited=[]):
    stack = [[iobj.Rectangle(PX_SIZE, PX_SIZE, FILL_COL[c if (x, y) not in visited else "B"])
              for x, c in enumerate(row)] for y, row in enumerate(field)]
    model = iobj.VerticalStack([iobj.HorizontalStack(row) for row in stack])
    if pos:
        circ = iobj.Translate(iobj.Circle(PX_SIZE // 2, FILL_COL["P"]), pos[0] * PX_SIZE + PX_SIZE // 4,
                              pos[1] * PX_SIZE + PX_SIZE // 4)
        model = iobj.Overlay([model, circ])
    bio.draw_object(model, 50, 50)

def find_way(field, path, visited, possible_paths):
    x, y = path[-1]
    print_map(field, (x, y), visited)
    sleep(0.02)

    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if possible_paths and len(path)+1 >= len(possible_paths[-1]):
            return
        nx, ny = x + dx, y + dy
        if field[ny][nx] == "A":
            possible_paths.append(path + [(nx, ny)])
        if (nx, ny) not in visited and field[ny][nx] == " ":
            find_way(field, path + [(nx, ny)], visited + [(nx, ny)], possible_paths)

if __name__ == "__main__":
    bio.start()
    maze = read_map("maze_small.txt")
    paths = []
    find_way(maze, [get_start(maze)], [], paths)

    bio.print_message("Found best route: " + " → ".join(map(str, paths[-1])))
    for x, y in paths[-1][1:-1]:
        maze[y][x] = "C"

    print_map(maze)
    bio.wait_close()

#2b: Alle weiteren Lösungen, die gefunden werden, haben weniger Schritte Zweige, als die Lösungen davor.