from random import randint
import jguvc_eip.basic_io as bio
from jguvc_eip import image_objects as iobj
from time import sleep

def display(name, stack):
    bio.print_message(name)
    bio.draw_object(stack, 50, 50)
    sleep(5)
    bio.clear_image()
    sleep(0.1)

if __name__ == "__main__":
    bio.start()

    nums = [randint(0, 100) for _ in range(50)]
    rects = [iobj.Rectangle(10, n, None) for n in nums]

    itr = iobj.HorizontalStack(rects)
    display("Iterativ", itr)

    comp_obj = rects[0]
    for rec in rects[1:]:
        comp_obj = iobj.HorizontalStack([comp_obj, rec])
    display("Rekursiv", comp_obj)

    def extract(obj):
        if isinstance(obj, iobj.HorizontalStack):
            return [obj.objects[0]] + extract(obj.objects[1])
        return [obj]
    ext = iobj.HorizontalStack(extract(comp_obj))
    display("Extrahiert", ext)