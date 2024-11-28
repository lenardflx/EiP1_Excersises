from time import sleep
from jguvc_eip import basic_io as bio

if __name__ == "__main__":
    dvd = bio.load_image('dvd_selfmade.png')
    bio.start()
    p1 = 295                     #Anfangspunkt (Mittelpunkt)
    p2 = 215
    d1 = 2                          #Richtungsvektor
    d2 = -1
    ecke_counter=0
    while (True):
        bio.clear_image()
        bio.draw_image(p1,p2,dvd)
        sleep(0.000000016)
        p1=p1+d1
        p2=p2+d2
        if(p1>590):
            d1=-2
        elif(p1<0):
            d1=2
        if(p2>430):
            d2=-1
        elif(p2<0):
            d2=1
        if(p1<31 and p2<31 or p1>559 and p2<31 or p1>559 and p2> 409 or p1<31 and p2>409):
            ecke_counter+=1
            bio.print_message(str(ecke_counter))
        key = bio.get_last_key_pressed_event()
        if key == 'q':
            break
    bio.close_and_exit()
