import jguvc_eip.basic_io as bio
from time import sleep
from jguvc_eip import image_objects as iobj


class FallingBall:
    def __init__(self, x, y, acceleration, rectangle_size, line_height, delta_time):
        self.offset = (x, y)
        self.acceleration = acceleration
        self.rectangle_size = rectangle_size
        self.line_height = line_height
        self.delta_time = delta_time
        self.time = 0
        self.position = rectangle_size
        self.buffer = (0,1)
        self._create_objects()

    def _create_objects(self):
        rect1 = iobj.Rectangle(self.rectangle_size, self.rectangle_size)
        rect2 = iobj.Rectangle(self.rectangle_size, self.rectangle_size)
        line = iobj.Rectangle(1, self.line_height, border_color=None)
        self.circ = iobj.Circle(self.rectangle_size, fill_color=(255, 0, 0))
        self.obj_stack = iobj.VerticalStack([rect1, line, rect2])

    def _calculate_position(self):
        self.position = 0.5 * self.acceleration * self.time**2 + self.rectangle_size

    def _create_draw_object(self):
        off_circ = iobj.Translate(self.circ, 0, int(self.position))
        return iobj.Overlay([self.obj_stack, off_circ])

    def _buffer_swap(self):
        bio.set_active_image(self.buffer[1])
        bio.set_visible_image(self.buffer[0])
        bio.copy_image(*self.buffer)
        self.buffer = (self.buffer[1], self.buffer[0])

    def draw_object(self):
        obj = self._create_draw_object()
        self._buffer_swap()
        bio.clear_image()
        bio.draw_object(obj, *self.offset)

    def run_step(self):
        self._calculate_position()
        self.time += self.delta_time
        sleep(self.delta_time)

    def run(self):
        while True:
            self.run_step()
            if self.position >= self.line_height:
                self.position = self.line_height
            self.draw_object()


if __name__ == "__main__":
    ball = FallingBall(200, 50, 200, 20, 200, 1/120)
    ball.run()
