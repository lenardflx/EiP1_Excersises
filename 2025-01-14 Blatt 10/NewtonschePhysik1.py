from jguvc_eip import basic_io as bio
from time import sleep
from jguvc_eip import image_objects as iobj

# Parameter
OFFSET = (200, 50)
ACCELERATION = 9.81
RECTANGLE_SIZE = 20
LINE_HEIGHT = 200
DELTA_TIME = 1 / 60
PIXEL_METER_RATIO = 100

model = iobj.VerticalStack([
    iobj.Rectangle(RECTANGLE_SIZE, RECTANGLE_SIZE),
    iobj.Rectangle(1, LINE_HEIGHT, border_color=(0, 0, 0)),
    iobj.Rectangle(RECTANGLE_SIZE, RECTANGLE_SIZE)
])
circ = iobj.Circle(RECTANGLE_SIZE, fill_color=(255, 0, 0))

if __name__ == "__main__":
    velocity = 0
    position = RECTANGLE_SIZE
    bio.start()

    while position < LINE_HEIGHT:
        velocity += ACCELERATION * DELTA_TIME * PIXEL_METER_RATIO
        position += velocity * DELTA_TIME

        if position >= LINE_HEIGHT:
            position = LINE_HEIGHT
            velocity = 0

        off_circ = iobj.Translate(circ, 0, int(position))
        bio.clear_image()
        bio.draw_object(iobj.Overlay([model, off_circ]), *OFFSET)

        sleep(DELTA_TIME)

    bio.wait_close()