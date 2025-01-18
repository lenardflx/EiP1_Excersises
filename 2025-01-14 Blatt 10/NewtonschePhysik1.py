import jguvc_eip.basic_io as bio
from time import sleep
from jguvc_eip import image_objects as iobj

# Parameter
OFFSET = (200, 50)
ACCELERATION = 200
RECTANGLE_SIZE = 20
LINE_HEIGHT = 200
DELTA_TIME = 1 / 60

model = iobj.VerticalStack([
    iobj.Rectangle(RECTANGLE_SIZE, RECTANGLE_SIZE),
    iobj.Rectangle(1, LINE_HEIGHT, border_color=None),
    iobj.Rectangle(RECTANGLE_SIZE, RECTANGLE_SIZE)
])
circ = iobj.Circle(RECTANGLE_SIZE, fill_color=(255, 0, 0))

if __name__ == "__main__":
    time = position = 0
    bio.start()

    while position < LINE_HEIGHT:
        position = 0.5 * ACCELERATION * time**2 + RECTANGLE_SIZE
        time += DELTA_TIME

        if position >= LINE_HEIGHT:
            position = LINE_HEIGHT
            time = 0

        off_circ = iobj.Translate(circ, 0, int(position))
        bio.clear_image()
        bio.draw_object(iobj.Overlay([model, off_circ]), *OFFSET)

        sleep(DELTA_TIME)

    bio.wait_close()