from math import cos, sin, pi
from time import sleep
from jguvc_eip import basic_io as bio

# Parameter
SPEED,LEN,ANCHOR = 1.5,200,(320, 0)
CIRCLES =[(100,(104,137,255)),(80,(63,81,181)),(60,(139,195,74)),(40,(156,39,176)),(20,(233,30,99))] # Radius,Farbe

def draw_concentric_circle(t, circle_center):
    for radius, color in CIRCLES:
        bio.draw_circle(circle_center[0], circle_center[1], (radius-t) % 100, None, color)

def draw_pendulum(angle):
    x,y = (int(ANCHOR[0] + LEN * sin(angle)), int(ANCHOR[1] + LEN * cos(angle)))
    bio.draw_line(ANCHOR[0], ANCHOR[1], x, y, thickness=2)
    bio.draw_circle(x, y, 20)
    return x, y

if __name__ == "__main__":
    bio.start()
    ctime = 0  # 60t/sek
    while True:
        bio.clear_image()
        pos = draw_pendulum((pi / 3) * sin(ctime * (SPEED / 60)))
        draw_concentric_circle(ctime, pos) # pi/2 aus Aufgabenstellung stimmt nicht mit erwartetem Ergebnis überein
        ctime += 1
        sleep(1/60)
