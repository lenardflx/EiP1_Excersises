from jguvc_eip import basic_io as bio
from math import sin, cos, radians
from time import sleep

# Konstanten
CENTER = (320, 140)
RECTANGLE_SIZE = 70
HALF_RECT_SIZE = RECTANGLE_SIZE // 2
TRIANGLE_LENGTH = 100

# Klasse um besser auf die Variablen zuzugreifen
def rotate_point(coordinates, angle):
    x = (coordinates[0] - CENTER[0]) * cos(angle) - (coordinates[1] - CENTER[1]) * sin(angle) + CENTER[0]
    y = (coordinates[0] - CENTER[0]) * sin(angle) + (coordinates[1] - CENTER[1]) * cos(angle) + CENTER[1]
    return int(x), int(y)

    # Zeichnen des Rechtecks
def draw_rot_rectangle(angle):
    corners = [ # Alle Eckpositionen
        rotate_point((CENTER[0] - HALF_RECT_SIZE, CENTER[1] - HALF_RECT_SIZE), angle),
        rotate_point((CENTER[0] + HALF_RECT_SIZE, CENTER[1] - HALF_RECT_SIZE), angle),
        rotate_point((CENTER[0] + HALF_RECT_SIZE, CENTER[1] + HALF_RECT_SIZE), angle),
        rotate_point((CENTER[0] - HALF_RECT_SIZE, CENTER[1] + HALF_RECT_SIZE), angle)
    ]
    bio.draw_polygon(corners, border_thickness=2, fill_color=None) # Polygon, da draw_rectangle keinen Winkel kennt

# Zeichnen von einzelnem Dreieck
def draw_triangle(angle):
    corners = [
        rotate_point((CENTER[0], CENTER[1] - TRIANGLE_LENGTH), angle), # Spitze
        rotate_point((CENTER[0], CENTER[1] - HALF_RECT_SIZE), angle), # Mitte
        rotate_point((CENTER[0] + HALF_RECT_SIZE, CENTER[1] - HALF_RECT_SIZE), angle) # Ecke
    ]
    bio.draw_polygon(corners, border_thickness=2, fill_color=None)

if __name__ == "__main__":
    bio.start()
    angle = 0
    while True:
        bio.clear_image()
        draw_rot_rectangle(radians(angle)) # Umrechnung von Grad in Bogenmaß
        for n in range(4):
            draw_triangle(radians(angle+n*90)) # Umrechnung von Grad in Bogenmaß + 90 Grad pro Dreieck
        angle = (angle + 1) % 360
        sleep(0.016)
    bio.wait_close()
