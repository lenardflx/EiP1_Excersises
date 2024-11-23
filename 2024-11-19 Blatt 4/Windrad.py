from jguvc_eip import basic_io as bio
from math import sin, cos
from time import sleep

# Parameter
CENTER = (320, 140)
RECTANGLE_SIZE = 70
TRIANGLE_LENGTH = 50
ANGLE_INC = 0.05

# Vorab Berechnungen
h = RECTANGLE_SIZE // 2
REC_CORNERS_OFF = [(-h, -h), (h, -h), (h, h), (-h, h)]  # Rechteck
TRI_CORNERS_OFF_LIST = [[(0, -h - TRIANGLE_LENGTH), (0, -h), (h, -h)],    # Dreieck Oben
                        [(h + TRIANGLE_LENGTH, 0), (h, 0), (h, h)],       # Dreieck Rechts
                        [(0, h + TRIANGLE_LENGTH), (0, h), (-h, h)],      # Dreieck Unten
                        [(-h - TRIANGLE_LENGTH, 0), (-h, 0), (-h, -h)]]   # Dreieck Links

def rotate_point(point, angle):
    cos_angle, sin_angle = cos(angle), sin(angle)
    return (int(CENTER[0] + point[0] * cos_angle - point[1] * sin_angle),
            int(CENTER[1] + point[0] * sin_angle + point[1] * cos_angle))

# Zeichnen des Rechtecks
def draw_rot_rectangle(angle):
    corners = [rotate_point(point, angle) for point in REC_CORNERS_OFF]
    bio.draw_polygon(corners, border_thickness=2, fill_color=None)

# Zeichnen von einzelnem Dreieck
def draw_rot_triangle(angle, ref_coords):
    corners = [rotate_point(point, angle) for point in ref_coords]
    bio.draw_polygon(corners, border_thickness=2, fill_color=None)

if __name__ == "__main__":
    bio.start()
    curr_angle = 0
    while True:
        bio.clear_image()
        draw_rot_rectangle(curr_angle)
        for triangle in TRI_CORNERS_OFF_LIST:
            draw_rot_triangle(curr_angle, triangle)
        curr_angle += ANGLE_INC
        sleep(0.016)
