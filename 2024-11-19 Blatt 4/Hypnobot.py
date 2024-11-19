from math import cos, sin, pi
from time import sleep
from jguvc_eip import basic_io as bio

# Parameter
OMEGA_VAL = 1
PENDULUM_LEN = 200
ANCHOR_POINT = (300, 0)
CIRCLES = [
    ((104, 137, 255), 20),
    ((63, 81, 181), 40),
    ((139, 195, 74), 60),
    ((156, 39, 176), 80),
    ((233, 30, 99), 100),
]

# Male die Kreise
def draw_concentric_circle(t, circle_center):
    for color, initial_radius in CIRCLES: # Iteriere durch alle Kreise
        current_radius = (initial_radius - t) % 100 # Berechne den Radius
        bio.draw_circle(
            circle_center[0], circle_center[1],
            current_radius, fill_color=None, border_color=color
        )

def draw_pendulum(angle):
    # Berechne die Position des Pendels
    x = int(ANCHOR_POINT[0] + PENDULUM_LEN * sin(angle))
    y = int(ANCHOR_POINT[1] + PENDULUM_LEN * cos(angle))

    # Zeichne die Linie zum Pendel
    bio.draw_line(
        ANCHOR_POINT[0], ANCHOR_POINT[1],
        x, y, color=(0, 0, 0), thickness=2
    )
    # Zeichne den Pendel
    bio.draw_circle(x, y, 20)

    return x, y

if __name__ == "__main__":
    bio.start()
    curr_t = 0
    omega = OMEGA_VAL * pi / 100
    while True:
        bio.clear_image()

        curr_angle = (pi / 4) * sin(curr_t * omega)

        position = draw_pendulum(curr_angle)
        draw_concentric_circle(curr_t, position)

        curr_t += 1
        sleep(0.016)

    bio.wait_close()
