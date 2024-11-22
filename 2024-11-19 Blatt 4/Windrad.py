from jguvc_eip import basic_io as bio
from math import sin, cos, radians
from time import sleep

# Parameter
CENTER = (320, 140)
RECTANGLE_SIZE = 70
TRIANGLE_LENGTH = 50
SPEED: float = 1.5

# Vorab Berechnungen
HALF_RECTANGLE_SIZE = RECTANGLE_SIZE // 2
RECTANGLE_CORNERS = [
    (CENTER[0] - HALF_RECTANGLE_SIZE, CENTER[1] - HALF_RECTANGLE_SIZE),  # Oben links
    (CENTER[0] + HALF_RECTANGLE_SIZE, CENTER[1] - HALF_RECTANGLE_SIZE),  # Oben rechts
    (CENTER[0] + HALF_RECTANGLE_SIZE, CENTER[1] + HALF_RECTANGLE_SIZE),  # Unten rechts
    (CENTER[0] - HALF_RECTANGLE_SIZE, CENTER[1] + HALF_RECTANGLE_SIZE)  # Unten links
]
TRIANGLE_CORNERS = [
    (CENTER[0], CENTER[1] - HALF_RECTANGLE_SIZE - TRIANGLE_LENGTH),  # Spitze
    (CENTER[0], CENTER[1] - HALF_RECTANGLE_SIZE),  # Mitte
    (CENTER[0] + HALF_RECTANGLE_SIZE, CENTER[1] - HALF_RECTANGLE_SIZE)  # Ecke
]


# Umrechnung von Koordinaten gegeben in Aufgabenstellung (und umrechnen in radians, da "math" dies benötigt)
def rotate_point_coord(coordinates, angle):
    cos_angle = cos(radians(angle))
    sin_angle = sin(radians(angle))
    x = (coordinates[0] - CENTER[0]) * cos_angle - (coordinates[1] - CENTER[1]) * sin_angle + CENTER[0]
    y = (coordinates[0] - CENTER[0]) * sin_angle + (coordinates[1] - CENTER[1]) * cos_angle + CENTER[1]
    return int(x), int(y)


# Zeichnen des Rechtecks
def draw_rot_rectangle(angle):
    corners = [rotate_point_coord(corner, angle) for corner in RECTANGLE_CORNERS]
    bio.draw_polygon(corners, border_thickness=2, fill_color=None)  # Polygon, da draw_rectangle keinen Winkel kennt


# Zeichnen von einzelnem Dreieck
def draw_triangle(angle):
    corners = [rotate_point_coord(corner, angle) for corner in TRIANGLE_CORNERS]
    bio.draw_polygon(corners, border_thickness=2, fill_color=None)


if __name__ == "__main__":
    bio.start()
    curr_angle = 0
    while True:
        bio.clear_image()
        draw_rot_rectangle(curr_angle)  # Umrechnung von Grad in Bogenmaß
        for n in range(4):
            draw_triangle(curr_angle + n * 90)  # Umrechnung von Grad in Bogenmaß + 90 Grad pro Dreieck
        curr_angle = (curr_angle + SPEED) % 360
        sleep(0.016)
    # bio.wait_close() Programm wird nie beendet, daher irrelevant
