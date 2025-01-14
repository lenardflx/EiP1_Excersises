from random import randint
import jguvc_eip.basic_io as bio
from jguvc_eip import image_objects as iobj
from time import sleep

def iter_stack(numbers):
    return iobj.HorizontalStack([iobj.Rectangle(10, n, fill_color=None) for n in numbers])

def rec_stack(numbers):
    if len(numbers) == 1:
        return iobj.Rectangle(10, numbers[0], fill_color=None)
    comp_obj = rec_stack(numbers[:-1])
    rect = iobj.Rectangle(10, numbers[-1], fill_color=None)
    return iobj.HorizontalStack([comp_obj, rect])

def extract_from_rec_stack(obj):
    if isinstance(obj, iobj.Rectangle):
        return [obj]
    return [item for o in obj.objects for item in extract_from_rec_stack(o)]

if __name__ == "__main__":
    bio.start()

    nums = [randint(0, 100) for _ in range(50)]

    itr = "Iterativ", iter_stack(nums)
    rec = "Rekursiv", rec_stack(nums)
    ext = "Extrahiert", iobj.HorizontalStack(extract_from_rec_stack(rec[1]))

    for name, stack in [itr, rec, ext]:
        bio.print_message(name)
        bio.draw_object(stack, 50, 50)
        sleep(5)
        bio.clear_image()
        sleep(0.3)

    bio.close_and_exit()