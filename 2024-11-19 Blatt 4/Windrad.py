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

LEFT_CORNER = CENTER[0] - HALF_RECTANGLE_SIZE
RIGHT_CORNER = CENTER[0] + HALF_RECTANGLE_SIZE
TOP_CORNER = CENTER[1] - HALF_RECTANGLE_SIZE
BOTTOM_CORNER = CENTER[1] + HALF_RECTANGLE_SIZE

RECTANGLE_CORNERS = [
    (LEFT_CORNER, TOP_CORNER),      # Oben links
    (RIGHT_CORNER, TOP_CORNER),     # Oben rechts
    (RIGHT_CORNER, BOTTOM_CORNER),  # Unten rechts
    (LEFT_CORNER, BOTTOM_CORNER)    # Unten links
]

TRIANGLE_CORNERS = [
    (CENTER[0], TOP_CORNER - TRIANGLE_LENGTH),  # Spitze
    (CENTER[0], TOP_CORNER),                    # Mitte
    (RIGHT_CORNER, TOP_CORNER)                  # Ecke
]


# Umrechnung von Koordinaten gegeben in Aufgabenstellung
def rotate_point_coord(coordinates, angle):
    angle_radians = radians(angle)
    cos_angle = cos(angle_radians)
    sin_angle = sin(angle_radians)

    offset_x = coordinates[0] - CENTER[0]
    offset_y = coordinates[1] - CENTER[1]

    x = offset_x * cos_angle - offset_y * sin_angle + CENTER[0]
    y = offset_x * sin_angle + offset_y * cos_angle + CENTER[1]

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
        draw_rot_rectangle(curr_angle)
        for n in range(4):
            draw_triangle(curr_angle + n * 90)
        curr_angle = (curr_angle + SPEED) % 360
        sleep(0.016)
    # bio.wait_close() Programm wird nie beendet, daher irrelevant
