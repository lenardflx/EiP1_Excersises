from jguvc_eip import basic_io as bio, image_objects as iobj
from time import sleep

# Parameters
OFFSET = (200, 50)
ACCELERATION = 9.81
SIZE = 15
LINE_HEIGHT = 250
DELTA_TIME = 1 / 60
PIXEL_METER_RATIO = 100
PRESS_REDUCTION = 50
BOUNCE = 0.8

model = iobj.VerticalStack([iobj.Rectangle(SIZE, SIZE),
        iobj.Rectangle(1, LINE_HEIGHT), iobj.Rectangle(SIZE, SIZE)])
active, visible = 0, 1

# ball properties
ball1 = iobj.Circle(SIZE, fill_color=(255, 0, 0))
ball2 = iobj.Circle(SIZE, fill_color=(0, 0, 255))
bm_edge, tp_edge = [LINE_HEIGHT, LINE_HEIGHT - SIZE], [SIZE * 2, SIZE]
pos,velocity, key = [SIZE + LINE_HEIGHT / 2, SIZE], [0, 0], ["u","r"]

if __name__ == "__main__":
    bio.start()
    try:
        while True:
            for ball in (0, 1):
                if key[ball] in bio.get_current_keys_down():
                    velocity[ball] -= PRESS_REDUCTION
                velocity[ball] += ACCELERATION * DELTA_TIME * PIXEL_METER_RATIO
                pos[ball] += velocity[ball] * DELTA_TIME

                if pos[ball] >= bm_edge[ball]:
                    pos[ball], velocity[ball] = bm_edge[ball], -velocity[ball] * BOUNCE
                elif pos[ball] <= tp_edge[ball]:
                    pos[ball], velocity[ball] = tp_edge[ball], 0

            if pos[1] >= pos[0] - SIZE:
                velocity[0], velocity[1] = velocity[1], velocity[0]
                pos[1] = pos[0] - SIZE

            off_ball1 = iobj.Translate(ball1, 0, int(pos[0]))
            off_ball2 = iobj.Translate(ball2, 0, int(pos[1]))

            active, visible = visible, active
            bio.set_active_image(active)
            bio.set_visible_image(visible)
            bio.copy_image(visible, active)

            bio.clear_image()
            bio.draw_object(iobj.Overlay([model, off_ball1, off_ball2]), *OFFSET)

            sleep(DELTA_TIME)
    except EOFError:
        pass