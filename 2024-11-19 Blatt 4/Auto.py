from time import sleep
from jguvc_eip import basic_io as bio


# 1) Auto zeichnen
def draw_car(position):
    car_color = (225, 44, 47)
    bio.draw_rectangle(position[0], position[1],
                       130, 35,
                       fill_color=car_color, border_thickness=2)
    bio.draw_circle(position[0] + 20, position[1] + 35,
                    15, fill_color=(0, 0, 0))
    bio.draw_circle(position[0] + 110, position[1] + 35,
                    15, fill_color=(0, 0, 0))


# 2) Haus zeichnen
def draw_house():
    house_color = (65, 82, 175)
    bio.draw_rectangle(400, 90,
                       120, 120,
                       fill_color=house_color, border_thickness=2)
    bio.draw_polygon([(400, 90), (460, 75), (520, 90)],
                     fill_color=house_color, border_thickness=2)


if __name__ == "__main__":
    bio.start()

    # 3) Auto vor Haus
    bio.print_message("Auto fährt vor Haus")
    car_position = [10, 160]
    while car_position[0] < 520:  # Ende vom Bildschirm
        bio.clear_image()
        draw_house()
        draw_car(car_position)
        car_position[0] += 2
        sleep(0.016)
    bio.print_message("Auto hält an")
    bio.print_message("Kurze Pause :)")
    sleep(3)

    # 4) Auto hinter Haus
    bio.print_message("Auto fährt hinter Haus")
    car_position = [10, 160]
    while car_position[0] < 520:  # Ende vom Bildschirm
        bio.clear_image()
        draw_car(car_position)
        draw_house()
        car_position[0] += 2
        sleep(0.016)
    bio.print_message("Auto hält an")

    bio.wait_close()
