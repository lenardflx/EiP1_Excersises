from jguvc_eip import basic_io as bio
from math import sin, cos, radians
from time import sleep

# Konstanten
CENTER = (320, 140)
RECTANGLE_SIZE = 70
TRIANGLE_LENGTH = 70
SPEED:float = 1

# Umrechnung von Koordinaten gegeben in Aufgabenstellung (und umrechnen in radians, da "math" dies voraussetzt)
def rotate_point_coord(coordinates, angle):
    x = (coordinates[0] - CENTER[0]) * cos(radians(angle)) - (coordinates[1] - CENTER[1]) * sin(radians(angle)) + CENTER[0]
    y = (coordinates[0] - CENTER[0]) * sin(radians(angle)) + (coordinates[1] - CENTER[1]) * cos(radians(angle)) + CENTER[1]
    return int(x), int(y)

# Zeichnen des Rechtecks
def draw_rot_rectangle(angle):
    corners = [ # Alle Eckpositionen
        rotate_point_coord((CENTER[0] - RECTANGLE_SIZE // 2, CENTER[1] - RECTANGLE_SIZE // 2), angle),
        rotate_point_coord((CENTER[0] + RECTANGLE_SIZE // 2, CENTER[1] - RECTANGLE_SIZE // 2), angle),
        rotate_point_coord((CENTER[0] + RECTANGLE_SIZE // 2, CENTER[1] + RECTANGLE_SIZE // 2), angle),
        rotate_point_coord((CENTER[0] - RECTANGLE_SIZE // 2, CENTER[1] + RECTANGLE_SIZE // 2), angle)
    ]
    bio.draw_polygon(corners, border_thickness=2, fill_color=None) # Polygon, da draw_rectangle keinen Winkel kennt

# Zeichnen von einzelnem Dreieck
def draw_triangle(angle):
    corners = [
        rotate_point_coord((CENTER[0], CENTER[1] - RECTANGLE_SIZE // 2 - TRIANGLE_LENGTH), angle), # Spitze
        rotate_point_coord((CENTER[0], CENTER[1] - RECTANGLE_SIZE // 2), angle), # Mitte
        rotate_point_coord((CENTER[0] + RECTANGLE_SIZE // 2, CENTER[1] - RECTANGLE_SIZE // 2), angle)  # Ecke
    ]
    bio.draw_polygon(corners, border_thickness=2, fill_color=None)

if __name__ == "__main__":
    bio.start()
    curr_angle = 0
    while True:
        bio.clear_image()
        draw_rot_rectangle(curr_angle) # Umrechnung von Grad in Bogenmaß
        for n in range(4):
            draw_triangle(curr_angle + n * 90) # Umrechnung von Grad in Bogenmaß + 90 Grad pro Dreieck
        curr_angle = (curr_angle + SPEED) % 360
        sleep(0.016)
    # bio.wait_close() Programm wird nie beendet, daher irrelevant