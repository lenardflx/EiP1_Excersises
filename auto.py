from jguvc_eip import basic_io as bio # Hauptbibliothek
from jguvc_eip.colors import * # [optional] Farbnamen
from jguvc_eip import image_objects # [optional] Bildobjekte
from time import sleep

if __name__ == '__main__':
  bio.start()
  k = 1
  while k < 640:
     bio.clear_image()
     bio.draw_polygon([(500, 150), (550, 140), (600, 150), (600, 230), (500, 230)], BLUE)
     bio.draw_rectangle(k, 210, 90, 20, RED)
     bio.draw_circle(k + 10, 230, 10, BLACK)
     bio.draw_circle(k + 80, 230, 10, BLACK)
     sleep(0.016)
     k = k + 2
  bio.clear_image()

if __name__ == '__main__':
  bio.start()
  k = 1
  while k < 640:
     bio.clear_image()
     bio.draw_rectangle(k, 210, 90, 20, RED)
     bio.draw_circle(k + 10, 230, 10, BLACK)
     bio.draw_circle(k + 80, 230, 10, BLACK)
     bio.draw_polygon([(500, 150), (550, 140), (600, 150), (600, 230), (500, 230)], BLUE)
     sleep(0.016)
     k = k + 2
bio.wait_close