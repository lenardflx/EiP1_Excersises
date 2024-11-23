from time import sleep
from jguvc_eip import basic_io as bio

# 1) Auto zeichnen
def draw_car(x_position):
    bio.draw_rectangle(x_position, 160,130, 35, (225, 44, 47), border_thickness=2)
    bio.draw_circle(x_position + 20, 160 + 35,15)
    bio.draw_circle(x_position + 110, 160 + 35,15)

# 2) Haus zeichnen
def draw_house():
    bio.draw_rectangle(400, 90,120, 120, (65, 82, 175), border_thickness=2)
    bio.draw_polygon([(400, 90), (460, 75), (520, 90)], (65, 82, 175), border_thickness=2)

if __name__ == "__main__":
    bio.start()
    # 3) Auto vor Haus
    x_pos = -130
    while x_pos < 700:
        bio.clear_image()
        draw_house()
        draw_car(x_pos)
        x_pos += 4
        sleep(0.016)
    # 4) Auto hinter Haus
    x_pos = -130
    while x_pos < 700:
        bio.clear_image()
        draw_car(x_pos)
        draw_house()
        x_pos += 4
        sleep(0.016)

    bio.wait_close()
