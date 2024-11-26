from time import sleep
from jguvc_eip import basic_io as bio

SCREEN_SIZE = (640, 480)
IMAGE_SIZE = (48, 25) # originell waren 50 aber zurechtgeschnitten für besseres Ergebnis
CORNER_THRESHOLD = 10

def update_position(position, direction, corner_collision_flag, corner_collision_count):
    for axis in range(2):  # Änder Richtung (0: x, 1: y)
        if position[axis] + IMAGE_SIZE[axis] >= SCREEN_SIZE[axis] or position[axis] <= 0:
            direction[axis] *= -1

    # Überprüft Eckenkollision
    corners = [(0,0),(SCREEN_SIZE[0]-IMAGE_SIZE[0],0),(0,SCREEN_SIZE[1]-IMAGE_SIZE[1]),
               (SCREEN_SIZE[0]-IMAGE_SIZE[0],SCREEN_SIZE[1]-IMAGE_SIZE[1])]
    in_corner = any(abs(position[0] - corner[0]) < CORNER_THRESHOLD and
                    abs(position[1] - corner[1]) < CORNER_THRESHOLD
                    for corner in corners)
    if in_corner and not corner_collision_flag[0]:
        corner_collision_count[0] += 1
        bio.print_message(f"Eckenkollision erkannt! Anzahl: {corner_collision_count[0]}")
        corner_collision_flag[0] = True
    elif not in_corner:
        corner_collision_flag[0] = False

    # Aktualisiert die Position
    position[0] += direction[0]
    position[1] += direction[1]

if __name__ == '__main__':
    bio.start()

    pos = [(SCREEN_SIZE[0] - IMAGE_SIZE[0]) // 2, (SCREEN_SIZE[1] - IMAGE_SIZE[1]) // 2]
    curr_dir = [1, 1]
    i = bio.load_image('dvd_selfmade.png')
    collision_flag = [False]
    collision_count = [0]

    while True:
        update_position(pos, curr_dir, collision_flag, collision_count)
        bio.clear_image()
        bio.draw_image(pos[0], pos[1], i)
        sleep(1 / 60)
