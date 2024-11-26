from time import sleep
from jguvc_eip import basic_io as bio

SCREEN_SIZE = (640, 480)
IMAGE_SIZE = (48, 25) # originell waren 50 aber zurechtgeschnitten für besseres Ergebnis
CORNER_OFFSET = 10 # 35-25 = 10

# Aktualisiert die Position des Bildes und prüft auf Kollisionen
def update_position(position, direction, collision_data):
    for axis in range(2):  # Änder Richtung (0: x, 1: y)
        if position[axis] + IMAGE_SIZE[axis] >= SCREEN_SIZE[axis] or position[axis] <= 0:
            direction[axis] *= -1

    # Prüft ob Ecke erreicht wurde (abhängig von Richtung und Threshold)
    in_corner = all(abs(position[axis] - (0 if direction[axis] < 0 else SCREEN_SIZE[axis] - IMAGE_SIZE[axis])) < CORNER_OFFSET for axis in (0, 1))
    if in_corner and not collision_data['flag']:
        collision_data['count'] += 1
        bio.print_message(f"Eckenkollision erkannt! Anzahl: {collision_data['count']}")
        collision_data['flag'] = True
    elif not in_corner:
        collision_data['flag'] = False

    position[0] += direction[0]
    position[1] += direction[1]

if __name__ == '__main__':
    bio.start()

    pos = [(SCREEN_SIZE[0]-IMAGE_SIZE[0])//2, (SCREEN_SIZE[1]-IMAGE_SIZE[1])//2]
    curr_dir = [1, 1]
    collision = {'flag': False, 'count': 0}
    image = bio.load_image('dvd_selfmade.png')

    while True:
        update_position(pos, curr_dir, collision)
        bio.clear_image()
        bio.draw_image(pos[0], pos[1], image)
        sleep(1 / 60)
