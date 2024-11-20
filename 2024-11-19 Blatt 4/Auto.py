from time import sleep
from jguvc_eip import basic_io as bio

# 1) Auto zeichnen
def draw_car(position):
    car_color = (225,44,47)
    bio.draw_rectangle(position[0], position[1],
                       130, 35,
                       fill_color=car_color,border_thickness=2)
    bio.draw_circle(position[0] + 20, position[1] + 35,
                    15,fill_color=(0, 0, 0))
    bio.draw_circle(position[0] + 110, position[1] + 35,
                    15,fill_color=(0, 0, 0))

# 2) Haus zeichnen
def draw_house():
    house_color = (65,82,175)
    bio.draw_rectangle(400, 90,
                       120, 120,
                       fill_color=house_color,border_thickness=2)
    bio.draw_polygon([(400, 90), (460, 75), (520, 90)],
                     fill_color=house_color,border_thickness=2)

# 3) und 4) Auto vor und hinter Haus vorbeifahren
def draw_screen(car_position,behind_house=False):
    while car_position[0] < 520: # Ende vom Bildschirm
        bio.clear_image()
        if behind_house:
            # erst Haus, dann Auto
            draw_car(car_position)
            draw_house()
        else:
            # erst Auto, dann Haus
            draw_house()
            draw_car(car_position)
        car_position[0] += 2
        sleep(0.016)

if __name__ == "__main__":
    bio.start()

    # Auto vor Haus
    draw_screen([10, 160],False)

    sleep(5)

    # Auto hinter Haus
    draw_screen([10, 160],True)

    bio.wait_close()