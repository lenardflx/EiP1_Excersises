from jguvc_eip import basic_io as bio
from jguvc_eip.colors import *
from time import sleep

if __name__ == '__main__':
    bio.start()
    #1) Auto zeichnen
    bio.draw_rectangle(40,150,100,30, RED ,border_thickness=1)
    bio.draw_circle(50,180,10,BLACK)
    bio.draw_circle(130, 180, 10, BLACK)
    #2) Haus zeichnen
    bio.draw_polygon([(500,210),(600,210),(600,100),(550,80),(500,100)],BLUE, BLACK, 1)
    #3) Auto fährt vor dem Haus

    autorechts=0
    autox = 40
    autoy = 150
    rad1x = 50
    rad1y = 180
    rad2x = 130
    rad2y = 180
    while(autorechts < 700):
        bio.clear_image(WHITE)
        bio.draw_rectangle(autox, autoy, 100, 30, RED, border_thickness=1)
        bio.draw_circle(rad1x,rad1y, 10, BLACK)
        bio.draw_circle(rad2x,rad2y, 10, BLACK)
        bio.draw_polygon([(500, 210), (600, 210), (600, 100), (550, 80), (500, 100)], BLUE, BLACK, 1)
        autox = autox+2
        rad1x = rad1x+2
        rad2x = rad2x+2
        autorechts= autox+100
        sleep(0.016)
    #4) Auto vor dem Haus
    autorechts=0
    autox = 40
    autoy = 150
    rad1x = 50
    rad1y = 180
    rad2x = 130
    rad2y = 180
    while(autorechts < 700):
        bio.clear_image(WHITE)
        bio.draw_polygon([(500, 210), (600, 210), (600, 100), (550, 80), (500, 100)], BLUE, BLACK, 1)
        bio.draw_rectangle(autox, autoy, 100, 30, RED, border_thickness=1)
        bio.draw_circle(rad1x,rad1y, 10, BLACK)
        bio.draw_circle(rad2x,rad2y, 10, BLACK)
        autox = autox+2
        rad1x = rad1x+2
        rad2x = rad2x+2
        autorechts= autox+100
        sleep(0.016)

    bio.wait_close()