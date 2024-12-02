from time import sleep
from jguvc_eip import basic_io as bio

# Parameter
SIZE, IMG_SIZE, CORNER_OFF, FPS = (640, 480), (48, 25), 10, 600 # FPS höher, damit schneller

if __name__ == "__main__":
    bio.start()
    pos = [(SIZE[i]-IMG_SIZE[i])//2 for i in (0,1)]
    direc, flag,count = [1,1], False,0
    image = bio.load_image("dvd_selfmade_own.png") # Eigene Version

    while True:
        bio.clear_image()
        bio.draw_image(pos[0], pos[1], image)
        # Prüft ob Ecke erreicht wurde
        if all([not flag, flag := all(not (CORNER_OFF < pos[i] < SIZE[i]-IMG_SIZE[i]-CORNER_OFF) for i in (0, 1))]):
            count += 1
            bio.print_message(f"Ecke getroffen! Anzahl: {count}")
        # Änder Richtung (0: x, 1: y)
        for i in (0, 1):
            direc[i] *= -1 if not (0 < pos[i] < SIZE[i]-IMG_SIZE[i]) else 1
            pos[i] += direc[i]
        sleep(1/FPS)