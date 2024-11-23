from math import cos, sin, pi
from time import sleep
from jguvc_eip import basic_io as bio

# Parameter
SPEED = 1.5
PENDULUM_LEN = 200
ANCHOR_POINT = (320, 0)
CIRC_COLORS = [(104, 137, 255),(63, 81, 181),(139, 195, 74),(156, 39, 176),(233, 30, 99)]

# Male die Kreise
def draw_concentric_circle(t, circle_center):
    for radius, color in zip(range(100, 0, -20), CIRC_COLORS):
        bio.draw_circle(circle_center[0], circle_center[1], (radius - t) % 100, None, color)

# Berechne Position vom Pendel und male ihn
def draw_pendulum(angle):
    x,y = (int(ANCHOR_POINT[0] + PENDULUM_LEN * sin(angle)), int(ANCHOR_POINT[1] + PENDULUM_LEN * cos(angle)))
    bio.draw_line(ANCHOR_POINT[0], ANCHOR_POINT[1],x, y, thickness=2)
    bio.draw_circle(x, y, 20)
    return x, y

if __name__ == "__main__":
    bio.start()
    curr_t = 0  # 60t/sek
    while True:
        bio.clear_image()
        curr_angle = (pi / 3) * sin(curr_t * (SPEED / 60))  # pi/2 aus Aufgabenstellung stimmt nicht mit erwartetem Ergebnis überein
        draw_concentric_circle(curr_t, draw_pendulum(curr_angle))
        curr_t += 1
        sleep(1/60)
