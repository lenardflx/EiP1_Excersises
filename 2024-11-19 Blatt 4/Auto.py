from time import sleep
from jguvc_eip import basic_io as bio

# 1) Auto zeichnen
def draw_car(position):
    bio.draw_rectangle(position[0], position[1],
                       130, 50,
                       fill_color=(255, 0, 0))
    bio.draw_circle(position[0] + 20, position[1] + 50,
                    15,fill_color=(0, 0, 0))
    bio.draw_circle(position[0] + 110, position[1] + 50,
                    15,fill_color=(0, 0, 0))

# 2) Haus zeichnen
def draw_house():
    bio.draw_rectangle(400, 90,
                       120, 130,
                       fill_color=(0, 0, 255))
    bio.draw_polygon([(400, 90), (460, 70), (520, 90)],
                     fill_color=(0, 0, 255))

# 3) und 4) Auto vor und hinter Haus vorbeifahren
def draw_screen(car_position,behind_house=False):
    while car_position[0] < 500:
        bio.clear_image()
        if behind_house:
            draw_car(car_position)
            draw_house()
        else:
            draw_house()
            draw_car(car_position)
        car_position[0] += 2
        sleep(0.016)

if __name__ == "__main__":
    bio.start()

    # Auto vor Haus
    car_pos = [10, 150]
    draw_screen(car_pos,False)

    sleep(5)

    # Auto hinter Haus
    car_pos = [10, 150]
    draw_screen(car_pos,True)

    bio.wait_close()
