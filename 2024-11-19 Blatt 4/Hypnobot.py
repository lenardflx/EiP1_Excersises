from math import cos, sin, pi
from time import sleep
from jguvc_eip import basic_io as bio

# Konstanten
SPEED:float = 1.5
OMEGA = 1
PENDULUM_LEN = 50
ANCHOR_POINT = (320, 0)
CIRCLES = [
    ((104, 137, 255), 20),
    ((63, 81, 181), 40),
    ((139, 195, 74), 60),
    ((156, 39, 176), 80),
    ((233, 30, 99), 100),
]
CIRCLES_MAX_RADIUS = 100

# Male die Kreise
def draw_concentric_circle(t, circle_center):
    for color, initial_radius in CIRCLES: # Iteriere durch alle Kreise
        current_radius = (initial_radius - t) % CIRCLES_MAX_RADIUS # Berechne den Radius
        bio.draw_circle(
            circle_center[0], circle_center[1],
            current_radius, fill_color=None, border_color=color
        )

def draw_pendulum(angle):
    # Berechne die Position des Pendels
    end_points = [
        int(ANCHOR_POINT[0] + PENDULUM_LEN * sin(angle)),
        int(ANCHOR_POINT[1] + PENDULUM_LEN * cos(angle))
    ]

    # Zeichne die Linie zum Pendel
    bio.draw_line(
        ANCHOR_POINT[0], ANCHOR_POINT[1],
        end_points[0],end_points[1], color=(0, 0, 0), thickness=2
    )
    # Zeichne den Pendel
    bio.draw_circle(end_points[0],end_points[1], 20)

    return end_points

if __name__ == "__main__":
    bio.start()
    curr_t = 0 # Zeit in 60/sek
    while True:
        bio.clear_image()

        curr_angle = (pi / 3) * sin((curr_t*(SPEED/60))*OMEGA) # pi/2 aus Aufgabenstellung stimmt nicht mit erwartetem Ergebnis überein

        position = draw_pendulum(curr_angle)
        draw_concentric_circle(curr_t, position)

        curr_t += 1
        sleep(0.016)