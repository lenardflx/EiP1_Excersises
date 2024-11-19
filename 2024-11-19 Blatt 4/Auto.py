from time import sleep
from jguvc_eip import basic_io as bio

# 1) Auto zeichnen
def draw_car(position):
    car_color = (255, 0, 0)
    wheel_color = (0, 0, 0)
    bio.draw_rectangle(position[0], position[1],
                       140, 50,
                       fill_color=car_color)
    bio.draw_circle(position[0] + 20, position[1] + 50,
                    15,
                    fill_color=wheel_color)
    bio.draw_circle(position[0] + 140 - 20, position[1] + 50,
                    15,
                    fill_color=wheel_color)

# 2) Haus zeichnen
def draw_house():
    house_color = (0, 0, 255)
    bio.draw_rectangle(400, 90,
                       120, 130,
                       fill_color=house_color)
    bio.draw_polygon([(400, 90), (460, 70), (520, 90)],
                     fill_color=house_color)
# 3) Auto vor Haus vorbeufahren
def move_car_in_front_of_house(car_position):
    while car_position[0] < 500:
        bio.clear_image()
        draw_house()
        draw_car(car_position)
        car_position[0] += 2
        sleep(0.016)
# 4) Auto hinter Haus vorbeifahren
def move_car_behind_house(car_position):
    while car_position[0] < 500:
        bio.clear_image()
        draw_car(car_position)
        draw_house()
        car_position[0] += 2
        sleep(0.016)

if __name__ == "__main__":
    bio.start()

    car_pos = [10, 150]

    move_car_in_front_of_house(car_pos)

    sleep(5)

    car_pos = [10, 150]
    move_car_behind_house(car_pos)

    bio.wait_close()
