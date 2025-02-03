from jguvc_eip import basic_io as bio
from time import sleep
from jguvc_eip import image_objects as iobj

# Parameter
OFFSET = (200, 50)
ACCELERATION = 9.81
SIZE = 15
LINE_HEIGHT = 250
DELTA_TIME = 1 / 60
PIXEL_METER_RATIO = 100
PRESS_REDUCTION = 25
BOUNCE = 0

model = iobj.VerticalStack([
    iobj.Rectangle(SIZE, SIZE),
    iobj.Rectangle(1, LINE_HEIGHT, border_color=(0, 0, 0)),
    iobj.Rectangle(SIZE, SIZE)
])
ball = iobj.Circle(SIZE, fill_color=(255, 0, 0))

if __name__ == "__main__":
    velocity, pos = 0, SIZE
    active, visible = 0, 1
    bio.start()
    try:
        while True:
            if "u" in bio.get_current_keys_down():
                velocity -= PRESS_REDUCTION

            velocity += ACCELERATION * DELTA_TIME * PIXEL_METER_RATIO
            pos += velocity * DELTA_TIME

            if pos >= LINE_HEIGHT:
                pos, velocity = LINE_HEIGHT, -velocity * BOUNCE
            elif pos <= SIZE:
                pos, velocity = SIZE, 0

            active, visible = visible, active
            bio.set_active_image(active)
            bio.set_visible_image(visible)
            bio.copy_image(visible, active)

            bio.clear_image()
            bio.draw_object(iobj.Overlay([model, iobj.Translate(ball, 0, int(pos))]), *OFFSET)

            sleep(DELTA_TIME)
    except EOFError:
        pass