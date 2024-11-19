from jguvc_eip import basic_io as bio
from math import sin, cos, pi
from time import sleep

# Klasse um besser auf die Variablen zuzugreifen
class RotatingWindmill:
    # Initialisiere die Klasse und setze die Variablen
    def __init__(self, basic_io, center, rectangle_size, triangle_length):
        self.center = center
        self.bio = basic_io
        self.half_rectangle_size = rectangle_size // 2
        self.triangle_length = triangle_length

    # Die Formeln aus 2) zu berechnen der Rotation mithhilfe von math
    def rotate_point(self, coordinates, angle):
        x = (coordinates[0] - self.center[0]) * cos(angle) - (coordinates[1] - self.center[1]) * sin(angle) + self.center[0]
        y = (coordinates[0] - self.center[0]) * sin(angle) + (coordinates[1] - self.center[1]) * cos(angle) + self.center[1]
        return int(x), int(y)

    # Zeichnen des Rechtecks
    def draw_rot_rectangle(self, angle):
        corners = [
            (self.center[0] - self.half_rectangle_size, self.center[1] - self.half_rectangle_size),
            (self.center[0] + self.half_rectangle_size, self.center[1] - self.half_rectangle_size),
            (self.center[0] + self.half_rectangle_size, self.center[1] + self.half_rectangle_size),
            (self.center[0] - self.half_rectangle_size, self.center[1] + self.half_rectangle_size)
        ]
        rotated_corners = [self.rotate_point(corner, angle) for corner in corners]
        self.bio.draw_polygon(rotated_corners, border_color=(0, 0, 0), border_thickness=2, fill_color=None)

    # Zeichnen eines Dreiecks
    def draw_triangle(self, angle):
        tip = self.rotate_point((self.center[0], self.center[1] - self.triangle_length), angle)
        left = self.rotate_point((self.center[0], self.center[1] - self.half_rectangle_size), angle)
        right = self.rotate_point((self.center[0] + self.half_rectangle_size, self.center[1] - self.half_rectangle_size), angle)
        self.bio.draw_polygon([tip, left, right], border_color=(0, 0, 0), border_thickness=2, fill_color=None)

    # Main-Loop
    def main(self):
        bio.start()
        angle = 0
        while True:
            self.bio.clear_image()
            self.draw_rot_rectangle(angle * pi / 180) # Umrechnung von Grad in Bogenmaß
            for n in range(4):
                self.draw_triangle((angle+n*90) * pi / 180) # Umrechnung von Grad in Bogenmaß + 90 Grad pro Dreieck
            angle = (angle + 1) % 360
            sleep(0.016)
        bio.wait_close()

if __name__ == "__main__":
    windmill = RotatingWindmill(basic_io=bio, center=(320, 140), rectangle_size=70, triangle_length=100)
    windmill.main()
